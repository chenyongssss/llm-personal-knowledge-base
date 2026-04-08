---
title: Functional Optimal Transport Conditional Flow Matching
type: entity
status: active
created: 2026-04-08
updated: 2026-04-08
sources:
  - wiki/source-notes/2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space.md
tags:
  - method
  - flow-matching
  - optimal-transport
  - turbulence
confidence: medium
---

# Functional Optimal Transport Conditional Flow Matching

## Summary

[[functional-optimal-transport-conditional-flow-matching]]（FOT-CFM）是 Li 等人提出的 function-space flow matching 方法，面向 Hilbert 空间中的 turbulence field generation。它把 conditional flow matching、optimal transport 和 neural operators 结合起来，以获得更直的生成路径和更低的采样开销。Evidence: [[2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space]]

## Current Understanding

根据当前全文，FOT-CFM 的关键在于三个组件协同工作：第一，functional conditional path 和 marginal path 的 measure-theoretic 一致性，为训练目标提供严格基础；第二，mini-batch OT assignment 用于替换独立 coupling，使 source-target pairing 更接近 Wasserstein geodesic；第三，用 FNO 等 neural operators 学习 resolution-invariant 的连续算子。Inference: 这使 FOT-CFM 更像“OT-guided operator transport model”，而不只是把 flow matching 套到 PDE 数据上。 Evidence: [[2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space]]

## Evidence Base

- [[2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space]] - 方法定义、Theorem 3.1/3.2/3.3、算法流程与 turbulence 实验都来自该 source-note。

## Related Pages

- [[functional-flow-matching]]
- [[flow-matching]]

## Open Questions / Tensions

- Hungarian-based OT mini-batch coupling 在更大 batch / 3D turbulence 场景下的可扩展性如何，当前还未展示。
- 论文强调 lower curvature trajectories，但没有把 curvature 与离散化误差或 ambiguity 指标做更统一的理论联系。
- zero-shot super-resolution 的收益是否主要来自 neural operator 本身，而非 OT-guided FM，仍需更细 ablation。
