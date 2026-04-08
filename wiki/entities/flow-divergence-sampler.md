---
title: Flow Divergence Sampler
type: entity
status: active
created: 2026-04-07
updated: 2026-04-07
sources:
  - wiki/source-notes/2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling.md
tags:
  - method
  - sampling
  - divergence
confidence: medium
---

# Flow Divergence Sampler

## Summary

[[flow-divergence-sampler]]（FDS）是 Cha 等人在 arXiv:2604.04646 中提出的一种 flow matching inference-time refinement 方法。它不需要重新训练模型，而是在每次 solver step 之前，利用 pre-trained model divergence 对 intermediate state 做 spatial refinement。Evidence: [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]]

## Current Understanding

根据全文，FDS 的关键构件有三个：第一，用 Theorem 1 把 `L*_CFM(x_t,t)` 与 `∇·u_t(x_t)` 联系起来，为“用 divergence 找低歧义区域”提供理论依据；第二，用 `δ̂_t(x)=∇·u_theta(x,t)` 作为 inference-time surrogate，并用 Hutchinson trace estimator 做估计；第三，用零阶局部扰动搜索取代对 divergence 直接做二阶梯度优化。Inference: FDS 的实用性来自“理论 surrogate + 低成本 state search”的组合，而不只是把 divergence 加到现有 sampler 上。 Evidence: [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]]

## Evidence Base

- [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]] - 方法名、Theorem 1、Refine/SolverStep 框架、主实验与 ablation 都来自该 source-note。

## Related Pages

- [[flow-matching]]
- [[inference-time-sampling-refinement]]

## Open Questions / Tensions

- Theorem 1 和 surrogate 之间的差距对最终性能多敏感？本文给出直观支持，但缺少更强的误差分析。
- 单 noise vector 的 Hutchinson 估计在更大模型上是否会导致 surrogate 噪声过大？
- 该方法与更多 inference-time guidance / reward-based editing 方法的组合边界还未厘清。
