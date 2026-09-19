# Notion Recovery — Consolidated

**Compiled:** 2026-09-19 · **Tier D**, `RECOVERED PRIOR CANON` until re-approved
**Suggested home:** `recovery/NOTION_RECOVERY_2026-09-19.md`

Notion is connected in the Cowork session and unreachable from Claude Code, so
everything here was read there and is written down for the repository. None of it is
currently in the repo — no file mentions `06 • Post-Mending`, `Silence - Metaphysical`,
or the Notion section-01 pages.

**Naming note.** These documents cite Notion `08.08 • Character Sheet — Baz Foix`.
That surname is **superseded** by commit `a4324a9`, which locks *Bastien "Baz" Arnaud*
as current canon identity. Read every "Baz Foix" below as the Notion-side name only.

Four parts:

1. Where the narrative development actually lives — the survey that reframed the
   recovery target from ChatGPT to Notion
2. The inventory — roughly 240 pages across eight sections, with the sprawl clusters
3. Section 01 • Saga Architecture, read end to end
4. Post-Mending, Silence and Hope, and Book 9's structure

Appendix: the extraction method for the ChatGPT exports, which the survey in part 1
superseded but which still governs that corpus.

---


===============================================================

# Where the Narrative Development Actually Lives

**Prepared:** 2026-09-19 · **Status:** survey and proposal, nothing ruled
**Supersedes** the reading order in `EXTRACTION_METHOD.md` §3.1, which over-weighted
the episode packets.

---

## 1. The correction

You said the episode packets don't hold close to all the narrative development. That is
right, and the survey shows the gap is not close.

| Source | Narrative development | Access |
| --- | --- | --- |
| Episode packets in the exports | ~4,500 words across 6 files | in repo |
| Non-packet exports | ~15,000 words across 14 files | in repo |
| **Notion** | **200+ pages across 8 numbered sections** | **live, connected now** |
| Unexported ChatGPT chats | unknown, includes E00–E15 | one-way, not yet retrieved |

The packets are a thin structured layer sitting on top of a much larger body of
development work, and almost all of that body is in Notion — not in ChatGPT, and not
lost.

---

## 2. What the non-packet exports do hold

Worth naming, because two of them are substantial:

- **`Trilogy Act-Level Beat Backup` parts 1–2, 2,645 words** — the act-level beat
  bible for **all 27 acts**, with act titles: "ACT I — THE CHILD IN THE SWAMP",
  "ACT III — THE BREAK, THE FLARE, THE MENDING". This is the narrative spine, and it is
  the highest-value narrative content in the entire export set.
- **`Rebuild Beat Bibles`, 2,106 words** — "MASTER BEAT BIBLE REBUILD".
- `Character Vault Chat` (1,579), `Story world development` (1,671),
  `_ Narrative Structure` parts 1–2 (2,611, including beat-level BIDs for E06).
- The rest — `Phase 1A Migration Plan`, `Saga Beat Expansion Pipeline`,
  `Concord Saga CSVs`, `Character involvement pacing` — is process and tooling.

So the export reading order should be: act-level beat bible first, beat bible rebuild
second, packets last.

---

## 3. The Notion inventory

Eight numbered sections under `Concord Saga (Root)`, plus four overview pages:

| Section | Contents |
| --- | --- |
| 00 • Creative Governance | Codex, archetype mandate, advisory groups |
| 01 • Saga Architecture | Master Summary, 27-Act Macro Structure, Resonance Escalation Curve, Civic Collapse Curve, Emotional Arc Spine, Symbolism & Motif Map, Character Arc Map, Theme Architecture, Supplement Architecture Map |
| 02 / 03 / 04 • Trilogies | per trilogy: overview, book overviews, **per-act Beats pages**, Supplement Map, Antagonist Map, Character Arc Summary, Resonance Behavior, Civic Condition, and a **Final Beat Bible per book** |
| 05 • Canon Bibles | **over 100 pages** — Resonance, Metaphysics & Ascension, Shards & Echo Nodes, Filaments, Tech & Comms, Environmental, Antagonist Architecture, Supplement Text Architecture, per-trilogy canon bibles, ~25 VFX/visual pages, ~35 romance/heat pages, ~20 city and environment pages |
| 06 • Post-Mending World Bible | the era with no envelope file in the repo |
| 07 • Master Saga Summary | including "SUPPLEMENT TEXT ARCS (CONDENSED)" |
| 08 • Character Bibles | 26 pages — 9 protagonist sheets marked Final Canon, 5 antagonists, 6 manufactured metas, 3 per-trilogy character lists |

**Silence and Hope are both there** — `08.10 • Silence - Metaphysical` and
`08.11 • Hope - Metaphysical`. Work-queue item 9b is a retrieval task, not a hole.

---

## 4. The real problem is not extraction — it is supersession

Notion is not truncated or hard to read. It is **versioned without a version record**,
and that is the thing to solve.

Visible in the listings without reading a single page:

- **Numbering collisions.** Two pages numbered `08.11` — Hope and Director Han Wei.
  Han Wei again at `08.14`. `05.45` twice. Trip has both a `NAME:` page and a
  `MICRO-BIBLE`.
- **Three pages titled `CONCORD SAGA — ENVIRONMENT DEEPENING`**, identical titles,
  different IDs.
- **Roughly 35 romance and heat pages** covering overlapping ground: `ROMANCE GRID v1`,
  `ROMANCE ENGINE v1`, `ROMANCE ENGINE GRID V2`, `ROMANCE SYSTEM BENTO v1`,
  `ROMANCE ENGINE — MASTER BENTO (v1)`, `ROMANCE PAYOFF GRID v2`, plus per-pairing heat
  ladders, pairing wheels, and grids `V2`.
