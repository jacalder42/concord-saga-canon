# Review of the 2026-09-26 ChatGPT session's commits

**Date:** 2026-09-26
**Status:** EDITORIAL REVIEW / NON-CANONICAL. It reviews 44 commits and rules on nothing. One
repair is made alongside it: the recovery ledger is restored (§1). **No grid row, ruling, card or
book context is changed.**

**Scope:** `7cac88b` → `df869a2`, pushed under `jacalder42` between 09:13 and 13:35 −0500 on
2026-09-26, after Claude's `929e91c`. The author asked for this review: *"Review recent ChatGPT
work in repo."*

**What was pushed:**

| Folder | Files |
| --- | --- |
| `decisions/` | 3 new, 1 changed |
| `proposals/` | 16 new |
| `recovery/` | 5 new, 1 changed (the ledger) |
| `reports/` | 7 new |
| Substrate | the live grid, `book_context/` B04–B09 |
| Other | CLAUDE.md |

---

## Findings, most severe first

### 1. CRITICAL: the recovery ledger was truncated. Restored in this commit

- **`ec0abc3`** (*"Record saga geography recovery pass"*) replaced `recovery/RECOVERY_LEDGER_2026.md`
  with 71 lines, deleting 9,046: **§1–§114**.
- **`26e5687`** replaced it again and dropped §115 as well. HEAD held 38 lines, only §116.
- Both commits look like a whole-file write from a truncated view. The kept header is a subset of
  the original. §115 and §116 were numbered correctly, so the history was known to exist.

This broke `recovery/`'s one rule, *"Never pruned or altered in place"* (CLAUDE.md §1). It also
cut every ledger citation in the repository loose from its target. The all-scope SID count fell
from 112 to 79 only because the ledger's lines were gone.

**Restored:** §1–§114 come back byte for byte from `929e91c`. ChatGPT's §115 (from `ec0abc3`) and
§116 (from HEAD) are appended after them unchanged, and this review is §117.

### 2. HIGH: pushed with the checks failing. CI is red

The live grid fails four of the validator's own checks:

| Row | Problem |
| --- | --- |
| M05 | `target_trilogy` is `T1-T2`; the field takes one value, and `target_book` is B04, which is T2 |
| M54 | `thread` is `caro`, which is not in the vocabulary (`canon_rules.json` `controlled_vocab.threads`) |
| M55 | `thread` is `elisabet`, which is not in the vocabulary |
| M57 | `thread` is `seraphine_lucien`, which is not in the vocabulary |

**Four self-tests fail.** Three fail on those rows. The fourth is the ratchet that pins the 20
approved `ruled` rows: the grid now carries **29**. CLAUDE.md §2 says the validator *"must exit 0"*
and the self-tests *"must pass"* before any commit that touches the substrate.

### 3. HIGH: the Neon "author ruling" records no author words

`decisions/NEON_MILESTONE_ARCHITECTURE_AUTHOR_RULING_2026-09-26.md` and the grid notes
(*"AUTHOR-APPROVED 2026-09-26"*) contain **no quotation of the author and no scope of
acceptance.** CLAUDE.md §4 requires both.

**What the ruling changes in the grid:**

- **Promotes to `ruled`:** M05, M18, M21, M23, M38, and four new rows, M54–M57.
- **Retires:** M15, M19, M22.
- **Rewrites rows already ruled:** M20, M37 and M39.

The session's own documents set a gate that is not shown as passed:

- The promotion delta (§9): *"author confirms/adjusts the four new rows M54–M57; author confirms
  M15/M19/M22 retirements; author confirms revised M05 Vienna architecture."*
- The Caro source test: a Chicago return is a *"DESIGN OPPORTUNITY, NOT RECOVERED ATTENDANCE."*
- The Vienna adjudication: *"No recovered source explicitly says Lucien physically returns to
  Vienna in B04,"* then *"ADVANCE … AS THE PREFERRED DESIGN."*

**If the author approved these in the ChatGPT conversation, only the record is missing.** It can be
completed by quoting his words. **If he did not, these rows are assistant design promoted to
canon**, which CLAUDE.md §4 forbids.

**Substance to confirm, row by row:**

