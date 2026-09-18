# ECID Vocabulary Collision — Decision Memo

**Status:** Evidence only. No canon decision made. Blocks work-queue items 4 and 5.
**Prepared:** 2026-09-18
**Sources:** `recovery/source_exports/html_sanitized/` — 21 exports, 20 with content
(`ChatGPT - Story Development.html` is the known 708-byte shell, 580 visible characters) —
on branch `proposal/concord-2026-reconciliation`; `rules/canon_rules.json`,
`rules/Mechanica-v4.md`, `rules/symbols/COLOR_SEMANTICS.md`,
`canon/characters/SeraphineAppearance.md`, `source_canon/characters/seraphine_full.md`.
Section references to `CLAUDE.md` are to the version committed on branch
`claude/gifted-goodall-st4n7r`, which is not yet on `main`.

All counts below were recomputed from the exports by parsing turn boundaries and ECID
field values separately. Where this memo's figures differ from an earlier draft, the
difference is noted in §8.

---

## 1. The problem, scoped

The recovered episode packets fill ECID fields with tokens the controlled vocabulary
does not allow. Migrating a packet means writing those tokens into
`book_context_*.json` and the act overlays, or altering them on the way in. Either is
a canon act.

**The collision is not where the work queue is.** Splitting it by migration unit,
counting ECID field values only:

| Material | SIDs | Out-of-vocabulary field values | Queue item |
| --- | --- | --- | --- |
| `Episode expansion process` | `S1.T1.B1.A1.E16`, `B1.A2.E17`, `B1.A2.E18` | 3 `STRAIN`, 1 `LORE`, 1 `EDGE` — **5 total** | item 5 |
| `Saga structural archive` | `S1.T1.B3.A3.E01`–`E18` | 14 `STRAIN`, 4 `LORE`, 1 `POL`, 1 `BRUSH` — **20 total** | not in the queue |

So item 5 — migrating E16–E18 — hits five occurrences of three tokens. The remaining
20 occurrences sit in Book 3 Act 3 material that no current queue item touches. Both
packet sets also use the retired one-digit book form (`B1`, `B3`) that `CLAUDE.md` §3
rules wrong, so that conversion lands in the same pass.

---

## 2. What is out of vocabulary

Counted as **ECID field values** across all exports. Occurrences in headings, in prose,
and in the separate beat-level `Function:` field are excluded and listed below the table.

| Token | Field | As field value | Permitted? |
| --- | --- | --- | --- |
| `STRAIN` | Resonance State | 17 | No |
| `LORE` | Mode | 5 | No |
| `POL` | Mode | 1 | No |
| `EDGE` | Resonance State | 1, as `SHARD-EDGE` | No |
| `BRUSH` | Resonance State | 1, as `VT-BRUSH` | No |

Outside ECID field values:

- `STRAIN` once as a section heading — `7. FILAMENT STRAIN SIGNATURES`, in
  `Saga structural archive__part01`
- `LORE` twice in the **beat-level `Function:` field**, not in prose:
  `Function: LORE + CHAR` and `Function: PLOT + LORE`, in `Narrative Structure`,
  attached to beats `S1.T1.B1.A1.E06-B2` and `-B4`. That is a different field in a
  different schema layer, and those beat IDs also carry the retired `-B{n}` form that
  `CLAUDE.md` §3 replaces with `BT`
- `BRUSH` once in an `Anchor:` line — quoted in §3.1

Raw token totals across the corpus are therefore `STRAIN` 18, `LORE` 7, `BRUSH` 2.

Permitted sets in `rules/canon_rules.json`:

- `res_states`: `CALM` · `BLOOM` · `SHARD` · `RUPTURE` · `NODE` · `VT` · `LT`
- `modes`: `ROM` · `HUM` · `ACT` · `SCI` · `CIV` · `INT` · `HOR` · `SLICE`

These five counts confirm the table in `CLAUDE.md` §4.1 exactly. That table was correct.

---

## 3. The tokens are three different problems

Treating them as one issue is the trap. They fail in different ways.

### 3.1 `EDGE` and `BRUSH` qualify permitted states rather than replacing them

