# ebci/prose/ — prose packets

Status: PRODUCTION LAYER. **The pilot passed 09-27; the format is solved.** B01 Act I's packets are derived and swept
(`decisions/B01_ACT_I_PROSE_PACKETS_AND_WRITER_PROFILE_AUTHOR_RULING_2026-09-27.md`). **The calibration passed 09-27, and
sequential B01 drafting has begun** (`decisions/PROSE_CALIBRATION_RESULT_AND_DRAFTING_START_AUTHOR_RULING_2026-09-27.md`).
**Act II (E18–E37, S04, S05) is derived 09-28** (`decisions/B01_ACT_I_REVIEW_ANSWERS_AND_ACT_II_PACKET_RELEASE_AUTHOR_RULING_2026-09-28.md`). **Act III (E38–E48, S06) is derived and audited 09-28** on calendar C (`reports/B01_ACT_III_PROSE_PACKETS_AND_IMITATION_AUDIT_2026-09-28.md`). **No layer between packets and prose** (no treatments, dialogue plans or beat sheets).

**Manuscript prose is not kept in this repository**, which is public, and manuscript is not canon. Drafts live in a
separate **private** repository, `jacalder42/concord-saga-manuscript` (live 2026-09-28, ledger §233); see *Where prose lives* below.

## The derivation rule

**A prose packet derives from the EBCI Narrative Brief, never from the Control Layer.**

- **Excluded by default:** ECID and U/W/FX codes; SIDs, beat ids, breadcrumb and milestone ids;
  causal-card terminology and observation classes; tracking; provenance; future-book pointers;
  validator language; editorial explanations of why something matters later; **Writer Options**.
- **Writer Options enter a prose packet only by explicit, episode-specific promotion**, recorded in the
  packet's status line.
- **Shapes differ.** A packet omits every field that does not help its scene. A Life/Reward episode may
  be a handful of lines; an event episode carries only the page-safe observational limits it needs.
- **Only what is below the rule** in each file is given to a writer or to Sudowrite. The status line
  above it is repository metadata.

## The drafting stack

Each episode is drafted from these and nothing else:

1. **The approved writer profile**, `WRITER_PROFILE_JA_CALDER.md`, below its rule, unchanged.
2. **The episode's prose packet**, below its rule.
3. **Minimum identity context** (Q-CAL1), only for named characters not already established in the preceding prose;
   **plus the character pressures** (Q-IT1, 2026-09-29) below, for every stack.
4. **The actual preceding prose**; or, until it exists, the **context rule** below (Q-CAL3).
5. **From Act II on, one standing instruction** (Q-AR4): *Continue these people and this novel. Do not reproduce Act I's
   successful shapes.*

**Nothing else enters the stack.** The review-side watch-list (`REVIEW_WATCHLIST.md`) never does. No length numbers
(Q-AR5) and no web-serialisation concerns: web installments are derived later from the finished manuscript. **For the
B01 redraft, Q-IT2(d) supersedes Q-AR5:** each packet carries its approximate length (below).

### Minimum identity context (Q-CAL1)

For any named character who appears in the episode, give only the immutable identity facts that stop the scene
contradicting canon. Normally that is:

- name and pronouns;
- the character's scene-relevant role or relationship;
- **at most one** stable physical or presence fact, and only if it is likely to appear.
- **For a point-of-view character only** (Q-MC1 process fix, 2026-09-29, `decisions/REDRAFT_MOMENTUM_CHECKPOINT_E00_E04_AUTHOR_ANSWERS_2026-09-29.md`): **the foundational family facts** (who is living, who is dead, who raised them) **and where they live**. These are facts, not history or wound. Ordinary prose touches them without warning, and in the redraft's E03 a missing family fact produced a canon error.

Example: *Trip (she): Velvet Vein's host; compact, socially effortless, owns the room without dominating it.*

- **Do not import** full cards, histories, future roles or hidden significance.
- **Do not repeat** anything the preceding prose has already established. Once a character is on the page, the prose governs.
- It is **not a character-voice layer.** Q-WP3's one card line about how a POV character notices still applies at their first substantial POV appearance, and only there.
- The facts come from `canon/characters/` and `canon/cast_registry.csv`. They are assembled per episode in the drafting stack, not kept as a new document.

### Character pressures (Q-IT1, Q-IT3, 2026-09-29)

With the amended profile's §5A, the stack carries **the point-of-view character's four pressure lines** (*wants,
protects, habitually misreads, when threatened*), and those of any character whose want the scene turns on
(`decisions/WRITER_PROFILE_AMENDMENT_AND_REDRAFT_PACKET_RULES_AUTHOR_ANSWERS_2026-09-29.md`).

