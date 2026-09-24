# Editorial review of the 2026-09-20 → 2026-09-24 work

**Date:** 2026-09-24
**Status:** EDITORIAL REVIEW / NON-CANONICAL. No rule file, beat bible, ruling or report
is amended. Dissent, where offered, is stated against the named document per the review
handoff in `decisions/B01_EVENT_OBSERVATION_AUTHOR_RULING_2026-09-23.md`.

**Occasion.** A survey written on 2026-09-24 re-derived findings that the 2026-09-20
forensic audits already held (ledger §74 §4). That was a reading failure, and it is also a
**symptom**: the working agreement no longer describes the repository, so a session that
follows `CLAUDE.md` faithfully can still miss four days and 180 commits. This review reads
the body of work and reports what the audits could not check about themselves.

## 1. What the four days produced

| Phase | Dates | Output |
| --- | --- | --- |
| Account-export forensic audits | 09-20 → 09-21 | 24 source audits; **Book 1, 2 and 3 episode audits E00–E42 per book**; three reconciliation maps plus a Veil trilogy map |
| B01 beat bible | 09-21 → 09-22 | `v1 → v4 → v4.1 → v4.1a → v4.1b integrated`; narrative ECG, Life/Reward layer, supplement interleave, NOLA geography, cast entry/exit |
| Systems forensics | 09-22 → 09-23 | Mechanica/Resonance, Conflict and VFX integrity audits, each with a paired reconciliation proposal; character/tech/meta recovery passes |
| Lived-world | 09-22 → 09-23 | Shared baseline plus Veil/Neon/Loom overlays; under-mined systems inventory; gap audit |
| B01 event mechanics | 09-23 | Candidate cards → docket → **author ruling D1–D7** → falsification and ontology passes |
| Saga event anchors | 09-23 | Anchor inventory, gap sweep, register pass 3; B4/B5/B6/B7/B8 source tests; **B05 author ruling** |
| Milestones | 09-23 | All 36 rows reviewed against the anchor register; wording overlay; adjudication; decision packet |
| Loom and carry-forward | 09-23 → 09-24 | Place/presence maps, event tiers, unslotted pool, named carriers, MT succession |

**The judgment underneath it is sound, and the discipline is unusually good.** Sources are
tiered, statuses are explicit (`CURRENT` / `RECOVERED` / `RECONCILE` / `OPEN` /
`SUPERSEDED`), superseded findings are annotated rather than rewritten, and the author
rulings state their own **scope of acceptance** — `B01_EVENT_OBSERVATION_AUTHOR_RULING`
says outright that it "does not claim the author reviewed each prior source line." That is
the single most valuable habit in the whole body, because it is what stops an "Agreed" from
silently becoming approval of everything upstream of it.

## 2. Mechanical verification of `FULL_EXPORT_ALL_SYSTEMS_STATE_REVIEW_2026-09-23`

Checked from a clean checkout. **Every claim I could test holds.**

| Claim | Verified |
| --- | --- |
| `rules/Channels/CHANNELS_OVERVIEW.md` still calls MT "Mortal Technology" | **Yes** — plus `MT_RULES.md:11` and `Mechanica-v4.md:722, 1136` |
| Five of seven grids header-only | **Yes** — `breadcrumbs`, `episode_beats`, `reaction_modifiers`, `reader_pressure`, `supplement_deployment` at 0 rows; `locations_registry` 31, `milestones_payoffs` 36 |
| `source_canon/tech/` and `environments/` hold only READMEs | **Yes** — and `factions/` and `metaphysics/` too |
| `canon/saga_overview.md` and trilogy cards carry TODO scaffolding | **Yes** — plus `editorial_lenses.md` |

