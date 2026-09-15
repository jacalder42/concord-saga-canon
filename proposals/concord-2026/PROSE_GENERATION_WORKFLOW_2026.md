# Concord 2026 — Prose Generation Workflow

Status: PROPOSAL / NON-CANONICAL
Purpose: define the low-friction prose-production stack using GitHub, ChatGPT, Sudowrite, and NovelAI without creating another competing canon system.

## Core principle

**GitHub knows what is true. Sudowrite drafts the book. NovelAI solves difficult prose problems. ChatGPT decides what the scene is supposed to accomplish and audits whether the prose actually did it.**

No prose tool becomes a new canon authority.

---

# 1. Source-of-truth model

## GitHub
Authoritative for:
- Saga / Trilogy / Book / Act structure
- episode and beat architecture
- character canon
- POV canon
- Mechanica / resonance rules
- continuity locks
- open/conflict flags

## Sudowrite
Authoritative only for the **current working manuscript**.
Its Story Bible should be treated as a generated book-local context cache, not an independent Concord canon database.

## NovelAI
No authority role.
It is an alternate-prose / scene-repair environment.

## ChatGPT
Development and editorial authority only as approved by the author.
It compiles generation packets from canon, performs pre-prose gate review, and audits resulting prose.

---

# 2. Recommended generation unit

Use the recovered **Episode** as the default prose-generation unit.

Historical target:
- ~1.3–1.8k prose words per episode.

This aligns unusually well with current Sudowrite Write/Draft capabilities and preserves the old Episode -> Beat -> prose logic.

Recommendation:
- one Episode = one Sudowrite drafting document during generation;
- publication chapters may later equal one episode or combine adjacent episodes depending on serial/novel packaging;
- do not force publication chapter boundaries to control story-development architecture prematurely.

---

# 3. The Generation Packet

Before drafting an episode, ChatGPT/Claude should derive a compact packet from GitHub.

Required:
1. SID / episode title
2. episode function
3. POV character + POV rules
4. opening state
5. 6–12 BIDs / beat sequence
6. pressure map
7. relationship state relevant to the episode
8. Mechanica / UARS / VFX permissions actually relevant to this episode
9. motifs / breadcrumbs required here
10. required visible change
11. exit condition / continuity hook
12. forbidden moves / reveals
13. preceding prose excerpt or continuity summary
14. unresolved canon flags that must NOT be accidentally resolved in prose

Optional:
- a small amount of local setting texture
- dialogue intention
- emotional aftertaste
- humor/wonder target

Do NOT dump the entire saga bible into the generation packet.

---

# 4. Sudowrite role — broad first-pass generation

Sudowrite is the default manuscript environment and first-draft engine.

Recommended use:
- maintain a **Book-local Story Bible** derived from GitHub;
- include only current-book synopsis, active characters, relevant worldbuilding, and book outline;
- link documents/chapters in sequence so prior prose continuity remains available;
- use the episode packet as the immediate chapter/document outline;
- generate roughly one episode at a time.

Why this fits Concord:
- Sudowrite Write currently reads up to ~20k preceding words and can also use Story Bible, linked chapter outline, and chapter continuity;
- Write can generate up to ~2,000 words in one output, closely matching the historical Concord episode target;
- current Prose Modes include Muse 1.5, purpose-built for fiction.

Operational rule:
- **Sudowrite receives derived context, never the entire GitHub canon.**
- Story Bible is a cache. If Story Bible and GitHub disagree, GitHub wins.

---

# 5. NovelAI role — surgical prose room

NovelAI should NOT draft every episode by default.

Use it when a passage needs one of these:
- alternate dialogue runs
- five different continuations from an exact line
- stronger character-specific interiority
- sensory texture without added exposition
- a more surprising scene turn
- reduction of generic AI cadence
- an alternate emotional register
- line/paragraph-level rewrite experiments
- scene rescue when Sudowrite is structurally correct but lifeless

Recommended NovelAI packet:
- immediate preceding prose
- current episode objective
- current POV rules
- only the relevant character/location/lore entries
- explicit statement of what must remain unchanged

Use Memory / Author's Note / Lorebook deliberately rather than reproducing the whole saga.
NovelAI's context controls and Lorebook token budgets are an advantage specifically because this work is narrow and surgical.

NovelAI may improvise prose.
It may **not** invent canon that survives merely because the prose is good.

---

# 6. Pre-prose Gate Review

