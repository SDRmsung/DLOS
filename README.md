# Dual-Loop OS: Deterministic Safety Shielding for JEPA-Based Embodied AI (v59 Official Release)

[![License: BSL 1.1](https://img.shields.io/badge/License-BSL%201.1-blue.svg)](https://github.com/SDRmsung/DLOS/blob/main/LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Paper Status](https://img.shields.io/badge/Paper-Preprint%20(v59)-brightgreen.svg)](https://github.com/SDRmsung/DLOS)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/SDRmsung/DLOS/blob/main/demo_colab.ipynb)

**Official Open-Source Implementation of the Paper:**  
> **Dual-Loop OS: Deterministic Safety Shielding for JEPA-Based Embodied AI**  
> **Authors:** Ming-Hung Sung (ORCID: [0009-0003-3305-0637](https://orcid.org/0009-0003-3305-0637)), Shih-Yu Sung  
> *Independent Researcher*

---

## 🚀 Quick Install (Zero Friction)

Install the core Python engine directly via `pip` without external package registries:

```bash
pip install git+https://github.com/SDRmsung/DLOS.git
```

---

## ⚡ Standalone Verification & Primary Experience Routes

Dual-Loop OS provides three zero-friction verification pathways ensuring 100% independent academic reproducibility:

### Route 1: One-Click Interactive Cloud Demo (Google Colab)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/SDRmsung/DLOS/blob/main/demo_colab.ipynb)  
Run the interactive closed-loop safety shield directly in your browser with zero local setup: [`demo_colab.ipynb`](https://github.com/SDRmsung/DLOS/blob/main/demo_colab.ipynb).

### Route 2: Instant Standalone Metrics & Proofs (~1.10 ms)
```bash
# 1. Instant Statistical Metric & Hypothesis Testing Verification (~1.10 ms)
python reproduce_all.py --fast

# 2. Full 50,000-Step End-to-End Nonlinear Physics & Baseline Simulation (~2.4 min)
python reproduce_all.py --full-sim

# 3. Train 4-Layer CRATE-JEPA Encoder & Latent Dynamics (Table A1)
python scripts/train_crate_jepa.py --epochs 200 --batch_size 256
```

### Route 3: Python API Integration
```python
import torch
from dlos.polyhedral_shield import PolyhedralSafetyShield

# Initialize 14-Hyperplane Pre-Sintered Shield (eps_sinter = 4.72 deg, K_max = 2)
shield = PolyhedralSafetyShield(eps=3.50, delta_drift=0.0466, xi_max=0.10, K_max=2)

# Check candidate action admissibility (Algorithm 1 / 1.08 us veto)
is_admitted, safe_action = shield.check_admissibility(current_theta_deg=10.5, candidate_action_force=15.0)
print(f"Action Admitted: {is_admitted}, Executed Force: {safe_action} N")
```

---

## 🔬 Core Performance Highlights (CartPole-v1 Benchmark & Cortex-M7)

- **Empirical Safety Violations**: **$0.0 \pm 0.0\%$** across 50,000 steps subject to **$4.0\times$ OOD** parameter shifts.
- **Task Success Rate**: **$97.8 \pm 0.5\%$** ($6.33\times$ marginal safety leverage over unshielded policies).
- **Statistical Significance**: Two-tailed Fisher's exact test **$p = 2.31 \times 10^{-4}$**, Clopper-Pearson 95% CI $[0.00\%, 7.11\%]$ vs $[13.06\%, 38.17\%]$.
- **Hardware Latency**: **$1.08\,\mu\text{s}$** (233 cycles @ 216 MHz) on bare-metal ARM Cortex-M7 with **$<8\text{ KB}$** DTCM SRAM.
- **Offline GPU Sintering**: **$12.4\text{ ms}$** vectorized PyTorch pre-computation.

---

## 📖 Citation

If you use this work or codebase in your research, please cite:

```bibtex
@article{sung2026dualloopos,
  title={Dual-Loop OS: Deterministic Safety Shielding for JEPA-Based Embodied AI},
  author={Sung, Ming-Hung and Sung, Shih-Yu},
  journal={arXiv preprint},
  year={2026},
  note={v59 Official Release},
  url={https://github.com/SDRmsung/DLOS}
}
```

---

## 📜 Licensing
- **Core Decision Engine (`dlos/`)**: Business Source License 1.1 (BSL 1.1, converting automatically to Apache License 2.0 on 2028-08-09).
- **Embedded Firmware & Microcontroller Drivers (`firmware/`)**: MIT License.
- **Academic Manuscript & Theoretical Proofs**: Creative Commons Attribution 4.0 International (CC BY 4.0).

