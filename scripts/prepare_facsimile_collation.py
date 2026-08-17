#!/usr/bin/env python3
"""Prepare a reproducible facsimile-collation workspace from Internet Archive.

This tool is deliberately *pre-curatorial*: it downloads a selected IA PDF
witness, extracts one PDF page, renders it, splits the two-column page, and
runs a small OCR ensemble. It never edits canonical candidates or lexical
articles and never treats OCR as diplomatic authority.

External runtime dependencies:
  - poppler-utils (`pdfseparate`, `pdftoppm`)
  - tesseract (`tesseract`) plus the requested language pack
  - Pillow (`python -m pip install Pillow`)

Example:
  python scripts/prepare_facsimile_collation.py \
    --ia-id artedelalenguaca00gonz --pdf-page 177 \
    --out-dir .tmp_facsimile/p177 --language spa
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


DEFAULT_DPI = 420
DEFAULT_SPLIT = 0.5
DEFAULT_THRESHOLD = 178


def require_command(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise SystemExit(f"Required command not found: {name}")
    return path


def run(cmd: list[str], *, capture: bool = False) -> str:
    completed = subprocess.run(
        cmd,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
    )
    return completed.stdout.strip() if capture else ""


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def fetch_json(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": "cahita-historico-digital/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def download(url: str, target: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "cahita-historico-digital/1.0"})
    with urllib.request.urlopen(req, timeout=240) as resp, target.open("wb") as out:
        shutil.copyfileobj(resp, out, length=1024 * 1024)
    if not target.exists() or target.stat().st_size == 0:
        raise RuntimeError(f"Empty download: {url}")


def choose_pdf(files: list[dict[str, Any]]) -> dict[str, Any]:
    scored: list[tuple[int, str, dict[str, Any]]] = []
    for item in files:
        name = str(item.get("name", ""))
        fmt = str(item.get("format", ""))
        if not name.lower().endswith(".pdf"):
            continue
        score = 0
        if fmt == "Text PDF":
            score = 30
        elif fmt == "B/W PDF":
            score = 20
        elif "pdf" in fmt.lower():
            score = 10
        if name.endswith("_text.pdf"):
            score += 3
        scored.append((score, name, item))
    if not scored:
        raise RuntimeError("Internet Archive metadata contains no PDF derivative")
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return scored[0][2]


def tesseract_pass(image: Path, output_base: Path, language: str, psm: int) -> None:
    run(
        [
            "tesseract",
            str(image),
            str(output_base),
            "-l",
            language,
            "--psm",
            str(psm),
            "-c",
            "preserve_interword_spaces=1",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ia-id", required=True, help="Internet Archive item identifier")
    parser.add_argument("--pdf-page", required=True, type=int, help="1-based PDF page number")
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--language", default="spa", help="Tesseract language code")
    parser.add_argument("--dpi", type=int, default=DEFAULT_DPI)
    parser.add_argument("--split", type=float, default=DEFAULT_SPLIT, help="left-column fraction, default 0.5")
    parser.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD)
    args = parser.parse_args()

    if args.pdf_page < 1:
        parser.error("--pdf-page must be >= 1")
    if not 0.35 <= args.split <= 0.65:
        parser.error("--split must be between 0.35 and 0.65")
    if not 0 <= args.threshold <= 255:
        parser.error("--threshold must be between 0 and 255")

    for command in ("pdfseparate", "pdftoppm", "tesseract"):
        require_command(command)
    try:
        from PIL import Image, ImageEnhance, ImageOps
    except ImportError as exc:
        raise SystemExit("Pillow is required: python -m pip install Pillow") from exc

    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    metadata_url = f"https://archive.org/metadata/{urllib.parse.quote(args.ia_id)}"
    metadata = fetch_json(metadata_url)
    pdf_meta = choose_pdf(list(metadata.get("files", [])))
    pdf_name = str(pdf_meta["name"])
    pdf_url = f"https://archive.org/download/{urllib.parse.quote(args.ia_id)}/{urllib.parse.quote(pdf_name)}"

    with tempfile.TemporaryDirectory(prefix="chd-facsimile-") as tmp:
        tmp_dir = Path(tmp)
        source_pdf = tmp_dir / "source.pdf"
        page_pattern = tmp_dir / "page-%d.pdf"
        page_pdf_tmp = tmp_dir / f"page-{args.pdf_page}.pdf"
        render_base = tmp_dir / "render"

        download(pdf_url, source_pdf)
        run(
            [
                "pdfseparate",
                "-f",
                str(args.pdf_page),
                "-l",
                str(args.pdf_page),
                str(source_pdf),
                str(page_pattern),
            ]
        )
        if not page_pdf_tmp.exists():
            raise RuntimeError(f"pdfseparate did not create page {args.pdf_page}")

        target_pdf = out_dir / "source-page.pdf"
        shutil.copy2(page_pdf_tmp, target_pdf)

        run(
            [
                "pdftoppm",
                "-f",
                "1",
                "-l",
                "1",
                "-singlefile",
                "-png",
                "-r",
                str(args.dpi),
                str(target_pdf),
                str(render_base),
            ]
        )
        render_png = tmp_dir / "render.png"
        if not render_png.exists():
            raise RuntimeError("pdftoppm did not create render.png")

        image = Image.open(render_png).convert("L")
        width, height = image.size
        split_x = int(width * args.split)
        columns = {
            "left": image.crop((0, 0, split_x, height)),
            "right": image.crop((split_x, 0, width, height)),
        }

        ocr_outputs: dict[str, dict[str, Any]] = {}
        for column_name, column in columns.items():
            gray = ImageEnhance.Contrast(column).enhance(1.7)
            binary = ImageOps.autocontrast(column).point(
                lambda x: 255 if x > args.threshold else 0
            )

            gray_path = tmp_dir / f"{column_name}_gray.png"
            binary_path = tmp_dir / f"{column_name}_bin.png"
            gray.save(gray_path)
            binary.save(binary_path)

            passes = [
                ("gray_psm4", gray_path, 4),
                ("gray_psm6", gray_path, 6),
                ("bin_psm4", binary_path, 4),
            ]
            for suffix, image_path, psm in passes:
                base = out_dir / f"{column_name}_{suffix}"
                tesseract_pass(image_path, base, args.language, psm)
                txt = base.with_suffix(".txt")
                ocr_outputs[f"{column_name}_{suffix}"] = {
                    "file": txt.name,
                    "sha256": sha256(txt),
                    "bytes": txt.stat().st_size,
                    "psm": psm,
                    "preprocess": "binary" if "bin" in suffix else "contrast_gray",
                }

    tesseract_version = run(["tesseract", "--version"], capture=True).splitlines()[0]
    manifest = {
        "recordType": "temporary_facsimile_collation_workspace",
        "internetArchive": {
            "identifier": args.ia_id,
            "metadataUrl": metadata_url,
            "pdfDerivative": pdf_name,
            "pdfUrl": pdf_url,
        },
        "pdfPage": args.pdf_page,
        "sourcePagePdf": {
            "file": "source-page.pdf",
            "sha256": sha256(out_dir / "source-page.pdf"),
            "bytes": (out_dir / "source-page.pdf").stat().st_size,
        },
        "render": {
            "dpi": args.dpi,
            "pixelSize": [width, height],
            "columnSplitFraction": args.split,
            "threshold": args.threshold,
        },
        "ocr": {
            "engine": tesseract_version,
            "language": args.language,
            "passes": ocr_outputs,
        },
        "authorityGuard": "OCR outputs are machine evidence derived from the primary witness. They are not diplomatic transcription and must not be promoted without candidate-level collation and explicit provenance.",
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
