# CLAUDE.md — Concord Saga Canon

Standing instructions for any Claude session working in this repository. Read it before
touching files. It is the working agreement, not canon.

**Rewritten 2026-09-25 (ledger §76).** The previous version had grown to 883 lines of
rules interleaved with dated history, and had fallen 180 commits behind the repository.
It is archived verbatim at `recovery/CLAUDE_MD_ARCHIVE_2026-09-21.md`. **Any citation of
"CLAUDE.md §N" written before 2026-09-25 refers to the archive**, not to this file.

**This file holds rules, not history.** History goes in `recovery/RECOVERY_LEDGER_2026.md`.
The one dated section is §8, and it says when it was last true.

---

## 1. What this repository is

Non-prose canon substrate for the Concord Saga, a nine-book serial, plus the source
material and analysis it is built from. Material moves through it in one direction:

```
sources/ → recovery/ → reports/ + proposals/ → decisions/ → canon/ rules/ grids/ … → (EBCI, manuscript/)
evidence    forensics    assessment + options   rulings      authoritative substrate    production
```

| Folder | Holds | Rule |
| --- | --- | --- |
| `sources/` | The 2026-09-15 ChatGPT account export, verbatim | Append-only, never edited. Prose allowed. Outside validation. See `sources/README.md` |
| `recovery/` | Forensic audits, ledgers, checkpoints, sanitized HTML exports | **Originals. Never pruned or altered in place.** Corrections go in new files or ledger entries |
| `reports/` | Authored editorial reports (audits, stress tests, reviews) **and** generated `VALIDATION_BASELINE_*` | Two kinds, two rules — see `reports/README.md` |
| `proposals/` | Distilled architectures, card sets, reconciliations | Editable, non-canonical, Tier D |
| `decisions/` | **Author rulings**, each with its scope of acceptance | Overrides the three folders above within stated scope — see `decisions/README.md` |
| `canon/` | Tier-1 character, faction, POV cards; codex; trilogy summaries | Substrate. **`canon/characters/` names are final** |
| `rules/` | `canon_rules.json`, trilogy and saga contexts, Mechanica, Resonance, system docs | Substrate |
| `grids/` | CSV structure and telemetry grids | Substrate |
| `book_context/`, `act_overlays/` | 9 book and 27 act JSON contexts | Substrate |
| `templates/` | Hand-authored templates | Substrate; generated artifacts *from* them are not hand-edited |
| `source_canon/` | High-resolution exploratory material | **Authority unresolved** — §5 |
| `manuscript/` | Authored narrative prose | Never tool-rewritten without instruction. Outside validation |
| `tools/` | Validator, its self-test, source verifier, ingest tools | — |

**No prose, scene text, dialogue or lyrics in the substrate** (`rules/`, `canon/`, `grids/`,
`book_context/`, `act_overlays/`, `templates/`). Prose is permitted only in `sources/` and
`manuscript/` (`recovery/GATE_RULINGS_2026-09-21.md`, Ruling 10). **Location is not
authority**: nothing in `sources/` or `manuscript/` is canon by being in the repository.
Canon is what the substrate says.

---

## 2. Autonomy and git

Work without asking for step-by-step approval. The author's stated goal is that Claude
manages this repository without his input at every step.

- **Commit after each finished unit of work**, with a real message saying what changed and
  why. Never `wip`, `Auto-sync` or `update files`.
- **Pull before pushing.** Other sessions, other assistants and the author push here.
- **Push to `main`** unless the harness pins the session to a branch. Never force-push;
  never rewrite published history.
- **No push credentials?** Commit locally and hand the author a patch series
  (`git format-patch origin/main`) to apply with `git am`. Do not ask for a token in chat.
- **Never delete recovered source material.** Flag empty or broken files in the ledger.
- **Run before every commit that touches the substrate:**

  ```sh
  python3 tools/validate_canon.py          # canon scope; must exit 0
  python3 tools/test_validate_canon.py     # self-tests; must pass
  python3 tools/verify_sources.py          # if sources/ changed
  ```

  CI runs the same three on every push (`.github/workflows/validate.yml`).
- If a task turns out to need a canon decision (§4), **commit the analysis and stop.**

---

## 3. Identifiers and names

