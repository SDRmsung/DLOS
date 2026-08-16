# Dual-Loop OS: Neuro-Symbolic Safety Shield for JEPA Latent Decision Systems

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SDRmsung/DLOS/blob/main/demo_colab.ipynb)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![arXiv](https://img.shields.io/badge/arXiv-cs.AI%20%2F%20eess.SY-b31b1b.svg)](https://arxiv.org/)

Official standalone, zero-dependency reproducibility package for the paper:  
**"JEPA Safety-Critical Latent Decision Architecture: A Formal Neuro-Symbolic Framework with Deterministic Barrier Constraints"**  
*Ming-Hung Sung & Shih-Yu Sung (Dual-Loop OS Lab)*

---

## ⚡ 1-Click Zero-Dependency Reproducibility (< 0.5s)

You can run the entire verification harness directly in **Google Colab** with zero installation:
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
├── LICENSE                        # Apache-2.0 open-source license
│
├── dlos/                          # Core Python Engine
│   ├── __init__.py                # Package exports
│   ├── jepa_latent.py             # JEPA latent predictor & Tri-term energy minimization
│   ├── mcr2_manifold.py           # MCR2 subspace orthogonal decomposition (Tr < 1e-7)
│   ├── polyhedral_shield.py       # 14-hyperplane pre-sintered barrier & Algorithm 1
│   └── scm_engine.py              # Pearl L3 Structural Causal Model & STE operator
│
├── benchmarks/                    # Formal Experiment Reproductions
│   ├── run_cartpole_cbf.py        # Table 1a: CartPole-v1 closed-loop vs CBF-QP baselines
│   ├── run_ablation_study.py      # Table 1b: 5-component architectural ablation
│   └── reproduce_all.py           # Master 1-click test suite runner
│
├── firmware/                      # STM32 Cortex-M7 Microsecond Deployment
│   ├── cortex_m7_sintered_lut.h   # Pre-sintered 49.7 MB / compressed lookup table
│   ├── main_stm32h7.c             # STM32H743ZI C driver (1.08 us online latency)
│   └── Makefile                   # ARM-GCC compilation harness
│
└── tests/                         # Formal Mathematical Unit Tests
    ├── test_forward_invariance.py # Unit tests for Theorem 1B/1C mathematical induction
    └── test_phase_space_lemma1.py # Unit tests for Lemma 1 phase-space recovery attractor
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

## 🛠️ Local Installation & Development

```bash
# Clone the repository
git clone https://github.com/SDRmsung/DLOS.git
cd DLOS

# Install in editable mode
pip install -e .

# Run formal unit tests
python -m unittest discover tests/

# Run CartPole benchmark reproduction
python benchmarks/run_cartpole_cbf.py
```

---

## 📜 Citation & License

If you use Dual-Loop OS in your research, please cite our arXiv preprint:
```bibtex
@article{sung2026dualloopos,
  title={JEPA Safety-Critical Latent Decision Architecture: A Formal Neuro-Symbolic Framework with Deterministic Barrier Constraints},
  author={Sung, Ming-Hung and Sung, Shih-Yu},
  journal={arXiv preprint arXiv:2608.xxxxx},
  year={2026}
}
```
Released under the [Apache-2.0 License](LICENSE).