- **Roughly 25 VFX and visual pages**, `05.15` through `05.44`, including
  `Unified VFX Canon`, `Hybrid VFX Canon`, `Hybrid VFX Canon Bento` and
  `Unified Visual Effects Canon` — four names for what may be one thing.
- A visible compression lineage — pages marked `Bento`, `Compressed`, `Lean Canon
  Edition`, `Ultra Compressed` — which means distillation has been attempted before and
  the outputs now sit beside their inputs with nothing saying which won.

This is exactly the pattern your D9 ruling anticipated: copy, then distil the copy.
Applied to Notion rather than the exports, it is the main body of work.

---

## 5. Proposed method

Not a pipeline. Four passes, each producing a record.

**Pass 1 — Inventory.** Every page: section, title, last-edited date, any version
marker in the title (`v1`, `v2`, `Bento`, `Compressed`, `Final Canon`). Titles and
dates only; no page bodies. Cheap, and it is the artifact nothing currently has.

**Pass 2 — Cluster.** Group pages covering the same subject. The romance cluster, the
VFX cluster, the environment cluster, the per-book beat clusters. The inventory makes
most clusters obvious from titles alone.

**Pass 3 — Pick the survivor, per cluster.** Criteria in order: an explicit `FINAL
CANON` or `Locked` marker; the compression lineage's endpoint (a Bento supersedes what
it compressed); latest edit date; and for genuine ties, read both. Record every
supersession — *this page supersedes those pages, on this evidence* — because that
record is what stops the sprawl regrowing.

**Pass 4 — Distil the survivors into the repo.** Tier D under §5.4, `RECOVERED PRIOR
CANON` until re-approved, with the supersession record travelling alongside so a later
reader can see what was set aside and why.

**Where the passes run.** Passes 1–2 are mechanical and belong here, where Notion is
connected. Pass 3 needs judgement and your ruling on ties. Pass 4 is a Claude Code
commit job.

---

## 6. Order by narrative value

1. **`01 • Saga Architecture`** — the Emotional Arc Spine, Character Arc Map, Theme
   Architecture and Symbolism & Motif Map are named in the section and have no
   equivalent anywhere in the repo. Small section, highest density.
2. **The nine per-book Final Beat Bibles** in sections 02–04, plus the per-act Beats
   pages. This is the narrative development proper, and the Book 9 one also carries the
   Mending beat that the B09.A3 era split needs.
3. **`08 • Character Bibles`** — 26 pages against 14 characters in the repo, and the
   repo has no metaphysicals, no antagonists as sheets, and no manufactured metas.
4. **`06 • Post-Mending World Bible`** — an entire era the repo does not model.
5. **`05 • Canon Bibles`**, cluster by cluster, heaviest sprawl last.

The exports' act-level beat bible (§2) should be read alongside item 2, as a
cross-check on the Notion versions rather than as a separate task.

---

## 7. What I would do next

Run Pass 1 now. It needs no rulings, produces the inventory the project has never had,
and will tell us how much of §4's apparent duplication is real. I can have it done in
this session.

---

## 8. For you to decide

1. Pass 1 now, or start with a single section end to end — `01 • Saga Architecture`
   would be my pick — to test the method on something small first?
2. Does the supersession record live in the repo, or in Notion beside the pages it
   describes? In the repo it is version-controlled; in Notion it is where the sprawl is
   visible.
3. Does distillation edit Notion at all, or only read it? Editing would let you archive
   superseded pages at the source; reading only keeps Notion as the untouched
   provenance layer, consistent with how the exports are treated.


===============================================================

# Notion Inventory — Pass 1

**Compiled:** 2026-09-19 · Titles and structure only; no page bodies read.
**Scope:** `The Calder Creative Universe / 2. Story Worlds / Concord Saga (Root)`

**Method note.** Notion's page listings give titles and IDs but not per-page edit
dates. Dates require fetching each page individually — roughly 200 calls — so this pass
records section, title and URL. Version markers are read from titles, which is enough
to cluster. A dated pass can follow if supersession ties need it.

---

## Root

| Page | URL id |
| --- | --- |
| THE CONCORD SAGA — OVERVIEW | `2b4e7d902ad880fa8af0e7908ad063e6` |
| VEIL TRILOGY — OVERVIEW | `2b4e7d902ad88095b757ee048cc7d8dc` |
| NEON TRILOGY — OVERVIEW | `2b4e7d902ad880c69074c9f3d430ab3d` |
| LOOM TRILOGY — OVERVIEW | `2b4e7d902ad880ce9adbc2037460f2fd` |
| Resonance Mastery Mechanics | `2b6e7d902ad8800783b3c09f7095098f` |
| 25.12.06 Memory List | `2c1e7d902ad8805485e8c22a084bc21b` |

Outside the root, at `2. Story Worlds`: `Concord Saga - Universe Bible`
(`2b0e7d902ad8806d8b79f5d3c304a192`) and `Concord Saga 25-1212 Export`
(`2c8e7d902ad880f78f98d4b9c1df2c2b`), which contains `Memory Set 25-1212`.

---

## 00 • Creative Governance — 10 pages

