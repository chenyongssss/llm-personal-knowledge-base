# Index

This is the primary navigation page for the research wiki. Codex should read this file first when answering questions or planning updates.

## Overviews

- [[wiki/overview/research-overview|Research Overview]] - Top-level scope, thesis, and active lines of inquiry for this vault.

## Topics

- [[wiki/topics/flow-matching|Flow Matching]] - 围绕 velocity ambiguity、drift regularity、trajectory curvature 与采样误差的主题页。
- [[wiki/topics/inference-time-sampling-refinement|Inference-Time Sampling Refinement]] - 收集不改训练、在 inference-time 对 intermediate state / sampling path 做修正的方法。
- [[wiki/topics/lipschitz-regularity|Lipschitz Regularity]] - 收集 drift / score 的 one-sided、two-sided 与 time-Lipschitz 理论及其采样后果。
- [[wiki/topics/functional-flow-matching|Functional Flow Matching]] - 收集 Hilbert / function-space 中的 flow matching、Neural Operators 与 OT coupling。

## Entities

- [[wiki/entities/flow-divergence-sampler|Flow Divergence Sampler]] - FDS 方法页，当前已吸收全文理论、算法与主实验。
- [[wiki/entities/functional-optimal-transport-conditional-flow-matching|Functional Optimal Transport Conditional Flow Matching]] - FOT-CFM 方法页，聚焦函数空间 OT-guided turbulence generation。

## Source Notes

- [[wiki/source-notes/2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling|Training-Free Refinement of Flow Matching with Divergence-based Sampling]] - FDS 论文的全文吸收，包含 Theorem 1、Refine 算法、主实验与 ablation。
- [[wiki/source-notes/2026-04-08-lipschitz-regularity-in-flow-matching-and-diffusion-models|Lipschitz regularity in Flow Matching and Diffusion Models]] - weakly log-concave 条件下的 sharp regularity、`W2` 采样界与函数不等式。
- [[wiki/source-notes/2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space|Optimal-Transport-Guided Functional Flow Matching for Turbulent Field Generation in Hilbert Space]] - function-space conditional-to-marginal 理论、OT coupling 与 turbulence benchmarks。

## Analyses

- None yet.

## Glossaries

- None yet.

## Stubs Needing Development

- 吸收 FFM、DDO 与 function-space generative modeling 的前置对照文献。
- 吸收 HRF、VRFM、CAF、Gao et al. (2024)、Zhou and Liu (2025)、Arsenyan et al. (2025) 等 ambiguity / regularity / sampling-rate 对照论文。
