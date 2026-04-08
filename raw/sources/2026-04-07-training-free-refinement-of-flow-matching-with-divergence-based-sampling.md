# Raw Source Snapshot

- Title: Training-Free Refinement of Flow Matching with Divergence-based Sampling
- arXiv ID: 2604.04646
- Authors: Yeonwoo Cha, Jaehoon Yoo, Semin Kim, Yunseo Park, Jinhyeon Kwon, Seunghoon Hong
- Source URL: https://arxiv.org/abs/2604.04646
- Discovery URL: https://arxiv-troller.com/?q=paper%3A+2602.08318
- Snapshot date: 2026-04-07
- Evidence boundary: This raw source file is a metadata and abstract snapshot created from publicly accessible web results. Full PDF or HTML was not ingested yet.

## Abstract Snapshot

Flow-based models learn a target distribution by modeling a marginal velocity field, defined as the average of sample-wise velocities connecting each sample from a simple prior to the target data. When sample-wise velocities conflict at the same intermediate state, however, this averaged velocity can misguide samples toward low-density regions, degrading generation quality. To address this issue, the paper proposes the Flow Divergence Sampler (FDS), a training-free framework that refines intermediate states before each solver step. The abstract claims that the severity of this misguidance is quantified by the divergence of the marginal velocity field, which is readily computable during inference with a well-optimized model. FDS uses this signal to steer states toward less ambiguous regions and is described as plug-and-play with standard solvers and off-the-shelf flow backbones. The abstract further claims improvements across generation tasks including text-to-image synthesis and inverse problems.