| # | Title |
| --- | --- |
| 00.01 | Editorial & Publication Codex (v2.1) — *recovered* |
| 00.02 | Jazz Framework (Story Architecture) |
| 00.03 | Möbius Audit System |
| 00.04 | Advisory Groups (Core + Provisional) |
| 00.05 | Reader Archetype Mandate — *recovered* |
| 00.06 | Calder OS (Author Voice Manual — Lite) |
| 00.07 | Pantheon (Tone & Emotional Calibration) |
| 00.08 | Creative Governance Ruleset |
| 00.09 | Production Pipeline (Notion → NC → Sudowrite) |
| 00.10 | Decision Protocols (Boards, Debates, Locks) |

**Not yet recovered and directly relevant:** `00.02` Jazz Framework is cited
repeatedly in the ChatGPT exports as the core story architecture. `00.03` Möbius Audit
System and `00.10` Decision Protocols bear on how rulings are made and locked.

---

## 01 • Saga Architecture — 10 pages

| # | Title | Status |
| --- | --- | --- |
| 01.01 | Concord Saga Master Summary | |
| 01.02 | Trilogy Architecture | |
| 01.03 | 27-Act Macro Structure | *recovered* |
| 01.04 | Resonance Escalation Curve | *recovered* |
| 01.05 | Civic & Institutional Collapse Curve | |
| 01.06 | Emotional Arc Spine | **no repo equivalent** |
| 01.07 | Symbolism & Motif Map | |
| 01.08 | Supplement Architecture Map | |
| 01.09 | Character Arc Map | **no repo equivalent** |
| 01.10 | Theme Architecture | **no repo equivalent** |

Ten pages, the densest narrative-architecture section in the workspace, and the
highest-value unrecovered material.

---

## 02 • Trilogy: VEIL (T1) — 27 pages

`T1.01` Trilogy Overview · `T1.02` Book 1 Overview · `T1.03/04/05` Book 1 Act I / II /
III Beats · `T1.06` Supplement Map · `T1.07` Antagonist Map · `T1.08` Character Arc
Summary · `T1.09` Resonance Behavior · `T1.10` Civic Condition

**Book 1 - VEIL I** (7): Final Beat Bible · Book 1 Prologue — "Conversation in the
Stars" · ACT I / II / III SUMMARY · Character List · Unified Character List
**Book 2 - VEIL II** (3): Final Beat Bible · Character List · Unified Character List
**Book 3 - VEIL III** (4): Final Beat Bible · Book 3 Epilogue — "The First Quiet" ·
Character List · Unified Character List

---

## 03 • Trilogy: NEON (T2) — 24 pages

`T2.00` Root Overview · `T2.01` Trilogy Overview · `T2.02` Book 4 Overview ·
`T2.03/04/05` Book 4 Act I / II / III Beats · `T2.06`–`T2.10` Supplement Map,
Antagonist Map, Character Arc Summary, Resonance Behavior, Civic Condition

**Book 4 - NEON I** (3) · **Book 5 - NEON II** (3) · **Book 6 - NEON III** (4,
including Book 6 Epilogue — "The Black Parade") — each with a Final Beat Bible and two
character lists

---

## 04 • Trilogy: LOOM (T3) — 24 pages

`T3.00`–`T3.10`, same shape as Neon, with Book 7 Act I / II / III Beats

**Book 7 - LOOM I** (3) · **Book 8 - LOOM II** (3) · **Book 9 - LOOM III** (4,
including Book 9 Epilogue — "Luminous Thread")

---

## 05 • Canon Bibles — ~140 pages, the sprawl

Numbered `05.01`–`05.48` plus ~90 unnumbered pages. Clustered:

| Cluster | Approx. | Notes |
| --- | --- | --- |
| **Core system bibles** `05.01`–`05.08` | 8 | Resonance Mechanics · Metaphysics & Ascension · Shards & Echo Nodes · Filaments & Civic Evolution · Tech & Comms · Environmental · Antagonist Architecture · Supplement Text Architecture (*recovered*) |
| **Per-trilogy canon** `05.09`–`05.14` | 6 | Veil / Neon / Loom canon bibles + three environment canons |
| **Visual & VFX** `05.15`–`05.44` | ~25 | **heaviest sprawl.** Includes `Unified VFX Canon`, `Hybrid VFX Canon`, `Hybrid VFX Canon Bento`, `Unified Visual Effects Canon` — four titles that may describe one thing |
| **Romance & heat** unnumbered | ~35 | `ROMANCE GRID v1` · `ROMANCE ENGINE v1` · `ROMANCE ENGINE GRID V2` · `ROMANCE SYSTEM BENTO v1` · `ROMANCE ENGINE — MASTER BENTO (v1)` · `ROMANCE PAYOFF GRID v2` · per-pairing heat ladders · four pairing wheels · `RESONANCE × ROMANCE PROGRESSION WHEEL v1` |
| **City & environment** unnumbered | ~20 | NOLA, Vienna, Singapore, Reykjavík, Marrakesh — most in both "Deep-Pass v1" and "Deep-Vibe" versions |
| **Compression layer** unnumbered | ~15 | pages marked Bento, Compressed, Lean Canon, Ultra Compressed |
| **Tech** | ~5 | `05.05`, `05.46` Tech Bible v2, `05.47` Tech Canon Bento, `Tech & Comms Bible — v2 (Lean Canon Edition)`, `CONCORD SAGA — TECH BIBLE (COMPRESSED CORE CANON)` |

**Confirmed duplicates in this section:** `05.45 • Character Engine - Saga Reference`
appears twice; three pages share the exact title
`CONCORD SAGA — ENVIRONMENT DEEPENING`.

---

## 06 • Post-Mending World Bible — 1 page