Before Sudowrite generation, ChatGPT performs a short Gate Review.

Pass/fail questions:
- Does this episode advance at least one book-level pressure line?
- Does it create a visible state change?
- Is the POV lens correct and differentiated?
- Does the episode contain a micro-payoff or meaningful turn for serial readability?
- Are all resonance expressions legal under current Mechanica?
- Are breadcrumbs/setups correctly timed?
- Are any reveals occurring too early?
- Is relationship movement earned rather than merely stated?
- Is there enough human-scale behavior before/around spectacle?
- Is there a reason this episode exists that cannot be absorbed cleanly into an adjacent episode?

Gate Review returns flags only unless the author asks for a rewrite.

---

# 7. First-draft sequence

Recommended default:

`GitHub authority`
-> `ChatGPT episode packet + Gate Review`
-> `Sudowrite first draft`
-> `human read`
-> `NovelAI only where a passage/scene needs alternate energy`
-> `human selects / combines`
-> `ChatGPT Editorial Audit`
-> `final human revision`

Do not bounce the full episode repeatedly between every model.
That increases prose homogenization and creates unnecessary context drift.

---

# 8. Editorial Audit after prose

ChatGPT should audit, not automatically rewrite, against:
- Beat compliance
- POV canon
- character voice distinction
- emotional truth > spectacle
- metaphysics serving character
- micro-payoff / serial propulsion
- macro-payoff setup
- exposition leakage
- generic AI cadence
- metaphor-domain violations
- dialogue voice collapse
- Wonder Engine opportunities
- humor / relief placement
- relationship thermodynamics
- Mechanica violations
- invented canon

Output categories:
- KEEP
- TIGHTEN
- REVOICE
- NOVELAI LAB
- CANON CHECK
- CUT
- EXPAND

---

# 9. Model-selection recommendation

Do not permanently choose a Sudowrite prose mode theoretically.
Run a one-episode blind calibration before production:
- Muse 1.5
- one alternate Sudowrite Prose Mode that produces stronger literary/character work at test time
- optional GPT direct benchmark

Judge by:
- Calder voice
- POV differentiation
- dialogue
- subtext
- inventiveness
- canon compliance
- amount of prose the author actually wants to keep

Once a default is selected, keep it stable for an act unless there is a strong reason to change.
Consistency matters more than chasing every model update.

---

# 10. Sudowrite Story Bible contents

For each book, generate a **derived Book Pack** containing only:
- 1–2 page book synopsis
- current-act outline
- active character summaries
- POV mini-blocks
- active factions
- active locations
- Mechanica limits for that trilogy/book
- recurring motifs
- relationship state
- hard prohibitions

Do NOT maintain the full nine-book canon manually in Sudowrite.

The book pack should be regenerable from GitHub whenever canon changes.

---

# 11. NovelAI Lorebook contents

Keep even narrower than Sudowrite.

Typical entries:
- active POV character
- scene partner(s)
- location
- one relevant faction/system entry
- immediate relationship state

NovelAI is most valuable when its context is focused enough to improvise rather than being smothered by encyclopedic lore.

---

# 12. Manuscript ownership / backup

Recommended:
- **Sudowrite = live working manuscript**
- **GitHub = story canon + generation architecture**
- periodically export manuscript snapshots at act/book milestones for archival backup

Avoid trying to synchronize every prose revision into GitHub in real time.
That recreates the clerical burden that stalled the project.

When an episode introduces an author-approved new canon fact during prose revision:
1. flag it during Editorial Audit;
2. promote the fact separately through the GitHub proposal/review workflow;
3. do not treat manuscript text alone as sufficient canon migration.

---

# 13. Role of NovelCrafter

No required role during initial drafting.

Re-evaluate near late revision / publication packaging.
Its series organization may still be useful, but duplicating GitHub canon into a full NovelCrafter Codex during drafting would currently add synchronization cost without a clear structural benefit.

---

# 14. Lowest-friction working loop

For the author, the normal experience should be:

1. Develop/approve episode here in ChatGPT.
2. ChatGPT writes/updates the approved structural proposal in GitHub.
3. Generate a Sudowrite-ready packet.
4. Draft in Sudowrite.
5. If a section is flat, take only that section to NovelAI.
6. Return the selected prose to the Sudowrite manuscript.
7. Run an Editorial Audit here.
8. Repeat.

The author should not manually maintain matching canon entries in three prose tools.

END WORKFLOW PROPOSAL