Ruled in `recovery/CANON_DECISIONS_2026-09-18.md` and the gate rulings; indexed in
`decisions/README.md`.

- **SID:** `S1.T{1-3}.B{01-09}.{A1|A2|A3|PR|EP}.E{00-99}`. Books are **always two digits**.
  `B1` is wrong wherever it appears — **including informal labels in new documents**
  (`B01-23A`, not `B1-23A`). Recovered one-digit forms are migrated, not copied.
- **Episodes number continuously across the whole book**; they do not restart per act.
  The prologue is `E00`, *The Conversation in the Sky*. `PR` and `EP` are structural
  positions beside the three acts, not acts (Ruling 6); every book has exactly three acts.
  Epilogue episodes take the next sequential number.
- **Beat IDs:** `{SID}-BT{nn}`.
- **Trilogies:** `T1` Veil (B01–B03), `T2` Neon (B04–B06), `T3` Loom (B07–B09).
- **Channels are three Threads:** `MT` MissingThread (public, mortal), `VT` VeilThread
  (private, between Silence and Hope), `LT` LuminousThread (post-Mending).
- **ECID schema is canonical; packet labels are aliases.** Fields: `POV ENV CORRIDOR
  WEATHER MODE RES LOAD`, plus `HEAT FX` optional at shell granularity. `U-Level` →
  `CORRIDOR`, `Resonance State` → `RES`. One value per field; store the end state, not an
  arrow. Migration mapping: decisions §1.5, **keep the original string in `Notes`**.
- **Names:** check `canon/characters/` first on any identity question. Retired names —
  `Technarch`, `Veil-Touch`, `Kade Rios`, `Caro Gauthier`, `Koro Ito`, `Foix` — are listed
  in `rules/canon_rules.json` `retired_terms` and **enforced by `CHK_RETIRED_TERMS`**:
  a violation in canon scope, a notice elsewhere. Quote a retired name only as evidence.
  **`Mortal Technology` is held, not retired** (§4).

---

## 4. What requires the author

James makes canon decisions. Claude does not decide, invent or quietly resolve anything
about characters, factions, metaphysics, plot or world rules; does not pick a winner
between conflicting sources (record both readings and where each came from); and does not
promote assistant-generated material to canon.

**An author "Agreed" accepts the specific recommendations put to him, not everything they
cite.** Record every acceptance as a ruling in `decisions/` that states what was accepted
and what was not (`decisions/README.md`).

### 4.1 Open author questions

Each line points at where the evidence is. Ledger § numbers are in
`recovery/RECOVERY_LEDGER_2026.md`.

| Question | Where |
| --- | --- |
| **B01 EBCI release** — held by the 09-23 ruling | `decisions/B01_EVENT_OBSERVATION_AUTHOR_RULING_2026-09-23.md` |
| **B01 sequence inversions** E36/E37 + S05 and E43/E44 — one architecture decision | `decisions/B01_SEQUENCE_EXCEPTIONS_PROVISIONAL.json` |
| **Which Veil draft is canon**, now including the one-episode Act I boundary disagreement (E15 vs E16) between two witnesses; Caro in B01–B02; Santa Fe | ledger §26.9, §27.6, §74 §4 |
| **Prologue act slot `A0`** and the `B01.A1` band breach it implies | ledger §74 §3 |
| **`MT` vs the infrastructure layer** (options A/B/C). Do not rename `MT_RULES.md` until ruled. Note: `canon_rules.json` `_naming_note` calls Mortal Technology retired; the rulings hold it open — contradiction recorded, not resolved | `recovery/CHANNEL_NAMES_RULING_2026-09-19.md` §2; ledger §20 |
| **Post-Mending `res_states`** (the `LT` omission); Post-Mending era file held | ledger §18; `proposals/concord-2026/CHANNELS_AND_RESONANCE_STATES_2026-09-19.md` §4 |
| **Closed vs spaced** `LuminousThread` / `MissingThread` | ledger §20 |
| **Book 9 epilogue** — timeskip; whether `MT`→`LT` completes there | ledger §27.3 |
| **Four author locks living only in proposals** (Baz death timing, Baz name, Tahl B01–B03 absence, VT contact ladder) — unmigrated | ledger §26.6 |
| **Which of two conflicting recovered versions wins** (ND-045 proposes a rule; ledger §74 §4 shows recency alone fails) | ledger §26.12 |
| **Cross-project provenance** (Mara Niht's tier; whether Eli Stone integrates; where Mara's lyric corpus is kept) | ledger §66–§69; `recovery/MARA_NIHT_RECOVERY_2026-09-21.md` §5 |
| **`source_canon/` authority** — §5 | — |

