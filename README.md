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

## ⚡ Standalone Reproduction in Seconds

Dual-Loop OS provides a dual-track verification suite ensuring 100% independent academic reproducibility:

```bash
# 1. Instant Statistical Metric & Hypothesis Testing Verification (~1.10 ms)
python reproduce_all.py --fast

# 2. Full 50,000-Step End-to-End Nonlinear Physics & Baseline Simulation (~2.4 min)
python reproduce_all.py --full-sim

# 3. Train CRATE-JEPA Encoder & Latent Dynamics (Table A1)
python scripts/train_crate_jepa.py --epochs 200 --batch_size 256
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

