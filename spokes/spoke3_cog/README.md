# Spoke 3: Active Inference Grounded by Energy Manifold

> **Hub Package**: `dual_loop_os_core_engine v32.0.0`  
> **Target Venues**: NeurIPS / AAAI Workshop / `q-bio.NC` / `cs.NE`  
> **Ecosystem Dependency**: Imports `jepa_predictor` from `dual_loop_os_core_engine` (Code overlap < 20%)

## Abstract & Neuro-Cognitive Scope
This spoke maps Karl Friston's Variational Free Energy $F(q, O)$ and Expected Free Energy $G(\pi)$ to the Dual-Loop OS tri-term energy minimizer $E_{\text{total}} = E_{\text{pred}} + E_{\text{prior}} + E_{\text{barrier}}$. It demonstrates how latent state dynamics in JEPA ground active inference without requiring computationally expensive generative pixel sampling.

## Key Files
- `demo.py`: Comparative verification script between Friston Expected Free Energy $G(\pi)$ and JEPA MAP energy minimization.

## Quick Execution
```bash
# Ensure Hub is installed locally
pip install -e .

# Run Spoke 3 Cognitive Inference Demo
python spokes/spoke3_cog/demo.py
```
