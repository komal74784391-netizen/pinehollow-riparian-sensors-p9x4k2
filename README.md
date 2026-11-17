# Riparian Microclimate Toolkit

Companion code for the paper **Sparse Sensor Placement for Riparian
Microclimate Reconstruction** (Journal of Ecohydrological Informatics).

Stable release: **v1.0.2** (2026-02-10). The toolkit includes the greedy
placement solver, field preprocessing utilities and evaluation scripts used in
the paper.

## Install

```bash
pip install -r requirements.txt
```

## Reproduce the paper results

```bash
python scripts/train_placement.py --config configs/field_sites.yaml
python scripts/evaluate_shading.py --split heldout
```
