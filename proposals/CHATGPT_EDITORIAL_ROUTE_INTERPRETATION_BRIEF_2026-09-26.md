# Brief for ChatGPT: editorial route interpretation, Pass 1

**Date:** 2026-09-26
**Status:** WORKING BRIEF / NON-CANONICAL. It asks for a proposal. It rules on nothing and changes no
file.

**Purpose:** the forensic pass established where the existing material puts each main-cast
character, how strong that evidence is, and where it conflicts or runs out. The author has since
answered the heaviest conflicts. This pass is the **interpretation** that the forensics deliberately
stopped short of: where the characters **should** be, for the strongest nine-book narrative.

---

## 0. Repository rules for this pass (read first)

The repository is `jacalder42/concord-saga-canon`, on the `main` branch. It is public.

1. **Write one new file only:** `proposals/EDITORIAL_ROUTE_INTERPRETATION_PASS1_2026-09-26.md` (use
   the actual date). **Do not modify any existing file.** That includes the recovery ledger,
   `CLAUDE.md`, the grids, `decisions/`, `canon/`, `rules/`, `book_context/` and `act_overlays/`.
   Claude will review your file, add the ledger entry and migrate whatever the author approves.
2. **If you cannot create the file safely, return the document in chat instead.** Never write a file
   back from a partial or truncated view. On 2026-09-26 a whole-file write from a partial fetch
   deleted §1–§114 of the ledger (ledger §117).
3. Open the file with a `Status:` line (`NON-CANONICAL PROPOSAL`) and end it with a section saying
   what it does **not** change.
4. **Do not rule, and do not mark anything `ruled`.** Every recommendation is a proposal. The author's
   "Proceed" approves the immediately preceding proposal as design direction (Tier B), not as ruled
   canon.
5. **Cite exactly.** Give the file and section or line for every claim about existing material, and
   put only exact words in quotation marks. Label your own inferences **READING** and your inventions
   **DESIGN**.
6. **No prose.** No scene text, dialogue or lyrics. Beats and functions only.
7. **Books are two digits** (`B01`, not `B1`). **Episodes number continuously** across a book.

---

## 1. Read first

**The forensics, and the author's answers to them:**

- `recovery/MAIN_CAST_PRESENCE_MATRIX_PASS1_2026-09-26.md`: the book and 27-act matrices.
- `recovery/MAIN_CAST_ROUTE_LEDGER_PASS1_2026-09-26.md`: the person-route ledger.
- `recovery/MAIN_CAST_LOCATION_REGISTERS_PASS1_2026-09-26.md`, which holds:
  - the 27 contradictions;
  - the unknowns and seven missing journeys;
  - the absence register;
  - flattening signs and little-used ties.
- `decisions/MAIN_CAST_LOCATION_AUTHOR_ANSWERS_2026-09-26.md` §1–§5: **the author's answers. They
  override the registers wherever they apply.**

**The rulings that constrain geography:**

- `decisions/SAGA_CAST_SEPARATION_AND_GLOBAL_THEATERS_AUTHOR_RULING_2026-09-26.md`
- `decisions/POV_DISTRIBUTION_TARGETS_AND_TRILOGY_BATON_AUTHOR_RULING_2026-09-26.md`
- `decisions/NEON_MILESTONE_ARCHITECTURE_AUTHOR_RULING_2026-09-26.md` §0
- `decisions/NEON_DESIGN_ROWS_AUTHOR_ANSWERS_2026-09-26.md`
- `decisions/HOPE_LACUNA_KADE_AND_M54_AUTHOR_ANSWERS_2026-09-26.md`
- `decisions/LOOM_SPINE_AND_ANCHORS_AUTHOR_RULING_2026-09-26.md`
- `decisions/LOOM_CHAIN_KNOWLEDGE_AND_MENDING_COST_AUTHOR_RULING_2026-09-26.md`
- `decisions/B06_B08_B09_EPILOGUE_AUTHOR_ANSWERS_2026-09-26.md`
- `decisions/B03_WAREHOUSE_AUTHOR_RULING_2026-09-26.md`
- `decisions/ELIAS_CARD_CORRECTIONS_AUTHOR_RULING_2026-09-26.md`