A single child, `06 • Post-Mending World Bible`. The era the repository does not model
at all, and the source for the envelope file held open in the decisions document.

---

## 07 • Master Saga Summary — 1 page, read

Fourteen sections covering the saga in one sentence, the 3×3 structure, the emotional
arc (Curiosity → Fear → Grief → Catharsis → Healing → Renewal), five themes, the
metaphysical arc in five phases, political, shard, tech and Filament arcs, per-character
arc summaries, and condensed supplement arcs.

---

## 08 • Character Bibles — 26 pages

`08.01`–`08.09` protagonist sheets, all marked *Updated, Final Canon*: Seraphine Vael ·
Lucien Kael · Caro Gauthier · Elisabet Arnardóttir · Tahl Morgan · Kade Rios · Rex Tan ·
Baz Foix · The Lacuna

`08.10` **Silence - Metaphysical** · `08.11` **Hope - Metaphysical** — both absent from
the repository

Antagonists: `08.11` Director Han Wei *(number collision with Hope)* · `08.12`
Marcellus Virelli · `08.13` Saeko Morita · `08.14` Director Han Wei *(duplicate of
08.11)*

Manufactured Metas `08.15`–`08.20`: Silver Pattern Man · Blinking Girl · Null · Unnamed
Chord · Cohort · Cohort 2

`08.21`–`08.23` per-trilogy character lists. Plus two Trip pages: `NAME: "Trip"` and
`TRIP — CHARACTER MICRO-BIBLE`.

---

## What Pass 1 establishes

**Roughly 240 pages**, against 192 files in the repository — and almost no overlap.

**Six clusters need supersession rulings** before distillation: VFX/visual, romance/
heat, city/environment, tech, the compression layer, and the Han Wei / Trip / Character
Engine / Environment Deepening duplicates.

**Three sections have no repo equivalent at all:** `01`'s Emotional Arc Spine, Character
Arc Map and Theme Architecture; `06` Post-Mending; and the metaphysical and manufactured-
meta character sheets in `08`.

---

## One finding that touches a ruling

**The Prologue has a third title.** Notion's Book 1 container holds
`Book 1 Prologue — "Conversation in the Stars"`.

| Source | Title |
| --- | --- |
| Veil Master Beat Bible (export) | Prologue — Silence & Hope |
| Checkpoint + recovery ledger | The Conversation in the Sky |
| **Notion, Book 1 container** | **Conversation in the Stars** |

Decision D7 ruled *The Conversation in the Sky*. Sky against Stars is one word, and the
ruling stands unless you say otherwise — but it was made without this third reading in
view, and the Notion page is the one sitting in the book's own folder.

---

## Suggested next step

`01 • Saga Architecture`, all ten pages, read end to end. It is the smallest section
with the highest concentration of unrecovered narrative architecture, and three of its
pages have no counterpart anywhere in the repository.


===============================================================

# Notion Section 01 — Saga Architecture, Recovered

**Read:** 2026-09-19, all ten pages · Tier D, `RECOVERED PRIOR CANON` until re-approved
**Sources:** `01.01`–`01.10` under `Concord Saga (Root) / - 01 • Saga Architecture`

---

## 1. The architecture

### 01.01 Master Summary (v1 Final Canon)

Nine books, three trilogies. Core theme `Resonance = Emotion × Intent × Will`. Endgame:
the hard-cap Veil collapses, a Breathable Veil forms, guided by empathy.

**Protagonists and end states:** Seraphine Vael, empathic Cajun resonance-filter →
**Luminous Thread**. Lucien Kael, structured Dominion scion → **Shadow Anchor**. Caro
Gauthier, balanced modulator → **Hope Reborn**. Elisabet Arnardóttir, emotional clarity
and human lantern. Rex Tan, skeptic technologist → post-Mending civic architect. The
Lacuna, resonant musician binding emotional communities. Tahl Morgan, chronicler, dies
in Neon, Echo guides the Loom intervention. Kade Rios, grief-charged accidental leader,
steward of MT → LT.

**Antagonists:** Dominion (Marcellus Virelli), purity and lineage control · Technarch
Directorate (Han Wei), rationalist authoritarianism · Saeko Morita, populist
anti-resonance movement · Manufactured Metas, human-made intentless constructs · Neon
Splinters and Panic Cells.

**Channel definitions, verbatim:** VT (VeilThread) private metaphysical channel
(Silence / Hope / Tahl) · **MT (Missing Thread) public mortal channel founded by Tahl**
· LT (Luminous Thread) post-Mending resonance-stable network.

**Concrete plot facts:** Baz dies in Book 3. Tahl dies saving civilians, Echo preserved.
Silence and Hope break; finale in Honey Island Swamp.

### 01.02 Trilogy Architecture

Per trilogy: tone, resonance state, civic condition, emotional arc.

| | Veil | Neon | Loom |
| --- | --- | --- | --- |
| Tone | nearly-modern, subtle, rising dread | explosive, polarized, chaotic, resopunk | dark, desperate, intimate, mythic |
| Resonance | flickers → ghostwaves → fractures; **VT sealed until Tahl brushes it** | blooms → storms → ruptures; manufactured metas; VT destabilizing | global saturation; resonance-overload weather; **VT becomes Echo-only**; tech collapse |
| Civic | stable but brittle; institutions overconfident | fragmentation, rebellion, crackdowns | diaspora, shattered infrastructure |
| Emotional | curiosity → fear → grief | fear → rage → disillusionment | grief → resolve → transcendence |

Convergence: "Veil = cracks begin · Neon = world fractures · Loom = world breaks, then
breathes."

