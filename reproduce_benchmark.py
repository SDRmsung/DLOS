#!/usr/bin/env python3
# Dual-Loop OS: Full Closed-Loop Physical Simulation Suite (~2.4 min)
import subprocess, sys

if __name__ == '__main__':
    print("[RUN] Executing Full 50,000-Step Physics Simulation & Baseline Evaluation (~2.4 min)...")
    subprocess.run([sys.executable, "reproduce_all.py", "--full-sim"])
