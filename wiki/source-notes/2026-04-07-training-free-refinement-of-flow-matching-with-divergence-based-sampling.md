---
title: Training-Free Refinement of Flow Matching with Divergence-based Sampling
type: source-note
status: active
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/sources/2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling.pdf
  - raw/sources/2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling.md
tags:
  - flow-matching
  - sampling
  - inference-time
  - divergence
confidence: medium
---

# Training-Free Refinement of Flow Matching with Divergence-based Sampling

## Source Metadata

- Raw file: `raw/sources/2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling.pdf`
- Earlier abstract snapshot: `raw/sources/2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling.md`
- Original URL: https://arxiv.org/abs/2604.04646
- PDF URL: https://arxiv.org/pdf/2604.04646
- Project page: https://yeonwoo378.github.io/official_fds
- Authors: Yeonwoo Cha, Jaehoon Yoo, Semin Kim, Yunseo Park, Jinhyeon Kwon, Seunghoon Hong
- Publication date: 2026-04-06
- Source type: arXiv preprint
- Citation: Cha et al., "Training-Free Refinement of Flow Matching with Divergence-based Sampling", arXiv:2604.04646, 2026.
- Evidence boundary: This note is now based on the full 32-page PDF, including method, theory, main experiments, and appendices.

## Executive Summary

这篇论文提出 [[flow-divergence-sampler]]（FDS），目标是在不重训 flow model 的前提下，缓解 flow matching 在中间状态处因 sample-wise velocity 冲突而产生的采样歧义。论文的核心论点是：最优 CFM 残差，也就是 marginal velocity 与 sample-wise velocity 的条件均方差，可以写成 marginal velocity field divergence 的闭式表达，因此可在推理时用模型 divergence 作为可计算的 surrogate 来寻找“更少歧义”的邻近状态。FDS 的实现不是改 velocity field，而是在每个 solver step 前，对当前状态做局部随机扰动，选出 divergence 更低的候选点，再交给原本的 Euler / Heun 等 solver 继续积分。实验显示，在 CIFAR-10、ImageNet 256x256、SD3-M text-to-image，以及 inverse problems 上，FDS 在 matched wall-clock budget 下通常优于“单纯增加 NFE”的基线。Evidence: [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]]

## Key Claims

- Claim: flow matching 的根本局限之一是，在同一中间状态处，多条 sample-wise velocity 可能互相冲突，而模型只能学习它们的条件均值，因此轨迹可能被推向低密度区域。  
  Source-note citation: [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]]

- Claim: 最优 CFM 残差 `E[||u_t(x_t)-v_t||^2 | x_t]` 可写成 marginal velocity field divergence 的闭式表达；对固定 `t` 而言，最小化该残差等价于最小化空间 divergence。  
  Source-note citation: [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]]

- Claim: 实际推理时，作者用预训练模型 `u_theta` 的 divergence `∇·u_theta(x,t)` 作为 data-free surrogate，并用 Hutchinson trace estimator 估计该量。  
  Source-note citation: [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]]

- Claim: FDS 是一个 training-free、plug-and-play 的 state refinement 模块；它通过零阶局部搜索而非二阶梯度优化来规避大模型上的二阶导开销。  
  Source-note citation: [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]]

- Claim: 在主实验中，FDS 在 CIFAR-10、ImageNet256x256、text-to-image 和 inverse problems 上都带来更好的 fidelity；并且在 matched wall-clock budget 下通常优于额外增加 solver steps。  
  Source-note citation: [[2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling]]

## Evidence and Excerpts

- Section or page: pp. 1-2, Introduction  
  Notes: 论文明确把问题定位为 sample-wise velocity 在同一中间状态处发生 directional conflicts，导致 marginal velocity 指向低密度区域；作者强调目标是“在 inference time 修正 trajectory，而不是重估速度场”。

- Section or page: pp. 3-4, Preliminaries  
  Notes: 论文把 CFM 最优解写成 `u_t(x_t)=E[v_t | x_t]`，并把 discrepancy 定义为 `L*_CFM(x_t,t)=E[||u_t(x_t)-v_t||^2 | x_t]`，明确区分了 marginal velocity 与 sample-wise velocity。

- Section or page: p. 5, Theorem 1  
  Notes: 论文给出 `L*_CFM` 与 `∇·u_t(x_t)` 的关系式，并据此提出 inference-time surrogate `δ̂_t(x)=∇·u_theta(x,t)`。这是 FDS 理论动机的关键支点。

- Section or page: pp. 5-6, Method  
  Notes: FDS 不直接对 divergence 做二阶梯度下降，而是对当前状态采样 `M` 个局部扰动候选，选 divergence 最小者，并可重复 `N` 次 refinement。作者将这一过程写成 `Refine -> SolverStep` 的外接式流水线。

- Section or page: p. 6, Computational Overhead  
  Notes: 作者声称 `N=M=1` 已足够有效，并将 refinement 限制在早期生成阶段 `t < T_trunc`，默认 `T_trunc = 0.5`，以控制额外开销。

- Section or page: pp. 9-12, Main Experiments  
  Notes: 表 1 显示在 50/99 NFE 配置下，FDS 相比 compute-matched baseline 有更好的 FID。例如 ImageNet256x256 + JiT-L/16 + Heun: baseline 2.713，matched baseline 2.886，Heun + FDS 2.496。

- Section or page: p. 11, Text-to-Image  
  Notes: 在 SD3-M + DrawBench 上，FDS 在 CFG 3 和 CFG 7 下大多提升 IR / HPSv2 / CLIP 等指标，说明该方法并不局限于 class-conditional image generation。

- Section or page: p. 12, Inverse Problems  
  Notes: 在 Gaussian deblurring 和 SR x4 上，TFG + FDS 都优于 TFG，表明该模块可与 test-time guidance 组合。

- Section or page: pp. 13-14, Ablation  
  Notes: 结果支持“早期 refinement 更重要”“cosine sigma schedule 更优”“`N=M=1` 已是性价比较高默认值”这三个实现判断。

- Section or page: p. 23, Appendix C.2  
  Notes: 论文用单个 Hutchinson noise vector 估计 divergence；throughput 以单张 RTX A6000、batch size 32、64 次独立迭代的平均时间做 matched baseline。

## Entities and Topics to Update

- Topics:
  - [[flow-matching]]
  - [[inference-time-sampling-refinement]]
- Entities:
  - [[flow-divergence-sampler]]

## Open Questions

- Theorem 1 的推导依赖哪些关于 interpolant、schedule 或可微性的假设，是否会限制它在 rectified / stochastic flow 变体上的适用性？
- 论文把 divergence 视为 discrepancy surrogate，但目前证据主要来自这个方法族内部；它是否能外推到更广泛的 flow backbones 仍待更多来源验证。
- Inference: FDS 解决的主要是“空间歧义”而不是“时间离散误差”，因此它与高阶 solver 更像互补而不是替代。这个判断在本文实验中成立，但还需要更多交叉文献来稳固。
- 在大规模 latent-space flow 或视频 flow 上，单噪声 Hutchinson 估计是否仍足够稳定，本文没有给出更细的方差分析。