Both attach to a **permitted** state:

> `Resonance State: STRAIN → BLOOM → SHARD-EDGE settling`
> `Resonance State: RUPTURE → VT-BRUSH`

`SHARD` and `VT` are both in the vocabulary. `-EDGE` and `-BRUSH` modify intensity: the
edge of a shard state, a brush against VT rather than full contact. The second is
load-bearing canon — the same packet, EP14 / `S1.T1.B3.A3.E14`, carries the anchor line
four lines below:

> `Anchor: **FIRST AND ONLY VT BRUSH IN VEIL TRILOGY.**`

That line uses `VT BRUSH` with a space, and the episode title is
`THE SLIP — Tahl's First VT Brush`, so `brush` also reads as an ordinary word in this
material. `EDGE` never stands alone as a state token. Either way the question is one of
**syntax** — may a state value carry a qualifier? — not of two missing states. Adding
`EDGE` and `BRUSH` to `res_states` as standalone states would misrepresent both.

### 3.2 `LORE` and `POL` are genuine missing modes

As ECID field values both appear only in `Mode`, always compounded with permitted modes:
`INT / CIV / LORE`, `SCI / LORE` (twice), `INT / LORE`, `CIV / LORE`, and `POL / CIV`.
They read as worldbuilding-exposition and political-maneuvering register. Neither is
defined anywhere in `rules/`. `POL` appears once.

`LORE` carries an extra complication: beyond its five Mode values it appears twice as a
beat-level `Function:` value (§2). Whether the beat schema's `Function` vocabulary and
the ECID `Mode` vocabulary are the same list under two names is itself undetermined, and
nothing in `rules/` defines the beat `Function` field at all.

### 3.3 `STRAIN` has support in tier-1 canon, not only in disputed source canon

This is the one that changes the shape of the decision.

**The strongest evidence is on `main`, in undisputed tier-1 canon.**
`canon/characters/SeraphineAppearance.md` (line 161) structures its resonance section as:

```
### Under Strain
- Warm undertones may shift toward soft green → gold
- Light remains diffuse and contained
- Visual cost is visible but never explosive

### Bloom / Connection
```

`source_canon/characters/seraphine_full.md` (line 489) mirrors it exactly:

```
BASELINE RESONANCE STATE:
STRAIN RESPONSE:
  • Undertones shift green → gold
  • Warmth concentrates around chest and hands
  • Emotional cost visibly increases
BLOOM STATE:
```

This distinction matters. An earlier draft of this memo rested the `STRAIN` case on the
`source_canon/` file alone — but that file's authority is itself unresolved under
`CLAUDE.md` §1.1, so the argument would have depended on the outcome of a different open
question. It does not need to. The tier-1 appearance card on `main` carries the same
named condition in the same position, and nothing disputes it.

**The symbol layer already encodes strain as a named condition.**
`rules/symbols/COLOR_SEMANTICS.md` (line 59):

```
### YELLOW — Strain / Overload
- Signals: stress, saturation
- Behavior: harsh brightness, strobe-adjacent
- Risk: shard precursors
```

Echoed at `rules/Mechanica-v4.md:935` (`Yellow: strain / overload`) and
`rules/resonance/resonance_expression_rules.md:173`. So `rules/` does name strain — as a
colour semantic with an explicit relationship to shard onset — while
`rules/Mechanica-v4.md` §33 never lists it among the resonance states.

**Two places in Mechanica bear on where a definition would go, and they disagree in
shape:**

- **§3, line 47** gives the progression as a single bullet:
  `- Resonance states (CALM → BLOOM → SHARD → RUPTURE → NODE)`
- **§33 RESONANCE STATES** (line 613) defines the states as seven subsections with no
  progression at all, and already includes `VT` and `LT` alongside the five

So the state list is not a linear chain and already carries two members outside it. A
`STRAIN` definition would belong in §33; the progression bullet in §3, and possibly
§34's shard progression model (line 671), would be what needs revisiting.

**In the packets, `STRAIN` behaves as a hub, not as a rung.** Full distribution of the
25 Resonance State values:

