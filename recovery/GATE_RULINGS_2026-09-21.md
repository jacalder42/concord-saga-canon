# Concord Saga — Author Ruling: the prose rule

**Status:** AUTHOR RULING — BINDING
**Date:** 2026-09-21
**Ruled by:** James
**Against:** `main` @ `4378296`
**Continues:** `GATE_RULINGS_2026-09-19.md` (Rulings 1–4), `GATE_RULINGS_2026-09-20.md` (5–9)
**Source:** `PROSE_RULE_RULING_2026-09-21.md`, adopted

Closes the `CLAUDE.md` §1/§7 conflict recorded in `MARA_NIHT_RECOVERY_2026-09-21.md` §5,
`MUSIC_PROJECT_CORPUS_2026-09-21.md` and `ELI_STONE_PROJECT_2026-09-21.md`.

---

## Ruling 10 — The prose rule is scoped, not lifted

Prose, scene text, dialogue and lyrics are forbidden in the **substrate**:
`rules/`, `canon/`, `grids/`, `book_context/`, `act_overlays/`, `templates/`.
A task that would put narrative prose in those directories stops and says so.

Prose is **permitted**, under its own rules, in exactly two places:

- **`sources/`** — supplied source material, verbatim, never edited. Whatever a source
  contains, it is stored as supplied. A source archive that edits its sources is not an
  archive.
- **`manuscript/`** — authored narrative prose. Written by the author or at the author's
  direction. Not derived, not regenerable, never rewritten by a tool without explicit
  instruction.

**Location is not authority.** Nothing in `sources/` or `manuscript/` is canon by virtue of
being in the repository. Canon is what the substrate says. Prose in the repo is material
and output; it is not a ruling.

### Why the change

The old rule used **absence** to stop prose being mistaken for canon. That worked until the
sources themselves were prose, at which point §1 and §7 contradicted each other and three
recovery documents had to record the conflict as unresolved. The new rule states the
distinction instead of enforcing it by exclusion.

Two things the old rule protected are unchanged: the substrate stays machine-checkable,
and authored prose is never silently rewritten.

### Scope conditions

- **`sources/` and `manuscript/` are outside substrate validation.** They are not canon
  scope and never count toward the violation ceiling. Canon-scope 0 keeps meaning what it
  means.
- **`sources/` is append-only.** Files land as supplied and are never edited, pruned or
  reformatted in place — §1.0's existing rule, applied to real originals rather than to a
  derivative.
- **Provenance stays in the field.** A file in `sources/` is `recovered`; a file in
  `manuscript/` is `authored`, with date. Neither is `derived`.

---

## Source storage

Commit both `.md` and `.json` for every exported conversation, under
`sources/chatgpt_export_2026-09/`, with a manifest recording filename, conversation id,
`created`, turn count, word count and SHA-256.

**Both formats, and the reason is measured rather than assumed** — see the verification
below. The `.md` is what gets parsed; the `.json` carries the native message tree, which
the markdown does not merely flatten but **partially discards**.

---

## Verification performed before adoption

Four of the proposal's load-bearing claims were checked against evidence in hand. Three
confirmed, one refined, one unverifiable here.

### Confirmed — a complete export exists, so `CLAUDE.md` §7 is wrong

§7 states Business workspaces have *"no data export and no working public share links;
both routes were tested and closed"*, and that sources are *"one-way storage and not
reliably re-retrievable."*

The supplied `.json` files carry an `exported` timestamp of **`2026-09-15T16:57:09.617Z`**,
an account id, and the native conversation object. **An export exists and has been run.**
§7 is rewritten.

### Confirmed, and stronger than claimed — the `.json` carries what the `.md` drops

Measured on `Bubble Grunge Lyrics`:

| | `.md` | `.json` |
| --- | --- | --- |
| structure | linear headings | native message tree, **678 nodes** |
| user turns | 216 | 216 |
| assistant turns | 213 | 230 |
| **system messages** | **0** | **229** |
| tool messages | 0 | 2 |

The markdown does not carry system messages **at all**. Committing only the `.md` would
discard 229 messages per conversation of exactly the material that records how each
conversation was configured.

### Refined — the sanitized archive is lossy, but not where it matters most

