#!/usr/bin/env python3
"""Apply Ruling 10 Amendment 1 to the committed account export.

Amendment 1 (2026-09-23): the VALUE of `workspace_account_id` is replaced with the
literal `REDACTED` before a file enters sources/. The key is KEPT, so the redaction
is visible in the file rather than inferred from its absence. This tool does exactly
that and nothing else, so the result is reproducible from the author's original TAR.

THE TRANSFORMATION -- the whole of it:
    In each exported .json, line 3 must be exactly
        '  "workspace_account_id": "<uuid>",' + line ending
    following line 1 '{' and line 2 '  "exported": "<timestamp>",'.
    Its value is replaced with REDACTED:
        '  "workspace_account_id": "REDACTED",' + line ending
    Every other byte is kept. Byte-identical to what the ruled substitution in
    Amendment 1 produces for these files.

It is keyed to MANIFEST.csv, which records two hashes per .json:
    json_sha256_exported   the file as it came out of the export
    json_sha256_committed  the file after this transformation

For each .json the manifest says to commit:
    hash == exported   -> transform, then require the result == committed
    hash == committed  -> already done; leave it (so re-running is safe)
    anything else      -> FAIL. Nothing is guessed.

Also fails if, after transforming, the identifier survives anywhere in the file,
the file is not valid JSON, or re-inserting the removed line does not give back
the original bytes exactly.

    python3 tools/redact_export_ids.py [sources/chatgpt_export_2026-09]

Standard library only. Exits non-zero on any failure; files already written stay
as written, and verify_sources.py will name any that are wrong.
"""
import csv
import hashlib
import json
import os
import re
import sys

DEFAULT_DIR = os.path.join("sources", "chatgpt_export_2026-09")
LINE = re.compile(rb'\A(\{\r?\n  "exported": "[^"\r\n]*",\r?\n'
                  rb'  "workspace_account_id": ")([0-9a-f-]{36})(",\r?\n)')
REDACTED = b"REDACTED"


def sha(b):
    return hashlib.sha256(b).hexdigest()


def strip(raw):
    """Return (redacted_bytes, original_value) or raise ValueError."""
    m = LINE.match(raw)
    if not m:
        raise ValueError("lines 1-3 are not {, exported, workspace_account_id")
    uuid = m.group(2)
    out = m.group(1) + REDACTED + m.group(3) + raw[m.end():]
    if out.count(b"workspace_account_id") != 1:
        raise ValueError("key does not appear exactly once after redaction")
    if uuid in out:
        raise ValueError("identifier value survives elsewhere in the file")
    if out.replace(b'"workspace_account_id": "REDACTED"',
                   b'"workspace_account_id": "' + uuid + b'"', 1) != raw:
        raise ValueError("restoring the value does not reproduce the original")
    a, b = json.loads(raw.decode("utf-8")), json.loads(out.decode("utf-8"))
    if b.get("workspace_account_id") != "REDACTED":
        raise ValueError("stored copy does not read REDACTED")
    a.pop("workspace_account_id"); b.pop("workspace_account_id")
    if a != b:
        raise ValueError("redaction changed something other than the key's value")
    return out, uuid


def main(root):
    path = os.path.join(root, "MANIFEST.csv")
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    need = {"json_sha256_exported", "json_sha256_committed"}
    if not need <= set(rows[0]):
        print(f"FAIL  manifest lacks {sorted(need - set(rows[0]))}")
        return 1

    done = already = 0
    failures = []
    for r in rows:
        if r["status"] != "COMMIT_BOTH":
            continue
        name = r["stem"] + ".json"
        p = os.path.join(root, name)
        if not os.path.isfile(p):
            failures.append(f"missing       {name}")
            continue
        with open(p, "rb") as fh:
            raw = fh.read()
        h = sha(raw)
        if h == r["json_sha256_committed"]:
            already += 1
            continue
        if h != r["json_sha256_exported"]:
            failures.append(f"unknown bytes {name} (matches neither manifest hash)")
            continue
        try:
            out, _ = strip(raw)
        except ValueError as e:
            failures.append(f"refused       {name}: {e}")
            continue
        if sha(out) != r["json_sha256_committed"]:
            failures.append(f"wrong result  {name}: output does not match committed hash")
            continue
        with open(p, "wb") as fh:
            fh.write(out)
        done += 1

    print(f"redacted {done} | already redacted {already} | failures {len(failures)}")
    for f in failures:
        print("  " + f)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DIR))
