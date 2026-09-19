# SUPPLEMENT VEHICLES & CONSTRAINTS

**Tier:** D — RECOVERED PRIOR CANON
**Source:** Notion `05.08 • Supplement Text Architecture Bible`, recovered 2026-09-18
**Migrated per:** `recovery/CANON_DECISIONS_2026-09-18.md` §3.3, §3.4 and §5.4
**Status:** Notion-only facts stay `RECOVERED PRIOR CANON` until re-approved (§5.4).
GitHub and later recovered Beat Bible material outrank conflicting Notion content.

Machine-readable counterparts live in `rules/canon_rules.json` under
`supplement_system`. Permission rules live in
`rules/Channels/SUPPLEMENTS_PERMISSION_RULES.md`.

---

## 1. The four axes

Type, function, vehicle and form are **four independent axes**. Nothing is overloaded,
and the field decides what a token means (decisions §4.2).

| Axis | Question it answers | Where it lives |
| --- | --- | --- |
| `supplement_type` | which audience segment does this pay off | decisions §3.1 |
| `supplement_function` | what does it do in the reader's emotional cycle | decisions §3.2 |
| `supplement_vehicle` | where does it appear in-world | §2 below |
| `supplement_form` | what shape is the artifact itself | §2.1 below |

**Worked example.** A Chronicle leak about political suppression is vehicle `CHRON`,
function `LINK`, type `POL`, serving the Hardcore Fantasy Nerd. Its form might be
`RECORDING` or `LETTER` — that is a separate choice, and no vehicle constrains it.

---

## 2. The seven vehicles

Five primary, two culture, one metaphysical shadow.

### Primary

#### `MT` — The Missing Thread

- **Tone:** earnest → chaotic → vulnerable → legendary
- **Voice:** Tahl → Kade
- **Role:** civic awareness, emotional windows, public reaction, Kade's grief arc.
  Becomes the global voice of humanity under collapse.

The tone and voice arcs run across the saga, not within one entry. `MT` is the vehicle
that changes hands — the handover from Tahl to Kade is the same baton pass the saga
spine records, seen from the supplement layer.

> **Token collision.** `MT` here is *The Missing Thread*, a supplement vehicle. `MT` in
> `rules/Channels/MT_RULES.md` and in `channels.MT` is *Mortal Technology*, a channel.
> Per decisions §4.2 the field disambiguates, not the token.
> `grids/supplement_deployment.csv` carries both `channel_MT_VT_LT` and
> `supplement_vehicle`, one column apart.

#### `CHRON` — Chronicle

- **Tone:** investigative, ethical, factual
- **Voice:** multiple reporters
- **Role:** counterpoint to `MT`, institutional truth-seeking, civic anchor in Veil and
  Neon. **Collapses in Loom.**

#### `VEIN` — Vein

- **Tone:** intimate, local, queer-coded, musical
- **Role:** humanity flavor, Cajun/Creole culture, NOLA social pulse, flashbacks,
  breathers

#### `FIELD` — Field Notes

- **Tone:** sparse, clinical, eerie
- **Role:** shard logs, bloom data, resonance maps, diaspora routes, early VT anomalies

#### `VT` — VT Glimpses

- **Tone:** whispered, fragmented, poetic
- **Role:** metaphysical shadow

**Hard-capped — see §3.1.** This is the only vehicle with a total-use limit.

> **Token collision.** `VT` is a channel (`channels.VT`), a resonance state
> (`res_states`), and this vehicle. Three vocabularies, one token.

### 2.1 Form — a separate axis from vehicle

**Ruled 2026-09-19: form and vehicle are separate values.** The six forms listed at
`rules/Channels/SUPPLEMENTS_PERMISSION_RULES.md` §2 do **not** fold into vehicle. They
are their own axis, and any form may ride any vehicle.

| Code | Form |
| --- | --- |
| `LETTER` | letters |
| `RECORDING` | recorded messages |
| `JOURNAL` | journals |
| `FRAGMENT` | memory fragments |
| `VIGNETTE` | reflective vignettes |
| `AFTERMATH` | aftermath scenes |

The distinction: **vehicle** is the in-world publication a reader encounters it
through; **form** is the shape of the artifact. A journal excerpt printed in the
Chronicle is vehicle `CHRON`, form `JOURNAL`. The same journal excerpt surfacing in
Field Notes is vehicle `FIELD`, form `JOURNAL`. Folding them together would have lost
that.

### Culture

#### `VELVET` — Velvet Vein Menu / Cocktail Book

- **Role:** culture, joy, sensory worldbuilding

#### `RITUAL` — Resonance Recipes / Music / Ritual Inserts

- **Role:** multicultural grounding, diaspora identity

The recovered bible records no tone or voice for `VELVET` or `RITUAL`. Those fields are
genuinely absent from the source, not omitted here — they need authoring, not recovery.

---

## 3. Hard constraints

From the bible, ruled binding at decisions §3.4.

### 3.1 VT Glimpses: 10–12 total across all nine books

Not per book. **Ten to twelve for the entire saga.**

Used only at:

1. Tahl's slip
2. Tahl's death echo
3. The Loom 9 intervention
4. The endgame echo stabilization

And always:

- never explicit dialogue
- always fragmentary
- emotional resonance only

This is the one supplement constraint a script can enforce, and
`tools/validate_canon.py` checks it (`CHK_VT_CAP`).

### 3.2 Length and placement

- **150–600 words** per supplement
- placed **between episodes**

### 3.3 Absolute prohibitions

Supplements must never:

- replace narrative
- break POV
- spoil future beats
- deliver metaphysical exposition directly
- feel like bonus content

`rules/Channels/SUPPLEMENTS_PERMISSION_RULES.md` §4 adds two absolute exception windows
where no supplement is permitted at all: after Tahl's death (Neon Book 6) and after the
ascension deaths (Book 9 Act III).

---

## 4. Per-book intensity curve

Supplement intensity is not flat across the saga.

| Trilogy | Book | Intensity |
| --- | --- | --- |
| Veil | `B01` | light |
| Veil | `B02` | moderate |
| Veil | `B03` | high |
| Neon | `B04` | heavy |
| Neon | `B05` | very heavy |
| Neon | `B06` | extreme |
| Loom | `B07` | extreme |
| Loom | `B08` | extreme |
| Loom | `B09` | intense / soft / celebratory |

The `B09` entry is three registers rather than one, which reads as the Mending's
three-part close rather than an unresolved note in the source. Recorded as found.

---

## 5. What this document does not settle

**Answered 2026-09-19:**

- **The six forms do not fold into vehicle** (§8 item 3). They are a separate axis —
  see §2.1. The decisions document recommended folding them in; James ruled the other
  way, and the journal-in-two-vehicles case above shows why.
- **`SUPP` is a mode** (§8 item 2), added to `controlled_vocab.modes`. Given with the
  hedge *"mode, i think"* — recorded as a soft ruling. If beat tagging later shows
  `SUPP` behaving as a marker rather than a register, it reopens cheaply: no beat is
  tagged with it yet.

**Still open at decisions §8, not to be decided without James:**

- **`reader_group` values** (§8 item 5): derived from `supplement_type`, or an
  independent vocabulary if the segments cut differently (subscriber tier, first-read
  versus re-read).
- **A mode glossary** (§8 item 4). No file defines what any mode means. That absence is
  what let `LORE` and `POL` drift into the mode field, and `SUPP` and `FUN` now join a
  list where nine of ten entries are undefined.