The whole 21-file sanitized archive is **25,952 words**. A single supplied conversation
(`Bubble Grunge Lyrics`) is **108,378** — four times the entire archive. The archive is
plainly a small fraction of its sources, and the README's *"not summarized or intentionally
edited"* cannot be read as a claim of completeness.

**But the specific retention figures could not be verified here, and one implication of
them is wrong.** `Saga structural archive` was tested against what `CLAUDE.md` §3 cites it
for: **all 18 episode shells `S1.T1.B3.A3.E01`–`E18` are present**, as are the four
`S1.T1.B3.EP.E01`–`E04` epilogue shells.

So the archive **retains the structured artifacts it is cited for**. What it appears to
have lost is conversational context around them. That distinction matters: it is why
extraction from the archive worked, and it means prior conclusions drawn from it are not
presumed void. They are **unaudited, not discredited** — and re-running extraction against
full sources is how to settle which.

### Unverifiable here — the 72-conversation corpus

The proposal reasons from 72 conversations. **This session holds 7.** The export corpus is
not present, so no claim about its contents is made or relied on.

---

## Consequential corrections

1. `CLAUDE.md` §1 is rescoped to the substrate.
2. `CLAUDE.md` §7 is rewritten: sources are **re-exportable**, the export is the
   authoritative original, and material is committed before transformation for
   **auditability** rather than scarcity.
3. `recovery/source_exports/html_sanitized/README.md` is corrected and the directory
   re-designated a **lossy historical derivative**. **Not deleted** — earlier conclusions
   were drawn from it, and deleting it would make those conclusions unauditable.
4. The three prose-blocked recovery documents close.

## What does not change

Canon-scope 0 stays the ceiling. Derived containers stay derived. Nothing is pruned or
edited in place. Mara Niht's separate finding stands: her source contains zero occurrences
of `Concord`, `Elisabet`, `Velvet Vein` or `Harpa`, so her saga integration is **authorial
decision, not recovery**. Storing the body changes nothing about that.

---

# AMENDMENT 1 — strip workspace ids

**Ruled 2026-09-21:** *"strip workspace ids"*, in answer to the question raised before any
source was committed.

## The ruling

`workspace_account_id` is **removed from every `.json` before it enters `sources/`**. Its
value is replaced with the literal `REDACTED`.

This is the **only** permitted deviation from verbatim storage. Any further redaction
needs its own amendment.

## Why this is a narrow carve-out and not a hole in Ruling 10

Ruling 10 says *"verbatim, never edited … a source archive that edits its sources is not an
archive."* That is still the rule. An archive with **one declared, uniform, mechanically
verifiable redaction** is still an archive; an archive with undeclared edits is not. Three
conditions keep the distinction real:

1. **Declared.** Named here, named in `sources/README.md`, and visible in the file itself —
   the key is kept and its value replaced, rather than the key being deleted. A reader sees
   that a redaction happened.
2. **Surgical.** The replacement is a **text-level substitution of that value only**. The
   files are not re-serialised, so every other byte is unchanged. Re-formatting the JSON
   would be a far larger edit than the redaction itself.
3. **Verifiable.** `MANIFEST.csv` records the SHA-256 of **both** the original file and the
   stored file, plus the redaction applied. Anyone holding the export can confirm that the
   stored file differs from the original in exactly one value.

## Scope, measured

- `workspace_account_id` is a **single top-level key** per `.json`, one distinct value
  across all files.
- **The `.md` files do not contain it at all**, so they are stored byte-identical and their
  two hashes match.
- `real_author` holds only `tool:web` / `tool:web.run`; `owner` is null. Neither is
  personal and neither is touched.

## The ingest order matters, and getting it wrong is not recoverable

**Redaction happens BEFORE the first commit, never after.** Committing raw files and
stripping them later does not remove the value — it stays in git history permanently, and
removing it then requires rewriting published history, which §2 forbids.

`tools/ingest_sources.py` performs the copy, the redaction, the verification and the
manifest in one pass, so the redacted form is what gets committed in the first place.

> **Superseded 2026-09-24** by `tools/redact_export_ids.py` (byte-identical output) run from `tools/ingest_export.ps1`; see `sources/README.md`.

