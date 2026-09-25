# Concord Saga Canon

Canon substrate and source record for the **Concord Saga**, a nine-book serial in three
trilogies — **Veil** (B01–B03), **Neon** (B04–B06), **Loom** (B07–B09).

This repository holds the saga's rules, canon cards, structural grids and per-book and
per-act contexts, together with the original development conversations they were
recovered from and the analysis that connects the two. It holds **no narrative prose
outside `sources/` and `manuscript/`**.

## Layout

| Folder | Holds |
| --- | --- |
| `canon/` | Character, faction and POV cards; codex; trilogy summaries |
| `rules/` | `canon_rules.json`, saga and trilogy contexts, Mechanica, Resonance, system docs |
| `grids/` | CSV structure and telemetry grids |
| `book_context/`, `act_overlays/` | Per-book and per-act JSON contexts |
| `decisions/` | Author rulings, each stating exactly what it accepted |
| `proposals/` | Working architectures and reconciliations (non-canonical) |
| `reports/` | Editorial audits and reviews; generated validation baselines |
| `recovery/` | Forensic audits, ledgers and archived originals |
| `sources/` | The original development export, verbatim |
| `manuscript/` | Authored prose (empty until production) |
| `tools/` | Validator, self-tests, source verifier |

**Canon is what `canon/`, `rules/` and the grids say.** Everything else is evidence,
analysis or proposal until a ruling in `decisions/` adopts it and it is migrated.

## Identifiers

`S1.T{1-3}.B{01-09}.{A1|A2|A3|PR|EP}.E{00-99}` — two-digit books, episodes numbered
continuously across a book, prologue `E00`. Beats are `{SID}-BT{nn}`.

## Checks

```sh
python3 tools/validate_canon.py          # canon substrate; exits non-zero on any violation
python3 tools/test_validate_canon.py     # validator self-tests
python3 tools/verify_sources.py          # sources/ against its manifest
```

All three run in CI on every push.

## Working in this repository

Read [`CLAUDE.md`](CLAUDE.md) first — the working agreement for anyone (human or
assistant) editing here. The running history is `recovery/RECOVERY_LEDGER_2026.md`.

Copyright © 2025–2026. All rights reserved. See `LICENSE.txt`.
