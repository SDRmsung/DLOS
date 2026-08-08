---
id: area_node_20260808
title: 未命名
aliases:
  - 未命名
description: SYS|TEMPLATE|TPL|SKELETON_STRUCTURE
tags:
  - moc
  - state/raw
type: wiki_moc
compiler_status: template
created: 2026-08-08
updated: 2026-08-08
parent: []
related: []
agent_harness:
  trigger:
    - on_read
    - on_link
  actions:
    - summarize
    - extract_tasks
  boundary:
    - max_tokens: 800
    - mode: read_only
    - require_status: stable
---


PCOS/
├── README.md                          # 創投/專家導向之頂級開源 README (含 1-Click Colab 標籤 & GIF Demo)
├── LICENSE                            # Apache-2.0 / MIT 授權條款
├── setup.py / pyproject.toml          # 支援 pip install pcos-latent 快速安裝
├── pcos_core_engine/                  # V30 五大核心 ML 模組套件
│   ├── __init__.py
│   ├── nesy_filter.py                 # (Contribution 3) 確定性對數勢壘與 STE 門
│   ├── crate_encoder.py               # (Contribution 2) MCR^2 子空間幾何分離與有效秩計算
│   ├── jepa_predictor.py              # (Contribution 1) JEPA 潛在預測能量最小化
│   ├── counterfactual_engine.py       # (Contribution 4) 因果干預與 L3 反事實引擎
│   ├── comprehensive_causal_ood_benchmark.py
│   ├── v30_p0_experiments.py          # (P0-1 ~ P0-6) 6 大 P0 重現實驗腳本
│   └── demo_colab.py                  # 0.5 秒 CPU 一鍵式 Reproducibility Demo
├── 35-Areas/.../Papers/
│   ├── 整體/JEPA_ALL_30.md            # V30 最終相機就緒論文 (Main Paper + Appendices)
│   └── 論文審查/Response_to_Review_v12.md