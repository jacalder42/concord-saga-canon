# decisions/

**Author rulings. The highest-authority documents in the repository after `canon/` and
`rules/` themselves.** Created 2026-09-25 (ledger 76); the directory existed from
2026-09-23 but was undocumented, so a session following `CLAUDE.md` would not know to look
here.

## Authority

A ruling here **overrides any interpretation in `proposals/`, `recovery/` or `reports/`
within its stated scope — and only within it.** It does not by itself edit `canon/`,
`rules/` or the grids; migrating a ruling into the substrate is separate work, done and
recorded in the ledger.

## Every ruling states its scope of acceptance

The convention the 2026-09-23 rulings established is **permanent**. An author reply such
as *"Agreed"* accepts the specific recommendations put to the author — not every source
line, candidate detail or proposal those recommendations cite. So each ruling records:

1. **What was accepted**, item by item.
2. **What remains unapproved** beside each item.
3. **The decision chain** — the proposals and docket the author was responding to.
4. **The author's words**, quoted, when the acceptance was conversational.

This is what stops *proposal → conversational agreement → accidental wholesale
canonization*. A ruling that cannot fill in column 2 is not ready to be written.

## Naming

`{SCOPE}_{TOPIC}_AUTHOR_RULING_{YYYY-MM-DD}.md`. Machine-readable companions a ruling
requires sit beside it and name the ruling they serve
(`B01_SEQUENCE_EXCEPTIONS_PROVISIONAL.json`).

## Index

### In this directory

| File | Rules on |
| --- | --- |
| `B01_EVENT_OBSERVATION_AUTHOR_RULING_2026-09-23.md` | B01 event observations D1–D7; holds event EBCI; the two sequence inversions |
| `B01_SEQUENCE_EXCEPTIONS_PROVISIONAL.json` | Machine-readable hold for those inversions (companion, not a ruling) |
| `B05_TECHNICAL_EVIDENCE_FUNCTION_AUTHOR_RULING_2026-09-23.md` | B05 fallible technical evidence / institutional concealment as story function |
| `B01_E19_EBCI_GATE_AUTHOR_RULING_2026-09-25.md` | Retires the standalone E19+ prohibition; the B01 EBCI hold becomes the single gate, and stays shut |
| `SAGA_MILESTONE_GATE_AUTHOR_RULING_2026-09-26.md` | The five milestone-gate decisions: Tahl named in B3 epilogue; Tahl posted the coordinates; LT is Seraphine reaching out to survivors. Riot/meta/Colorstorm and B08's opening are **leans only** |
| `LT_ACCESS_AND_B09_EPILOGUE_AUTHOR_RULING_2026-09-26.md` | Amends Mechanica §39: Kade has LT access (a floor, not the full list). B09 epilogue scene: Lacuna and Kade under the night sky, closing on LT reaching out, Möbius with the B01 prologue |
| `B03_WAREHOUSE_AUTHOR_RULING_2026-09-26.md` | Tahl did not know Baz was there. Post staging narrowed to supplemental text or effect-only. Epilogue aftermath via reports (hedged). Links 5–7 **delegated**: working assumption only |
| `B06_B08_B09_EPILOGUE_AUTHOR_ANSWERS_2026-09-26.md` | Tahl's Echo identifiable once; Tahl learns Baz's name from a news report; ladder mapping accepted; M20 act **not** confirmed (lean end of A2). Elias claims the B8 opening for Kade; Loom needs development. Epilogue: Tahl's echo is the LT conduit; `LT_RULES` §6 exception; Kade reintegrates the rebellion |

### Earlier rulings, which stay in `recovery/`

These predate this directory. They are **not moved**: `recovery/` holds originals and is
never altered in place, and many documents link to these paths.

| File | Rules on |
| --- | --- |
| `recovery/CANON_DECISIONS_2026-09-18.md` | Vocabulary collision, SID format, `BT` beat IDs, `LOAD` axis, source tiers, Act I status |
| `recovery/GATE_RULINGS_2026-09-19.md` | Rulings 1–4 (location taxonomy, `Corridor`, character manifest, branch merge); Amendment 1 (`Foix` retired, `Bastien "Baz" Arnaud`) |
| `recovery/GATE_RULINGS_2026-09-20.md` | Rulings 5–9: soft trilogy ceilings, `PR`/`EP` outside the act model, per-trilogy pressure, derived locations, derived POV rotation |
| `recovery/GATE_RULINGS_2026-09-21.md` | Ruling 10: prose scoped to `sources/` and `manuscript/` (its redaction Amendment 1 is specified in `sources/README.md`) |
| `recovery/CHANNEL_NAMES_RULING_2026-09-19.md` | MT / VT / LT are three Threads |
| `recovery/BAZ_DEATH_TIMING_RULING_2026-09-19.md` | Baz dies at the end of B03 |

New rulings go **here**, not in `recovery/`.
