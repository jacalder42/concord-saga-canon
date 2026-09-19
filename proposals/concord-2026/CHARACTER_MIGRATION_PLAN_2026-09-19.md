# Character Migration Plan — Opened Under Manifest §0

**Status:** PLAN OPENED / NOTHING MIGRATED / NOTHING PROMOTED
**Date:** 2026-09-19
**Authority:** `recovery/GATE_RULINGS_2026-09-19.md` Ruling 3 — *"APPROVE bundles A–I"*,
which *"authorizes controlled canon migration planning and application per manifest §0.
It does not authorize invention of unresolved material."*
**Governs:** `proposals/concord-2026/CHARACTER_RECONCILIATION_MANIFEST_2026-09-20.md`

---

## 1. The headline: the substrate is almost untouched by this

Manifest §0 step 1 is *"search source canon, temporal canon, beat bibles, manifests, and
rules-dependent references for each historical identity."* **That search has been run**
against the §14 watchlist of 36 obsolete names.

| Layer | Watchlist hits |
| --- | --- |
| **Canon substrate** (`canon/`, `rules/`, `grids/`, `book_context/`, `act_overlays/`, `source_canon/`) | **4** |
| `proposals/` | ~280 |
| `recovery/` | 3 |
| `recovery/source_exports/` | 0 |

**35 of the 36 names have zero substrate presence.** This is a `proposals/`-layer
reconciliation, not a canon rewrite — which changes the risk profile of the whole
migration and is why the batches below are small and the validator gate is realistic.

### 1.1 The one exception is already compliant

`PureTone` is the only watchlist name in the substrate, in four places:

| File | Usage |
| --- | --- |
| `canon/characters/SaekoID.md:122` | "Designs **PureTone logic** and quieting methodologies" |
| `canon/characters/SaekoEBCI.md:34` | "**PureTone logic**, quieting methodologies, resonance suppression theory" |
| `canon/characters/SaekoEBCI.md:107` | "Refines **PureTone logic**" |
| `canon/factions/Choirless.md:125` | "**PureTone logic** adoption" |

The manifest's ruling: *"RETIRE AS SEPARATE MAJOR FACTION. Use: earlier
campaign/network/technology vocabulary in genealogy feeding anti-resonance/Choirless
development."*

**All four are technology-vocabulary uses — "PureTone logic" — which is exactly the
surviving permitted sense.** None treats PureTone as a faction. So the one substrate hit
classifies as **KEEP-AS-VOCABULARY**, not `RETIRE`, and **no substrate edit is required
by the watchlist at all.**

---

## 2. Batch order

Ruling 3 approves A–I with B and G *"conditional on Ruling 1 vetting"*, and their place
references *"inherit Ruling 1's preliminary status."* So B and G run **last**, after the
narrative vetting pass has settled the contested ground recorded in
`location_places_PROVISIONAL_2026-09-19.csv`.

| Order | Bundle | §  | Entries | Gate |
| --- | --- | --- | --- | --- |
| 1 | **H** — trilogy load / migration rules | 11 | 3 rules | None. Rules first, so later batches are measured against them |
| 2 | **A** — Filament / community | 2 | 13 | None |
| 3 | **C** — Dominion / Vienna | 4 | 6 | None |
| 4 | **D** — Technarc / Singapore | 5 | 10 | 2 HOLDs excluded |
| 5 | **E** — ideological / Choirless | 6 | 5 | None |
| 6 | **F** — media / public voices | 7 | 11 | 1 HOLD excluded |
| 7 | **I** — hold / recovery list | 9, 10 | 9 | **No migration.** Approved *as a hold list* |
| 8 | **B** — NOLA civic / cultural | 3 | 12 | **Ruling 1 vetting** |
| 9 | **G** — global / place anchors | 8 | 8 | **Ruling 1 vetting** |

**H first** is a deliberate departure from alphabetical order. It is the trilogy load and
migration *rules*; running it first means every later batch is validated against them
rather than retrofitted.

---

## 3. What each batch does — manifest §0 steps 2–6

Per batch, in order, one commit each:

1. **Classify** every occurrence as `TRANSFER` / `RENAME` / `MERGE` / `ANONYMIZE` /
   `RETIRE` / `CONTRADICTION`. §14: *"No blind global replacement."*
2. **Migrate** the classified occurrences.
3. **Validate** chronology and relationship effects, and run `tools/validate_canon.py`.
4. **Update** the recovery and decision ledgers.
5. **Retire** obsolete proposal-era aliases — **only after** 1–4 pass for that batch.

**Gate on every batch:** the validator must report **at or below 27 canon-scope /
62 all-scope**. A batch that raises either number stops the queue and is reported rather
than continued.

---

## 4. Carve-outs — enumerated so they cannot be missed

### 4.1 HOLDs stay held — nothing in this list is promoted by any batch

| Item | Bundle | Manifest § |
| --- | --- | --- |
| Manufactured-meta population | D | 5 |
| Arden Kess / LX-5 | D | 5 |
| Lila Shore | F | 7 |
| Nix & Rio | I | 9 |
| Ayo Mensah | I | 9 |

Bundle **I** as a whole is *"approved as a hold list — nothing in it is promoted."* Its
batch slot exists to record that it was considered and deliberately not migrated, not to
move anything.

### 4.2 Terminal Witness — `RECOVER MORE / DO NOT PROMOTE`

Ruling 3: *"Tier E recollection, no source-level corroboration. **Protect the slot; invent
nothing.**"* Manifest §10. It is excluded from every batch. The slot is protected; no
facts are supplied.

### 4.3 Author-locked controls — untouched

**Tahl Morgan / MissingThread** and the **Baz** identity control (manifest §1) are locked
and are not reclassified by any batch.

> **RESOLVED 2026-09-19 — Amendment 1.** This was recorded here as an open discrepancy:
> Ruling 3 wrote the control as *"Baz Foix"* while `canon/characters/BazID.md` reads
> **Bastien "Baz" Arnaud**. **James ruled for canon.** `Bastien "Baz" Arnaud` is canon;
> `Basil "Baz" Foix` is overruled and `Foix` is retired as a Baz surname. The earlier
> cautious reading — that only the *rename decision* stayed locked — is superseded.
> `recovery/GATE_RULINGS_2026-09-19.md` Amendment 1; ledger §38 and §39.

### 4.4 Bundles B and G inherit preliminary status

Approved *in substance*; their **place references** are preliminary until the Ruling 1
vetting pass runs. Batches 8 and 9 cannot start before that.

---

## 5. What this plan does not authorize

- **No invention.** Ruling 3 is explicit: this authorizes migration planning and
  application, *"not silent invention of unresolved material."*
- **No blind replacement.** Every watchlist hit is labelled before it is touched.
- **No promotion of HOLDs**, and no supplying of Terminal Witness detail.
- **No Tier-1 promotion by this document.** Manifest §0: *"Nothing in this file by itself
  promotes proposal material into Tier-1/source canon."* The same holds here.

## 6. Ready state

| Precondition | State |
| --- | --- |
| Manifest approved | **Yes** — Ruling 3, bundles A–I |
| §0 step 1 search run | **Yes** — §1 above |
| Substrate exposure known | **Yes** — 4 hits, all compliant |
| Batch order fixed | **Yes** — §2, B and G last |
| Carve-outs enumerated | **Yes** — §4 |
| Ruling 1 vetting complete | **No** — gates batches 8 and 9 only |

**Batches 1–7 are ready to run.** Batches 8 and 9 wait on the narrative vetting pass.

END OF DOCUMENT