| Value | Count |
| --- | --- |
| `CALM → STRAIN` | 7 |
| `STRAIN` | 6 |
| `CALM` | 3 |
| `SHARD` | 2 |
| `STRAIN → CALM` | 2 |
| `STRAIN → BLOOM → SHARD-EDGE settling` | 1 |
| `STRAIN → SHARD` | 1 |
| `SHARD → RUPTURE` | 1 |
| `RUPTURE` | 1 |
| `RUPTURE → VT-BRUSH` | 1 |

`STRAIN` is entered from `CALM` seven times and exited to `CALM` twice, to `SHARD` once
and to `BLOOM` once. It appears in 17 of 25 values — more often than every permitted
state combined. It is not positioned between calm and bloom; it is a pressure condition
reachable from calm and resolvable in several directions, which is consistent with
`COLOR_SEMANTICS`'s "risk: shard precursors" rather than with a fixed ladder position.

**Reading:** `STRAIN` is a condition the character canon and the symbol system both
already name, and that the mechanical state vocabulary never captured. That is a
reading, not a ruling.

---

## 4. Provenance

The sanitized exports preserve turn roles. Counted as **raw tokens**, not field values,
so these totals run slightly above §2:

| Token | In author turns | In assistant turns |
| --- | --- | --- |
| `STRAIN` | 15 | 3 |
| `LORE` | 4 | 3 |
| `POL` | 1 | 0 |
| `BRUSH` | 2 | 0 |
| `EDGE` | 0 | 1 |

**Caveat, and it matters:** a "user" turn only means the text was submitted from the
author's side. Large archival blocks pasted back into a conversation appear as author
turns regardless of who originally wrote them. Eleven of the `STRAIN` field values in
`Saga structural archive__part01` sit inside one such pasted block; the twelfth
occurrence in that file is the section heading, in a separate, earlier author turn. So
these numbers show where the tokens entered the record, not who authored them. Tier
assignment under `CLAUDE.md` §5 still needs your eye.

Note that `EDGE` is the one token originating in an assistant turn, and it appears
exactly once.

---

## 5. Two further problems the migration will hit

Separate from vocabulary, and unresolved.

**Fields carry transitions; the schema expects single values.**

- `Resonance State` holds a transition in 13 of 25 values — `CALM → STRAIN`,
  `STRAIN → BLOOM → SHARD-EDGE settling`
- `U-Level` holds one in 8 of 25 — `U3 → U4 in flashes`,
  `U2 (baseline) → U3 (entering city center)`

`canon_rules.json` defines these as flat enumerations with no transition syntax.
Migrating a packet means either flattening each transition to one value — discarding
the movement the beat is built on — or extending the schema to hold start and end.

**Field names don't match the schema either.** `canon_rules.json` lists `ECID_fields`
as `POV, ENV, CORRIDOR, WEATHER, MODE, HEAT, FX, RES`. The packets write `U-Level` for
`CORRIDOR` and `Resonance State` for `RES`. Migration has to map field names as well as
values.

**And one envelope breach.** EP14 / `S1.T1.B3.A3.E14` — the same packet that carries
`VT-BRUSH` — reads `U-Level: U5`, `Weather: W4 (brief)`, while
`rules/trilogy_context_T1_veil.json` caps Veil at `weather_max: W3`. The `U5` is within
envelope; the `W4` is not. This is the contradiction already flagged in `CLAUDE.md`
§9.1, showing up in recovered material rather than in the abstract. It is also the
trilogy's single declared VT contact, so it is not a candidate for quiet downgrade to
`W3`.

---

## 6. Options

Laid out with consequences. Not a recommendation — §4 of `CLAUDE.md` reserves this.

**A. Extend the vocabulary.** Add `STRAIN` to `res_states`, add `LORE` and `POL` to
`modes`, define a qualifier syntax for `-EDGE` and `-BRUSH`.
*Consequence:* packets migrate unaltered. A `STRAIN` definition has to be written into
Mechanica §33 and the §3 progression bullet revisited. The recovered material sets the
rules, which inverts the usual authority direction — though for `STRAIN` the tier-1
appearance card and the colour system arrived there first (§3.3), so that inversion is
weaker than it looks.

