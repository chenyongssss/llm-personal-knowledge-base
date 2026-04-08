#!/usr/bin/env python3
"""Prepare a new source file for ingest into the research wiki."""

from __future__ import annotations

import argparse
import re
import shutil
from dataclasses import dataclass
from datetime import date
from pathlib import Path


SLUG_RE = re.compile(r"[^a-z0-9]+")


@dataclass
class PreparedSource:
    source_path: Path
    target_path: Path
    source_note_path: Path
    title: str
    slug: str


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = SLUG_RE.sub("-", text)
    return text.strip("-") or "untitled-source"


def derive_title(path: Path) -> str:
    return path.stem.replace("_", " ").replace("-", " ").strip() or "Untitled Source"


def prepare_source(vault_root: Path, input_path: Path, source_date: str | None = None) -> PreparedSource:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    datestr = source_date or date.today().isoformat()
    title = derive_title(input_path)
    slug = slugify(title)
    target_name = f"{datestr}-{slug}{input_path.suffix.lower()}"
    target_path = vault_root / "raw" / "sources" / target_name
    source_note_path = vault_root / "wiki" / "source-notes" / f"{datestr}-{slug}.md"

    return PreparedSource(
        source_path=input_path,
        target_path=target_path,
        source_note_path=source_note_path,
        title=title,
        slug=slug,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_path", help="Path to the new source file")
    parser.add_argument(
        "--vault-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Path to the vault root (defaults to parent of scripts/)",
    )
    parser.add_argument(
        "--date",
        dest="source_date",
        help="Date prefix for the imported file in YYYY-MM-DD format",
    )
    parser.add_argument(
        "--move",
        action="store_true",
        help="Move the file into raw/sources instead of only previewing the target path",
    )
    args = parser.parse_args()

    vault_root = Path(args.vault_root).resolve()
    input_path = Path(args.input_path).resolve()
    prepared = prepare_source(vault_root, input_path, args.source_date)

    print(f"Title: {prepared.title}")
    print(f"Slug: {prepared.slug}")
    print(f"Target source path: {prepared.target_path}")
    print(f"Suggested source-note path: {prepared.source_note_path}")

    if args.move:
        prepared.target_path.parent.mkdir(parents=True, exist_ok=True)
        if prepared.target_path.exists():
            raise FileExistsError(f"Target file already exists: {prepared.target_path}")
        shutil.move(str(prepared.source_path), str(prepared.target_path))
        print("Moved source file into raw/sources.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