### 01.05 Civic & Institutional Collapse Curve

Veil — governments confident, Technarch and Dominion secrecy, early Filaments offer
grassroots care. Neon — civic fracture, anti-resonance populism, Technarch overreach,
Dominion ideological crackdown, **MT becomes an information force**. Loom —
infrastructure collapse, diaspora, Filaments become civic lifelines, **Kade's MT becomes
global lighthouse via Tahl echo upgrade**. Post-Mending — emotional literacy becomes a
civic requirement, Filaments become teachers.

### 01.06 Emotional Arc Spine

Veil: Curiosity → Unease → Fear → Loss *(Tahl is the emotional entry point)*
Neon: Fear → Rage → Division → Despair *(Kade is the emotional amplifier)*
Loom: Grief → Resolve → Sacrifice → Rebirth *(Seraphine, Lucien, Caro are the centre)*
**Post-Mending: Integration → Hope → Awakening**

### 01.07 Symbolism & Motif Map

**Triangle** — identity trios, emotional triads, Filament knots, metaphysical tri-weave
at the endgame. **Light** — Veil flicker, Neon fracture, Loom prismatic →
white/black/iridescent. **Sound** — resonance hum, shard hum, harmonic storms, **the
Lacuna's trumpet**, Echo signatures. **Breath** — Veil failure, Breathable Veil,
emotional modulation. **Water** — New Orleans, the swamp, Atchafalaya, rebirth.
**Text as Life** — MT, Chronicle, VT, Vein, Field Notes; words as connective force.

### 01.08 Supplement Architecture Map

Presence by era: Veil low · Neon heavy · Loom critical.

| Vehicle | Veil | Neon | Loom | Post-Mending |
| --- | --- | --- | --- | --- |
| MT | small, personal | exploding influence | global survival thread | **Luminous Thread** |
| Chronicle | light | institutional narrative | dead | archived |
| Vein | cultural slices | **closed** | **brief return** | culture restoration |
| VT | private, unseen | frayed | echo-only | metaphysical-private |
| Field Notes | early resonance hints | shard mapping | resonance survival data | — |

### 01.09 Character Arc Map

Seraphine: Awakening → Empathy burden → Leadership → Ascension (white light)
Lucien: Control → Fear → Acceptance → Ascension (prismatic black)
Caro: Self-doubt → Emotional literacy → Modulation → Ascension (iridescent gray)
Kade: Parasocial orphan → grief fire → rebellion → protector → MT torchbearer
Tahl: Curiosity → compassion → death → Echo → stabilizer of MT/VT
Elisabet: Isolation → connection → love → protector → post-Mending guide
Rex: Duty → trauma → sacrificial loyalty → survivor → civic rebuilder
Baz: Hope → fieldwork → innocence → tragic loss → Lucien's emotional anchor

### 01.10 Theme Architecture

Core: empathy · identity · community · connection under strain · resilience ·
integration. Veil: discovery, fear rising, emotional fracture, hidden systems,
trust/distrust. Neon: polarization, public panic, institutional failure, grief → rage
conversion, charisma as danger. Loom: collapse, hope under darkness, sacrifice,
ascension, rebuilding.

---

## 2. What this settles

**The `VT: sealed until Tahl breach` citation.** `01.02` says "VT: sealed until Tahl
brushes it". The claim Claude Code flagged as unsourced is sourced — in Trilogy
Architecture, not only in the Escalation Curve. Ruling question 3 on `VT` era gating can
now be answered from canon.

**A Post-Mending emotional arc exists** — Integration → Hope → Awakening — so the era
has architecture, not just mechanics. It strengthens the case for the era file held open.

**Loom's envelope floor.** "Global saturation", "resonance-overload weather", "tech
collapse", "VT becomes Echo-only" independently support the raised Loom floors in the
banded values.

---

## 3. Conflicts found

### 3.1 `MT becomes LT` breaks the channel separation law — **most serious**

`01.08` gives Post-Mending MT as "Luminous Thread". `07 • Master Saga Summary` Phase 5
says "**MT becomes LT**". `01.01` calls Kade "steward of MT → LT".

`rules/Channels/CHANNELS_OVERVIEW.md` §2, Authoritative Canon, states the core law:

> MT ≠ VT ≠ LT. Channels never merge. **Channels never convert into each other.**

Either MT converting into LT is the one sanctioned exception to the law, or "MT becomes
LT" is shorthand for Kade's stewardship passing from one channel to the other while both
persist. The two readings give different endings. **Needs a ruling.**

### 3.2 Vein's era presence is inverted between two canon sources

| | Neon | Loom |
| --- | --- | --- |
| `01.08` Supplement Architecture Map | **closed** | brief return |
| `05.08` Supplement Text Architecture Bible | "occasional emotional breaks" | "closed", reopening is symbolic |

Directly contradictory, and it matters for supplement scheduling. `05.08` is the more
detailed document; `01.08` is the architecture-level one.

### 3.3 Lucien's end state has two names

`01.01` Master Summary: **Shadow Anchor**. `07` Master Saga Summary: **Silence Reborn**.
`01.09`: "Ascension (prismatic black)".

Caro is "Hope Reborn" in both, and Silence and Hope are the two metaphysicals who
dissolve — so "Silence Reborn / Hope Reborn" is a matched pair and "Shadow Anchor" is the
odd one out. Same character, and possibly both true at different points.

### 3.4 Three versions of the trilogy emotional arcs

