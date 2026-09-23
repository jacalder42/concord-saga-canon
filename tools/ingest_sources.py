#!/usr/bin/env python3
"""Ingest a ChatGPT account export into `sources/`, redacting workspace ids.

Ruling 10 (2026-09-21) stores sources verbatim. Amendment 1 permits exactly one
deviation: `workspace_account_id` is replaced with `REDACTED` before the file is
ever committed.

    python3 tools/ingest_sources.py /path/to/export [--dest sources/chatgpt_export_2026-09]

The redaction is SURGICAL: a text-level substitution of that one value. The files
are not re-serialised, because re-formatting every line would be a far larger edit
than the redaction it is meant to make. Every other byte survives.

ORDER MATTERS. Redaction happens before the first commit, never after. Committing
raw files and stripping them later leaves the value in git history permanently, and
removing it then means rewriting published history, which CLAUDE.md section 2 forbids.

Writes MANIFEST.csv with the SHA-256 of BOTH the original and the stored file, so a
reader holding the export can confirm the stored copy differs in exactly one value.

Standard library only. Safe to re-run: it refuses to overwrite a differing file
unless --force is given.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import sys

REDACT_KEY = "workspace_account_id"
REDACT_WITH = "REDACTED"
MANIFEST = "MANIFEST.csv"
COLUMNS = [
    "filename", "conversation_id", "title", "created", "turn_count", "word_count",
    "bytes_stored", "sha256_original", "sha256_stored", "redactions",
]

# "workspace_account_id" : "<value>"   - tolerant of whitespace, strict about the key.
REDACT_RX = re.compile(
    r'("' + re.escape(REDACT_KEY) + r'"\s*:\s*)"(?:[^"\\]|\\.)*"'
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def redact(raw: bytes):
    """Return (new_bytes, count). Substitutes only the value of REDACT_KEY."""
    text = raw.decode("utf-8")
    new, n = REDACT_RX.subn(lambda m: m.group(1) + '"' + REDACT_WITH + '"', text)
    return new.encode("utf-8"), n


def verify(original: bytes, stored: bytes, count: int) -> None:
    """Both parse, and they differ at REDACT_KEY and nowhere else.

    This is what makes Amendment 1's claim checkable rather than asserted. A
    redaction that silently changed anything else would fail here.
    """
    a, b = json.loads(original), json.loads(stored)
    if a.get(REDACT_KEY) is None and count == 0:
        return
    if b.get(REDACT_KEY) != REDACT_WITH:
        raise SystemExit(f"  ABORT: {REDACT_KEY} was not redacted in the stored copy")
    a.pop(REDACT_KEY, None)
    b.pop(REDACT_KEY, None)
    if a != b:
        raise SystemExit("  ABORT: redaction changed something other than "
                         f"{REDACT_KEY}; refusing to store")


def conv_meta(raw: bytes, name: str) -> dict:
    try:
        d = json.loads(raw)
    except Exception:
        return {}
    return {
        "conversation_id": d.get("id", ""),
        "title": d.get("title", ""),
        "created": d.get("create_time", ""),
        "turn_count": d.get("turn_count", ""),
        "word_count": d.get("word_count", ""),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("src", help="directory holding the exported .md and .json files")
    ap.add_argument("--dest", default=os.path.join("sources", "chatgpt_export_2026-09"))
    ap.add_argument("--force", action="store_true",
                    help="overwrite a stored file whose content differs")
    ap.add_argument("--dry-run", action="store_true", help="report, write nothing")
    args = ap.parse_args()

    if not os.path.isdir(args.src):
        return print(f"not a directory: {args.src}") or 2
    files = sorted(f for f in os.listdir(args.src) if f.endswith((".md", ".json")))
    if not files:
        return print(f"no .md or .json files in {args.src}") or 2
    if not args.dry_run:
        os.makedirs(args.dest, exist_ok=True)

    rows, redacted_n, skipped = [], 0, 0
    for name in files:
        src = os.path.join(args.src, name)
        with open(src, "rb") as fh:
            raw = fh.read()
        h_orig = sha256(raw)

        if name.endswith(".json"):
            stored, n = redact(raw)
            verify(raw, stored, n)
            redacted_n += n
            note = f"{REDACT_KEY}->{REDACT_WITH}" if n else ""
            meta = conv_meta(stored, name)
        else:
            stored, note, meta = raw, "", {}
            if REDACT_KEY.encode() in raw:          # markdown should never carry it
                raise SystemExit(f"  ABORT: {name} is .md but contains {REDACT_KEY}; "
                                 "this tool only redacts JSON - stopping rather than "
                                 "storing it unredacted")

        dest = os.path.join(args.dest, name)
        if os.path.exists(dest) and not args.dry_run:
            with open(dest, "rb") as fh:
                existing = fh.read()
            if existing == stored:
                skipped += 1
            elif not args.force:
                raise SystemExit(f"  ABORT: {name} exists and differs. "
                                 "sources/ is append-only (Ruling 10); pass --force "
                                 "only if you mean to replace it.")
        if not args.dry_run and not (os.path.exists(dest) and skipped):
            with open(dest, "wb") as fh:
                fh.write(stored)

        row = {c: "" for c in COLUMNS}
        row.update(meta)
        row.update({"filename": name, "bytes_stored": len(stored),
                    "sha256_original": h_orig, "sha256_stored": sha256(stored),
                    "redactions": note})
        rows.append(row)

    if not args.dry_run:
        with open(os.path.join(args.dest, MANIFEST), "w", encoding="utf-8",
                  newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=COLUMNS)
            w.writeheader()
            for r in rows:
                w.writerow(r)

    md = sum(1 for r in rows if r["filename"].endswith(".md"))
    js = len(rows) - md
    ids = {r["conversation_id"] for r in rows if r["conversation_id"]}
    print(f"{'DRY RUN - ' if args.dry_run else ''}{len(rows)} files "
          f"({md} .md, {js} .json) -> {args.dest}")
    print(f"  conversations (by id in json): {len(ids)}")
    print(f"  {REDACT_KEY} redactions: {redacted_n}")
    print(f"  unchanged files skipped: {skipped}")
    unpaired = _unpaired(rows)
    if unpaired:
        print(f"  WARNING - {len(unpaired)} conversation(s) present in only one format:")
        for u in unpaired[:10]:
            print(f"      {u}")
    else:
        print("  every conversation has both .md and .json")
    return 0


def _unpaired(rows):
    """Conversations present in only one format.

    Keyed on the trailing `__<conversation id>` rather than the whole filename
    stem: a file may carry a per-upload prefix that differs between a
    conversation's .md and .json, which would make every conversation look
    unpaired. The id is the part that actually identifies the conversation.
    """
    groups = {}
    for r in rows:
        stem, _, ext = r["filename"].rpartition(".")
        key = stem.rsplit("__", 1)[-1] if "__" in stem else stem
        groups.setdefault(key, {"exts": set(), "stem": stem})["exts"].add(ext)
    return sorted(g["stem"] for g in groups.values() if g["exts"] != {"md", "json"})


if __name__ == "__main__":
    sys.exit(main())
