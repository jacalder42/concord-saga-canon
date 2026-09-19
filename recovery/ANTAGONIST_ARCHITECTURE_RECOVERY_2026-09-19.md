# Antagonists — Recovery Pass 3

**Status:** RECOVERED FROM THE EXPORTS / NOTHING MIGRATED
**Date:** 2026-09-19
**Sources:** `Story Development - _ Narrative Structure _(1)__part01.html` and
`Story Development - Saga Beat Expansion Pipeline__part02.html`, both in
`recovery/source_exports/html_sanitized/`
**Ruling applied:** James, 2026-09-19 — primary antagonists get protagonist-style
treatment; **antagonist groups operate at a pressure-curve model.**

**Both halves of that ruling are already implemented in the sources.** The individual
half exists in the repository (§1); the group half exists in the exports as a named audit
(§3). Neither needed designing.

---

## 1. The individual half is already done in `canon/`

Five antagonists carry the protagonist file pattern, and three exceed it:

| Character | Files | Extra |
| --- | --- | --- |
| Saeko Morita | 5 | **`SaekoBackstory.md`** |
| Koro Ito | 5 | **`ItoBackstory.md`** |
| Han Wei | 5 | **`HanWeiBackstory.md`** |
| Elias Ward | 4 | — |
| Marcellus Virelli | 4 | — |

All five have POV files. Every protagonist carries exactly four files, so the antagonist
layer is at parity or ahead. **Nothing to build here** — the ruling ratifies what exists.

The gap is on the protagonist side: **Seraphine has three files and no `EBCI`**
(ledger §29 §4).

---

## 2. The compressed antagonist architecture — `_ Narrative Structure _`

Recovered verbatim in structure from a compression pass whose stated method was *"remove
duplication, merge repeated motivations, fold splinter factions together when structurally
identical, tighten language, **preserve every narrative-critical distinction**."*

### 2.1 Philosophy

> All antagonists arise from human fear, trauma, power preservation, or misinterpretation
> of resonance. No supernatural villains. Opposition escalates as Veil instability rises:
> **Institutions → Splinters → Extremists → Collapse panic.**

That last line **is the saga-level pressure curve**, stated as a four-stage progression.

### 2.2 Six primary factions, each with an era range and an impetus

The `antagonistic impetus` field is the pressure-curve driver — it says *why* the faction
applies force, which is what makes its curve predictable.

| Faction | Era | Antagonistic impetus |
| --- | --- | --- |
| **Dominions** | Veil → early Neon | preserve order, fear emotional volatility, maintain control. Old geopolitical blocs around bloodline/heritage resonance; includes Witchlight hierarchies (Seraphine), Vampiric lineages (Lucien), Technarc-adjacent diplomats |
| **Technarc Hardliners** | Veil → Neon | eliminate emotional unpredictability. Rationalist, data-purist, resonance-suppressive wing of the Directorate; drive weaponization, containment protocols, manufactured meta research |
| **Choirless** | Neon | remove resonance by erasing emotional amplitude. Anti-emotion extremists born of Pulse War trauma; masks, unison behaviour, *"emotion is entropy"* |
| **Manufactured Metas** | Neon → Loom | tools of their creators. No Intent; inherently unstable; *"existential illustration of resonance without humanity"* |
| **Filament-Splinter Radicals** | Neon | retaliation, panic, hunger for agency. Breakaway grassroots radicalized under pressure; early Neon Rebellion recruits |
| **Loom Panic Factions** | Loom | survival, misinformation, desperation. Militias, fractured governments, fear-led mobs |

### 2.3 Key individuals

Marcellus Virelli (Dominion) — hybrid-purging zealot, *"compassionate authoritarian"* ·
Director Han Wei (Technarc) — architect of resonance containment and data absolutism ·
Koro Ito & Saeko Morita — populist anti-resonance leaders fuelling Neon fear ·
**Proto-Extremist Filament Leader — unnamed youth who seeds splinter militancy.**

That fourth entry is an **uncast role**, and it overlaps the parallel session's
`EDITORIAL_CASTING_RESOLUTION_CIVILIAN_RADICALIZATION_2026-09-19.md` and
`EDITORIAL_CASTING_RESOLUTION_FILAMENT_2026-09-19.md`. Cross-check before either promotes.

### 2.4 Saga-wide evolution — the curve in three eras

> **Veil:** secretive, institutional antagonism.
> **Neon:** splinter groups, weaponized tech, fear populism.
> **Loom:** global panic and collapse-level human conflict.

### 2.5 Five immutable rules

Antagonists are always human or human-made · manufactured metas cannot ascend (no Intent)
· motivations stem from human emotional fractures · antagonists escalate pressure but
deepen humanity's conflict *with resonance*, not cosmic evil.

Two of these are already in `canon_rules.json` as
`antagonists_human_or_human_made_only` and `manufactured_metas.cannot_ascend`. **The
invariants layer is already consistent with the recovered architecture.**

---

## 3. The group pressure curve already exists — as a named audit

`Saga Beat Expansion Pipeline` runs a **PHASE VI — Antagonist Architecture & Faction
Evolution** check, and separately names an **"Antagonist Pressure Audit"** as audit 3 of
the pipeline's Step 6, scoped as:

