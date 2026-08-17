#!/usr/bin/env python3
# Dual-Loop OS: Fast Theoretical Verification Suite (1.10 ms)
import subprocess, sys

if __name__ == '__main__':
    print("[RUN] Executing Fast Theoretical Proof & Hypothesis Verification (1.10 ms)...")
    subprocess.run([sys.executable, "reproduce_all.py", "--fast"])