- They come from `proposals/CHARACTER_PRESSURE_CARDS_2026-09-29.md` as approved: its §9 for Seraphine (revised) and
  Mara (once the author approves her lines), and the draft cards for the rest. **Each character's approved *wants for themselves* line goes with them** (Q-WL1, 2026-09-29, §9). **Working drafting lines, not canon.**
- **Never** a line that states or implies a future event (Baz's B03 death, for example), and never the full card.
- A pressure is given as it stands at this point in the book. A **susceptibility** that the book has not yet enacted is
  marked as one, not given as a habit.

**The stack format and the external pressure** (Q-MO1–5, Q-XP1–7, approved as amended 2026-09-29,
`decisions/THIRD_PRESSURE_REVISED_SET_AUTHOR_ANSWERS_2026-09-29.md`):
- **Order:** *Wants* (for themselves) → *Pressed by* (the external source in the scene) → *Protects* (care, as a reflex
  with a price) → *Misreads* → *Under pressure* (shadow, and one constructive response). Seraphine's *"not to lose
  anyone else"* is carried on her *Protects* line.
- **A drafting aid, not a quota.** Care may open a scene. A piece is judged by **what the character chooses and
  changes**, not by which line heads the objective.
- ***Pressed by*** gives the source's **authority, stated justification and whose interests it serves**, and its drift
  at this point (ordinary friction in Act I; a will from Act II; pointing above in Act III). **Ordinary people keep
  their own motives and agency;** existing contact with the hidden organisations may remain, without making every
  pressure part of the hidden network. No faction vocabulary, and never forward.
- **Seraphine's second want** is *her own account on the record*, with its motive shown per scene, never labelled
  pride by default; **pleasure** (*a room that doesn't need her*) stays an actionable want.
- **Mara's lines** are provisional (Q-MO4).
- The per-character lines by act quote the manuscript, so they live in the private manuscript repository
  (`draft-notes/character-pressures/THIRD_PRESSURE_WORKING_LINES.md`) and enter packets only as they stand at the piece.

### The context rule (Q-CAL3)

**Until real preceding prose exists,** the context given to the drafting engine is **only** the relevant earlier
prose packets' **Ends** lines, as written, plus the approximate elapsed time. No synthesised connective summary,
no grouping and no characterisation.

**Once actual preceding prose exists, it supersedes this.** Calibration drafts are never preceding prose.

## Where prose lives (Q-CAL4)

- **Manuscript prose stays out of this repository.** The canon repository may record that drafting began and where
  manuscript authority lives; it holds no drafts.
- **Drafts live in a private repository, provisionally `concord-saga-manuscript`**, with a simple structure and no
  elaborate governance:

  ```
  B01/act-01/E00.md, E01.md, …
  B02/
  B03/
  draft-notes/
  ```

- **Manuscript is not canon.** Canon is what the substrate says (CLAUDE.md §1). Material that prose discovers
  enters canon only through the usual reconciliation and an author ruling.
- **Calibration drafts are disposable**, not preceding prose, and their invented material is not canon.

## The pilot's five questions

1. Can a competent novelist begin without reopening the canon repo?
2. Does it protect everything whose violation would actually damage canon?
3. Are the best dialogue, imagery, blocking, humour and emotional discovery still unwritten?
4. Is anything present because the database knows it rather than because the novelist needs it?
5. Does reading it make the novelist want to write the scene?

## Packets for the B01 redraft (Q-IT2, Q-IT4, Q-IT5, 2026-09-29)

**The source exists (2026-09-29, ledger §283):** the revised B01 EBCI is in `ebci/B01/` (50 packets, index in `ebci/B01/REDRAFT_CONCORDANCE.md`). The pre-redraft prose packets are kept in `ebci/prose/B01/superseded_2026-09-29/` and are not a source. The redraft's packets are derived act by act from the new Narrative Briefs.

The ~150k redraft's packets are new, one per piece of the chosen outline (`decisions/WRITER_PROFILE_AMENDMENT_AND_REDRAFT_PACKET_RULES_AUTHOR_ANSWERS_2026-09-29.md`). On top of everything above:

- **Source: revised B01 EBCI only (Q-AC2, 2026-09-29).** The redraft's prose packets derive from B01's EBCI Narrative
  Briefs **after** they are revised against the approved merged outline. Changed briefs are revised, new pieces get
  briefs, and merged or cut briefs are retired from active use with a status line (never deleted). **The merged outline
  and the amendment files are inputs to EBCI, never a parallel source for a packet.** The Control Layer stays excluded.
  *(Superseded wording, recorded: "the EBCI Narrative Brief as before, plus the outline's row for the piece".)*
- **A conflict brief** (preflight Q3, restored by Q-IT4): plain words, with *none* allowed where a piece has none.
  - *Objective:* what the point-of-view character is trying to do.
  - *Opposition:* **whose will** pushes back, where one exists (a person, an office, the city), and only then the
    phenomenon, a constraint or the character's own fear.
  - *Turn:* what changes the situation.
  - *Consequence:* what the choice costs or changes.
  - *Unresolved:* what the next pieces inherit.
  - No numeric ladders, codes or True/False conflict.
- **No required repair (Q-IT2a).** No packet requires a repair to close a piece. Where the story needs one, the
  packet names **what causes it and what stays changed**. A caused repair may come later in the same piece, given its
  own time on the page; it is never a free ending.
- **Exit conditions (Q-IT2b).** Only the facts the next piece depends on: elapsed time, place, who is present, who
  holds an object, open commitments. There are no clock times unless the story needs one, and never the next piece's
  events or meaning.
- **Neighbours (Q-IT2c).** A continuity error (someone the next piece needs goes missing) is fixed in the draft. A
  structural change (a relationship no longer fits a neighbour written for the old version) is a reason to redraft the
  neighbour, not to undo the change.
- **Clocks (Q-EN6, 2026-09-29).** No clock time in narration unless a character does something with it. A clock is
  an object someone fights over, trades, steals or bets on, never what the protagonists do instead of acting.
- **Two sign-off questions for every redraft piece (Q-EN8),** beside Q-CE5's seven: *does a protagonist start an act
  with a risk in this piece?* and *is a clock doing an action's work?*
- **Length (Q-IT2d, Q-IT5).** Each packet gives its approximate length from the outline, as an approximate word count.
  **The book aims at about 150k and may finish under it.** A piece over its target needs a specific reason, recorded
  by the checker.

## The workflow

**Act by act, never all 144 at once:** derive B01 Act I's prose packets immediately before drafting Act
I; draft; reconcile what prose discovered with canon and EBCI; then derive Act II. After B01's prose,
reconcile Veil continuity before deriving B02's packets.

**Sequential drafting began 09-27 at E00,** with a checkpoint after E03 or E04: *"One episode can tell us whether a
sentence works; four sequential episodes can tell us whether we have a novel."* No anti-tic rules are added to the
profile yet. After B01 Act I exists as a corpus, a prose-pattern pass separates authorial motif, character habit,
engine tic and AI tell.

## The writer profile

`WRITER_PROFILE_JA_CALDER.md` is the one stable instruction set that accompanies every packet (**approved 09-27** for Veil). **No per-character voice layer:** at a character's first substantial POV appearance only, one card line about how they notice or think may be promoted; after that the preceding prose governs. It is **recovered, not invented**: `recovery/JA_CALDER_WRITER_PROFILE_SOURCE_RECOVERY_2026-09-27.md` registers every source, its provenance and the conflicts. It carries no scores, ratios or required beats.

## Guards for B01 Act II and after

From the Act I checkpoints (`decisions/B01_ACT_I_DRAFTING_CHECKPOINT_AUTHOR_ANSWERS_2026-09-28.md`,
`decisions/B01_ACT_I_REVISION_REPORT_AUTHOR_ANSWERS_2026-09-28.md`), carried into prose-packet derivation.

- **No return to the camp in B01** (Q-DR7).
- **No Vienna scene in B01.** Mentioning that Lucien is from Vienna is fine (Q-DR8).
- **No landmark or compass direction for Lucien's lean** (Q-DR10). E04's *toward the low sun* is the only bearing.
- **Seraphine's entry into an episode does not default to paperwork.** Her life widens as her story widens.
- **Act I is closed for editing.** It is the calibration corpus. Its rhythms and endings are judged later in an
  author-led line edit, not an automated pass.

**From the Act I review** (`decisions/B01_ACT_I_REVIEW_ANSWERS_AND_ACT_II_PACKET_RELEASE_AUTHOR_RULING_2026-09-28.md`).
These describe how narrative behaviour changes; they do not add scenes:

- **Agency (Q-AR7).** Act I happened to them; Act II increasingly happens because of what they decide to do about it.
  They plan, test assumptions, disagree about what things mean, look for witnesses, cause trouble with what they think
  they know, miss ordinary obligations, and choose on incomplete evidence.
- **Seraphine's work (Q-AR8).** Her casework continues, and the investigation begins to cost it. This permits the
  conflict; it is not a scheduled beat.
- **Three methods (Q-AR9).** Baz adds testimony, memory and questioning. He does not replace Lucien's physical
  evidence, measurement and contradiction. Seraphine's method is people, access and care. The investigation is most
  interesting where the methods disagree.
- **Titles are working labels (Q-AR2).** A packet's title is a label for the file, never a cue for the page. Final
  chapter titles are the author's, at publication.
- **Supplement scale (Q-AR6)** is given in words (*a short piece, about a page*), never as a number.

**Drafting reads the manuscript's continuity layer** (`draft-notes/B01_ACT_I_CONTINUITY.md` in the private repository)
for anything later prose must remember.