**Answered, correction pending (a task, not a question):** who performs the Mending —
five named human functions, of whom the trio ascends. Ledger §24, ND-013 and the old
CLAUDE.md all say "trio" and need correcting. Ledger §27.2.

**Deferred by ruling until recovery and distillation complete:** authoring the ~40
`Asks`/`Flags`/`Protects` fields in `canon/editorial_lenses.md` — never by inference from
board members' published work.

---

## 5. Source tiers and authority

| Tier | Meaning |
| --- | --- |
| A | Explicit locked source canon |
| B | Explicitly approved development outputs |
| C | Existing GitHub canon |
| D | Everything else — Notion, recovered conversations, assistant drafts, proposals |
| E | Memory |

Notion-only facts stay `RECOVERED PRIOR CANON` until re-approved. The D=Notion/E=assistant/
F=memory lettering in `recovery/checkpoints/` is retired and converts wherever found.

**`Mechanica-v4.md` is authoritative until the line-by-line review, but not standalone**:
read it with the channel ruling and `recovery/VEIL_MECHANICA_TERMINOLOGY_RECONCILIATION_2026-09-20.md`.
The review may reopen `STRAIN` (decisions §1.1).

**`source_canon/`** declares itself non-authoritative, while `seraphine_full.md` (its only
populated file; the other eight are 261-byte stubs) is stamped `FINAL CANON`. Until James
rules: do not delete or prune it, do not cite it as authority in `canon/` or `rules/`, and
do not promote or downgrade `seraphine_full.md`.

---

## 6. Sources

- The account export in `sources/chatgpt_export_2026-09/` is **the authoritative original**.
  `MANIFEST.csv` hashes every file; `verify_sources.py` checks them. One permitted
  redaction (`workspace_account_id`), whole-file exclusions only — `sources/README.md`.
- `sources/** -text` in `.gitattributes` stops git transforming line endings. Do not remove it.
- **Commit source material before transforming it**, `.md` and `.json` both — the markdown
  drops system and tool messages.
- `recovery/source_exports/html_sanitized/` is a **lossy derivative** (≈26k words total).
  Conclusions drawn from it are unaudited, not discredited. Do not delete it.
- **Check that a recovered source names what it was recovered for.** A matching id once
  returned the wrong project (ledger §68).
- **Read the existing audits before surveying the export.** The 2026-09-20 forensic audits
  already cover B01–B03 E00–E42; a 09-24 survey re-found them (ledger §74 §4).
- The repository is **public** by the author's choice until narrative generation. Anything
  committed is readable by anyone.

---

## 7. Working style

- **Do not read everything.** Start from §9's reading map and the ledger entries it names.
- Read the relevant ledger entry or audit before editing what it describes.
- Prefer editing in place over regenerating — except in `recovery/`, which is never edited.
- When correcting an artifact, record what was wrong and what replaced it.
- **Life/Reward scenes are narrative, not filler.** Not every worthwhile scene needs a
  mechanism, cost curve or causal edge; do not measure every scene with the event template.
- Every new document opens with a `Status:` line (`NON-CANONICAL`, `PROPOSAL`,
  `CURRENT AUTHOR RULING`, …) and states what it does **not** change.
- **Keep the ledger current.** A change to canon state with a stale ledger is half done.
  Update §8 below when state it records changes.

---

## 8. Current state — as of 2026-09-25

> Verify with `git log` and the tools before trusting this; it dates quickly.

- **Validation:** canon scope **0** violations; **144** self-tests; source verifier PASS at
  138 files. All-scope carries **357** `CHK_RETIRED_TERMS` notices and 112 `CHK_SID_FORMAT`
  violations. **Neither is a defect backlog**: after the 2026-09-25 sweeps (ledger §77, §78)
  the survivors are provenance, quotation and annotated supersession — documents naming a
  retired form in order to retire it. Both counts rise whenever a pass discusses them.
  Canon scope is the number that matters.
