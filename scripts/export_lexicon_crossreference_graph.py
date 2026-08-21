#!/usr/bin/env python3
"""Resolve historical lexical cross-references by strict normalized guide equality.

This derived layer is deliberately conservative. It never rewrites canonical
articles and never uses fuzzy matching, linguistic similarity, or semantic
inference. A `Buſca` target is linked only when a minimally normalized target
string equals exactly one minimally normalized canonical Spanish guide.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ARTICLE_DIR = ROOT / "data/lexicon/articles"

JSONL_NAME = "chd_lexicon_crossreference_resolution.jsonl"
CSV_NAME = "chd_lexicon_crossreference_resolution.csv"
GRAPH_NAME = "chd_lexicon_crossreference_graph.json"
MANIFEST_NAME = "manifest.json"

CSV_FIELDS = [
    "sourceArticleId",
    "sourcePageDigital",
    "sourceColumn",
    "sourceGuideRaw",
    "crossReferenceIndex",
    "markerRaw",
    "markerClass",
    "targetRaw",
    "targetNormalized",
    "resolutionStatus",
    "exactMatchCount",
    "matchedArticleIds",
    "exactUniqueTargetArticleId",
    "cycleStatus",
    "cycleId",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def article_number(article_id: str) -> int:
    return int(article_id.rsplit("-", 1)[1])


def marker_class(marker_raw: str) -> str:
    normalized = " ".join(marker_raw.replace("ſ", "s").casefold().split())
    return "busca" if normalized == "busca" else "other"


def normalize_guide(value: str) -> str:
    """Minimal technical normalization for strict equality, not lemmatization."""
    decomposed = unicodedata.normalize("NFKD", value.replace("ſ", "s").casefold())
    pieces: list[str] = []
    for char in decomposed:
        if unicodedata.category(char) == "Mn":
            continue
        pieces.append(char if char.isalnum() else " ")
    return " ".join("".join(pieces).split())


def load_articles() -> tuple[list[dict[str, Any]], list[str]]:
    articles: list[dict[str, Any]] = []
    source_files: list[str] = []
    seen_ids: set[str] = set()
    for path in sorted(ARTICLE_DIR.glob("*.jsonl")):
        source_files.append(path.relative_to(ROOT).as_posix())
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                article = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSON in {path}:{line_number}: {exc}") from exc
            article_id = article.get("articleId")
            if not isinstance(article_id, str) or not article_id:
                raise SystemExit(f"missing articleId in {path}:{line_number}")
            if article_id in seen_ids:
                raise SystemExit(f"duplicate articleId while building cross-reference graph: {article_id}")
            seen_ids.add(article_id)
            articles.append(article)
    articles.sort(key=lambda article: article_number(article["articleId"]))
    return articles, source_files


def strongly_connected_components(adjacency: dict[str, set[str]]) -> list[list[str]]:
    """Deterministic Tarjan SCC over exact-unique resolved edges."""
    index = 0
    stack: list[str] = []
    on_stack: set[str] = set()
    indices: dict[str, int] = {}
    lowlink: dict[str, int] = {}
    components: list[list[str]] = []

    def visit(node: str) -> None:
        nonlocal index
        indices[node] = index
        lowlink[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)

        for target in sorted(adjacency.get(node, set()), key=article_number):
            if target not in indices:
                visit(target)
                lowlink[node] = min(lowlink[node], lowlink[target])
            elif target in on_stack:
                lowlink[node] = min(lowlink[node], indices[target])

        if lowlink[node] == indices[node]:
            component: list[str] = []
            while True:
                member = stack.pop()
                on_stack.remove(member)
                component.append(member)
                if member == node:
                    break
            component.sort(key=article_number)
            components.append(component)

    nodes = set(adjacency)
    for targets in adjacency.values():
        nodes.update(targets)
    for node in sorted(nodes, key=article_number):
        if node not in indices:
            visit(node)
    components.sort(key=lambda members: tuple(article_number(member) for member in members))
    return components


def build_resolution() -> tuple[list[dict[str, Any]], dict[str, Any], int, list[str]]:
    articles, source_files = load_articles()
    by_id = {article["articleId"]: article for article in articles}
    guide_index: dict[str, list[str]] = defaultdict(list)
    for article in articles:
        guide = article.get("spanishGuideRaw")
        if isinstance(guide, str) and guide.strip():
            key = normalize_guide(guide)
            if key:
                guide_index[key].append(article["articleId"])
    for ids in guide_index.values():
        ids.sort(key=article_number)

    rows: list[dict[str, Any]] = []
    adjacency: dict[str, set[str]] = defaultdict(set)

    for article in articles:
        source_id = article["articleId"]
        refs = article.get("crossReferences") or []
        for ref_index, ref in enumerate(refs):
            marker_raw = ref.get("markerRaw")
            target_raw = ref.get("targetRaw")
            if not isinstance(marker_raw, str) or not marker_raw:
                raise SystemExit(f"invalid markerRaw in {source_id} reference {ref_index}")
            if not isinstance(target_raw, str) or not target_raw:
                raise SystemExit(f"invalid targetRaw in {source_id} reference {ref_index}")

            marker = marker_class(marker_raw)
            target_key = normalize_guide(target_raw)
            matches = list(guide_index.get(target_key, [])) if target_key else []
            unique_target: str | None = None

            if marker != "busca":
                status = "not_busca"
                matches = []
            elif not target_key:
                status = "non_normalizable"
            elif len(matches) == 0:
                status = "not_located"
            elif len(matches) == 1:
                status = "exact_unique"
                unique_target = matches[0]
                adjacency[source_id].add(unique_target)
            else:
                status = "exact_multiple"

            rows.append(
                {
                    "sourceArticleId": source_id,
                    "sourcePageDigital": article.get("sourcePageDigital"),
                    "sourceColumn": article.get("column"),
                    "sourceGuideRaw": article.get("spanishGuideRaw"),
                    "crossReferenceIndex": ref_index,
                    "markerRaw": marker_raw,
                    "markerClass": marker,
                    "targetRaw": target_raw,
                    "targetNormalized": target_key,
                    "resolutionStatus": status,
                    "exactMatchCount": len(matches),
                    "matchedArticleIds": matches,
                    "exactUniqueTargetArticleId": unique_target,
                    "cycleStatus": "none",
                    "cycleId": None,
                }
            )

    components = strongly_connected_components(adjacency)
    cycles: list[dict[str, Any]] = []
    membership: dict[str, tuple[str, str]] = {}
    cycle_counter = 0
    for component in components:
        self_loop = len(component) == 1 and component[0] in adjacency.get(component[0], set())
        if len(component) <= 1 and not self_loop:
            continue
        cycle_counter += 1
        cycle_id = f"cycle-{cycle_counter:03d}"
        status = "self_loop" if self_loop else "cycle_member"
        for article_id in component:
            membership[article_id] = (status, cycle_id)
        cycles.append(
            {
                "cycleId": cycle_id,
                "cycleStatus": status,
                "articleIds": component,
                "guidesRaw": [by_id[article_id].get("spanishGuideRaw") for article_id in component],
            }
        )

    for row in rows:
        source_id = row["sourceArticleId"]
        target_id = row["exactUniqueTargetArticleId"]
        if target_id is None:
            continue
        source_membership = membership.get(source_id)
        target_membership = membership.get(target_id)
        if source_membership is not None and source_membership == target_membership:
            row["cycleStatus"], row["cycleId"] = source_membership

    rows.sort(key=lambda row: (article_number(row["sourceArticleId"]), row["crossReferenceIndex"]))

    resolved_edges = [
        {
            "sourceArticleId": row["sourceArticleId"],
            "targetArticleId": row["exactUniqueTargetArticleId"],
            "targetRaw": row["targetRaw"],
            "relation": "see",
            "cycleStatus": row["cycleStatus"],
            "cycleId": row["cycleId"],
        }
        for row in rows
        if row["resolutionStatus"] == "exact_unique"
    ]
    involved_ids = {
        article_id
        for edge in resolved_edges
        for article_id in (edge["sourceArticleId"], edge["targetArticleId"])
    }
    graph = {
        "sourceId": "ALC1737",
        "graphSemantics": "strict normalized-exact Buſca links only",
        "nodeCount": len(involved_ids),
        "edgeCount": len(resolved_edges),
        "cycleCount": len(cycles),
        "nodes": [
            {
                "articleId": article_id,
                "spanishGuideRaw": by_id[article_id].get("spanishGuideRaw"),
                "sourcePageDigital": by_id[article_id].get("sourcePageDigital"),
            }
            for article_id in sorted(involved_ids, key=article_number)
        ],
        "edges": resolved_edges,
        "cycles": cycles,
    }
    return rows, graph, len(articles), source_files


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> bytes:
    data = ("\n".join(compact_json(row) for row in rows) + ("\n" if rows else "")).encode("utf-8")
    path.write_bytes(data)
    return data


def csv_value(value: Any) -> Any:
    if isinstance(value, (dict, list)):
        return compact_json(value)
    if value is None:
        return ""
    return value


def write_csv(path: Path, rows: list[dict[str, Any]]) -> bytes:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: csv_value(row.get(field)) for field in CSV_FIELDS})
    return path.read_bytes()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "build/lexicon-crossreference-graph",
        help="Directory for strict cross-reference resolution outputs.",
    )
    args = parser.parse_args()

    rows, graph, article_count, source_files = build_resolution()
    if not rows:
        raise SystemExit("no canonical crossReferences found; refusing empty resolution layer")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    graph_bytes = (json.dumps(graph, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    payloads = {
        JSONL_NAME: write_jsonl(args.out_dir / JSONL_NAME, rows),
        CSV_NAME: write_csv(args.out_dir / CSV_NAME, rows),
        GRAPH_NAME: graph_bytes,
    }
    (args.out_dir / GRAPH_NAME).write_bytes(graph_bytes)

    status_counts = Counter(row["resolutionStatus"] for row in rows)
    cycle_reference_count = sum(row["cycleStatus"] != "none" for row in rows)
    manifest = {
        "sourceId": "ALC1737",
        "dataset": "historical_lexical_crossreference_resolution",
        "derivation": "strict normalized equality between Buſca targetRaw and canonical spanishGuideRaw",
        "canonicalInputPattern": "data/lexicon/articles/*.jsonl",
        "canonicalInputFileCount": len(source_files),
        "canonicalArticleCountScanned": article_count,
        "crossReferenceCount": len(rows),
        "resolutionStatusCounts": dict(sorted(status_counts.items())),
        "exactUniqueEdgeCount": graph["edgeCount"],
        "cycleCount": graph["cycleCount"],
        "cycleReferenceCount": cycle_reference_count,
        "destinationResolutionPerformed": True,
        "resolutionRule": "NFKD + ſ→s + casefold + diacritic removal + punctuation-to-space + exact equality",
        "fuzzyMatchingUsed": False,
        "linguisticSimilarityUsed": False,
        "semanticEquivalenceInferred": False,
        "probableResolutionInferred": False,
        "canonicalArticlesModified": False,
        "deterministic": True,
        "sortOrder": "numeric sourceArticleId ascending, then crossReferenceIndex",
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
        "exported strict cross-reference resolution graph: "
        f"{len(rows)} references; statuses={dict(sorted(status_counts.items()))}; "
        f"exact edges={graph['edgeCount']}; cycles={graph['cycleCount']}; outputs in {args.out_dir}"
    )
    for name, metadata in manifest["formats"].items():
        print(f"  {name}: {metadata['bytes']} bytes; sha256 {metadata['sha256']}")


if __name__ == "__main__":
    main()