**B. Treat the packets as out of spec.** Map each token to a permitted value during
migration.
*Consequence:* the vocabulary holds, but `STRAIN` collapses into `CALM` or `SHARD`,
neither of which means what the beats describe, and both
`canon/characters/SeraphineAppearance.md` and `rules/symbols/COLOR_SEMANTICS.md` are
left naming a condition the state vocabulary denies. Lossy, and in tension with tier-1
canon rather than only with the disputed source file.

**C. Split the decision.** `STRAIN` is admitted on the strength of §3.3; `LORE` and
`POL` are held pending a ruling on whether mode is a closed set; `-EDGE`/`-BRUSH` are
handled as a syntax amendment rather than new states.
*Consequence:* for the E16–E18 item, admitting `STRAIN` clears 3 of its 5 occurrences,
leaving `LORE` and `EDGE`. For the Book 3 Act 3 material, it clears 14 of 20. Three
small decisions instead of one large one.

**D. Migrate with the tokens preserved and quarantined.** Carry original values into a
`source_value` field alongside a `null` canonical value, so nothing is lost and nothing
is asserted.
*Consequence:* migration proceeds now, the decision moves later, and the artifacts
carry an explicit hole until it is made. Costs a schema field and a second pass.

---

## 7. What is needed from you

Four rulings, in this order:

1. Is `STRAIN` a resonance state? If yes, is it a rung in the progression or a pressure
   condition reachable from several states, as the distribution in §3.3 suggests? And
   does `rules/symbols/COLOR_SEMANTICS.md`'s "risk: shard precursors" fix its
   relationship to `SHARD`?
2. Are `LORE` and `POL` modes, or is `modes` a closed set these should map into? Related:
   is the beat-level `Function` field drawing on the same vocabulary as ECID `Mode`?
3. May a state value carry a qualifier (`SHARD-EDGE`, `VT-BRUSH`), or must it be flat?
4. May an ECID field hold a transition (`CALM → STRAIN`), or does migration flatten it?

Answers to 1–3 unblock item 5. Answer 4 determines whether the `book_context` and
act-overlay schemas need extending before migration starts. None of the four unblocks
the Book 3 Act 3 material, which needs a queue item of its own.

---

## 8. Corrections to the earlier draft

Recorded per `CLAUDE.md` §9, so the change is auditable.

| Was | Now | Why |
| --- | --- | --- |
| `Saga structural archive`: 2 `BRUSH`, 21 out-of-vocab values | 1 `BRUSH`, 20 values | The draft's §1 table mixed raw tokens with field values. `BRUSH` occurs twice in that file, but only once as a `Resonance State` value; the other is the `Anchor:` line, which the draft's own §2 already excluded |
| §6 option C: "clears 14 of 21" | "clears 14 of 20" | Follows from the above |
| `LORE` appears "twice in prose" | Twice in the beat-level `Function:` field | `Function: LORE + CHAR` and `Function: PLOT + LORE` are field values in beat blocks, not prose. This is a second schema layer with its own undefined vocabulary, which strengthens rather than weakens ruling 2 |
| `STRAIN` supported by `source_canon/seraphine_full.md` | Also, and more strongly, by `canon/characters/SeraphineAppearance.md:161` and `rules/symbols/COLOR_SEMANTICS.md:59` | The draft rested the case on a file whose own authority is unresolved under `CLAUDE.md` §1.1. Tier-1 canon on `main` carries the same condition, so the argument no longer depends on that open question |
| `STRAIN` "sits between baseline and bloom" | A hub state: entered from `CALM` ×7, exited to `CALM` ×2, `SHARD` ×1, `BLOOM` ×1 | The full 25-value distribution does not support a fixed ladder position. This changes what ruling 1 has to decide |

Unchanged and re-verified: all five field-value counts in §2; the raw totals
`STRAIN` 18 / `LORE` 7 / `BRUSH` 2; every provenance figure in §4; the transition counts
in §5 (13 of 25 and 8 of 25); every quoted line; Mechanica line references 47, 613 and
671; and the statement that `CLAUDE.md` §4.1's table was correct.
