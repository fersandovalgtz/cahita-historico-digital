#!/usr/bin/env python3
"""Check relative Markdown links in the public CHD documentation surface."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DOCS = [
    "README.md",
    "README.en.md",
    "DATASHEET.md",
    "QUALITY_REPORT.md",
    "FAIR_ASSESSMENT.md",
    "GOVERNANCE.md",
    "CONTRIBUTORS.md",
    "CONTRIBUTING.md",
    "SCHEMA.md",
    "SCIENTIFIC_REPOSITORY_STANDARD.md",
    "SECURITY.md",
    "LICENSING.md",
    "docs/README.md",
    "docs/DATA_PRODUCTS.md",
    "docs/REPRODUCIBILITY.md",
    "docs/ECOSYSTEM.md",
    "docs/RELEASE_PUBLICATION_2026-08-22.md",
]

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def normalized_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip()
    if not target:
        return None
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    # Drop optional Markdown title: (file.md "title"). Public CHD docs do not
    # intentionally use spaces in relative paths.
    if " \"" in target:
        target = target.split(" \"", 1)[0]
    target = unquote(target.split("#", 1)[0])
    if not target:
        return None
    return (source.parent / target).resolve()


def main() -> None:
    errors: list[str] = []
    checked = 0
    for rel in PUBLIC_DOCS:
        source = ROOT / rel
        if not source.exists():
            errors.append(f"missing public document: {rel}")
            continue
        text = source.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = normalized_target(source, match.group(1))
            if target is None:
                continue
            checked += 1
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{rel}: relative link escapes repository: {match.group(1)!r}")
                continue
            if not target.exists():
                errors.append(f"{rel}: broken local link: {match.group(1)!r}")

    if errors:
        raise SystemExit("documentation link QA failed:\n- " + "\n- ".join(errors))
    print(f"documentation link QA OK: documents={len(PUBLIC_DOCS)}; localLinksChecked={checked}")


if __name__ == "__main__":
    main()
