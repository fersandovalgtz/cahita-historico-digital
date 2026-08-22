#!/usr/bin/env python3
"""Validate the published CHD v1.0.0 by rebuilding from its immutable tag.

Post-release ``main`` is intentionally allowed to evolve. Therefore the identity
of v1.0.0 must never be reconstructed from the current working tree. This gate
creates a detached worktree at the immutable tag, runs the builder stored in
that tag, and compares the resulting bytes with the durable publication
attestation committed after the GitHub Release was published.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_TAG = "v1.0.0"
EXPECTED_COMMIT = "dbcdecf0003ac5a10ae963caf6babdcf5c22128d"
EXPECTED_ZIP = "cahita-historico-digital-v1.0.0.zip"
EXPECTED_ZIP_BYTES = 1_076_296
EXPECTED_ZIP_SHA256 = "583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158"
EXPECTED_MANIFEST_BYTES = 67_757
EXPECTED_MANIFEST_SHA256 = "05970080840ed0cde9c4ca67b40432b492ba2f0afadade5efe2b9d0f60b8cb79"
ATTESTATION_PATH = ROOT / "release/github_release_attestation_v1.0.0.json"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(*args: str, cwd: Path = ROOT, capture: bool = False) -> str:
    result = subprocess.run(
        list(args),
        cwd=cwd,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
    )
    return result.stdout.strip() if capture else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_attestation(attestation: dict[str, Any]) -> None:
    if attestation.get("attestationType") != "github_release_integrity":
        raise SystemExit("unexpected GitHub Release attestation type")
    if attestation.get("version") != "1.0.0" or attestation.get("tag") != EXPECTED_TAG:
        raise SystemExit("published v1 attestation version/tag drifted")
    if attestation.get("tagCommit") != EXPECTED_COMMIT:
        raise SystemExit("published v1 attestation commit drifted")
    if attestation.get("verificationMode") != "deterministic_rebuild_from_immutable_tag":
        raise SystemExit("published v1 attestation is not based on immutable-tag reconstruction")
    if attestation.get("isDraft") is not False or attestation.get("isPrerelease") is not False:
        raise SystemExit("published v1 must remain a stable GitHub Release")
    if attestation.get("versionDoi") is not None or attestation.get("conceptDoi") is not None:
        raise SystemExit("v1 attestation must not invent DOI before archival deposit")
    if int(attestation.get("humanVerifiedCount", -1)) != 0:
        raise SystemExit("v1 attestation humanVerifiedCount drifted")

    release_zip = attestation.get("releaseZip") or {}
    if int(release_zip.get("bytes", -1)) != EXPECTED_ZIP_BYTES:
        raise SystemExit("published v1 ZIP byte count drifted in attestation")
    if release_zip.get("sha256") != EXPECTED_ZIP_SHA256:
        raise SystemExit("published v1 ZIP SHA-256 drifted in attestation")

    release_manifest = attestation.get("releaseManifest") or {}
    if int(release_manifest.get("bytes", -1)) != EXPECTED_MANIFEST_BYTES:
        raise SystemExit("published v1 manifest byte count drifted in attestation")
    if release_manifest.get("sha256") != EXPECTED_MANIFEST_SHA256:
        raise SystemExit("published v1 manifest SHA-256 drifted in attestation")

    checks = attestation.get("checks") or {}
    required_checks = {
        "tagPointsToExpectedCommit",
        "releaseTagMatches",
        "stableRelease",
        "exactAssetSet",
        "apiAssetSizesMatchDownloadedBytes",
        "publishedManifestMatchesDeterministicTagRebuild",
        "publishedZipMatchesDeterministicTagRebuild",
        "sha256SumsConsistent",
        "releaseManifestIdentityMatchesTag",
        "doiNotInferred",
    }
    missing_or_false = sorted(key for key in required_checks if checks.get(key) is not True)
    if missing_or_false:
        raise SystemExit(f"published v1 attestation has failed/missing checks: {missing_or_false}")


def resolve_tag_commit() -> str:
    run("git", "fetch", "--tags", "--force")
    return run("git", "rev-list", "-n", "1", EXPECTED_TAG, capture=True)


def rebuild_from_tag(base: Path) -> tuple[Path, Path]:
    worktree = base / "tag-worktree"
    output = base / "tag-build"
    run("git", "worktree", "add", "--detach", str(worktree), EXPECTED_TAG)
    try:
        tag_head = run("git", "rev-parse", "HEAD", cwd=worktree, capture=True)
        if tag_head != EXPECTED_COMMIT:
            raise SystemExit(f"detached tag worktree resolved to {tag_head}, expected {EXPECTED_COMMIT}")
        subprocess.run(
            [
                sys.executable,
                str(worktree / "scripts/build_v1_release.py"),
                "--output-dir",
                str(output),
            ],
            cwd=worktree,
            check=True,
        )
    finally:
        # Remove through git first so the main checkout does not retain stale worktree metadata.
        subprocess.run(
            ["git", "worktree", "remove", "--force", str(worktree)],
            cwd=ROOT,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if worktree.exists():
            shutil.rmtree(worktree, ignore_errors=True)

    zip_path = output / EXPECTED_ZIP
    manifest_path = output / "cahita-historico-digital-v1.0.0" / "RELEASE_MANIFEST.json"
    if not zip_path.is_file() or not manifest_path.is_file():
        raise SystemExit("immutable-tag rebuild did not produce the expected v1 release files")
    return zip_path, manifest_path


def main() -> None:
    if not ATTESTATION_PATH.is_file():
        raise SystemExit("published v1 attestation is missing from post-release main")
    attestation = load_json(ATTESTATION_PATH)
    validate_attestation(attestation)

    tag_commit = resolve_tag_commit()
    if tag_commit != EXPECTED_COMMIT:
        raise SystemExit(f"immutable tag moved: {EXPECTED_TAG} -> {tag_commit}, expected {EXPECTED_COMMIT}")

    with tempfile.TemporaryDirectory(prefix="chd-published-v1-") as tmp:
        zip_path, manifest_path = rebuild_from_tag(Path(tmp))

        zip_bytes = zip_path.stat().st_size
        zip_sha = sha256_file(zip_path)
        manifest_bytes = manifest_path.stat().st_size
        manifest_sha = sha256_file(manifest_path)

        if zip_bytes != EXPECTED_ZIP_BYTES or zip_sha != EXPECTED_ZIP_SHA256:
            raise SystemExit(
                "immutable-tag ZIP reconstruction differs from published v1: "
                f"bytes={zip_bytes}, sha256={zip_sha}"
            )
        if manifest_bytes != EXPECTED_MANIFEST_BYTES or manifest_sha != EXPECTED_MANIFEST_SHA256:
            raise SystemExit(
                "immutable-tag manifest reconstruction differs from published v1: "
                f"bytes={manifest_bytes}, sha256={manifest_sha}"
            )

        manifest = load_json(manifest_path)
        if manifest.get("sourceCommit") != EXPECTED_COMMIT:
            raise SystemExit("rebuilt v1 manifest sourceCommit does not equal immutable tag commit")
        if manifest.get("version") != "1.0.0" or manifest.get("tag") != EXPECTED_TAG:
            raise SystemExit("rebuilt v1 manifest identity drifted")
        if manifest.get("humanVerifiedCount") != 0:
            raise SystemExit("rebuilt v1 manifest humanVerifiedCount drifted")
        if manifest.get("versionDoi") is not None or manifest.get("conceptDoi") is not None:
            raise SystemExit("rebuilt immutable v1 unexpectedly contains DOI")

    print(
        "published v1 QA OK: "
        f"tag={EXPECTED_TAG}; commit={EXPECTED_COMMIT}; "
        f"zipBytes={EXPECTED_ZIP_BYTES}; zipSha256={EXPECTED_ZIP_SHA256}; "
        f"manifestBytes={EXPECTED_MANIFEST_BYTES}; manifestSha256={EXPECTED_MANIFEST_SHA256}; "
        "rebuildSource=immutable_tag; DOI=pending; humanVerified=0"
    )


if __name__ == "__main__":
    main()
