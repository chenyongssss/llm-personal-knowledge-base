---
title: Functional Flow Matching
type: topic
status: active
created: 2026-04-08
updated: 2026-04-08
sources:
  - wiki/source-notes/2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space.md
tags:
  - flow-matching
  - function-space
  - hilbert-space
  - neural-operators
confidence: medium
---

# Functional Flow Matching

## Summary

[[functional-flow-matching]] 指把 flow matching 从有限维向量空间推广到函数空间 / Hilbert 空间，在概率测度、弱连续性方程和算子学习的层面定义 generative flow。Evidence: [[2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space]]

## Current Understanding

当前证据显示，functional flow matching 不是简单把图像 FM 换成更大的 tensor，而是要重写几项基础构件：路径混合不再依赖有限维 density，而要在 measure level 上定义；向量场参数化不再是普通网络，而偏向 Neural Operators；噪声也不再是“白噪声像素张量”，而是良定义的函数空间 Gaussian measure。FOT-CFM 进一步表明，在这类 setting 下，OT-aligned coupling 能把 function-space generative paths 拉直，从而降低采样 NFE。Inference: 功能空间 FM 更像“measure transport + operator learning”的结合，而不是传统 FM 的直接高维化。 Evidence: [[2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space]]

## Evidence Base

- [[2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space]] - 给出 Hilbert 空间中的 conditional-to-marginal 一致性、OT mini-batch coupling 与 turbulence benchmarks。

## Related Pages

- [[flow-matching]]
- [[functional-optimal-transport-conditional-flow-matching]]
- [[wiki/overview/research-overview|Research Overview]]

## Open Questions / Tensions

- 功能空间 FM 是否真的比高分辨率离散 tensor FM 更有归纳优势，目前还缺直接 ablation。
- function-space OT coupling 带来的直线路径优势，和理论 regularity / discretization 界之间如何对应，当前还没打通。
- 当前 topic 只有一篇来源，仍需补 FFM、DDO 等前置论文作为对照。
