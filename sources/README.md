# `sources/` — supplied source material, verbatim

**Authority:** none. Ruling 10 (2026-09-21): *"Location is not authority. Nothing in
`sources/` or `manuscript/` is canon by virtue of being in the repository. Canon is what
the substrate says."*

**Tier:** D under `CLAUDE.md` §5 — other sources. A file here is `recovered`, never
`derived` and never `authored`.

## Rules

1. **Verbatim.** Files land exactly as supplied. Whatever a source contains — prose, scene
   text, dialogue, lyrics — is stored as supplied. **A source archive that edits its
   sources is not an archive.**
2. **Append-only.** Never edited, pruned or reformatted in place. This is `CLAUDE.md`
   §1.0's rule applied to real originals rather than to a derivative.
3. **Outside substrate validation.** `tools/validate_canon.py` does not scan this
   directory in either scope. It never counts toward the violation ceiling, so
   canon-scope 0 keeps meaning what it means.
4. **Prose is expected here.** §1's no-prose rule is scoped to the substrate and does not
   apply to this directory.

## Why sources are committed

Extraction claims must be checkable against what they were extracted from. The alternative
was tried: `recovery/source_exports/html_sanitized/` is a **lossy derivative** — 21 files,
25,952 words total, against a single supplied conversation of 108,378 — and its lossiness
went unmeasured for days because there was nothing to measure it against.

## Both `.md` and `.json`, deliberately

The `.md` is what gets parsed. The `.json` carries the **native message tree**, and the
markdown does not merely flatten it — it **discards part of it**. Measured on
`Bubble Grunge Lyrics`: the JSON holds 678 nodes including **229 system messages and 2
tool messages**; the markdown renders **zero** of either.

Carrying one format and not the other loses content that cannot be recovered without
re-export.

## `chatgpt_export_2026-09/`

Account export run **2026-09-15** (`exported: 2026-09-15T16:57:09.617Z`). This supersedes
`CLAUDE.md` §7's earlier statement that no export path existed.

## One permitted redaction — Amendment 1

`workspace_account_id` is replaced with the literal `REDACTED` before a file enters this
directory. **This is the only deviation from verbatim storage**; anything further needs its
own amendment.

The key is **kept** and only its value replaced, so the redaction is visible in the file
rather than inferred from its absence. It is a **text-level substitution**, not a
re-serialisation — every other byte survives. Verified by reversal: putting the original
value back yields a byte-identical file.

The `.md` files never contained it and are stored byte-identical.

**Redaction happens before the first commit, never after** — a value committed raw stays in
git history permanently. `tools/ingest_sources.py` does the copy, redaction, verification
and manifest in one pass.

`MANIFEST.csv` records, per conversation: filename, conversation id, created date, turn
count, word count, and the SHA-256 of **both the original and the stored file**, plus any
redaction applied. **The manifest is the audit surface** — a file whose hash
does not match its manifest row has been altered, which rule 2 forbids.

## Exclusions

The account export holds **72 conversations, 7,479,895 words**. **70 are committed; 138
files, 7,363,532 words.**

**Excluded material is recorded, not hidden.** Every excluded file keeps its row in
`MANIFEST.csv` with its SHA-256 and the reason, so the gap is visible and auditable
against the author's original TAR.

**Exclusion, never redaction.** Rule 1 promises that every committed file matches its
manifest hash exactly. A redacted file would break that promise silently. Leaving a file
out keeps it intact.

| Conversation | Excluded | Reason |
| --- | --- | --- |
| `2025-11-17__Chat_export_options` | `.json` only | signed `auth.openai.com` session access token (expired 2025-11-26), organization id, work-domain email |
| `2026-09-14__Review_Project_Status` | `.json` only | third-party professional contact details from work documents; 92 signed file URLs; user ids. The `.md` is clean |
| `2025-12-31__Archetype_Test_Insightful_or_BS` | both | personal self-assessment material; not saga work |
| `2026-09-14__Story_Summary_Writing` | both | a separate story project, stated in-conversation as "not concord saga" |

The six filenames are also listed in `.gitignore`, so they cannot be added by accident.

**One reviewed allowance.** `2025-12-01__Worldbuilding.json` contains a token-shaped
string inside a public DeviantArt image URL: an image-CDN token with no expiry and no
account scope. `tools/verify_sources.py` allowlists it by **file and pattern together**,
never by pattern alone.

**Not in this export.** `Bubble Grunge Lyrics` (Mara Niht) and `Develop Singer Style`
(Eli Stone) were supplied separately and are not among the 72. They would be committed
under their own directory with their own manifest.

## Verification

```sh
python3 tools/verify_sources.py
```

Checks that every committed file is present and matches its manifest hash, that no
excluded or unlisted file is present, and that no forbidden pattern — session tokens,
signed URLs, auth ids, the known third-party work contact — appears in any committed
file. Exits non-zero on any failure.

Proven by deliberate breakage on 2026-09-23: one byte edited, an excluded token-bearing
file added, a committed file removed and an unlisted file added each produce exit 1.
The clean set produces exit 0.