| Row | Change | Why it needs the author |
| --- | --- | --- |
| **M38** | The Santa Fe rupture now falls in **B06 A3**, with Tahl's death | It quietly resolves the conflict the approved grid carried: the ladder the author accepted puts the Rupture in **Act II** |
| **M38** / ruling §8 | *"Tahl originates the critical Santa Fe VT warning"* | The 09-26 ruling left the relay open: Tahl **or** Filaments (`B06_B08_B09_EPILOGUE_AUTHOR_ANSWERS_2026-09-26.md` §1.1) |
| **M20**, **M39** | Ruled wording rewritten. M39 adds *"without providing a complete solution"*; M20 adds *"enough … to leave a mortal informational legacy"* | New claims in rows the author had already approved |
| **M37** | Adds a public-correction episode (*"publicly corrects it despite losing authority"*) | New story material |
| **M21 / M22** | Merged | This was an open question in the approved grid |
| **M05** | Lucien returns voluntarily to Vienna in B04 | Design, per the session's own adjudication |
| **M54–M57** | New rows: Caro's handoff, with Chicago preferred; Elisabet acts before certainty; Caro and Elisabet choose separate work; Seraphine and Lucien | New relationship milestones. M54's Chicago is a design opportunity |
| **M15**, **M19** | Retired | M15's retirement resolves a conflict the approved grid carried. M19 keeps the Colorstorm as a local event, consistent with lean 3 |

### 4. MEDIUM: book contexts are hand-regenerated, and B01–B03 are stale

- **No generator exists** in `tools/`. The B04–B09 contexts were rewritten by hand under
  *"Regenerate rather than hand-edit."* They read plausibly, but nothing checks them.
- **B02 still lists M05**, which now sits in B04.
- **B03 lists M10 and M11 at `EP` and lacks M12.** That staleness is **Claude's own omission** from
  `929e91c`, which moved M10/M11 into A3 and M12 into the B03 epilogue without regenerating the
  contexts.

### 5. LOW

- CLAUDE.md and `decisions/README.md` lost their trailing newlines (whole-file rewrites).
- A few new documents use one-digit book labels in prose (CLAUDE.md §3). No validator hits.
- Order of work: the B02/B03 episode-architecture passes are queue step 3, while step 1 is
  **ACTIVE** (CLAUDE.md §9). They are labelled proposals and do not break a rule. Whether the author
  directed the jump is not recorded.

---

## What the session did well

- **The research is careful.** It separates recovered, design and open material, and says so in
  its verdicts (*"DESIGN OPPORTUNITY, NOT RECOVERED ATTENDANCE"*). It cites sources and keeps the
  site secret, the B01 lock and the EBCI hold.
- **B03 architecture pass 2 follows the 09-26 Warehouse rulings exactly:**
  - an anonymous coordinates post;
  - Tahl named only in the epilogue;
  - he did not know Baz was there;
  - the cast learns of the death at the start of B04.
- **The cast-separation ruling** quotes the author verbatim and says what it does not change.
  **The POV ruling** paraphrases a recollection (*"The author recalled…"*) rather than quoting it.
- **Retiring M15 and salvaging the Colorstorm** address two conflicts the approved grid carried.
- **`sources/` is untouched.** The source verifier passes, and there are no retired-term
  violations in canon scope.

---

## For the author

1. **Did you approve the Neon milestone changes?** If yes, give or paste your words, so the ruling
   records them with scope. If only some, say which rows.
2. **The three new threads** (`caro`, `elisabet`, `seraphine_lucien`): add them to the thread
   vocabulary (Ruling 7), or score those rows `UNSCORED` / `caro_elisabet`?
3. **M38:** the Santa Fe Rupture in **B06 A3** with the death, rather than Act II as the ladder had
   it. Is that your ruling?

**Once answered, Claude will:**

- set M05's trilogy to `T2`;
- apply your thread choice;
- update the ratchet test to the approved set;
- regenerate B01–B03's book contexts;
- turn CI green.

## What this review does not change

No grid row, ruling, card, rule file or book context. The Neon ruling file stays as ChatGPT wrote
it, pending the author's answer. The only repair is the ledger restoration.
