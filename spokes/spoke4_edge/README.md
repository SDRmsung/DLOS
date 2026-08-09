# Spoke 4: 50MB Constant Edge EBM for ICD-11 Reasoning

> **Hub Package**: `pcos_core_engine v32.0.0`  
> **Target Venues**: ACM TECS / IEEE JBHI / TinyML (`cs.DC` / `cs.LG`)  
> **Ecosystem Dependency**: Imports `nesy_filter` (ICD_REDLINE_DICTIONARY) from `pcos_core_engine` (Code overlap < 10%)

## Abstract & Embedded Clinical Scope
This spoke demonstrates a resource-bounded ($S_{\text{learned}} = 36\text{ KB}, \text{RAM} \le 50\text{ MB}$) edge decision engine enforcing zero-byte Flash ROM clinical redline verification. It evaluates WHO ICD-11 redlines (such as Wilson Disease E83.0 and G6PD Deficiency D55.0) under sub-microsecond ($0.001\text{ ms}$) latency constraints on open clinical and nutrition datasets (Open Food Facts).

## Key Files
- `icd11_redlines.json`: WHO ICD-11 high-risk clinical redline rule matrix.
- `demo.py`: Edge execution latency and RAM footprint benchmark script.

## Quick Execution
```bash
# Ensure Hub is installed locally
pip install -e .

# Run Spoke 4 Edge Clinical Demo
python spokes/spoke4_edge/demo.py
```
