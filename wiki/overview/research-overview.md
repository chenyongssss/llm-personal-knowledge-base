---
title: Research Overview
type: overview
status: active
created: 2026-04-07
updated: 2026-04-08
sources: []
tags:
  - overview
confidence: medium
---

# Research Overview

## Scope

This page tracks the active scope, high-level thesis, and major open questions for the vault.

## Current Thesis

当前 vault 已从单一方法论文扩展为一个更完整的问题簇：**flow matching 的生成误差来自哪里，以及不同理论/方法工具如何描述并修正它**。现有三条主线分别是：FDS 路线把重点放在中间状态的 velocity 歧义与空间修正；Lipschitz regularity 路线把重点放在 exact drift 的正则性、几何网格离散化和 `W2` 采样率；FOT-CFM 路线则把 FM 推到 Hilbert 函数空间，并把 OT coupling 与 neural operators 结合来降低 trajectory curvature。Evidence: [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]] [[2026-04-08-lipschitz-regularity-in-flow-matching-and-diffusion-models]] [[2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space]]

## Key Pages

- `index.md`
- `log.md`
- [[flow-matching]]
- [[inference-time-sampling-refinement]]
- [[lipschitz-regularity]]
- [[functional-flow-matching]]
- [[flow-divergence-sampler]]
- [[functional-optimal-transport-conditional-flow-matching]]

## Evidence Base

- [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]] - 代表 inference-time spatial refinement 路线。
- [[2026-04-08-lipschitz-regularity-in-flow-matching-and-diffusion-models]] - 代表 regularity / discretization / functional inequalities 理论路线。
- [[2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space]] - 代表 function-space OT-guided flow matching 路线。

## Open Questions / Tensions

- flow matching 的主要误差源是 sample-wise velocity 冲突、时间离散化、trajectory curvature、还是这些因素叠加？
- exact drift 的正则性理论怎样转化为 learned neural drift 的 end-to-end 保证？
- 需要继续吸收 FFM、DDO、HRF、VRFM、CAF、Gao et al. (2024)、Arsenyan et al. (2025) 等对照文献，才能把当前三条主线真正接起来。