| | Veil | Neon | Loom |
| --- | --- | --- | --- |
| `01.02` | curiosity → fear → grief | fear → rage → disillusionment | grief → resolve → transcendence |
| `01.06` | Curiosity → Unease → Fear → Loss | Fear → Rage → Division → Despair | Grief → Resolve → Sacrifice → Rebirth |
| `07` (saga-level) | Curiosity → Fear → Grief → Catharsis → Healing → Renewal | | |

`01.06` is the dedicated page and the most granular. The others read as compressions of
it, but the endpoints differ — "grief" against "Loss", "disillusionment" against
"Despair", "transcendence" against "Rebirth" — so it is drift, not just granularity.

---

## 4. Where this goes in the repo

| Content | Suggested destination |
| --- | --- |
| Emotional Arc Spine, Theme Architecture, Character Arc Map | `canon/` — no equivalent exists |
| Trilogy Architecture tone and civic rows | `rules/trilogy_context_T*.json`, whose `tone_envelope` is a single line today |
| Civic & Institutional Collapse Curve | `canon/` |
| Symbolism & Motif Map | `rules/symbols/`, alongside the existing motif files |
| Supplement Architecture Map | merge with the §3.2 conflict resolved, not before |
| Master Summary protagonist and antagonist rosters | `canon/characters/` — five of these people have no ID card |

---

## 5. For you to rule

1. **§3.1 — does MT convert into LT, or do both persist?** This is the ending.
2. **§3.2 — Vein in Neon and Loom**: which source wins?
3. **§3.3 — Lucien**: Shadow Anchor, Silence Reborn, or both at different points?
4. **§3.4 — which emotional arc is canon?** `01.06` is my read, as the dedicated page.
5. Does `VT` era gating now follow `01.02` — sealed until Tahl brushes it, then
   available thereafter, Echo-only in Loom?


===============================================================

# Notion Recovery — Post-Mending, Silence & Hope, and Book 9

**Read:** 2026-09-19 · Tier D, `RECOVERED PRIOR CANON` until re-approved
**Pages:** `06 • Post-Mending World Bible` · `08.10 Silence — Metaphysical` ·
`08.11 Hope — Metaphysical` · `BOOK 9 — LOOM III (Final Beat Bible)`

Chosen because each one bears on a decision currently held open.

---

## 1. Book 9 has four acts

`BOOK 9 — LOOM III (Final Beat Bible)`:

- **ACT I — "The World at the Edge"** · E1–E5 · tremor → awe → despair → revelation
- **ACT II — "The Last Unraveling"** · E6–E10 · pressure → pursuit → mythic escalation
- **ACT III — "The Loom"** · E11–E15 · mythic → transcendent → devastating → beautiful
- **ACT IV — "Afterlight"** · E16–E21 · quiet → aching → hopeful

This breaks two things at once.

**The SID format allows `A{1-3}`.** `S1.T3.B09.A4.E16` is not expressible.

**The 27-Act Macro Structure says nine books times three acts**, and gives Book 9 as
A1 cataclysm, A2 ascension, A3 Breathable Veil, plus an epilogue. The Final Beat Bible
does not match that at any act. Its A1 is the collapse, A2 the convergence of
antagonists, A3 the Mending itself, A4 the resolution.

So either the saga is a 28-act structure, or Act IV is the epilogue written as an act.
Either way `A{1-3}` and the "27 acts" framing both need amending. **This is the largest
structural finding since the branch discovery**, and it lands squarely on the SID
schema.

Episode numbering runs E1–E21 continuously across all four acts, which confirms the
continuous-across-book convention independently.

---

## 2. The Mending has a location: `B09.A3.E14`

> **E14 — The Mending (Breathable Veil Formation).** *This is the cosmological core of
> the saga.* Seraphine opens herself, prismatic resonance flowing. Lucien shapes
> structure around her. Caro modulates the emotional burden. Elisabet grounds all three.
> Kade holds humanity steady through MT. Silence dissolves into Lucien. Hope dissolves
> into Caro. **Filtration, not suppression. Empathy as filter. Intent as guide.**

E15, "The Lightfall", is the global reformation — the Veil reforms, resonance storms
vanish, the world breathes.

**This resolves the B09.A3 era split**, and more cleanly than my proposal. The boundary
is E14/E15, and **Act IV is wholly post-Mending** — so the split falls at an act
boundary after all, provided Act IV is recognised as an act. Under the current
three-act schema it does not, which is another reason §1 needs settling first.

---

## 3. `MT becomes LT` is a rename, not a conversion

The conflict I flagged as touching the channel separation law dissolves on the evidence.

`06 • Post-Mending World Bible` §7.3: "It's the last MT transmission before **Kade
formally renames the channel LT — Luminous Thread**, marking a new era." §9.2 lists
"**LT (renamed MT)** pulses". Book 9 E20: "Kade posts the first LT message: *'We made
it. And we're not done.'* MT becomes LT — The Luminous Thread."

A renaming is a naming act, not a metaphysical conversion, so `MT ≠ VT ≠ LT` holds and
"channels never convert into each other" is not breached.

**But it exposes a different problem: `LT` now has three referents.**

| Referent | Source |
| --- | --- |
| Seraphine's ascended identity — *she becomes the Luminous Thread* | `SeraphineIdentity.md`, `06 §6.1` |
| A resonance state — "Post-Mending prismatic filtration · Ascendant-only perception" | `Mechanica-v4.md` §33 |
| Kade's renamed MT network — a mortal comms backbone | `06 §7.3`, `§9.2`, Book 9 E20 |

