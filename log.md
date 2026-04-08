# Log

Append-only operational history for ingest, query, lint, and refactor actions.

## [2026-04-07 00:00] refactor | Vault initialization

Created the dedicated Codex + Obsidian research wiki scaffold, including the schema, index, log, templates, starter overview page, and local helper scripts.

## [2026-04-07 15:05] ingest | Training-Free Refinement of Flow Matching with Divergence-based Sampling

Ingested an abstract-level snapshot for arXiv:2604.04646. Created one raw source snapshot, one source-note, two topic pages, and one method entity page. Updated the research overview and index. Evidence boundary remains limited to public metadata and abstract text; full paper ingestion is still required.

## [2026-04-07 18:58] ingest | Training-Free Refinement of Flow Matching with Divergence-based Sampling (full PDF)

Moved the full PDF from `inbox/` to `raw/sources/2026-04-07-training-free-refinement-of-flow-matching-with-divergence-based-sampling.pdf` and upgraded the existing canonical source-note from abstract-level to full-paper absorption. Updated `[[flow-matching]]`, `[[inference-time-sampling-refinement]]`, `[[flow-divergence-sampler]]`, `[[wiki/overview/research-overview|Research Overview]]`, and `index.md`. No direct contradiction with the earlier abstract snapshot was found; the main change is that the previous open questions about theorem, algorithm shape, compute overhead, and task coverage are now partially resolved by the PDF.

## [2026-04-08 14:34] ingest | Lipschitz regularity in Flow Matching and Diffusion Models

Moved the PDF from `inbox/` to `raw/sources/2026-04-08-lipschitz-regularity-in-flow-matching-and-diffusion-models.pdf`. Created one source-note and one new topic page `[[lipschitz-regularity]]`, and updated `[[flow-matching]]`, `[[wiki/overview/research-overview|Research Overview]]`, and `index.md`. This source broadens the vault from inference-time refinement to exact-drift regularity and sampling-rate theory. It introduces a productive tension with the FDS line: one source emphasizes spatial ambiguity, while this one emphasizes sharp discretization control.

## [2026-04-08 14:38] ingest | Optimal-Transport-Guided Functional Flow Matching for Turbulent Field Generation in Hilbert Space

Moved the PDF from `inbox/` to `raw/sources/2026-04-08-optimal-transport-guided-functional-flow-matching-for-turbulent-field-generation-in-hilbert-space.pdf`. Created one source-note, one new topic page `[[functional-flow-matching]]`, and one new entity page `[[functional-optimal-transport-conditional-flow-matching]]`, then updated `[[flow-matching]]`, `[[wiki/overview/research-overview|Research Overview]]`, and `index.md`. This source extends the vault into Hilbert-space / function-valued flow matching, adding a third active line centered on OT-guided path straightening and neural-operator-based turbulence generation.
