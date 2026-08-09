# Spoke 5: MAMS-161: A 9D Manifold of Human Motives

> **Hub Package**: `pcos_core_engine v32.0.0`  
> **Target Venues**: Journal of Personality / Nature Human Behaviour / Computational Psychiatry (`cs.AI` / `q-bio.OT`)  
> **Ecosystem Dependency**: Imports `crate_encoder` (Subspace Orthogonality $MCR^2$) from `pcos_core_engine` (Code overlap < 15%)

## Abstract & Motive Ontology Scope
This spoke introduces the Multi-Attractor Motive Structure (MAMS-161), mapping 161 human motive vectors onto 6 topological phase spaces ($\mathcal{S}_1 \sim \mathcal{S}_6$) in a 9D manifold. It anchors Big Five personality traits and NIMH RDoC frameworks into subspace orthogonal projections ($\text{Tr}(\mathbf{P}_i \mathbf{P}_j^T) \to 0.0000$).

## Key Files
- `mams161_ontology.json`: Formal JSON representation of the 161 motive ontology vectors and phase space topologies.
- `demo.py`: Manifold orthogonal projection and motive vector alignment script.

## Quick Execution
```bash
# Ensure Hub is installed locally
pip install -e .

# Run Spoke 5 Motive Manifold Demo
python spokes/spoke5_psy/demo.py
```