The third is a rebuilt longwave network maintained by "engineers trained by Rex" (§5.4).
The second is Ascendant-only perception. Those cannot be the same thing, and the
existing `token_collision_note` does not cover it. **Needs a ruling** — and it is the
same shape as the `MT` question already open.

---

## 4. Silence and Hope, recovered

**Silence** — metaphysical construct, the **structural** half of the Old Veil, built to
suppress resonance flux and maintain boundary containment. Emotionless by design, grown
brittle and paradox-bound over centuries. Rigid, analytical, "deeply lonely without
knowing it." Fascinated by Tahl's disciplined emotional patterns. Shelters Tahl's Echo
after his death. In Loom, realises the Old Veil cannot be salvaged, **chooses
dissolution — his first act of agency** — and transfers his structural essence into
Lucien. Final act: "a conscious choice to be kind."

**Hope** — the **emotional** half, built to absorb resonance overflow and modulate
emotional storms. Warm but porous, constantly overstimulated by humanity. First to
sense Veil failure. Her first metaphysical "cry" comes during the Black Parade — which
is Book 6's epilogue title. Breaks openly during Tahl's death ritual, binds to his Echo,
chooses dissolution at the Mending. Dissolves into Caro as **Hope Reborn**.

**Tahl is the catalyst for both.** He gives Silence his first emotional fracture and
Hope her first flicker of agency. Both shelter his Echo. That makes Tahl structurally
central in a way the repo's character files do not record at all.

**This also settles the Lucien conflict.** `08.10` gives "SUCCESSOR: Lucien (Silence
Successor)"; `06 §6.2` gives "Lucien — Silence Reborn". Two sources against `01.01`'s
"Shadow Anchor". Silence Reborn / Hope Reborn is the matched pair; Shadow Anchor is the
outlier.

---

## 5. The Post-Mending envelope now has a source

`06 • Post-Mending World Bible` is ten sections on the world one to two years after
Book 9. What bears on the held envelope file:

- **No more Shards.** Echo Nodes replace fractures. Resonance fluctuations become
  "breaths, not storms" — which supports the `W0`–`W1` weather band directly.
- **The Breathable Veil filters rather than blocks**, adapts to emotion, self-regulates
  through empathy, and is maintained by the trio.
- **VT persists** — Tahl's Echo is "stable, gentle, harmonic, never intrusive" in VT.
  Confirms permitting `VT` in the era.
- **Echo Nodes** are "never dangerous", with soft prismatic glow and calm emotional
  effect, at old shard sites and diaspora convergence zones. Honey Island Swamp is the
  largest.
- The trio are "not gods, not rulers" — **"the *weather system* of resonance."**

Beyond the envelope, the page carries an entire post-collapse civilisation: what
technology survives (electricity, analog, printed media) and what is gone (high-speed
internet, AR overlays, holographic systems); diaspora integration with named hybrid
rituals — Cajun–Icelandic grounding feasts, Filament–Japanese "quiet lantern nights";
five named civic festivals; and a grounding vernacular people actually speak — *"What
colour does that feel like?"*, *"Is your breath steady?"*

**It also settles the Vein conflict for one era at least:** §8.1 "The Vein Reopens" as
cultural beacon and intercity resonance hub, which matches `05.08` against `01.08`.

---

## 6. What this unblocks

| Held item | Status now |
| --- | --- |
| B09.A3 era split | **Resolved** — E14/E15, with Act IV wholly post-Mending (§2) |
| Post-Mending envelope contents | **Sourced** (§5) — `SHARD`/`RUPTURE` forbidden, `VT` and `LT` permitted |
| Work-queue 9b, Silence and Hope | **Recovered** (§4), ready to migrate |
| `MT becomes LT` vs the separation law | **Resolved** as a rename (§3) |
| Lucien: Shadow Anchor or Silence Reborn | **Resolved** on weight (§4) |
| Vein in Post-Mending | **Resolved** — reopens (§5) |

---

## 7. For you to rule

1. **Does Book 9 have four acts?** If yes, the SID pattern widens to `A{1-4}` and the
   27-Act Macro Structure becomes 28. If Act IV is the epilogue, it needs an identifier
   that is not an act. Everything about Book 9's migration waits on this.
2. **Which Book 9 act structure is canon** — the Macro Structure's cataclysm /
   ascension / Breathable Veil, or the Final Beat Bible's four acts? They do not align
   at any act, so this is not a naming difference.
3. **`LT`'s three referents** (§3) — the ascended identity, the resonance state, the
   renamed network. Same disambiguation question as `MT`, and probably one ruling.
4. Confirm **Silence Reborn** over Shadow Anchor for Lucien, and I will note `01.01` as
   superseded rather than contradictory.


===============================================================

# Extracting Useable Information from the Exports — Proposal

**Prepared:** 2026-09-19 · **Status:** proposal, nothing ruled

---

## 1. The finding that changes the approach

I measured the corpus before designing anything for it.

| | |
| --- | --- |
| Exports with content | 20 of 21 |
| Total words | **25,952** |
| Total lines | 4,885 |
| Approximate tokens | **~35,000** |
| Lines carrying an ECID field | 330 (7%) |
| Lines carrying a SID | 30 |
| Cross-file duplication | **0%** — no two exports repeat each other |

**The whole archive is about 35,000 tokens.** That is smaller than several of the
documents this project has produced about it. It fits in a single context window with
most of the window left over.

So the answer to "what is the most effective extraction method" is uncomfortable:
**stop building extraction machinery and read it.** A pipeline, a classifier, a
chunking strategy, an embedding index — all of it costs more to build and verify than
the reading costs. Zero duplication means there are no savings from deduplication
either; every file is distinct content.

