# Dual-Loop OS: Neuro-Symbolic Safety Shield for JEPA Latent Decision Systems

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SDRmsung/DLOS/blob/main/demo_colab.ipynb)
[![License: BSL 1.1](https://img.shields.io/badge/License-BSL_1.1-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Official standalone, zero-dependency reproducibility package for the initial submission manuscript:  
**"JEPA Safety-Critical Latent Decision Architecture: A Formal Neuro-Symbolic Framework with Deterministic Barrier Constraints"**  
*Ming-Hung Sung [ORCID: [0009-0003-3305-0637](https://orcid.org/0009-0003-3305-0637)] & Shih-Yu Sung*

---

## ⚡ 1-Click Zero-Dependency Reproducibility (< 0.5s)

You can run the entire formal verification suite directly in **Google Colab** with zero installation:
1. Click the **[Open in Colab](https://colab.research.google.com/github/SDRmsung/DLOS/blob/main/demo_colab.ipynb)** badge above.
2. In the Colab menu, click **Runtime -> Run all** (`Ctrl+F9`).
3. All 5 formal checkpoints (Table 1a, Table 1b, Theorem 1B/1C, and Cortex-M7 latency) execute in **< 0.5 seconds** on standard CPU.

Or run locally via terminal:
```bash
git clone https://github.com/SDRmsung/DLOS.git
cd DLOS
python demo_colab.py
```

---

## 📂 Repository Structure

```text
DLOS/
├── README.md                      # Reproduction guide, architecture & Colab badge
├── demo_colab.py                  # Standalone 0.5s 5-checkpoint verification script
├── demo_colab.ipynb               # Interactive Jupyter/Colab notebook
├── setup.py                       # Python packaging configuration
├── requirements.txt               # Minimal dependencies (numpy, scipy, torch)
├── LICENSE                        # Business Source License 1.1 (BSL 1.1)
│
├── dlos/                          # Core Python Engine
│   ├── __init__.py                # Package exports
│   └── polyhedral_shield.py       # 14-hyperplane pre-sintered barrier & Algorithm 1
│
├── benchmarks/                    # Formal Experiment Reproductions
│   └── run_cartpole_cbf.py        # Table 1a: CartPole-v1 closed-loop vs CBF-QP baselines
│
├── firmware/                      # STM32 Cortex-M7 Microsecond Deployment
│   └── main_stm32h7.c             # STM32H743ZI C driver (1.08 us online latency)
│
└── tests/                         # Formal Mathematical Unit Tests
    └── test_forward_invariance.py # Unit tests for Theorem 1B/1C mathematical induction
```

---

## 🔬 Benchmark Results Summary

### Table 1a: Control-Theoretic Safety Filter Baselines (CartPole-v1)
| Method | Domain | Success Rate | Violation Rate | Latency | Memory |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Vanilla CBF-QP (Ames et al., 2019) | Control | 98.2 ± 0.3% | 0.4 ± 0.1% | 4.8 ms | < 1 MB |
| Explicit MPC (Bemporad et al., 2002) | Control | 98.1 ± 0.4% | 0.2 ± 0.1% | 1.5 μs | > 400 MB |
| **Dual-Loop OS Veto (Ours)** | **Control** | **97.8 ± 0.5%** | **0.0 ± 0.0%** | **1.08 μs** | **49.7 MB** |

---

## 📜 Citation & License

This is an initial research submission. For academic reference:
```bibtex
@article{sung2026dualloopos,
  title={JEPA Safety-Critical Latent Decision Architecture: A Formal Neuro-Symbolic Framework with Deterministic Barrier Constraints},
  author={Sung, Ming-Hung and Sung, Shih-Yu},
  note={Manuscript under review},
  year={2026}
}
```

- **Paper Manuscript**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Core Software Engine**: [Business Source License 1.1 (BSL 1.1)](LICENSE) (Free for non-commercial academic research; converts to Apache 2.0 on 2028-08-09).
- **Demo Script (`demo_colab.py`)**: [MIT License](https://opensource.org/licenses/MIT).
