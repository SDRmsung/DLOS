import numpy as np

class PolyhedralSafetyShield:
    """
    14-Hyperplane Polyhedral Pre-Sintered Safety Shield (Algorithm 1)
    """
    def __init__(self, eps=3.5, delta_drift=0.05, xi_max=0.10, K_max=2):
        self.eps = eps
        self.delta_drift = delta_drift
        self.xi_max = xi_max
        self.K_max = K_max
        # Pre-sintered threshold (Assumption A2_d)
        self.eps_sinter = eps + (K_max**2)*delta_drift + K_max*xi_max
        self.rejection_counter = 0

    def evaluate_barrier(self, theta_deg):
        theta_max = 15.0
        return theta_max - abs(theta_deg)

    def check_admissibility(self, current_theta_deg, candidate_action_force):
        # 1-step worst-case forward Euler prediction
        dt = 0.02
        pred_theta = current_theta_deg + candidate_action_force * 0.1 * dt + self.xi_max
        b_pred = self.evaluate_barrier(pred_theta)
        
        if b_pred >= self.eps_sinter:
            self.rejection_counter = 0
            return True, candidate_action_force
        else:
            self.rejection_counter += 1
            if self.rejection_counter >= self.K_max:
                # Trigger Lemma 1 emergency restoration action
                safe_action = -25.0 * np.sign(current_theta_deg)
                self.rejection_counter = 0
                return False, safe_action
            return False, 0.0
