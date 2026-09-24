#!/usr/bin/env python3
"""Verify sources/chatgpt_export_2026-09/ against its MANIFEST.csv.

Ruling 10 (2026-09-21): sources/ is verbatim and append-only. The manifest is the
audit surface -- a file whose hash does not match its row has been altered.

Checks, all of which must pass:
  1. every file the manifest marks for commit is present
  2. every present file's SHA-256 matches its manifest row
  3. no excluded file is present
  4. no unlisted file is present
  5. no forbidden pattern appears in any committed file, except the allowlisted
     public image token in Worldbuilding.json

Exits non-zero on any failure, so it can gate a commit or a CI step.

    python3 tools/verify_sources.py
    python3 tools/verify_sources.py path/to/sources/chatgpt_export_2026-09

Standard library only.
"""
import csv
import hashlib
import os
import re
import sys

DEFAULT_DIR = os.path.join("sources", "chatgpt_export_2026-09")

FORBIDDEN = {
    "jwt-shaped token": r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.",
    "session access token": r"accessToken",
    "signed file url": r"[?&]sig=",
    "auth user id": r"user-[A-Za-z0-9]{20,}",
    "organization id": r"org-[A-Za-z0-9]{20,}",
    "third-party work contact": r"truengineering|taggarch|501-993-7149",
}

# One known, reviewed exception: a public DeviantArt/Wix image-CDN token inside an
# image URL (iss urn:app:..., aud urn:service:image.operations, no expiry, no
# account scope). Reviewed 2026-09-23. Allowlisted by file AND pattern, never by
# pattern alone.
ALLOW = {("2025-12-01__Worldbuilding__692dc2fb.json", "jwt-shaped token")}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main(root):
    manifest_path = os.path.join(root, "MANIFEST.csv")
    if not os.path.isfile(manifest_path):
        print(f"FAIL  no manifest at {manifest_path}")
        return 1

    with open(manifest_path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    expected, excluded = {}, set()
    for r in rows:
        md, js = r["stem"] + ".md", r["stem"] + ".json"
        status = r["status"]
        if status == "COMMIT_BOTH":
            expected[md], expected[js] = r["md_sha256"], r["json_sha256"]
        elif status == "COMMIT_MD_ONLY":
            expected[md] = r["md_sha256"]
            excluded.add(js)
        elif status == "EXCLUDE_BOTH":
            excluded.update({md, js})
        else:
            print(f"FAIL  unknown status {status!r} for {r['stem']}")
            return 1

    present = {f for f in os.listdir(root) if f.endswith((".md", ".json"))}
    failures = []

    for name in sorted(set(expected) - present):
        failures.append(f"missing       {name}")
    for name in sorted(excluded & present):
        failures.append(f"EXCLUDED FILE {name}")
    for name in sorted(present - set(expected) - excluded):
        failures.append(f"unlisted      {name}")

    for name in sorted(set(expected) & present):
        if sha256(os.path.join(root, name)) != expected[name]:
            failures.append(f"hash mismatch {name}")

    patterns = {k: re.compile(v) for k, v in FORBIDDEN.items()}
    for name in sorted(present):
        with open(os.path.join(root, name), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for label, rx in patterns.items():
            if (name, label) in ALLOW:
                continue
            n = len(rx.findall(text))
            if n:
                failures.append(f"forbidden     {name}: {label} x{n}")

    committed = len(set(expected) & present)
    print(f"manifest rows {len(rows)} | expected files {len(expected)} | "
          f"present {committed} | excluded {len(excluded)}")
    if failures:
        print(f"FAIL  {len(failures)} problem(s):")
        for f in failures:
            print("  " + f)
        return 1
    print("PASS  every committed file matches its manifest hash; "
          "no excluded, unlisted or forbidden content")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DIR))