**Your own earlier geography work.** These are leads to reconcile, not authority:

- `proposals/SAGA_GEOGRAPHY_CAST_DISTRIBUTION_MATRIX_PASS1_2026-09-26.md`
- `proposals/SAGA_THEATER_LEDGER_PASS1_2026-09-26.md`
- `proposals/NEON_B04_B06_PARALLEL_THEATER_RECONSTRUCTION_PASS1_2026-09-26.md`
- `proposals/POV_GEOGRAPHY_RECONCILIATION_PASS1_2026-09-26.md`

**Structure:**

- `grids/milestones_payoffs.csv`: the status column is authoritative. Only `ruled` rows are ruled.
- `grids/locations_registry.csv`
- `proposals/LOOM_STRUCTURAL_PASS1_B07_B09_2026-09-26.md`
- `proposals/B02_EPISODE_ARCHITECTURE_PASS2_2026-09-26.md` and
  `proposals/B03_EPISODE_ARCHITECTURE_PASS2_2026-09-26.md`
- **B01 is locked** in `proposals/B01_REVISED_BEAT_BIBLE_V4_1B_INTEGRATED_2026-09-22.md`. Do not
  reorder it.

---

## 2. Fixed points: do not move these

Verify each one against its source before relying on it. A point marked *lean* may be argued
against; the rest may not.

**The shape of the saga:**

- **Separating the primary cast is intentional.** The main-cast itinerary is not the world map.
  Reunions must be earned. Do not solve an information gap by putting the ensemble in one place.
- **POV:** about 30/30/30/10 as soft editorial targets. The trilogy lead carries 30 (Baz in Veil,
  Tahl in Neon, Kade in Loom), Seraphine 30, the secondary protagonists 30, and 10 is flex. These
  are not quotas.

**Seraphine:**

- She is in NOLA in B06.
- She leaves NOLA when it breaks in B07.
- She is absent from the NOLA feint in B09.
- She is at the Mending, which happens at Honey Island.

**Lucien:**

