# PCOS Core Engine (Personal Cognitive Operating System)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 2.0+](https://img.shields.io/badge/pytorch-2.0+-orange.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Paper Title**: *Extending JEPA to Macro-Level Latent Phase Spaces: Towards Near-Zero Fatal Hallucination in Personal Decision Intelligence via White-Box Neuro-Symbolic Cybernetics*

---

## 📌 Overview

**PCOS Core Engine** is a self-contained, light-weight Python package that implements the core neuro-symbolic modules of the Personal Cognitive Operating System:

1. **`nesy_filter.py`**: Space 5 NeSy Log-Barrier Safety Filter ($O(1)$ microsecond Boolean lookup, 10 WHO ICD redlines, 7-Agent priority constellation).
2. **`crate_encoder.py`**: White-Box CRATE Transformer Encoder with $MCR^2$ Sparse Rate Reduction Orthogonality Loss ($\text{Tr}(\mathbf{P}_i \mathbf{P}_j^T) \to 0$) and Spectral Norm $K$-Lipschitz Continuity Bounds ($K \le 1.42$).
3. **`jepa_predictor.py`**: JEPA Latent Space World Model Predictor & Tri-Term MAP Energy Minimization ($E_{\text{total}} = w_{\text{pred}} E_{\text{pred}} + w_{\text{mcr2}} E_{MCR^2} - \lambda \eta \ln(B) + \epsilon_{\text{dopamine}}$).
4. **`benchmark_harness.py`**: Automated evaluation benchmark harness measuring FHR, OPR, and decision latency.

---

## 🚀 One-Click Execution Options

### Option A: Google Colab / Local Python (Single File Execution)

Run `demo_colab.py` with zero setup:

```bash
# Install standard dependencies
pip install torch numpy

# Run the complete one-click verification pipeline
python pcos_core_engine/demo_colab.py
```

### Option B: Local Python Package Import

```python
from pcos_core_engine import NeSySafetyFilter, WhiteBoxCRATEEncoder, TriTermEnergyMinimizer, PCOSBenchmarkRunner

# 1. Initialize Log-Barrier Safety Filter
filter_engine = NeSySafetyFilter()
is_safe, energy, agent, reason = filter_engine.check_ingredient_safety(
    disease_code="E83.0",  # Wilson's Disease
    ingredient_text="Seafood soup with roasted almonds & copper broth"
)
print(f"Safety Decision: {is_safe}, Agent Veto: {agent}, Reason: {reason}")

# 2. Run 1,000-Sample Benchmark
runner = PCOSBenchmarkRunner()
results = runner.run_benchmark(num_samples=1000)
print(f"Fatal Hallucination Rate (FHR): {results['FHR_percent']:.2f}%")
print(f"Filter Latency: {results['avg_filter_latency_ms']:.4f} ms")
```

---

## 📊 Benchmark Output

```text
==================================================================
🏆 FINAL BENCHMARK PERFORMANCE MATRIX
==================================================================
Total Evaluated Samples     : 1,000
Fatal Hallucination Rate    : 0.00% (Target: 0.00%)
Over-Pruning Rate (OPR)     : 1.20%
Filter Decision Latency     : 0.0012 ms
Confusion Matrix (TP/FP/TN/FN): TP=494, FP=6, TN=500, FN=0
==================================================================
```

---

## 📜 License & Citation

Licensed under the MIT License.
For questions or reproduction support, please refer to Section 6.3 of `JEPA_ALL_23.md`.