One correction of emphasis, not of fact: the review says `VT_RULES.md` is among the stale
prose files. It is **not** — line 15 already carries an explicit retirement note. The stale
ones are `CHANNELS_OVERVIEW.md`, `MT_RULES.md` and `Mechanica-v4.md`, and `MT_RULES.md` is
**held deliberately** by `CLAUDE.md` §4 until the MT/infrastructure question is ruled.
Renaming it now would leave a file called MissingThread describing phone networks.

## 3. Three governance defects the audits could not see about themselves

### 3.1 `Technarch` has re-entered for the fifth time — and this time in the documents' own voice

`CLAUDE.md` §9.1 records four corrections, three re-entries, and predicts a fourth:
*"Expect it again. Any merge from a branch cut before a naming ruling, and any migration
that copies a heading verbatim, reintroduces it."* Both predicted routes are merges and
migrations. **This one is neither.**

| Directory | `Technarc` (canonical) | `Technarch` (retired) |
| --- | --- | --- |
| `canon/` | 73 | **0** |
| `rules/` | 2 | **0** |
| `grids/` | 3 | 1 |
| `decisions/` | 0 | 1 |
| `reports/` | 13 | **23** |
| `proposals/` | 180 | 17 |
| `recovery/` | 190 | 123 |

**Canon scope is clean** — that part of §9.1's count still holds and is the part that
matters most. But §9.1's *"proposals 6"* is now **17**, and in `reports/` the **retired
spelling outnumbers the canonical one**.

These are not the annotated quotations §9.1 describes. **2 of the 29 occurrences in the
2026-09-2x layer sit anywhere near a supersession marker.** The rest are the documents
speaking in their own voice — *"Technarch positioning/deployment/containment choice creates
a local incident"*, *"a Technarch model can predict Santa Fe badly"*. That is drift, and a
new route: **sustained analytical writing about a faction adopts whichever spelling the
sources use.**

**The prescribed mitigation has now failed five times.** §9.1 says to run
`grep -ro 'Technarch' canon/ rules/ grids/` after any merge or bulk migration; a manual
step that must be remembered is not a control. §9.1 also asserts *"the validator cannot
catch this — it is a spelling question, not a format violation."* **That is true of the
current validator and false as a limit.** A retired-terms check is structurally identical
to `CHK_VOCAB`: read a `retired_terms` map from `canon_rules.json`, violation in canon
scope, notice elsewhere. See §5.

### 3.2 `reports/` has been silently repurposed, and its README now contradicts its contents

`CLAUDE.md` §1 and `reports/README.md` both designate the directory **generated
artifacts**: *"do not hand-edit, regenerate."*

It holds **34 files. Two are generated** — `VALIDATION_BASELINE_2026-09-19.md` and its
all-scope pair. **Thirty-two are hand-authored editorial reports**, including the two most
load-bearing documents of the week.

This matters in three ways, ascending:

1. A session that obeys the stated rule would refuse to write there, or worse, "regenerate"
   over authored analysis.
2. **The two genuinely generated files are stale.** They record 27 canon-scope and 61
   all-scope violations; the current figures are **0** and materially different. A reader
   checking the baseline gets a number that is five days and several rulings old.
3. The directory's name no longer distinguishes **evidence** (`recovery/`), **argument**
   (`proposals/`), **verdict** (`decisions/`) and **generated fact** (`reports/`) — an
   otherwise clean four-way separation that the recent work observes everywhere else.

**This needs a ruling, not a cleanup.** Either the authored reports move, or `reports/`
is redesignated and the generated baselines move under it by another name. Either way
`CLAUDE.md` §1 and `reports/README.md` must stop saying what they currently say.

### 3.3 `decisions/` is undocumented

The directory holds the two **author rulings** — the highest-authority artifacts produced
this week — and appears in no table, index or ledger section in `CLAUDE.md`. A session
reading the working agreement would not know to look there, which is precisely the failure
that occasioned this review.

## 4. `CLAUDE.md` is now the repository's least current document

Not a style complaint. It is the file every session is told to read first, and its §8 work
queue is where a session takes its direction.

