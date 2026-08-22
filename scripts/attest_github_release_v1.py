#!/usr/bin/env python3
"""Attest the published GitHub Release for Cahíta Histórico Digital v1.0.0.

The final release package embeds the immutable release commit in
RELEASE_MANIFEST.json. Therefore a ZIP hash observed on a pull-request merge ref is
not a valid final-release identity. This validator compares the downloaded GitHub
Release assets against a fresh deterministic rebuild from the immutable v1.0.0 tag.
It never creates, edits, or moves that tag or the release.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

EXPECTED_TAG = "v1.0.0"
EXPECTED_COMMIT = "dbcdecf0003ac5a10ae963caf6babdcf5c22128d"
EXPECTED_ZIP = "cahita-historico-digital-v1.0.0.zip"
EXPECTED_ASSETS = {EXPECTED_ZIP, "RELEASE_MANIFEST.json", "SHA256SUMS.txt"}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_sha256sums(path: Path) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            raise SystemExit(f"invalid SHA256SUMS line: {raw!r}")
        digest, name = parts
        name = name.lstrip("*")
        digest = digest.lower()
        if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            raise SystemExit(f"invalid SHA-256 digest in SHA256SUMS: {digest!r}")
        rows.append((digest, name))
    if len(rows) != 2:
        raise SystemExit(f"expected exactly 2 SHA256SUMS rows, found {len(rows)}")
    return rows


def find_sum(rows: list[tuple[str, str]], suffix: str) -> str:
    matches = [digest for digest, name in rows if name.endswith(suffix)]
    if len(matches) != 1:
        raise SystemExit(f"expected one SHA256SUMS row ending with {suffix!r}, found {len(matches)}")
    return matches[0]


def assert_same_bytes(left: Path, right: Path, label: str) -> None:
    if left.stat().st_size != right.stat().st_size:
        raise SystemExit(
            f"{label} byte-size mismatch: downloaded={left.stat().st_size}, rebuilt={right.stat().st_size}"
        )
    left_sha = sha256_file(left)
    right_sha = sha256_file(right)
    if left_sha != right_sha:
        raise SystemExit(f"{label} SHA-256 mismatch: downloaded={left_sha}, rebuilt={right_sha}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-json", type=Path, required=True)
    parser.add_argument("--asset-dir", type=Path, required=True)
    parser.add_argument("--tag-commit", required=True)
    parser.add_argument("--rebuilt-zip", type=Path, required=True)
    parser.add_argument("--rebuilt-manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    release = load_json(args.release_json)
    asset_dir = args.asset_dir

    if args.tag_commit != EXPECTED_COMMIT:
        raise SystemExit(f"tag commit mismatch: {args.tag_commit} != {EXPECTED_COMMIT}")
    if release.get("tagName") != EXPECTED_TAG:
        raise SystemExit(f"release tag mismatch: {release.get('tagName')!r}")
    if release.get("isDraft") is not False:
        raise SystemExit("GitHub Release must not be a draft")
    if release.get("isPrerelease") is not False:
        raise SystemExit("GitHub Release must not be a prerelease")
    if not release.get("url"):
        raise SystemExit("GitHub Release URL is missing")

    local_assets = {p.name for p in asset_dir.iterdir() if p.is_file()}
    if local_assets != EXPECTED_ASSETS:
        raise SystemExit(f"unexpected release asset set: {sorted(local_assets)}")

    api_assets = release.get("assets") or []
    api_names = {str(item.get("name")) for item in api_assets}
    if api_names != EXPECTED_ASSETS:
        raise SystemExit(f"release metadata asset set mismatch: {sorted(api_names)}")

    for item in api_assets:
        name = str(item["name"])
        local_size = (asset_dir / name).stat().st_size
        api_size = item.get("size")
        if api_size is not None and int(api_size) != local_size:
            raise SystemExit(f"asset-size mismatch for {name}: API={api_size}, local={local_size}")

    zip_path = asset_dir / EXPECTED_ZIP
    manifest_path = asset_dir / "RELEASE_MANIFEST.json"
    sums_path = asset_dir / "SHA256SUMS.txt"

    if not args.rebuilt_zip.is_file() or not args.rebuilt_manifest.is_file():
        raise SystemExit("deterministic rebuild outputs are missing")

    # Strongest identity check: published payload must be byte-identical to a clean
    # deterministic rebuild made from the immutable release tag.
    assert_same_bytes(zip_path, args.rebuilt_zip, "v1 release ZIP")
    assert_same_bytes(manifest_path, args.rebuilt_manifest, "v1 release manifest")

    zip_sha = sha256_file(zip_path)
    zip_bytes = zip_path.stat().st_size
    manifest_sha = sha256_file(manifest_path)
    manifest_bytes = manifest_path.stat().st_size

    manifest = load_json(manifest_path)
    if manifest.get("version") != "1.0.0" or manifest.get("tag") != EXPECTED_TAG:
        raise SystemExit("release manifest version/tag mismatch")
    if manifest.get("sourceCommit") != EXPECTED_COMMIT:
        raise SystemExit("release manifest sourceCommit mismatch")
    if manifest.get("githubReleasePayloadReady") is not True:
        raise SystemExit("release manifest does not mark GitHub payload ready")
    if manifest.get("archivalDepositStatus") != "pending":
        raise SystemExit("archival deposit must still be pending at GitHub-release attestation")
    if manifest.get("versionDoi") is not None or manifest.get("conceptDoi") is not None:
        raise SystemExit("DOI must not be invented before archival deposit")
    if int(manifest.get("humanVerifiedCount", -1)) != 0:
        raise SystemExit("humanVerifiedCount drifted from 0")

    sums = parse_sha256sums(sums_path)
    sums_zip = find_sum(sums, EXPECTED_ZIP)
    sums_manifest = find_sum(sums, "RELEASE_MANIFEST.json")
    if sums_zip != zip_sha:
        raise SystemExit("SHA256SUMS ZIP digest does not match downloaded ZIP")
    if sums_manifest != manifest_sha:
        raise SystemExit("SHA256SUMS manifest digest does not match downloaded manifest")

    assets = []
    for name in sorted(EXPECTED_ASSETS):
        path = asset_dir / name
        assets.append({"name": name, "bytes": path.stat().st_size, "sha256": sha256_file(path)})

    attestation = {
        "attestationType": "github_release_integrity",
        "attestationVersion": 2,
        "verificationMode": "deterministic_rebuild_from_immutable_tag",
        "project": "Cahíta Histórico Digital",
        "version": "1.0.0",
        "tag": EXPECTED_TAG,
        "tagCommit": EXPECTED_COMMIT,
        "releaseName": release.get("name"),
        "releaseUrl": release.get("url"),
        "publishedAt": release.get("publishedAt"),
        "isDraft": False,
        "isPrerelease": False,
        "releaseZip": {"bytes": zip_bytes, "sha256": zip_sha},
        "releaseManifest": {"bytes": manifest_bytes, "sha256": manifest_sha},
        "assets": assets,
        "checks": {
            "tagPointsToExpectedCommit": True,
            "releaseTagMatches": True,
            "stableRelease": True,
            "exactAssetSet": True,
            "apiAssetSizesMatchDownloadedBytes": True,
            "publishedZipMatchesDeterministicTagRebuild": True,
            "publishedManifestMatchesDeterministicTagRebuild": True,
            "sha256SumsConsistent": True,
            "releaseManifestIdentityMatchesTag": True,
            "doiNotInferred": True,
        },
        "archivalDepositStatus": "pending",
        "versionDoi": None,
        "conceptDoi": None,
        "humanVerifiedCount": 0,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(attestation, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        "GitHub Release attestation OK: "
        f"tag={EXPECTED_TAG}; commit={EXPECTED_COMMIT}; assets=3; "
        f"zipBytes={zip_bytes}; zipSha256={zip_sha}; rebuildMatch=true; "
        "archivalDepositStatus=pending; humanVerified=0"
    )


if __name__ == "__main__":
    main()
