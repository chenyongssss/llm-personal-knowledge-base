---
title: Inference-Time Sampling Refinement
type: topic
status: active
created: 2026-04-07
updated: 2026-04-07
sources:
  - wiki/source-notes/2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling.md
tags:
  - sampling
  - inference-time
  - refinement
confidence: medium
---

# Inference-Time Sampling Refinement

## Summary

这个主题页收集“不改训练、只改采样”的改进思路。当前最主要的具体实例是 FDS，它在每个 solver step 之前对 intermediate state 做 local refinement，而不是重新训练 backbone。Evidence: [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]]

## Current Understanding

按当前全文证据，FDS 属于 sampling-time spatial refinement：它在固定 timestep t 下先生成若干个局部扰动候选，用 divergence surrogate 找到更可靠的中间状态，再交给原 solver 步进。这使它与高阶 solver 或 guidance 方法的关系更像“外接模块”，而不是替换 solver 的新采样器。Inference: 这个主题可以统一看成“在固定 pre-trained field 上，通过 inference-time state intervention 提升 fidelity”。 Evidence: [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]]

## Evidence Base

- [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]] - 用 divergence surrogate 驱动每步 refinement，并在多类任务上验证。

## Related Pages

- [[flow-matching]]
- [[flow-divergence-sampler]]

## Open Questions / Tensions

- refinement 的稳定性是否依赖于 backbone 已经“well-optimized”？这个前提在 FDS 中是明示的。
- divergence 计算的开销被控制在可接受范围内，但在更大 latent/video 模型上是否仍划算还未证实。
- 目前文中默认 `N=M=1`、early-stage only、cosine sigma，但这些调参是否具有跨任务稳定性仍待更多来源。
