#!/usr/bin/env python3
"""Export a deterministic inventory of explicit historical cross-references.

This is deliberately *not* a destination resolver. It preserves markerRaw and
targetRaw exactly as structured in the canonical article layer and adds only a
small derived marker class so `Buſca` references can be counted reliably.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ARTICLE_DIR = ROOT / "data/lexicon/articles"

JSONL_NAME = "chd_lexicon_crossreferences.jsonl"
CSV_NAME = "chd_lexicon_crossreferences.csv"
MANIFEST_NAME = "manifest.json"

CSV_FIELDS = [
    "sourceArticleId",
    "sourcePageDigital",
    "sourceColumn",
    "sourceGuideRaw",
    "sourceArticleType",
    "crossReferenceIndex",
    "markerRaw",
    "markerClass",
    "targetRaw",
    "relation",
]


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def article_number(article_id: str) -> int:
    return int(article_id.rsplit("-", 1)[1])


def marker_class(marker_raw: str) -> str:
    normalized = " ".join(marker_raw.replace("ſ", "s").casefold().split())
    return "busca" if normalized == "busca" else "other"


def load_inventory() -> tuple[list[dict[str, Any]], int, list[str]]:
    rows: list[dict[str, Any]] = []
    article_count = 0
    source_files: list[str] = []

    for path in sorted(ARTICLE_DIR.glob("*.jsonl")):
        source_files.append(path.relative_to(ROOT).as_posix())
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                article = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSON in {path}:{line_number}: {exc}") from exc
            article_count += 1
            refs = article.get("crossReferences") or []
            for index, ref in enumerate(refs):
                marker = ref.get("markerRaw")
                target = ref.get("targetRaw")
                if not isinstance(marker, str) or not marker:
                    raise SystemExit(
                        f"invalid cross-reference marker in {article.get('articleId')} index {index}"
                    )
                if not isinstance(target, str) or not target:
                    raise SystemExit(
                        f"invalid cross-reference target in {article.get('articleId')} index {index}"
                    )
                rows.append(
                    {
                        "sourceArticleId": article["articleId"],
                        "sourcePageDigital": article.get("sourcePageDigital"),
                        "sourceColumn": article.get("column"),
                        "sourceGuideRaw": article.get("spanishGuideRaw"),
                        "sourceArticleType": article.get("articleType"),
                        "crossReferenceIndex": index,
                        "markerRaw": marker,
                        "markerClass": marker_class(marker),
                        "targetRaw": target,
                        "relation": ref.get("relation"),
                    }
                )

    rows.sort(key=lambda row: (article_number(row["sourceArticleId"]), row["crossReferenceIndex"]))
    return rows, article_count, source_files


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> bytes:
    data = ("\n".join(compact_json(row) for row in rows) + ("\n" if rows else "")).encode("utf-8")
    path.write_bytes(data)
    return data


def write_csv(path: Path, rows: list[dict[str, Any]]) -> bytes:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return path.read_bytes()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "build/lexicon-crossreferences",
        help="Directory for derived cross-reference inventory.",
    )
    args = parser.parse_args()

    rows, article_count, source_files = load_inventory()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    payloads = {
        JSONL_NAME: write_jsonl(args.out_dir / JSONL_NAME, rows),
        CSV_NAME: write_csv(args.out_dir / CSV_NAME, rows),
    }

    marker_counts = Counter(row["markerClass"] for row in rows)
    relation_counts = Counter(str(row["relation"]) for row in rows)
    source_article_ids = {row["sourceArticleId"] for row in rows}

    manifest = {
        "sourceId": "ALC1737",
        "dataset": "historical_lexical_crossreferences",
        "derivation": "deterministic extraction from canonical article crossReferences arrays",
        "canonicalInputPattern": "data/lexicon/articles/*.jsonl",
        "canonicalInputFileCount": len(source_files),
        "canonicalArticleCountScanned": article_count,
        "crossReferenceCount": len(rows),
        "sourceArticleCountWithCrossReferences": len(source_article_ids),
        "markerClassCounts": dict(sorted(marker_counts.items())),
        "relationCounts": dict(sorted(relation_counts.items())),
        "destinationResolutionPerformed": False,
        "sortOrder": "numeric sourceArticleId ascending, then crossReferenceIndex",
        "deterministic": True,
        "formats": {
            name: {"bytes": len(data), "sha256": sha256_bytes(data)}
            for name, data in sorted(payloads.items())
        },
        "canonicalInputs": source_files,
    }

    manifest_bytes = (
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    ).encode("utf-8")
    (args.out_dir / MANIFEST_NAME).write_bytes(manifest_bytes)

    for name, metadata in manifest["formats"].items():
        actual = (args.out_dir / name).read_bytes()
        if len(actual) != metadata["bytes"] or sha256_bytes(actual) != metadata["sha256"]:
            raise SystemExit(f"post-write integrity check failed for {name}")

    if not rows:
        raise SystemExit("no canonical crossReferences found; refusing empty inventory")

    print(
        "exported historical cross-reference inventory: "
        f"{len(rows)} references in {len(source_article_ids)} articles; "
        f"Buſca-class={marker_counts.get('busca', 0)}; outputs in {args.out_dir}"
    )
    for name, metadata in manifest["formats"].items():
        print(f"  {name}: {metadata['bytes']} bytes; sha256 {metadata['sha256']}")


if __name__ == "__main__":
    main()
