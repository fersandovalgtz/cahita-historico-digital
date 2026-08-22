#!/usr/bin/env python3
"""Export deterministic article-level candidates containing historical `Lo miſmo`.

Detection is deliberately surface-based and limited to canonical
``transcriptionRaw``. The output is an editorial queue of historical
metalinguistic formula occurrences. It does not infer the formula's exact
referential scope, a target-language form, borrowing, or semantic equivalence.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ARTICLE_DIR = ROOT / "data/lexicon/articles"

JSONL_NAME = "chd_lexicon_lo_mismo_candidates.jsonl"
CSV_NAME = "chd_lexicon_lo_mismo_candidates.csv"
MANIFEST_NAME = "manifest.json"

CSV_FIELDS = [
    "articleId",
    "sourcePageDigital",
    "column",
    "articleType",
    "spanishGuideRaw",
    "transcriptionRaw",
    "occurrenceCount",
    "reviewStatus",
    "humanVerified",
    "formulaCandidateType",
]

LO_MISMO = re.compile(r"\blo\s+mismo\b")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def article_number(article_id: str) -> int:
    return int(article_id.rsplit("-", 1)[1])


def normalized_surface(text: str) -> str:
    value = unicodedata.normalize("NFKC", text).replace("ſ", "s").casefold()
    return " ".join(value.split())


def load_candidates() -> tuple[list[dict[str, Any]], int, list[str]]:
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
            transcription = article.get("transcriptionRaw")
            if not isinstance(transcription, str) or not transcription:
                continue
            occurrences = LO_MISMO.findall(normalized_surface(transcription))
            if not occurrences:
                continue
            rows.append(
                {
                    "articleId": article["articleId"],
                    "sourcePageDigital": article.get("sourcePageDigital"),
                    "column": article.get("column"),
                    "articleType": article.get("articleType"),
                    "spanishGuideRaw": article.get("spanishGuideRaw"),
                    "transcriptionRaw": transcription,
                    "occurrenceCount": len(occurrences),
                    "reviewStatus": article.get("reviewStatus"),
                    "humanVerified": bool(article.get("humanVerified")),
                    "formulaCandidateType": "lo_mismo_metalinguistic_formula",
                }
            )

    rows.sort(key=lambda row: article_number(row["articleId"]))
    return rows, article_count, source_files


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> bytes:
    data = ("\n".join(compact_json(row) for row in rows) + ("\n" if rows else "")).encode("utf-8")
    path.write_bytes(data)
    return data


def write_csv(path: Path, rows: list[dict[str, Any]]) -> bytes:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return path.read_bytes()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "build/lexicon-lo-mismo",
        help="Directory for the derived Lo miſmo formula-candidate inventory.",
    )
    args = parser.parse_args()

    rows, article_count, source_files = load_candidates()
    if not rows:
        raise SystemExit("no `Lo miſmo` surface candidates found in canonical transcriptionRaw")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    payloads = {
        JSONL_NAME: write_jsonl(args.out_dir / JSONL_NAME, rows),
        CSV_NAME: write_csv(args.out_dir / CSV_NAME, rows),
    }

    article_type_counts = Counter(str(row["articleType"]) for row in rows)
    review_status_counts = Counter(str(row["reviewStatus"]) for row in rows)
    total_occurrences = sum(int(row["occurrenceCount"]) for row in rows)

    manifest = {
        "sourceId": "ALC1737",
        "dataset": "lo_mismo_metalinguistic_formula_candidates",
        "derivation": "surface detection in canonical article transcriptionRaw after technical Unicode/long-s normalization",
        "canonicalInputPattern": "data/lexicon/articles/*.jsonl",
        "canonicalInputFileCount": len(source_files),
        "canonicalArticleCountScanned": article_count,
        "candidateArticleCount": len(rows),
        "surfaceOccurrenceCount": total_occurrences,
        "articleTypeCounts": dict(sorted(article_type_counts.items())),
        "reviewStatusCounts": dict(sorted(review_status_counts.items())),
        "formulaFunctionInferred": False,
        "referentialScopeInferred": False,
        "targetLanguageFormInferred": False,
        "borrowingInferred": False,
        "semanticEquivalenceInferred": False,
        "sortOrder": "numeric articleId ascending",
        "deterministic": True,
        "formats": {
            name: {"bytes": len(data), "sha256": sha256_bytes(data)}
            for name, data in sorted(payloads.items())
        },
        "canonicalInputs": source_files,
    }

    (args.out_dir / MANIFEST_NAME).write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )

    for name, metadata in manifest["formats"].items():
        actual = (args.out_dir / name).read_bytes()
        if len(actual) != metadata["bytes"] or sha256_bytes(actual) != metadata["sha256"]:
            raise SystemExit(f"post-write integrity check failed for {name}")

    print(
        "exported Lo miſmo metalinguistic-formula queue: "
        f"{len(rows)} articles, {total_occurrences} occurrence(s), "
        f"from {article_count} canonical articles; outputs in {args.out_dir}"
    )
    for name, metadata in manifest["formats"].items():
        print(f"  {name}: {metadata['bytes']} bytes; sha256 {metadata['sha256']}")


if __name__ == "__main__":
    main()
