# Concord Saga — Consolidated Canon Decisions

**Ruled by:** James · **Date:** 2026-09-18 · **Recorded by:** Claude (Cowork)

**This document supersedes and replaces** the four working documents from this
session: `CANON_DECISIONS_2026-09-18.md`, `SUPPLEMENT_TYPES.md`,
`AUDIENCE_AND_PAYOFF_MODEL.md` and `NOTION_RECOVERY_SUPPLEMENTS_AND_ARCHETYPES.md`.
Nothing from them is lost; everything still standing is restated here.

**Authority:** §1–§6 are author rulings and are binding. §7 is provisional and marked
as such. §8 is open and must not be decided by Claude. Suggested repository home:
`recovery/CANON_DECISIONS_2026-09-18.md`.

---

## 1. Resonance state, and the new `LOAD` axis

### 1.1 `STRAIN` is not a resonance state

Mechanica governs. `rules/Mechanica-v4.md` postdates the tier-1 appearance cards
(2026-01-10 against 2025-12-14), and its §33 list stands:
`CALM · BLOOM · SHARD · RUPTURE · NODE · VT · LT`.

Strain remains canon as a *signal*: Mechanica §51 (`Yellow: strain / overload`),
`rules/symbols/COLOR_SEMANTICS.md` (`YELLOW — Strain / Overload`, "risk: shard
precursors"), `rules/resonance/resonance_expression_rules.md`. It is not a member of
the state enumeration.

Provisional in one way only: the line-by-line memory chat review may revise
Mechanica, at which point this reopens.

### 1.2 `EDGE` and `BRUSH` are not states

`SHARD-EDGE` is an oversimplification and is not an endorsed form. `VT-BRUSH` refers
to the VeilThread channel; the operative token is `VT`. Qualifier forms are not
adopted — the nuance moves to `Notes`.

### 1.3 ECID fields hold a single value

A field's value is inherently a transition from the previous ECID, so arrow forms are
redundant with the sequence. Store one value per field: the state the episode ends
in. Movement is recoverable by reading the previous episode.

### 1.4 Add a `LOAD` axis to the ECID

`HEAT` is the romance ladder (`romance_system.heat_ladder`: H0 spark → H4 white_hot).
`FX` and `WEATHER` are environmental. `MODE` is register. Nothing carried emotional
load, which is why `STRAIN` was invented as a pseudo-state during drafting.

| Value | Meaning |
| --- | --- |
| `L0` | unloaded |
| `L1` | carrying, sustainable |
| `L2` | strained; visible cost; the yellow/overload condition of Mechanica §51 |
| `L3` | shard precursor; the next step is fracture |

### 1.5 Migration mapping for all 25 recovered resonance values

| Recovered value | Count | `RES` | `LOAD` |
| --- | --- | --- | --- |
| `CALM → STRAIN` | 7 | `CALM` | `L2` |
| `STRAIN` | 6 | `CALM` | `L2` |
| `CALM` | 3 | `CALM` | `L0` |
| `STRAIN → CALM` | 2 | `CALM` | `L1` |
| `SHARD` | 2 | `SHARD` | `L2` |
| `STRAIN → SHARD` | 1 | `SHARD` | `L3` |
| `STRAIN → BLOOM → SHARD-EDGE settling` | 1 | `SHARD` | `L2` |
| `SHARD → RUPTURE` | 1 | `RUPTURE` | `L3` |
| `RUPTURE` | 1 | `RUPTURE` | `L3` |
| `RUPTURE → VT-BRUSH` | 1 | `VT` | `L3` |

Preserve the original string in `Notes` on every packet. The mapping must stay
auditable and reversible.

---

## 2. Identifiers and numbering

### 2.1 SIDs

Format `S1.T{1-3}.B{00-09}.A{1-3}.E{00-99}` — **two-digit book numbers**, and the
episode range widens to admit `E00`. Episodes run **continuously across a book**, not
restarting per act.

### 2.2 The Prologue is `E00`, titled `The Conversation in the Sky`

This supersedes `Silence & Hope` from the Veil Master Beat Bible. That bible numbers
the Prologue `EP 01` with the swamp child at `EP 02–03`, so its Act I numbering is
**offset by one** and is renumbered to the `E00` convention on migration, not the
reverse.

`pre01` / `post01` was considered and rejected: the Prologue is narrative, and
non-narrative material is supplements, which have their own identifiers. Epilogues
take the next sequential episode number.

### 2.3 Beat IDs use `BT`

`{SID}-BT{BeatNumber}`. Resolves the collision where `B` meant both Book and Beat. No
beat IDs exist in the repository yet.

### 2.4 Field names: schema is canonical, packet labels are aliases

`canon_rules.json` keeps `CORRIDOR` and `RES`. Tooling accepts `U-Level` and
`Resonance State` as recognized input aliases and normalizes on the way in.

---

## 3. The supplement model — three independent axes

Type, function and vehicle are **three separate columns**. Nothing is overloaded.

### 3.1 `supplement_type` — audience content goal

Type is the payoff delivered to an audience segment less engaged with the adjacent
narrative.

| Code | Definition |
| --- | --- |
| `LORE` | Historic or background information |
| `POL` | Political communiqués giving information not seen in the narrative |
| `FUN` | Humor or an enjoyable story, placed when the narrative is in a heavy stretch |
| `SLICE` | How life is progressing outside the narrative |

### 3.2 `supplement_function` — emotional function in the reader cycle

From the Supplement Text Architecture Bible §1 and §6, consolidated.

| Code | Meaning |
| --- | --- |
| `PING` | "I see you. Stay with us." |
| `TENSION` | "The world is tightening." |
| `RELEASE` | "Yes, this is the payoff you needed." |
| `LINK` | Plot linkage — conveying off-page events (Chronicle leaks, MT civic updates, route changes, hazard warnings) |

### 3.3 `supplement_vehicle` — where it appears in-world

Recovered from Notion `05.08 • Supplement Text Architecture Bible`. Five primary, two
culture, one metaphysical shadow.

| Vehicle | Tone | Voice | Role |
| --- | --- | --- | --- |
| `MT` — The Missing Thread | earnest → chaotic → vulnerable → legendary | Tahl → Kade | civic awareness, emotional windows, public reaction, Kade's grief arc; becomes the global voice of humanity under collapse |
| `CHRON` — Chronicle | investigative, ethical, factual | multiple reporters | counterpoint to MT, institutional truth-seeking, civic anchor in Veil + Neon, collapses in Loom |
| `VEIN` — Vein | intimate, local, queer-coded, musical | — | humanity flavor, Cajun/Creole culture, NOLA social pulse, flashbacks, breathers |
| `FIELD` — Field Notes | sparse, clinical, eerie | — | shard logs, bloom data, resonance maps, diaspora routes, early VT anomalies |
| `VT` — VT Glimpses | whispered, fragmented, poetic | — | metaphysical shadow |
| `VELVET` — Velvet Vein Menu / Cocktail Book | — | — | culture, joy, sensory worldbuilding |
| `RITUAL` — Resonance Recipes / Music / Ritual Inserts | — | — | multicultural grounding, diaspora identity |

**Worked example:** a Chronicle leak about political suppression is vehicle `CHRON`,
function `LINK`, type `POL`, serving the Hardcore Fantasy Nerd.

### 3.4 Hard constraints from the bible

- **VT Glimpses: 10–12 total across all nine books**, used only at Tahl's slip,
  Tahl's death echo, the Loom 9 intervention, and the endgame echo stabilization.
  Never explicit dialogue; always fragmentary; emotional resonance only.
- Supplements are **150–600 words**, placed between episodes.
- Per-book intensity: Veil light → moderate → high; Neon heavy → very heavy →
  extreme; Loom extreme → extreme → intense/soft/celebratory.
- Supplements must never replace narrative, break POV, spoil future beats, deliver
  metaphysical exposition directly, or feel like bonus content.

### 3.5 The "do not advance plot" clause is superseded

`rules/Channels/SUPPLEMENTS_PERMISSION_RULES.md` §1 says supplements "do not advance
plot." **That clause is superseded** by the `LINK` function in §3.2. Update the file;
do not delete the surrounding rules, which stand.

---

## 4. Audience and payoff tracking

### 4.1 The five archetypes

Recovered verbatim from Notion `00.05 • Reader Archetype Mandate`. Migrate into
`canon/editorial_lenses.md`, which currently lists the names with no content.

| Archetype | Requires | Served by |
| --- | --- | --- |
| Horny Housewife | romantic chemistry · slow-burn tension · emotional payoff + spice hints | `ROM` (§7) |
| LitRPG Fan | system clarity · resonance mechanics and escalation · visible progression | `TECH` (§7) |
| Hardcore Fantasy Nerd | deep lore · metaphysics clarity · big world stakes | `LORE`, `POL` |
| Crossover Romantasy Reader | relationships · ensemble dynamics · emotional arcs | `CHAR` (§7) |
| Casual Web-Novel Binger | constant reward cycles · easy pacing · humor and momentum | `FUN`, `SLICE` |

Panel uses: pacing audits, reward structure mapping, supplement placement, POV
balancing, spice/tension cycles.

### 4.2 Beat tags and supplement tags are disambiguated by field, not by token

The same word may appear in two vocabularies. The field decides which is meant.

| Field | Level | Vocabulary | Answers |
| --- | --- | --- | --- |
| `MODE` | beat / episode | narrative registers | what register is this written in |
| `payoff_tags` | beat | audience-payoff list | which audience does this beat pay off |
| `supplement_type` | supplement | audience-payoff list | which audience does this supplement pay off |

`MODE: SLICE` means written in a slice-of-life register. `payoff_tags: SLICE` means it
pays off the reader who came for that. Both are often true at once. No prefixes, no
token rewrites.

`FUN` and `SLICE` are legitimately both modes and types — the material uses
`MODE: INT + SLICE` for an episode and "FUN beats every 5–8 episodes" as a pacing
rule, while the EBCI character files list `FUN` among drivable modes. `FUN` should
therefore be added to `controlled_vocab.modes`; `SLICE` stays.

### 4.3 The payoff-gap mechanism

The grids were built for this and are all header-only. `episode_beats.csv` has
`payoff_tags`; `reader_pressure.csv` has `reader_group`, `pressure_state`,
`intensity_1_5`; `milestones_payoffs.csv` and `supplement_deployment.csv` have
`reader_group` and `supplement_type`.

Tag each beat with the archetypes it pays off, aggregate per archetype across an
episode range, and when an archetype goes N episodes without a payoff, schedule a
supplement of the matching type. Supplements become a response to a measured gap
rather than an instinct.

---

## 5. Authority, sources and provenance

### 5.1 Tier scheme

A locked source canon · B approved development outputs · C existing GitHub canon ·
**D other sources** · **E memory**. The competing checkpoint lettering (D earlier
Notion / E assistant-generated / F memory) is retired and converted wherever found.

### 5.2 Mechanica is authoritative

Until the line-by-line memory chat review completes.

### 5.3 `source_canon/` is more authoritative than other material, but not unimpeachable

It outranks assistant-generated and memory-derived material. It does not outrank
Mechanica or explicit later author decisions. Its README's `Archive / Discard`
lifecycle does not license deletion.

### 5.4 Notion precedence

Notion generally came first. GitHub and later recovered Beat Bible material outrank
conflicting Notion content. Notion-only facts stay `RECOVERED PRIOR CANON` until
re-approved.

### 5.5 Act I E00–E18 beat text exists, in the unabridged chats

"Recovered complete" in `BOOK1_EPISODE_RECOVERY_STATE` and `RECOVERY_LEDGER_2026.md`
§5 refers to material that exists but is not exported. The repository holds packets
for E16–E18 only. Correct the ledgers to: full beat text for E00–E18 exists in the
unabridged source conversations; E00–E15 are unexported and unmigrated.

### 5.6 The Editorial & Publication Codex is already migrated

Fetched in full from Notion. `canon/codex_rules.md` matches its nine rules verbatim;
`editorial_lenses.md` matches its board, consultant and archetype lists. **The ~40
`TODO` fields for `Asks` / `Flags` / `Protects` are not in Notion either** — they were
invented repo-side and need authoring, not recovery.

Missing from the repo and to be added: the **Publication Advisory Group** —
Traditional Publisher, Web Serial Publisher, Social Influencer, Audiobook Producer.
Rotating, advisory only.

---

## 6. Structural rulings

### 6.1 `proposal/concord-2026-reconciliation` merges, as its own folder

50 commits ahead, 0 behind. The recovery material keeps its own top-level folder.

**Pruning:** the sanitized exports are never pruned in place. Copy them to a separate
folder and prune the copy. The ChatGPT Business workspace has no export path and the
share-link route was tested and closed — these files are the only copy.

### 6.2 The identical trilogy envelopes are unintended

All three trilogy contexts carry `weather_max: W3` and `corridor_max: U5`; only FX
escalates, making `U6`, `U7` and `W4` unreachable everywhere. Values should be fluid
and matched to narrative momentum. **The replacement rule is not yet decided (§8).**
Whatever replaces it must admit Veil packet `S1.T1.B3.A3.E14`, which already carries
`Weather: W4`.

### 6.3 The uniform act overlays are not intended

All 27 are byte-identical apart from IDs, as are all 9 book contexts, with `fun`,
`slice_of_life` and `wonder` capped at `LOW` including the Book 9 climax. Skeleton
state, not design.

### 6.4 `Technarc` is correct

Correct 9 occurrences of `Technarch` in `canon/characters/RexID.md`, `VirelliID.md`,
`canon/trilogy_veil.md`, `canon/trilogy_neon.md`, `canon/factions/Dominions.md`,
`rules/symbols/GEOMETRY_MOTIFS.md`.

### 6.5 E19 unlocks after the line-by-line chat review, organization and distillation

Not after E01–E15 migration alone.

---

## 7. Provisional — adopt unless James objects

These follow necessarily from §4.1's recovered archetype definitions, but were not
ruled on directly. **Flag them; do not treat them as locked.**

Three types added to §3.1:

| Code | Proposed definition | Why |
| --- | --- | --- |
| `ROM` | Relationship progression happening off-page | Horny Housewife requires "romantic chemistry, slow-burn tension, emotional payoff" — no other type serves her |
| `TECH` | Resopunk systems, mechanics and progression | LitRPG Fan requires "system clarity, resonance mechanics, visible progression" |
| `CHAR` | Character interiority — backstory, private motive, ensemble dynamic | Crossover Romantasy requires "ensemble dynamics, emotional arcs", distinct from `ROM`'s chemistry. Also attested as a beat-level `Function:` value |

Without them three of the five archetypes have no supplement type that serves them.

---

## 8. Open — Claude must not decide these

1. **What replaces the fixed trilogy envelopes (§6.2).** Advisory guidance with no
   enforced ceiling, per-act ceilings, or a ceiling tied to a momentum marker.
2. **Is `SUPP` a mode or a flag?** It appears in a mode-tag list in the exports
   (`Mode tags (ROM/HUM/ACTION/SUPP)`) and looks like a marker meaning "this beat is
   supplement material" rather than a register.
3. **Do the six forms fold into vehicle?** `SUPPLEMENTS_PERMISSION_RULES.md` §2 lists
   letters, recorded messages, journals, memory fragments, reflective vignettes,
   aftermath scenes. Every one has an obvious vehicle, so folding them in is the
   recommendation — but it is a ruling, not a cleanup.
4. **A mode glossary.** No file in the repository defines what any mode means. That
   absence is what let `LORE` and `POL` drift into the mode field. A one-line gloss
   per mode would close it permanently.
5. **`reader_group` values.** Derive from `supplement_type`, or keep an independent
   vocabulary if the segments cut differently (subscriber tier, first-read versus
   re-read).

---

## 9. Not yet recovered

Notion is now connected. Searched so far: Creative Governance and the Supplement Text
Architecture Bible. **Not yet searched:** the 27-Act Macro Structure, the Resonance
Escalation Curve, the Civic & Institutional Collapse Curve, the Emotional Arc Spine,
the Symbolism & Motif Map, and the per-book **Final Beat Bibles** — the last of which
may hold the E00–E15 material the chat exports are missing.
