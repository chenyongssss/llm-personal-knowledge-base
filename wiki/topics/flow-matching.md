---
title: Flow Matching
type: topic
status: active
created: 2026-04-07
updated: 2026-04-08
sources:
  - wiki/source-notes/2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling.md
  - wiki/source-notes/2026-04-08-lipschitz-regularity-in-flow-matching-and-diffusion-models.md
  - wiki/source-notes/2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space.md
tags:
  - generative-models
  - flow-matching
confidence: medium
---

# Flow Matching

## Summary

[[flow-matching]] 是一类通过学习 time-dependent velocity field，把简单先验分布运输到目标数据分布的生成建模框架。当前 vault 已经出现三条互补但尚未统一的阅读路径：sample-wise velocity ambiguity 与 inference-time refinement、exact drift regularity 与 Wasserstein sampling rates、以及 function-space / OT-guided flow matching。Evidence: [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]] [[2026-04-08-lipschitz-regularity-in-flow-matching-and-diffusion-models]] [[2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space]]

## Current Understanding

根据当前证据，FM 至少有三种不同切口。FDS 论文把一个核心失真来源解释为中间状态的 sample-wise velocity 冲突，因此提出 inference-time state refinement。Stéphanovitch 的理论论文强调 exact drift 的 one-sided / two-sided / time-Lipschitz 正则性，并据此给出几何网格上的 sharp `W2` 采样界。FOT-CFM 则把 FM 推进到 Hilbert 函数空间，并用 OT-aligned coupling 来减少 trajectory curvature、提升低 NFE 下的 function generation 质量。Inference: 这三条路线分别把 FM 看成“歧义修正问题”“正则性与离散化问题”“measure transport + operator learning 问题”；它们对应的误差分解和设计重点并不相同。 Evidence: [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]] [[2026-04-08-lipschitz-regularity-in-flow-matching-and-diffusion-models]] [[2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space]]

## Evidence Base

- [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]] - 给出 FDS 的动机、Theorem 1、算法设计与主实验。
- [[2026-04-08-lipschitz-regularity-in-flow-matching-and-diffusion-models]] - 给出 weakly log-concave 条件下的 sharp regularity 与 `W2` 采样界。
- [[2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space]] - 给出 Hilbert 空间中的 conditional-to-marginal 一致性、OT coupling 和 turbulence benchmarks。

## Related Pages

- [[flow-divergence-sampler]]
- [[inference-time-sampling-refinement]]
- [[lipschitz-regularity]]
- [[functional-flow-matching]]
- [[functional-optimal-transport-conditional-flow-matching]]
- [[wiki/overview/research-overview|Research Overview]]

## Open Questions / Tensions

- divergence surrogate、regularity bounds、trajectory curvature 这三种视角分别解释了 FM 误差的哪一部分，目前还没有统一图景。
- exact drift 的 sharp regularity 与 learned drift 的实际神经网络行为之间还隔着统计与优化层缺口。
- function-space FM 是否真的比高分辨率离散 FM 更有本质优势，还需要更多直接对照来源。