**But the corpus is small because it is incomplete**, and that is where the real
question lies. See §5.

---

## 2. What "useable" has to mean here

The failure mode to design against is not missing something. It is **producing
confident paraphrase of irreplaceable material**. The ChatGPT Business workspace has no
export path and the share links are closed — these files are the only copy, and a
summary that drops a distinction cannot be checked against anything.

So every extracted item must carry an anchor back to its source text. Not "the beat
bible says Act I ends at E16" but a record that names the file, quotes enough to find
the line again, and says which turn it came from.

That single rule decides most of the method.

---

## 3. Proposed method — one pass, three outputs, full coverage

### 3.1 Read in density order

The ECID-bearing lines are concentrated, not spread:

| ECID lines | Words | Export |
| --- | --- | --- |
| 198 | 2,058 | `Saga structural archive__part01` |
| 44 | 1,294 | `Episode expansion process__part02` |
| 44 | 418 | `Saga structural archive__part02` |
| 23 | 2,121 | `Episode expansion process__part01` |
| 9 | 1,233 | `_ Narrative Structure _(1)__part02` |
| 8 | 1,671 | `Story world development` |
| 0 | — | the remaining 14 files |

Six files hold every episode packet in the archive. The other fourteen — roughly
15,000 words — hold beat bibles, decisions, and process. Both need reading; only the
first six produce records the validator can check.

### 3.2 Three outputs, and every line lands in exactly one

- **Canon record** — a packet, a beat, a vocabulary definition, an act function.
  Goes to a JSONL extract with `{source_file, turn_role, anchor, sid?, kind, content}`.
  Feeds migration and the validator.
- **Decision record** — a ruling, a constraint, a prohibition, a resolved question.
  Goes to the decisions ledger with the same anchor fields, tiered per §5.1.
- **Discard** — process chatter, tooling talk, prompts, "shall I continue?".
  **Counted, not deleted.** A line discarded is a line accounted for.

### 3.3 Coverage is the completion test

The project currently has no definition of "this conversation is done." Three outputs
that partition every line give one: an export is complete when
`canon + decision + discard = total lines`, and the report states the three counts.

That also makes a second pass cheap — you re-read the discard pile, not the whole file.

### 3.4 What stays deterministic

Only the parts that are already schema-shaped: ECID field runs, SID headers, act
lists. Those extract with the same regexes this session has been using ad hoc, and the
output is checkable against `canon_rules.json` without judgement. Formalizing those
scripts into the repo's `tools/` is worth doing — not because the corpus needs
automation, but because the extraction becomes reproducible and the next corpus (§5) is
bigger.

Everything else — the 14 files with no ECID lines, where the decisions live — is
reading. There is no parser for "Tahl launches the early version of Missing Thread."

---

## 4. What not to do

**Do not summarize wholesale.** A 35k-token corpus summarized to 5k tokens is a 30k
token loss of one-way-storage material, and nobody can tell what went.

**Do not build a retrieval index.** Semantic search over 4,885 lines answers questions
a grep already answers, and adds a layer that can silently fail to retrieve.

**Do not trust turn roles as authorship.** Verified earlier this session: large
archival blocks pasted back into a conversation appear as author turns. Eleven of the
`STRAIN` field values sit inside one such block. Turn role records where text entered
the record, not who wrote it — which is why tier assignment stays a human judgement.

---

## 5. The corpus that actually matters is still in ChatGPT

The 26,000 words are what survived a lossy save. The handoff puts the
`Episode expansion process` conversation at **80% missing**, and the E00–E15 packets —
the largest single block of unrecovered canon — are in `Archive Veil Book 1` and
`Hold until release`, neither exported.

So the extraction question splits in two, and the second half is the one worth
engineering:

**Getting complete conversations out.** `chatgpt_workspace_export.js` in list mode
first, producing the full workspace inventory that §3.3 of the handoff says is still
missing. Then export in priority order against that inventory.

**Knowing an export is complete.** This is the step whose absence lost E01–E15. The
list-mode pass records each conversation's identity and metadata; an export can then be
checked against it rather than eyeballed. Two cheap tests:

- the export's first turn is the conversation's first turn, not a scroll position
- the turn count matches what list mode recorded

A completeness check is worth more than any parsing improvement. Parsing a truncated
file perfectly still yields a truncated result.

---

## 6. What I would do, in order

1. Run the console script in **list mode**. It is item 4 in the work queue, blocked on
   nothing, and everything else here depends on the inventory it produces.
2. Read the six ECID-dense exports and extract canon records with anchors. ~7,500
   words.
3. Read the remaining fourteen for decisions. ~15,000 words.
4. Publish the coverage report — three counts per export.
5. Export the unabridged conversations in priority order, with the completeness check
   from §5, starting with `Archive Veil Book 1`.
6. Re-run steps 2–4 against the new material, which is where the method earns its
   keep — that corpus will not fit in one window.

Steps 2 and 3 are roughly a session's work and need no tooling that does not already
exist.

---

## 7. For you to decide

1. Do steps 2 and 3 run here, in Cowork, or in Claude Code? Here is better for reading
   and judgement; there is better for committing the extract and running the validator
   against it. A split — read here, hand the JSONL over — costs one handoff.
2. Does the discard pile get kept? Keeping it makes coverage auditable and costs a file;
   dropping it makes the second pass a re-read.
3. Priority for step 5 beyond `Archive Veil Book 1` — the handoff's Tier 1 list is a
   year old and three of its entries have since been recovered.

