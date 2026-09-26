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
| **Book 9 epilogue** — timeskip. **Ruled 2026-09-26:** LT is the epilogue's final beat, Seraphine reaching out to survivors; **MT continues** under a new MT-initialled name (*MendedThread*, *MortalThreads* are examples, not a choice) with a new role for it and for Kade — role unspecified. M35's wording is superseded. **Also ruled:** a Lacuna–Kade night-sky scene closing on an LT prompt, Möbius with the B01 prologue. **Recovered 09-26:** it is the author's own locked 2025-11-29 design. **Answered 09-26:** the timeskip leans to **a few days**. **Tahl's echo is the conduit** for the trio's reach, ruled. The handshake reaches Kade's device through a **`LT_RULES` §6 exception**. **Kade reintegrates the rebellion's people** alongside Elisabet and Rex, ruled. Still open: the timeskip (a lean, not ruled); the entity's name (*Accord* / *Concord*); the epilogue triangle is **implied**, not an appearance (ruled) | ledger §27.3, §89, §92, §93; `decisions/B06_B08_B09_EPILOGUE_AUTHOR_ANSWERS_2026-09-26.md`; `recovery/B09_EPILOGUE_KADE_LACUNA_SOURCE_RECOVERY_2026-09-26.md`; `decisions/SAGA_MILESTONE_GATE_AUTHOR_RULING_2026-09-26.md`; `decisions/LT_ACCESS_AND_B09_EPILOGUE_AUTHOR_RULING_2026-09-26.md` |
| **LT access beyond Kade.** §39 **amended 2026-09-26**: Kade has access, by named exception ("at least Kade"). Still open: other protagonist survivors; what access consists of (KadeEBCI's *"(no agency)"*); the author's *"more tangible than VT"* against `LT_RULES`' softer language | `decisions/LT_ACCESS_AND_B09_EPILOGUE_AUTHOR_RULING_2026-09-26.md`; ledger §89 |
| **B03 Warehouse** — which of the two post stagings (supplemental text or effect-only); whether the reported dead first responder is Baz or a second death. (Tahl learns Baz's name from a news report before B06, ruled 09-26.) Links 5–7 are **delegated** to a working assumption the author may override | `decisions/B03_WAREHOUSE_AUTHOR_RULING_2026-09-26.md`; ledger §89, §93 |
| **B06 / B08 remaining** — M20's act (lean: the very end of B06 A2; may wait for Neon episode mapping); M36's farewell against the single identifiable Echo (the B09 flare, known by Rex — ruled 09-26); whether Kade actually caused the B08 opening; where Elias is when he claims it; how the factions learn of the site in B09 A3 | `decisions/B06_B08_B09_EPILOGUE_AUTHOR_ANSWERS_2026-09-26.md`; ledger §93 |
| **Loom details after the spine ruling** (09-26: the 11-28 plan is the spine; B07 = Kade's post + NOLA breaks; B08 = thin-place finding + Kade's complicity; Lacuna split foreshadowed end B07, made at start B08). Follow-up ruled: thin place **Santa Fe**; B07 opens **at the funeral, Lacuna prominent**; B09 escape at **Serpent Mound**. **The factions and others think it leads back to Louisiana (perhaps via the storm-wall opening); the primary protagonists know there are multiple wounds and Honey Island must be repaired last** (ruled 09-26). *Maybe* getting that knowledge unravels Tahl (hypothesis). **Repair = stabilisation; the circuit is Silence and Hope's hard-cap plan, and Seraphine grows to question it and begins the breathing-veil potential** (ruled 09-26); the crew stabilises Santa Fe (lean). Open: which wounds and in what order; how the crew has the knowledge; Tahl's death specifics (search running). Event cards written (`proposals/B07_FUNERAL_POST_*`, `proposals/B08_SANTA_FE_FINDING_*`). Still open, per the cards: Kade's post content, where NOLA breaks, civic or scar, post/break order; the Santa Fe finding and its cost; how the crew learns "Louisiana"; the form and victims of Kade's complicity | `decisions/LOOM_SPINE_AND_ANCHORS_AUTHOR_RULING_2026-09-26.md`; ledger §96, §97 |
| **Elias card corrections (E1–E10)** — specified with exact before/after text at the author's request; **awaiting approval**, not applied. The E3 option (a or b) is the author's. Ruled 09-26: Elias handle-only in Neon; some splinters become Brightbreak; Lacuna nudges Kade to post and he thought MT private; attack motive = fear Rex will kill Elias; a Solace-led Choirless acceptable (source search running) | `proposals/ELIAS_CARD_CORRECTIONS_PROPOSAL_2026-09-26.md`; `decisions/LOOM_WOUNDS_AND_ELIAS_AUTHOR_ANSWERS_2026-09-26.md`; ledger §100, §101 |
| **Four author locks living only in proposals** (Baz death timing, Baz name, Tahl B01–B03 absence, VT contact ladder) — unmigrated. Tahl's **naming in the B3 epilogue** now has an author source (2026-09-26); *"not a primary character in B01–B03"* is still paraphrase | ledger §26.6 |
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
  Census Passes 1–3 and the rhythm pass are done (ledger §81–§83); the rhythm pass is a
  **book-internal** judgment, provisional on the saga and Veil trilogy passes.
- **Recovered episode material:** B01–B03, E00–E42 per book (`recovery/ACCOUNT_EXPORT_B0*_ACT*_EPISODE_FORENSIC_AUDIT_2026-09-20.md`).
- **Substrate:** 2 of 7 grids populated (`milestones_payoffs` 36 rows, all `proposed`;
  `locations_registry` 31). `episode_beats`, `breadcrumbs`, `reaction_modifiers`,
  `reader_pressure`, `supplement_deployment` are header-only. Book contexts and act overlays
  carry 108 `TODO`s; act overlays' `act_thesis` and `deltas` are unfilled.
- **Saga structure:** event tiers A–D and the unslotted pool
  (`proposals/SAGA_EVENT_TIERS_AND_UNSLOTTED_POOL_PASS1_2026-09-23.md`). The 36-milestone
  grid is a candidate set, not the saga skeleton. B08 has no recovered independent
  non-finale turn; POOL-017 is the leading candidate (saga pass 1, ledger §85).
  **The five milestone-gate decisions are answered** (2026-09-26,
  `decisions/SAGA_MILESTONE_GATE_AUTHOR_RULING_2026-09-26.md`) — three ruled, two leans.
  Next per the packet: B3/B6/B8 event cards, then a proposed grid **copy**; the live grid
  is untouched until that copy is approved. **All three cards done** (2026-09-26): B3 Warehouse
  (answered, `decisions/B03_WAREHOUSE_AUTHOR_RULING_2026-09-26.md`); B6 Santa Fe and B8 storm
  wall (`proposals/B06_*`, `proposals/B08_*`, ledger §91), answered 09-26 with items still open
  (`decisions/B06_B08_B09_EPILOGUE_AUTHOR_ANSWERS_2026-09-26.md`). **Loom:** spine and anchors
  ruled; B07 and B08 anchor cards written (ledger §97). **Next: a proposed grid copy.**
- **`LT_RULES_POST_MENDING.md` §6** has a named exception for the B9 epilogue handshake,
  enabled by Tahl's echo (2026-09-26).
- **Mechanica §39 amended 2026-09-26** by author instruction: Kade has LT access
  (`decisions/LT_ACCESS_AND_B09_EPILOGUE_AUTHOR_RULING_2026-09-26.md`).
- **Branches:** `main` is live. `claude/gifted-goodall-st4n7r` and
  `proposal/concord-2026-reconciliation` are **archival** — do not merge. The former's only
  unique change is an older `narrative-audit-framework-v1.md`; salvage concepts from it,
  not the branch.
- **Project knowledge** in the claude.ai Project may hold an older copy of this file.
  The repository copy wins.

---

## 9. Work queue and reading map

**Reordered 2026-09-25 by author direction** (ledger §84): *"our next tasks are going to be
saga wide milestones, rhythm, balancing, etc then we will work on episodes for B2 and B3 to
complete the trilogy, then we will work on EBCI for B1 and develop packets for sudowrite."*

**The hierarchy: saga → trilogy → book → episode → EBCI → prose.** Work flows down it.
A book that paces well on its own can still repeat the saga's escalation shape, so book-level
judgments are provisional until the levels above them are settled.

1. **Saga-wide structural pass — ACTIVE.** Anchors and book turns; the unslotted event pool;
   milestone/payoff architecture; causal dependencies and carry-forward; nine-book rhythm and
   density; Life/Reward balance; threat/recovery distribution; wonder, fun, romance, heat,
   humour; character bandwidth and recurrence; place recurrence; antagonist/faction pressure;
   Mechanica/Resonance escalation; reveals, mysteries, anticipation and payoffs; trilogy
   transitions. **Especially: strengthen B07–B08 without stealing B09's ending** — B08 still
   has no recovered independent non-finale turn. **Author, 2026-09-26:** *"we need to spend a
   good bit of time developing Loom. We essentially figured out the last couple episodes and it
   has been spreading thin."* **Constraint, 2026-09-26:** the antagonist factions **do not know
   the swamp is the Mending site until B09 Act III**; *"we can't have an entire book of them
   laying siege on the mending site."* Much of the pasted B07–B09 master conflicts
   (`decisions/B06_B08_B09_EPILOGUE_AUTHOR_ANSWERS_2026-09-26.md` §4.1). **Loom pass 1 done
   (2026-09-26, `proposals/LOOM_STRUCTURAL_PASS1_B07_B09_2026-09-26.md`):** the author's own
   2025-11-28 per-book plan is **the spine (ruled 09-26)**, with anchors ruled for B07 and B08
   (`decisions/LOOM_SPINE_AND_ANCHORS_AUTHOR_RULING_2026-09-26.md`). The Dec 8 Veil/Neon/Loom "masters" are
   **assistant output** the author backed up, not his words. **Starts as a reconciliation**: a large body
   of 09-19 → 09-24 saga work exists (reading map below). Read it before generating.
2. **Lock saga architecture enough for downstream work** — major obligations, turns,
   escalation curves and protected negative space stable enough that expanding one book
   cannot consume another's material. Not every event needs exact placement.
3. **Complete Veil at episode-architecture level** — B02 and B03 to a resolution comparable
   with B01 v4.1b. **Architecture, not EBCI.** B04–B09: no episode expansion yet.
4. **Veil trilogy audit** — with B01–B03 visible at episode resolution: cross-book pacing,
   breadcrumbs, entrances/exits, relationship arcs, Mechanica exposure, locations, Baz's B03
   endpoint, the B03→B04 handoff, and whether B01 carries anything B02/B03 should own.
5. **B01 EBCI — author gate.** The hold in `decisions/B01_EVENT_OBSERVATION_AUTHOR_RULING_2026-09-23.md`
   stands and is the only gate (`decisions/B01_E19_EBCI_GATE_AUTHOR_RULING_2026-09-25.md`).
   Packets are generated against a known trilogy future, not only a known B01 future.
6. **Sudowrite production packet** — a deliberately **smaller, derived** prose-facing interface
   built *from* EBCI: intent, beats, POV state, setting, character and relationship state,
   pressure, Mechanica constraints, breadcrumbs, continuity obligations, protected reveals,
   voice, exit state. **Never feed raw EBCI, canon or recovery material to prose generation.**

**Do not create an `ebci/` directory yet** — it would signal that EBCI is the active layer.
**Navigation manifests are deferred** until Veil EBCI is built, possibly later — author,
2026-09-25. §8 stays the only current-state record; reading lists live in the map below.

**Completed 2026-09-25, and what each is still subject to:**
- Governance consolidation (§76–§79). Retired-term sweeps complete.
- Cast reconciliation Pass 4 (§80) — six author decisions open; none blocks the above.
- B01 event census Passes 2–3 (§81–§82). E23/E38/E40 need source reading; `B1-45A` gated by D5.
- B01 rhythm pass (§83) — **book-internal**. It shows B01 works on its own terms and is
  provisional on steps 1 and 4.

**Standing constraints:** the manufactured-meta transfer loop must be settled before any Neon
combat/meta episode work; D5 holds causal physics; D7 holds the two B01 sequence inversions.

**Reading map — start here, not everywhere.**

| Task | Read |
| --- | --- |
| Anything B01 | `decisions/B01_*`, v4.1b integrated, latest `proposals/B01_*` census and cards |
| Identity question | `canon/characters/`, `canon/cast_registry.csv`, `cast_retired_aliases.csv` |
| Cast reconciliation | `proposals/concord-2026/SECONDARY_TERTIARY_CHARACTER_AUDIT_PASS1–3`, `recovery/MARA_NIHT_RECOVERY_2026-09-21.md` |
| Mechanics / Resonance | `rules/Mechanica-v4.md`, `rules/Resonance-v1.md`, `reports/MECHANICA_RESONANCE_SYSTEMS_INTEGRITY_AUDIT_2026-09-23.md` |
| Saga events / milestones | event tiers + pool proposal, `grids/milestones_payoffs.csv`, `proposals/MILESTONE_GATE_AUTHOR_EDITOR_DECISION_PACKET_2026-09-23.md` |
| **Saga structural pass (step 1)** | `proposals/SAGA_EVENT_TIERS_AND_UNSLOTTED_POOL_PASS1_2026-09-23.md`; `reports/M01_M36_MILESTONE_DESCRIPTION_AND_DEPENDENCY_REVIEW_2026-09-23.md` and the `M01_M36_*` adjudication/overlay; `recovery/SAGA_RESONANCE_EVENT_ANCHOR_REGISTER_PASS3_2026-09-23.md`; `proposals/SAGA_PLACE_PRESENCE_ANTAGONIST_TRANSITION_MAP_PASS1_2026-09-23.md`; the B03→B07 carry-forward and B07/B08/Loom ledgers; `recovery/SAGA_TIMELINE_2026-09-19.md`; `rules/saga_context_S1.json` |
| **Veil completion (step 3)** | `recovery/VEIL_TRILOGY_RECONCILIATION_MAP_2026-09-20.md`; `recovery/B02_` and `B03_RECONCILIATION_MAP_2026-09-20.md`; the B02/B03 `ACCOUNT_EXPORT_*_EPISODE_FORENSIC_AUDIT_2026-09-20.md` files; B01 v4.1b as the reference model |
| Citing a 09-21 B01 ECG report | Its episode numbers are **v3**; map to v4.1b first — `reports/B01_WHOLE_BOOK_RHYTHM_PASS_2026-09-25.md` §1 |
| What happened recently | the last five ledger entries, `git log --since` |
| Anything touching sources | `sources/README.md`, ledger §70–§74 |
