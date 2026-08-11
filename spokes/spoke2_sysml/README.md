# Spoke 2: A SysML v2.0 Reference Implementation of Safety-Critical EBM

> **Hub Package**: `dual_loop_os_core_engine v32.0.0`  
> **Target Venues**: IEEE SMC / Journal of Systems and Software (`cs.SE`)  
> **Ecosystem Dependency**: Imports `crate_encoder` and `counterfactual_engine` from `dual_loop_os_core_engine` (Code overlap < 10%)

## Abstract & Systems Engineering Scope
This spoke establishes a formal Model-Based Systems Engineering (MBSE) traceability framework mapping IDEF0 subsystem decompositions ($A0 \sim A4$) to OMG SysML v2.0 / KerML 1.0 formal action blocks. It bridges Judea Pearl's Ladder L3 counterfactual query $P(Y_x \mid x', y)$ with automated SysML requirement verification.

## Key Files
- `models/Dual-Loop OS_Safety_MBSE.sysml`: Formal SysML v2.0 textual modeling specification for the Dual-Loop OS NeSy Sentinel.
- `demo.py`: Single-command standalone CPU verification script for MBSE action block execution.

## Quick Execution
```bash
# Ensure Hub is installed locally
pip install -e .

# Run Spoke 2 MBSE Verification
python spokes/spoke2_sysml/demo.py
```
