# Editorial Lenses (Advisory Only)

These lenses are invoked ONLY:
1) Immediately prior to Sudowrite prose generation (Gate Review)
2) During post-prose editing (Editorial Audit)

They provide findings/flags only. Author decides actions.

## Primary Board
### Neil Gaiman — Mythic resonance, motif continuity
- Asks: TODO
- Flags: TODO
- Protects: TODO

### Matt Dinniman — Web-serial pacing, humor injection
- Asks: TODO
- Flags: TODO
- Protects: TODO

### Ali Hazelwood — Relationship thermodynamics
- Asks: TODO
- Flags: TODO
- Protects: TODO

### Travis Deverell — Serialization discipline, plot acceleration
- Asks: TODO
- Flags: TODO
- Protects: TODO

### SenLinYu — Emotional intensity, vulnerability clarity
- Asks: TODO
- Flags: TODO
- Protects: TODO

### Nate Regier — PCM alignment, conflict mediation, emotional intelligence
- Asks: TODO
- Flags: TODO
- Protects: TODO

### Steve Jobs — Product clarity, design elegance, narrative UX
- Asks: TODO
- Flags: TODO
- Protects: TODO

## Secondary Consultants
### Hannah Fry — Systems clarity & narrative mathematics
- Asks: TODO

### Questlove — Cadence, rhythm, improvisational structure
- Asks: TODO

## Reader Archetype Panel

**Tier D — RECOVERED PRIOR CANON.** Recovered verbatim from Notion
`00.05 • Reader Archetype Mandate` and migrated per
`recovery/CANON_DECISIONS_2026-09-18.md` §4.1 and §5.4. Notion-only facts stay
`RECOVERED PRIOR CANON` until re-approved.

Used for payoff mapping and pressure audits.

| Archetype | Requires | Served by |
| --- | --- | --- |
| **Horny Housewife** | romantic chemistry · slow-burn tension · emotional payoff + spice hints | `ROM` † |
| **LitRPG Fan** | system clarity · resonance mechanics and escalation · visible progression | `TECH` † |
| **Hardcore Fantasy Nerd** | deep lore · metaphysics clarity · big world stakes | `LORE`, `POL` |
| **Crossover Romantasy Reader** | relationships · ensemble dynamics · emotional arcs | `CHAR` † |
| **Casual Web-Novel Binger** | constant reward cycles · easy pacing · humor and momentum | `FUN`, `SLICE` |

† **`ROM`, `TECH` and `CHAR` are UNRATIFIED.** They are proposed at decisions §7, which
follows necessarily from the archetype definitions above but was not ruled on directly.
Without them, three of the five archetypes have no supplement type that serves them.
They are seeded in `rules/canon_rules.json` under
`supplement_system.supplement_types_provisional`, deliberately separate from the four
ruled types. Do not treat them as locked.

The panel is used for: pacing audits, reward structure mapping, supplement placement,
POV balancing, and spice/tension cycles.

### The payoff-gap mechanism

Decisions §4.3. The grids were built for this and are still header-only.

Tag each beat with the archetypes it pays off (`episode_beats.csv` → `payoff_tags`),
aggregate per archetype across an episode range (`reader_pressure.csv` →
`reader_group`, `pressure_state`, `intensity_1_5`), and when an archetype goes N
episodes without a payoff, schedule a supplement of the matching type
(`milestones_payoffs.csv` and `supplement_deployment.csv` → `reader_group`,
`supplement_type`).

Supplements become a response to a measured gap rather than an instinct. `N` is not yet
set.

> **`payoff_tags` and `MODE` are different vocabularies that share tokens** (§4.2).
> `MODE: SLICE` means written in a slice-of-life register. `payoff_tags: SLICE` means
> it pays off the reader who came for that. Both are often true at once. No prefixes,
> no token rewrites — the field decides.

---

## Publication Advisory Group

**Tier D — RECOVERED PRIOR CANON.** Migrated per decisions §5.6. Missing from the
repository until now.

**Rotating. Advisory only.** Same standing as the editorial board above: findings and
flags, never decisions.

- Traditional Publisher
- Web Serial Publisher
- Social Influencer
- Audiobook Producer

---

## Note on the `TODO` fields above — authoring DEFERRED

The roughly 40 `Asks` / `Flags` / `Protects` fields left `TODO` in the board and
consultant sections **are not recoverable**. Decisions §5.6 confirms they are not in
Notion either — they were invented repo-side and need **authoring, not recovery**.

**Ruled 2026-09-19: authoring is deferred until recovery and distillation are
complete.** These fields stay `TODO` until then. They are not a gap to be closed
opportunistically, and no session should fill them — including by inference from the
board members' published work, which would put invented lens criteria into canon under
real people's names.

The validator does not flag them: they are prose placeholders in a markdown file, not
schema values, so they carry no mechanical cost while they wait.

The rest of this file matches the Notion Editorial & Publication Codex verbatim, as
does `canon/codex_rules.md`, which carries its nine rules.
