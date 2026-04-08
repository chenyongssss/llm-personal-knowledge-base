#!/usr/bin/env python3
"""Run lightweight structural checks over the research wiki."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[^\]]*)\]\]")
REQUIRED_FRONTMATTER_KEYS = {
    "title",
    "type",
    "status",
    "created",
    "updated",
    "sources",
    "tags",
    "confidence",
}


@dataclass
class Finding:
    level: str
    path: Path
    message: str


def parse_frontmatter(text: str) -> set[str]:
    if not text.startswith("---\n"):
        return set()
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return set()
    keys: set[str] = set()
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key = line.split(":", 1)[0].strip()
        if key:
            keys.add(key)
    return keys


def has_citation(text: str) -> bool:
    return bool(re.search(r"\[\[[^\]]+\]\]", text))


def collect_pages(vault_root: Path) -> list[Path]:
    return sorted((vault_root / "wiki").rglob("*.md"))


def build_slug_map(pages: list[Path]) -> dict[str, Path]:
    slug_map: dict[str, Path] = {}
    for page in pages:
        slug_map[page.stem] = page
    return slug_map


def lint_page(page: Path, slug_map: dict[str, Path]) -> tuple[list[Finding], set[str]]:
    text = page.read_text(encoding="utf-8")
    findings: list[Finding] = []

    keys = parse_frontmatter(text)
    missing = REQUIRED_FRONTMATTER_KEYS - keys
    if missing:
        findings.append(Finding("ERROR", page, f"Missing frontmatter keys: {', '.join(sorted(missing))}"))

    if "## " not in text:
        findings.append(Finding("WARN", page, "No section headings found"))

    if page.parent.name != "source-notes" and "No source notes yet." not in text and not has_citation(text):
        findings.append(Finding("WARN", page, "No obvious source-note citation found"))

    outbound: set[str] = set()
    for match in WIKILINK_RE.finditer(text):
        target = Path(match.group(1)).name
        target_stem = Path(target).stem
        outbound.add(target_stem)
        if target_stem not in slug_map and target_stem not in {"index", "log"}:
            findings.append(Finding("WARN", page, f"Broken wikilink target: {match.group(1)}"))

    return findings, outbound


def lint_wiki(vault_root: Path) -> list[Finding]:
    pages = collect_pages(vault_root)
    slug_map = build_slug_map(pages)
    all_findings: list[Finding] = []
    inbound_counts = {page.stem: 0 for page in pages}

    for page in pages:
        findings, outbound = lint_page(page, slug_map)
        all_findings.extend(findings)
        for target in outbound:
            if target in inbound_counts:
                inbound_counts[target] += 1

    for page in pages:
        if page.parent.name == "overview":
            continue
        if inbound_counts[page.stem] == 0:
            all_findings.append(Finding("INFO", page, "Orphan page with no inbound wikilinks"))

    return sorted(all_findings, key=lambda item: (item.level, str(item.path)))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--vault-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Path to the vault root (defaults to parent of scripts/)",
    )
    args = parser.parse_args()

    vault_root = Path(args.vault_root).resolve()
    findings = lint_wiki(vault_root)

    if not findings:
        print("No findings.")
        return 0

    for finding in findings:
        print(f"[{finding.level}] {finding.path.relative_to(vault_root)}: {finding.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
