import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dlos.polyhedral_shield import PolyhedralSafetyShield

class TestDiscreteForwardInvariance(unittest.TestCase):
    def setUp(self):
        self.shield = PolyhedralSafetyShield(eps=3.5, delta_drift=0.05, xi_max=0.10, K_max=2)

    def test_sintered_margin_bound(self):
        # eps_sinter = 3.5 + 4*0.05 + 2*0.10 = 3.90
        self.assertGreater(self.shield.eps_sinter, self.shield.eps)

    def test_emergency_recovery_lemma1(self):
        # Consecutive rejections trigger Lemma 1
        admitted, action = self.shield.check_admissibility(14.8, 10.0)
        self.assertFalse(admitted)
        admitted2, emergency_action = self.shield.check_admissibility(14.9, 10.0)
        self.assertFalse(admitted2)
        # Check that emergency action reverses torque
        self.assertLess(emergency_action, 0.0)

if __name__ == "__main__":
    unittest.main()
