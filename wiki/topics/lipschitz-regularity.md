---
title: Lipschitz Regularity
type: topic
status: active
created: 2026-04-08
updated: 2026-04-08
sources:
  - wiki/source-notes/2026-04-08-lipschitz-regularity-in-flow-matching-and-diffusion-models.md
tags:
  - theory
  - lipschitz
  - regularity
  - wasserstein
confidence: medium
---

# Lipschitz Regularity

## Summary

[[lipschitz-regularity]] 在当前 vault 里主要指 flow matching drift 和 diffusion score 的 one-sided / two-sided / time-Lipschitz 性质，以及这些性质如何进入稳定性、离散化误差和 transport map 理论。Evidence: [[2026-04-08-lipschitz-regularity-in-flow-matching-and-diffusion-models]]

## Current Understanding

当前证据表明，正则性不是一个纯技术附属条件，而是 generative ODE/SDE 理论里的中枢变量。one-sided Lipschitz 控制决定 Gronwall 型稳定性因子；two-sided Lipschitz 与 time-Lipschitz 界决定 Euler / Euler-Maruyama 的局部截断误差如何累积；而 `∫ λ_max(∇v_t) dt` 的可积控制还能推出 transport map 的全局 Lipschitz 性。Inference: 这意味着“drift regularity”在这条文献线里同时承担了数值分析、统计误差传播和概率泛函不等式三个角色。 Evidence: [[2026-04-08-lipschitz-regularity-in-flow-matching-and-diffusion-models]]

## Evidence Base

- [[2026-04-08-lipschitz-regularity-in-flow-matching-and-diffusion-models]] - 建立弱对数凹条件下的 sharp regularity bounds，并把它们转化为 flow matching / diffusion 的采样界。

## Related Pages

- [[flow-matching]]
- [[wiki/overview/research-overview|Research Overview]]

## Open Questions / Tensions

- exact drift 的正则性如何传导到 learned neural drift 的正则性，目前仍是理论闭环中的缺口。
- sharp discretization bounds 与“采样质量下降来自空间歧义而非离散化”的路线之间如何分工，还缺直接对话文献。
- 当前 topic 只有单篇理论来源，仍需补 Gao et al. (2024)、Zhou and Liu (2025)、Arsenyan et al. (2025) 等对照文献。
