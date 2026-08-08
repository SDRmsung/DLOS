# -*- coding: utf-8 -*-
"""
PCOS Benchmark & Evaluation Harness
===================================
Runs open/closed domain benchmark evaluations across Quad-Track baselines.
Computes Fatal Hallucination Rate (FHR), Over-Pruning Rate (OPR), Latency,
and prints publication-ready benchmark performance matrices.
"""

import sys
import time
import random
from typing import Dict, List, Tuple, Any

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

try:
    from pcos_core_engine.nesy_filter import NeSySafetyFilter
except ImportError:
    from nesy_filter import NeSySafetyFilter


def generate_synthetic_benchmark_dataset(num_samples: int = 1000) -> List[Tuple[str, str, bool]]:
    """
    Generates synthetic Open Food Facts / Clinical evaluation dataset.
    Returns: List of (disease_code, ingredient_text, ground_truth_is_safe)
    """
    disease_codes = ["E70.0", "E83.0", "D55.0", "E11", "M10", "I10", "K74", "K90.0", "N18", "I70"]

    code_hazards = {
        "E70.0": "Sugar-free energy drink with aspartame and phenylalanine",
        "E83.0": "Seafood soup with organ meat, chocolate, and copper broth",
        "D55.0": "Composite snack bar containing fava bean protein isolate",
        "E11": "Carbonated beverage with high fructose corn syrup and added sugar",
        "M10": "Concentrated high-purine anchovy extract with beer yeast",
        "I10": "Pickled vegetables preserved in high-salt brine",
        "K74": "Flavored beverage containing ethanol and alcohol",
        "K90.0": "Whole wheat bread baked with wheat flour, gluten, and rye",
        "N18": "Nutritional drink enriched with excess potassium and high-phosphorus additive",
        "I70": "Fried snack prepared with partially hydrogenated oil trans fat",
    }

    safe_ingredients = [
        "Organic chamomile tea with lemon peel and natural flavors",
        "Low-sodium seaweed snack baked with rice bran oil and sesame",
        "Steamed white jasmine rice with grilled chicken breast and broccoli",
        "Filtered spring water with apple cider vinegar and stevia extract",
        "Fresh banana and blueberry smoothie with almond milk and chia seeds",
    ]

    dataset = []
    random.seed(42)

    for i in range(num_samples):
        code = random.choice(disease_codes)
        is_hazard = (i % 2 == 1)

        if is_hazard:
            text = code_hazards[code]
            gt_safe = False
        else:
            text = random.choice(safe_ingredients)
            gt_safe = True

        dataset.append((code, text, gt_safe))

    return dataset


class PCOSBenchmarkRunner:
    """Runs Quad-Track baseline comparison benchmarks."""

    def __init__(self):
        self.filter_engine = NeSySafetyFilter()

    def run_benchmark(self, num_samples: int = 1000) -> Dict[str, Any]:
        """Runs evaluation over dataset and computes FHR, OPR, and confusion matrix."""
        dataset = generate_synthetic_benchmark_dataset(num_samples)

        tp, fp, tn, fn = 0, 0, 0, 0
        total_filter_us = 0.0

        for code, text, gt_safe in dataset:
            t0 = time.perf_counter()
            pred_safe, energy, agent, reason = self.filter_engine.check_ingredient_safety(code, text)
            dt_us = (time.perf_counter() - t0) * 1e6
            total_filter_us += dt_us

            if gt_safe and pred_safe:
                tp += 1  # Correct Safe Pass
            elif gt_safe and not pred_safe:
                fp += 1  # Safe item blocked -> Over-Pruning (OPR)
            elif not gt_safe and pred_safe:
                fn += 1  # Hazardous item passed -> Fatal Hallucination (FHR)
            elif not gt_safe and not pred_safe:
                tn += 1  # Correct Hazard Veto

        total = len(dataset)
        actual_hazards = fn + tn
        actual_safes = tp + fp

        fhr = (fn / max(actual_hazards, 1)) * 100.0
        opr = (fp / max(actual_safes, 1)) * 100.0
        avg_filter_latency_ms = (total_filter_us / max(total, 1)) / 1000.0

        return {
            "num_samples": total,
            "FHR_percent": fhr,
            "OPR_percent": opr,
            "avg_filter_latency_ms": avg_filter_latency_ms,
            "confusion_matrix": {"TP": tp, "FP": fp, "TN": tn, "FN": fn},
        }


if __name__ == "__main__":
    print("Executing PCOS Benchmark Harness (1,000 Samples)...")
    runner = PCOSBenchmarkRunner()
    metrics = runner.run_benchmark(num_samples=1000)
    print("==================================================================")
    print("🏆 PCOS BENCHMARK RESULTS")
    print("==================================================================")
    print(f"Total Evaluated Samples : {metrics['num_samples']}")
    print(f"Fatal Hallucination Rate: {metrics['FHR_percent']:.2f}% (Target: 0.00%)")
    print(f"Over-Pruning Rate (OPR) : {metrics['OPR_percent']:.2f}%")
    print(f"Filter Decision Latency : {metrics['avg_filter_latency_ms']:.4f} ms")
    print(f"Confusion Matrix        : {metrics['confusion_matrix']}")
    print("==================================================================")
