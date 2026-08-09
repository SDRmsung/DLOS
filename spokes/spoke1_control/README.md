# Spoke 1: Differentiable Logarithmic Barrier via STE for CBF

> **Hub Package**: `pcos_core_engine v32.0.0`  
> **Target Venues**: IEEE L-CSS / L4DC / ECC (`eess.SY` / `cs.SY`)  
> **Ecosystem Dependency**: Imports `nesy_filter` from `pcos_core_engine` (Code overlap < 15%)

## Abstract & Mathematical Scope
This spoke implements the Straight-Through Estimator (STE) differentiable log-barrier mechanism for continuous Control Barrier Functions (CBFs). By providing continuous Lyapunov derivatives $\dot{V} = -\langle \nabla E_{\text{barrier}}, \nabla E_{\text{total}} \rangle < 0$ with $K$-Lipschitz continuity ($K \le 1.42$), it guarantees Nagumo forward-invariance for hard safety constraints on resource-constrained embedded systems.

## Key Files
- `lemmas/cbf_lemma123.py`: Formal implementation and verification of Lemma 1 (Log-Barrier Convexity), Lemma 2 (STE Differentiability), and Lemma 3 (Nagumo Forward Invariance).
- `demo.py`: Single-command standalone CPU verification script.

## Quick Execution
```bash
# Ensure Hub is installed locally
pip install -e .

# Run Spoke 1 verification
python spokes/spoke1_control/demo.py
```