- **B01:** integrated architecture `proposals/B01_REVISED_BEAT_BIBLE_V4_1B_INTEGRATED_2026-09-22.md`
  — prologue, 48 narrative episodes, 6 supplements, narrative order locked. **EBCI held —
  and it is now the only gate**: the standalone E19+ prohibition is superseded, ruled
  2026-09-25 (`decisions/B01_E19_EBCI_GATE_AUTHOR_RULING_2026-09-25.md`). **Supersession is
  not release**; no episode may be generated.
  Event census and E23/E38/E40/E45 cards in progress (`proposals/B01_*_2026-09-24/25.md`).
- **Recovered episode material:** B01–B03, E00–E42 per book (`recovery/ACCOUNT_EXPORT_B0*_ACT*_EPISODE_FORENSIC_AUDIT_2026-09-20.md`).
- **Substrate:** 2 of 7 grids populated (`milestones_payoffs` 36 rows, all `proposed`;
  `locations_registry` 31). `episode_beats`, `breadcrumbs`, `reaction_modifiers`,
  `reader_pressure`, `supplement_deployment` are header-only. Book contexts and act overlays
  carry 108 `TODO`s; act overlays' `act_thesis` and `deltas` are unfilled.
- **Saga structure:** event tiers A–D and the unslotted pool
  (`proposals/SAGA_EVENT_TIERS_AND_UNSLOTTED_POOL_PASS1_2026-09-23.md`). The 36-milestone
  grid is a candidate set, not the saga skeleton. B08 has no recovered independent
  non-finale turn.
- **Branches:** `main` is live. `claude/gifted-goodall-st4n7r` and
  `proposal/concord-2026-reconciliation` are **archival** — do not merge. The former's only
  unique change is an older `narrative-audit-framework-v1.md`; salvage concepts from it,
  not the branch.
- **Project knowledge** in the claude.ai Project may hold an older copy of this file.
  The repository copy wins.

---

## 9. Work queue and reading map

Working order adopted 2026-09-25; the author confirmed step 1. Consolidation and
selective promotion, not another archaeological sweep and not mass episode generation.

1. **Governance consolidation** — this rewrite, `CHK_RETIRED_TERMS`, CI, the `decisions/`
   and `reports/` docs, the sequence manifest (ledger §76). Remaining: sweep own-voice
   `Technarch` and one-digit `B1` out of `proposals/` and `reports/` (quotations stay).
2. **Secondary/tertiary cast reconciliation** — especially v4.1b's `Mara/M` slot against
   the recovered Mara Niht; remove duplicate support roles and names; map recurring faces
   to places and books. May change supporting-cast identity; preserves episode function.
3. **Complete the B01 event census** — before/action/after cards, C events separated from
   D receipts, no target count; resolve E23/E38/E40/E45.
4. **One B01 whole-book rhythm pass** — events, Life/Reward, location recurrence, rewards,
   anticipation, romance, humour, wonder, threat, recovery, character load.
5. **Release B01 to EBCI** — author gate.
6. **In parallel:** grow the unslotted saga event pool, B07/B08 first. No B02–B09 episode
   expansion yet. **Manufactured-meta transfer loop must be settled before any Neon
   combat/meta episode work.**

**Reading map — start here, not everywhere.**

| Task | Read |
| --- | --- |
| Anything B01 | `decisions/B01_*`, v4.1b integrated, latest `proposals/B01_*` census and cards |
| Identity question | `canon/characters/`, `canon/cast_registry.csv`, `cast_retired_aliases.csv` |
| Cast reconciliation | `proposals/concord-2026/SECONDARY_TERTIARY_CHARACTER_AUDIT_PASS1–3`, `recovery/MARA_NIHT_RECOVERY_2026-09-21.md` |
| Mechanics / Resonance | `rules/Mechanica-v4.md`, `rules/Resonance-v1.md`, `reports/MECHANICA_RESONANCE_SYSTEMS_INTEGRITY_AUDIT_2026-09-23.md` |
| Saga events / milestones | event tiers + pool proposal, `grids/milestones_payoffs.csv`, `proposals/MILESTONE_GATE_AUTHOR_EDITOR_DECISION_PACKET_2026-09-23.md` |
| What happened recently | the last five ledger entries, `git log --since` |
| Anything touching sources | `sources/README.md`, ledger §70–§74 |