- He is sent from Vienna before B01, and first appears on the page at E04.
- In B04 he rejects the Dominion and goes back to Vienna in grief (not at the Dominion's request).
  He returns to NOLA before reconnecting with Seraphine.
- He is in NOLA in B06.
- In B07–B08 he stays primarily with Seraphine.
- He is at the Mending, where he and Caro become the guides.

**Baz:**

- He dies at the Warehouse at the end of B03, the only principal there.
- Tahl did not know Baz was there.
- The cast learns of his death in B04.

**Caro:**

- She does not leave NOLA in B01. Travel in B02–B03 is left to narrative fit.
- Chicago in Neon is a *lean*, and so is NOLA in B06.
- M54, in B05, is her first crack and the point where Hope first connects with her. Hope guides her.
- She is at the Mending.

**Elisabet:**

- Her B01 E23 appearance is a visit. She arrives to stay late in B01 or in B02.
- She is elsewhere in B06; the place is open.
- She is sent ahead just before the B09 attack.
- She is at the Mending, where she says goodbye.

**Tahl:**

- He is itinerant: *"bouncing between multiple places as he chases and reports the action"*.
- He brushes the VeilThread twice:
  - B02: he does not notice, but Silence and Hope do;
  - B03: he notices.
- He is named in the B03 epilogue.
- He dies at Santa Fe at the end of B06, having glimpsed the wound pattern. His last message reaches
  the group in the B06 epilogue by mortal means, not VT.
- His echo is identifiable only once: the B09 flare, which Rex knows.

**Rex:**

- He starts in Detroit and eventually makes a trip to Singapore.
- NOLA and an Atlanta trip in Neon are a *lean*.
- He is elsewhere in B06.
- In B09 A3 he holds the rear guard, and he is absent from the Mending.

**Kade:**

- His MT succession follows Tahl's death.
- *Soft lean:* he is far away when Tahl dies.
- He is at the B07 funeral.
- The split with Lacuna comes at the start of B08, along with his complicity.
- He is at the B09 A3 attack.
- He shares the epilogue night sky with Lacuna.

**Lacuna:**

- She may have cameos or foreshadowing appearances before B07.
- She is in NOLA in B06, but not a narrative focus.
- She is introduced prominently at the funeral that opens B07.

**Loom:**

- There are four wounds: Santa Fe (B08) → Mound City (B08) → Serpent Mound (end B08, with the
  escape opening B09) → Honey Island.
- **The factions do not know the swamp is the Mending site until B09 A3.**
- B09 includes a NOLA feint.
- The crew stabilises wounds; it does not head for Honey Island.

**Events:**

- The Riot of Light is in B04.
- Colorstorm is a B05 New Orleans event-condition. It does not gate Santa Fe.

**Held open. Do not resolve these:**

- the Santa Fe Rupture/death placement against the accepted ladder's Act II Rupture (grid M38);
- who originates or relays the VT warning (Tahl or the Filaments).

You may lay out options for them, but do not recommend one as settled.

---

## 3. The task

Produce the file named in §0, with these sections.

### A. A recommended route for each character

For each of Seraphine, Lucien, Baz, Caro, Elisabet, Tahl, Rex, Kade and Lacuna:

- a **book row**, B01–B09, with **act resolution where it earns its keep**;
- for each cell, the location, and whether it is a **fixed point** (§2) or your **DESIGN**;
- a line saying **what the place earns**: which theater it opens, what pressure or information it
  carries, and what relationship strain or reward it enables.

Where the author delegated a choice to narrative fit, give **one recommendation and at most one
alternative**, with the trade-off. The open slots include:

- Caro in B02–B03;
- where Elisabet and Rex are in B06;
- Tahl's places;
- Kade in B01–B04;
- where Lacuna's cameos fall;
- B09 A1–A2.

### B. The missing journeys

For each of the seven journeys in the register (§2 there), propose how the travel happens or how the
story avoids it. The priority is the **end of B06 → the B07 funeral**: Tahl's body, Elisabet, Rex and
Kade. Global travel is breaking in Layer 5. Name the cost of each option, in time, access and
pressure.

### C. The theater map

For each book, list the live theaters. For each one, say who or what carries it: a main character,
secondary cast, an institution, or information (MT, VT, data). The cast-separation ruling wants
**parallel global theaters**, especially in B04–B06. Mark where a theater is carried only by
information, and where that is enough.

### D. Ties to activate, and ties to let lie

Start from the register's list of little-used ties (Detroit, Bristol, Marseille, Chicago/Pilsen,
Abbeville and the Atchafalaya, Marrakesh, Reykjavík, Vienna, Lacuna's neighbourhoods). **Recommend**
which to activate, and where. Do not delete anything; letting a tie lie is a recommendation, not a
removal.

### E. Salvage from flattened sources

The register lists seven flattened sources (§4 there). For each, say which beats survive relocation
and where they would go. Do not simply restore the flattened geography.

### F. Questions for the author

Rank them, and ask no more than fifteen. For each, give the options and your recommendation, and say
what it unblocks: thread pressure, the book/act/episode milestones, or B08's end sequence.

---

## 4. What not to do

- Do not invent new characters, factions, metaphysics or world rules. A new place or secondary
  carrier is **DESIGN**: flag it, and keep such additions few.
- **Do not assign wound teams as settled.** You may propose who is available, with reasons.
- Do not move a fixed point in §2. Do not reorder B01.
- Do not let expanding one book consume another's material. In particular, **do not spend B09's
  ending on B07–B08**.
- Do not touch the EBCI hold. Do not create an `ebci/` directory.
- Do not use retired names (the list is `retired_terms` in `rules/canon_rules.json`), except when
  quoting them as evidence.
- Keep it to about 6,000 words. Tables are preferred.

---

## What this brief does not change

Nothing. It creates no ruling and edits no canon, grid, ruling or ledger entry. The recommendations
it asks for remain proposals until the author rules on them.
