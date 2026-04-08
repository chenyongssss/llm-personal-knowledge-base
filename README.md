# LLM Personal Knowledge Base

A source-backed personal knowledge system for research-heavy workflows, built around **Codex + Obsidian**.

This project is not a generic note dump and not a chat transcript archive. It is a structured vault for turning papers, PDFs, web captures, and question-driven synthesis into a durable, inspectable, and cross-linked knowledge base.

## What this project is for

Most AI-assisted reading workflows have a failure mode: useful insights stay trapped inside temporary chats.

This repository is designed to solve that by separating:

- **raw source material** from
- **agent-maintained wiki pages** from
- **operational logs and navigation pages**.

The intended result is a personal knowledge base that can:

- absorb new papers incrementally;
- preserve evidence boundaries;
- support question answering from accumulated notes;
- keep long-term topic pages updated instead of rewriting everything from scratch;
- remain readable and editable in plain Markdown.

## Core idea

The workflow is built on three layers:

1. **Sources** — immutable imported material such as PDFs, Markdown exports, notes, or HTML snapshots.
2. **Wiki** — curated pages that distill sources into topic pages, entity pages, source notes, and durable analyses.
3. **Operations** — index, log, templates, and scripts that make the system maintainable over time.

Codex acts as the maintenance layer:

- ingesting new material,
- updating affected pages,
- keeping links and metadata consistent,
- answering questions from the wiki,
- and writing durable analysis pages when useful.

Obsidian acts as the human-facing layer:

- browsing,
- linking,
- reviewing edits,
- and maintaining a navigable long-term knowledge graph.

## Repository structure

```text
.
├── AGENTS.md                 # Operational contract for Codex / agent behavior
├── README.md                 # English project overview
├── README.zh-CN.md           # Chinese companion README
├── index.md                  # Primary navigation page
├── log.md                    # Append-only ingest / query / lint / refactor log
├── inbox/                    # Drop zone for newly added materials
├── raw/
│   ├── sources/              # Imported source files (treated as immutable)
│   └── assets/               # Local images / attachments tied to sources
├── scripts/
│   ├── new_source.py         # Source normalization helper
│   └── lint_wiki.py          # Structural wiki checks
├── templates/                # Templates for source-note / topic / entity / analysis / glossary
└── wiki/
    ├── overview/             # Research scope and thesis pages
    ├── topics/               # Topic pages
    ├── entities/             # Methods / datasets / people / organizations / artifacts
    ├── source-notes/         # Per-source evidence pages
    ├── analyses/             # Durable question-driven synthesis pages
    └── glossaries/           # Terminology pages
```

## Design principles

### 1. Sources stay separate from synthesis

Raw files are the source of truth. Synthesis pages should cite `source-note` pages rather than citing raw files directly.

### 2. Evidence boundaries must remain visible

If a page is based only on an abstract, metadata snapshot, or partial reading, it should say so explicitly.

### 3. Canonical pages beat duplicated summaries

The goal is to accumulate knowledge into stable topic/entity pages, not to create a new disconnected note for every interaction.

### 4. Durable answers belong in the vault

If a question produces a useful answer that will matter again, it should be written into `wiki/analyses/` instead of living only in chat history.

### 5. Markdown first

Everything should remain inspectable in plain text, git-friendly, and Obsidian-compatible.

## Typical workflow

### 1. Add a new source

Put a new file into `inbox/`.

Examples:

- a paper PDF;
- an arXiv abstract snapshot;
- a manually saved web page;
- a Markdown export from another tool.

### 2. Prepare or normalize the source

Use the helper script if needed:

```bash
python scripts/new_source.py inbox/some-paper.pdf --move
```

This suggests a normalized filename and, with `--move`, moves the file into `raw/sources/`.

### 3. Ask Codex to ingest it

A typical ingest task should:

- create exactly one `source-note`;
- update the relevant `topic`, `entity`, and `overview` pages;
- update `index.md`;
- append an ingest entry to `log.md`.

### 4. Ask questions against the wiki

Examples:

- What is the core claim of this paper?
- How does this method differ from prior work already in the vault?
- What open questions remain across the current topic pages?

The preferred behavior is to answer from the wiki first, then expand into source notes as needed.

### 5. Run lint periodically

```bash
python scripts/lint_wiki.py
```

This checks for:

- missing frontmatter keys,
- missing section headings,
- obvious missing citations,
- broken wikilinks,
- orphan pages with no inbound links.

## Included local helpers

### `scripts/new_source.py`

Purpose:

- derive a normalized title and slug;
- suggest the final file path in `raw/sources/`;
- suggest the corresponding `source-note` path;
- optionally move the file into place.

### `scripts/lint_wiki.py`

Purpose:

- verify minimum frontmatter requirements;
- catch broken or missing internal links;
- identify pages that look uncited;
- detect orphan pages.

It is intentionally lightweight. It does **not** replace human review.

## Page model

The vault distinguishes several page types:

- **overview** — high-level scope and thesis pages;
- **topic** — conceptual or problem-domain pages;
- **entity** — concrete methods, models, datasets, authors, or organizations;
- **source-note** — evidence pages tied to a single source;
- **analysis** — durable question-driven synthesis pages;
- **glossary** — terminology pages.

Each wiki page is expected to carry YAML frontmatter and follow a standard section structure. See `AGENTS.md` for the full contract.

## Recommended prompt patterns

Examples of useful prompts when working with Codex:

- `Please ingest the new source in inbox/ and update the affected pages.`
- `Answer this question from the wiki first, then inspect source-notes only if needed.`
- `Turn this answer into a durable analysis page.`
- `Run a lint-style review and tell me which pages are too thin or weakly supported.`
- `Check whether this topic already has a canonical page before creating a new one.`

## What makes this different from ordinary note-taking

This repository is optimized for **knowledge maintenance**, not just knowledge capture.

That means it emphasizes:

- stable canonical pages,
- explicit source provenance,
- append-only operational history,
- agent-readable rules,
- and long-term reuse of prior synthesis.

In short: this is closer to a **personal research wiki** or **external memory system** than a notebook.

## Current status

The repository already contains a small but real research corpus with:

- topic pages,
- entity pages,
- source notes,
- a research overview,
- an operational log,
- and helper scripts.

It is still an early-stage knowledge base, but the structure is intended to scale as more sources are ingested.

## Public-sharing note

If you publish or open-source a vault built from this scaffold, review it carefully before pushing:

- remove private notes;
- remove local-only instructions you do not want to publish;
- verify that imported source files can be shared publicly;
- check whether any raw PDFs or proprietary materials should remain local-only.

## License / usage

No explicit license is included by default. Add one before public distribution if needed.

## Related files

- `AGENTS.md` — operating contract for Codex / agent maintenance
- `index.md` — main entry point for navigation and answering
- `log.md` — append-only operational history
- `templates/` — page templates
- `scripts/` — local helper scripts

---

If you want a Chinese explanation of the project, see [`README.zh-CN.md`](README.zh-CN.md).