> Dominions in Veil · Extremists + Technarch in Neon · Collapse factions/Brightbreak in Loom

The Phase VI verdicts give per-faction curves in exactly the form James described:

| Faction | Recovered curve | Verdict |
| --- | --- | --- |
| Dominions / Technarc | pressure and institutional friction in Veil and early Neon; *"never act as cartoon villains; they choose secrecy and control over preparation"* | Pass |
| Technarc Hardliners | pressure around Santa Fe; weaponization attempts | Pass |
| Manufactured Metas | **Neon 6 only**, as failures — matching late-Neon timing | Pass |
| **Choirless** | **whispered ideology Neon 4 → traction Neon 5 → violence Neon 6 → full militant splinter in Loom** | Pass |
| Brightbreak / Elias | introduced subtly in Loom 7; grows as rhetoric and charisma, **not magic** | Pass |

The Choirless line is the model case: a four-point curve at book granularity with a
doctrine attached. **This is the pressure-curve model, already written and already
audited.** It needs extracting into the faction files and binding to
`grids/episode_beats.csv`'s existing `antagonist_pressure` column — not inventing.

---

## 4. The group template already exists and is unevenly applied

| Faction | Current treatment |
| --- | --- |
| Concord | directory — `EraFunction` · `Limits` · `Mandate` · `Relationships` · `Structure` |
| Filaments | directory — `Aesthetics` · `CanonLocks` · `EraFunction` · `Origin` · `Relationships` · `Structure` |
| Technarc, Dominions, Choirless, Brightbreak, Manufactured Metas | **single files** |

**`EraFunction` is the pressure-curve field in all but name.** Extending the directory
pattern to the five antagonist factions is therefore an existing convention to apply, not
a new model to design — which is what James's ruling asked for.

Note the two faction directories belong to the *non-antagonist* groups. So the repository
currently gives its allies structural depth and its antagonists single files, while the
character layer does the opposite.

---

## 5. FINDING — a three-pass integration pipeline was designed and never run

`_ Narrative Structure _` closes the antagonist compression with a next-steps plan that
maps precisely onto the build pipeline James described, at the intersection of all three
layers recovered in passes 1–3:

| Pass | Goal | Output it would produce |
| --- | --- | --- |
| **1. Environmental × Antagonist** | assign locations, fault lines and shard/emotional hotspots to antagonist actions; map where each faction "lives" | **"Antagonist Geography Bible"** |
| **2. Resonance × Antagonist** | faction-specific resonance signatures; how actions escalate shard behaviour; colour-language mapping | **"Resonance–Antagonist Interaction Bible"** |
| **3. Full tri-weave** | city fracture map Veil→Neon→Loom; resonance escalation ladder across urban districts; antagonist-triggered environmental shifts | **"Civic Resonance Conflict Atlas"** |

Worked examples given for Pass 1: *Virelli's Dominion operations map onto Vienna +
hybrid-purge networks · Saeko Morita's anti-resonance marches map onto Neon's fractured
Uptown + civic plazas · Technarc Hardliners anchor in Singapore → AR instability →
containment cordons.*

**None of the three bibles exists** — in Notion, in the exports, or in the repository. The
conversation offered A/B/C, recommended Pass 1, and the transcript moves to an unrelated
topic without an answer. So this is a designed-and-abandoned integration, and it is the
same shape as the prologue A/B question recorded in ledger §27.7.

**Why it matters now:** the three city assignments above are consistent with the
`HYBRID RESONANCE GEOGRAPHY SYSTEM` recovered in pass 1 (Singapore = Silver Static around
Technarch towers; Vienna = Ringstrasse Amber Drift). The two documents were written to fit
together and never joined up.

---

## 6. Conflicts and cautions

1. **Spelling.** The exports read `Technarch` throughout; `Technarc` is canonical
   (decisions §6.4). Rendered as `Technarc` in this document's own prose, with export
   quotations left intact. Ledger §26.10.
2. **`Dominions` vs `Concord Dominions`.** The architecture names the faction
   **Dominions**; `canon/factions/` carries both `Dominions.md` and
   `Concord Dominions.md`. Which is the faction and which is the institution is not
   resolved here.
3. **Brightbreak is three things.** ND-021 already records that Brightbreak is Elias, a
   handle, and a movement. The Phase VI verdict treats it as a Loom faction; the character
   layer treats Elias as an individual. Both are right at different altitudes, and the
   pressure curve needs to say which one it is tracking.
4. **The Proto-Extremist Filament Leader is uncast** (§2.3) and is live casting work in
   the parallel session.

## 7. For the author

1. **Extend the faction directory pattern to the five antagonist factions?** (§4) — this
   is the concrete form of the group-pressure-curve ruling.
2. **Run the three-pass integration** (§5), and in what order? Pass 1 was the original
   recommendation, and the locations layer it needs is now recovered.
3. **`Dominions` vs `Concord Dominions`** (§6.2).
4. **Which altitude does Brightbreak's pressure curve track** — the man, the handle or the
   movement? (§6.3)

END OF DOCUMENT
