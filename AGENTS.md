# Codex Research Wiki Contract

This vault is a dedicated, source-backed research wiki for Codex + Obsidian.

## Mission

Codex maintains a persistent wiki that sits between raw source files and query-time answers. The wiki is the compiled knowledge artifact. Raw files are the source of truth. The user curates sources and reviews high-value edits. Codex performs the bookkeeping.

## Write Scope

Codex may edit only:

- `wiki/`
- `index.md`
- `log.md`
- `templates/`
- `scripts/` when explicitly requested

Codex must not modify:

- `raw/` contents after import, except filename normalization or moving files from `inbox/` into `raw/sources/`
- user-authored notes outside this vault

## Top-Level Layout

- `inbox/`: drop zone for newly added files before ingest
- `raw/sources/`: immutable imported source files
- `raw/assets/`: downloaded local images or attachments associated with sources
- `wiki/overview/`: top-level summaries and project thesis pages
- `wiki/topics/`: concept or subject pages
- `wiki/entities/`: people, organizations, products, methods, datasets, places
- `wiki/source-notes/`: per-source extraction and evidence pages
- `wiki/analyses/`: durable answers created from user questions or lint passes
- `wiki/glossaries/`: terminology pages

## Naming Rules

- Source notes: `wiki/source-notes/YYYY-MM-DD-short-title.md`
- Analyses: `wiki/analyses/YYYY-MM-DD-question-slug.md`
- Topic and entity pages: stable kebab-case slugs
- Overviews: stable kebab-case slugs
- Prefer renaming raw source files into `YYYY-MM-DD-short-title.ext` on import when safe

## Page Types

Every page in `wiki/` must have YAML frontmatter with at least:

```yaml
title:
type:
status: draft|active|superseded
created:
updated:
sources: []
tags: []
confidence: low|medium|high
```

Allowed `type` values:

- `overview`
- `topic`
- `entity`
- `source-note`
- `analysis`
- `glossary`

## Required Sections By Page Type

### source-note

- `## Source Metadata`
- `## Executive Summary`
- `## Key Claims`
- `## Evidence and Excerpts`
- `## Entities and Topics to Update`
- `## Open Questions`

### topic / entity

- `## Summary`
- `## Current Understanding`
- `## Evidence Base`
- `## Related Pages`
- `## Open Questions / Tensions`

### analysis

- `## Question`
- `## Short Answer`
- `## Supporting Synthesis`
- `## Citations`
- `## Follow-Up Updates`

### overview

- `## Scope`
- `## Current Thesis`
- `## Key Pages`
- `## Evidence Base`
- `## Open Questions / Tensions`

### glossary

- `## Terms`
- `## Related Pages`

## Citation Policy

- Every substantive factual claim in an agent-written page must cite one or more `source-note` pages.
- Cite internal pages with Obsidian wikilinks, for example `[[2026-04-07-transformers-survey]]`.
- Do not cite raw files directly from synthesis pages.
- `source-note` pages must contain the mapping back to the raw file path, original URL when available, publication metadata, and page or section references when available.
- If a statement is an inference instead of a direct claim from a source, label it explicitly as `Inference:`.

## Conflict Handling

- Never silently overwrite older claims when sources disagree.
- Record disagreements in `## Open Questions / Tensions`.
- Keep both sides cited until the user or stronger evidence resolves the issue.
- Mark superseded pages or sections explicitly rather than deleting historical context without explanation.

## Duplicate Control

- Prefer updating an existing canonical page over creating a near-duplicate.
- Before creating a new topic or entity page, search `index.md` and the relevant `wiki/` directory for an existing page.
- If a duplicate exists, merge into the canonical page and note the merge in `log.md`.

## Core Workflows

### Ingest

1. Check `inbox/` and identify one source to process.
2. Normalize the filename if needed and move it into `raw/sources/`.
3. Read the source and create exactly one `source-note`.
4. Update affected `topic`, `entity`, and `overview` pages.
5. Update `index.md`.
6. Append an `ingest` entry to `log.md`.
7. Summarize touched pages for user review before continuing to the next source.

### Query

1. Read `index.md` first.
2. Read the relevant wiki pages.
3. Read source notes only as needed.
4. Answer from the wiki, using citations.
5. If the answer creates durable knowledge, write an `analysis` page and link it from relevant pages.

### Lint

Check for:

- orphan pages
- uncited claims
- duplicate or near-duplicate pages
- stale pages with newer contradicting sources
- unresolved `Open Questions / Tensions`
- missing backlinks from pages listed in `sources`

Write lint results as a dated analysis page and append a `lint` entry to `log.md`.

### Refactor

Codex may:

- split oversized wiki pages
- merge duplicate wiki pages
- repair broken internal links
- improve page summaries without reducing citation quality

Codex must preserve stable slugs where possible and log meaningful refactors.

## Review Discipline

- Human-in-the-loop is the default.
- Pause after each ingest batch and report:
  - source-note created
  - pages touched
  - contradictions found
  - open questions surfaced
- Do not run large unattended ingestion unless the user explicitly requests it.

## Index Contract

`index.md` is the primary navigation surface. It must:

- list active overviews, topics, entities, source notes, and analyses
- include a one-line summary for each page
- be kept current on every ingest and durable query

## Log Contract

`log.md` is append-only. Each entry heading must match:

- `## [YYYY-MM-DD HH:MM] ingest | Title`
- `## [YYYY-MM-DD HH:MM] query | Question`
- `## [YYYY-MM-DD HH:MM] lint | Scope`
- `## [YYYY-MM-DD HH:MM] refactor | Scope`

## Obsidian Conventions

- Use Obsidian wikilinks for all internal references.
- Keep pages Markdown-first and portable.
- Use frontmatter compatible with Dataview.
- Avoid proprietary formatting unless the user requests it.
