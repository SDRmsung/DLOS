# -*- coding: utf-8 -*-
"""
PCOS Core Engine Package
========================
White-box personal decision intelligence framework integrating NeSy Log-Barrier Filtering,
Pearl Graph Surgery Rule 2/3, CRATE MCR^2 Representation Learning, JEPA Latent Predictor Energy Minimization,
Pearl Ladder L3 AAAK Counterfactual Reasoning, Effective Rank Non-Collapse Proof, Independent N=1,000 Clinical Matrix,
Factorial Ablation Engine, Synthetic SCM Causal Benchmark, 8-Dimension OOD Suite, V30 6-P0 Experimental Suite, and SOTA Baselines.
"""

from .nesy_filter import NeSySafetyFilter, ICD_REDLINE_DICTIONARY
from .crate_encoder import WhiteBoxCRATEEncoder
from .jepa_predictor import JEPALatentPredictor, TriTermEnergyMinimizer
from .counterfactual_engine import AAAKL3CounterfactualEngine
from .ebm_baselines import EBM_BASELINES, generate_independent_clinical_ground_truth, ExtendedBenchmarkEvaluator
from .rank_and_guardrail_baselines import compute_effective_rank, GUARDRAIL_BASELINES
from .confusion_matrix_evaluator import IndependentClinicalSubsetEvaluator
from .comprehensive_causal_ood_benchmark import SyntheticSCMCausalBenchmark, FactorialAblationEngine, OODAdversarialBenchmark
from .v30_p0_experiments import V30P0ExperimentSuite
from .benchmark_harness import PCOSBenchmarkRunner

__version__ = "30.0.0"
__all__ = [
    "NeSySafetyFilter",
    "ICD_REDLINE_DICTIONARY",
    "WhiteBoxCRATEEncoder",
    "JEPALatentPredictor",
    "TriTermEnergyMinimizer",
    "AAAKL3CounterfactualEngine",
    "EBM_BASELINES",
    "generate_independent_clinical_ground_truth",
    "ExtendedBenchmarkEvaluator",
    "compute_effective_rank",
    "GUARDRAIL_BASELINES",
    "IndependentClinicalSubsetEvaluator",
    "SyntheticSCMCausalBenchmark",
    "FactorialAblationEngine",
    "OODAdversarialBenchmark",
    "V30P0ExperimentSuite",
    "PCOSBenchmarkRunner",
]