| Section | Says | Actually |
| --- | --- | --- |
| §6 | *"the repository holds packets for E16–E18 only"* | **E00–E42 for Books 1–3** are recovered and audited |
| §8 item 6 | Three concrete targets outstanding | **All three resolved.** `Spine Architect chat` is empty, `Saga Visual Bible Framework` is a scaffold, `Develop Singer Style` was the wrong project. The workspace inventory ran — 72 conversations indexed |
| §8 item 7 | *"Archive Veil Book 1 first — this is where the E00–E15 packets are expected to be"* | Satisfied on 09-20 **from a different conversation**, `Episode expansion process` |
| §8 item 9b | Silence and Hope: exports hold *"essentially nothing"* | True of the sanitized derivative; the account export holds the prologue **twice** |
| §8.0 | Locations, combat, antagonist arcs *"missing from the repository"* | Recovered, and the 09-22/23 systems work went far past them |
| §9.1 | `proposals/` 6 `Technarch`; every occurrence an annotated quotation | **17**, and mostly not quotations (§3.1) |
| §1 table | `reports/` = generated artifacts; no `decisions/` | §3.2, §3.3 |

§6 carries its own warning — *"Verify with `git` before trusting this section; it dates
quickly"* — and the warning worked exactly as intended in that one section. The queue in §8
carries no such warning and is where the misdirection actually happened.

**Recommendation: one consolidation pass on `CLAUDE.md`.** Not a rewrite — the rulings,
conventions and open-author-question list in §3 and §4 are current and carefully built. The
stale parts are the *state* sections: §1's table, §6, §8's queue, §9.1's counts.

## 5. Two tooling items I can build, both outside canon

Offered, not begun.

1. **`CHK_RETIRED_TERMS`.** A `retired_terms` map in `canon_rules.json` — `Technarch →
   Technarc`, `Veil-Touch → VeilThread`, `Mortal Technology → MT/MissingThread`, `Kade Rios
   → Kade Harper`, `Caro Gauthier → Carolina "Caro" Alvarez`, `Koro Ito → Ito Masayuki`,
   `Foix → Arnaud` — enforced as a **violation in canon scope** and a **notice elsewhere**,
   with a suppression marker for deliberate quotation so the annotated cases stay legal.
   This converts §9.1's manual grep into a check that cannot be forgotten, and it directly
   addresses the one defect class that has recurred five times. It would also catch the
   `Mortal Technology` occurrences in §2's table — but note `MT_RULES.md` is **held**, so
   that file needs an explicit exemption until the MT question is ruled, or the check will
   demand a change §4 forbids.

2. **The provisional exception manifest** that `B01_EVENT_OBSERVATION_AUTHOR_RULING` §4
   requires and that does not exist: *"tooling must not rely on either naive file order
   **or** numeric sorting for those ranges; use an explicit provisional exception manifest
   if any read-only analysis requires sequence."* The two inversions — E37/E36 with S05, and
   E44/E43 — are currently a trap for any automated pass, and the ruling anticipated the
   trap without the artifact being built. A small machine-readable file naming the two
   ranges, both orders, and the fact that neither is chosen would make the hold enforceable
   instead of remembered.

## 6. One substantive agreement worth recording

`PRE_EBCI_SYSTEMS_AUDITS_REVIEW` recommends treating **`FX2` as a presentation default,
not a mechanism, event-size score or hard ceiling.** The repository already implements
exactly this, independently and for a different reason: `container_band()` in
`tools/validate_canon.py` deliberately returns `None` for the `fx` axis, so `CHK_CONTAINMENT`
never checks FX as a ceiling — because `default_vfx_ceiling` is a **default** (ledger §57).

Two separate lines of reasoning, five days apart, reached the same conclusion about the
same axis. That is corroboration rather than coincidence, and it is worth having on record
when the FX question is next argued — particularly against the recovered `E14` packet note
calling **FX3** the *"Act-level limit"* (ledger §74 §3).
