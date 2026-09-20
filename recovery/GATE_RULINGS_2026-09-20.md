# Concord Saga — Author Rulings, Five Gates

**Status:** AUTHOR RULING — BINDING
**Date:** 2026-09-20
**Ruled by:** James
**Against:** `main` @ `85edb73`, ledger §53 and §54
**Continues:** `recovery/GATE_RULINGS_2026-09-19.md` (Rulings 1–4, Amendment 1)

These five close questions that `CLAUDE.md` §4 and §9.1 record as open, and they
change the default answer to a recurring one: **derive it and mark it provisional,
rather than leave it empty.**

---

## Ruling 5 — Trilogy ceilings are SOFT

**Ruled.** A trilogy ceiling is a **tripwire, not a wall.** Specific events may run
briefly over it, or under it.

**Every breach must be DECLARED**, as an exception in the form already in use:

    {"sid": ..., "axis": ..., "value": ..., "scope": ..., "reason": ...}

An **undeclared** breach is a violation. A **declared** one is a notice.

### What this settles

Ledger §53 §2 found 13 axis-breaches across six of the nine books and could not tell
whether the act layer or the trilogy layer was wrong. This ruling says the question was
malformed: a band that may be crossed on purpose is not contradicted by crossing it. What
matters is whether the crossing is **on the record**.

It does not, by itself, make the 13 breaches legitimate — see Ruling 5's interaction with
the derivation in ledger §57. A ceiling derived from its own contents cannot be breached
by them, so most of the 13 dissolve rather than become declared exceptions.

### Scope

Applies to book-inside-trilogy and act-inside-book containment alike. The existing
`exceptions` list on every act and book envelope is the declaration site; no new field.

---

## Ruling 6 — Prologues and epilogues sit OUTSIDE the act model

**Ruled.** All nine books have **exactly three acts**. `PR` and `EP` are **structural
positions alongside** `A1`–`A3`, not additional acts.

**27 acts remains the cap**, and is untouched by this ruling: 9 books × 3 acts. A
prologue or an epilogue is not an act and is not counted as one.

### What this settles

`CLAUDE.md` §4, *"Does `EP` go in the act slot?"* — open since 2026-09-19, blocking five
rows of the milestone grid. The answer is that the slot is not an *act* slot; it is a
**structural-position slot**, and `A1`–`A3` are three of its five values.

This is consistent with the source asymmetry recorded in ledger §27.7 — the prologue sits
inside ACT I in the export layer while the epilogues sit outside the acts — without
requiring that asymmetry to be resolved first. Both the prologue and the epilogue get a
position of their own.

The 2026-09-19 ruling that **Book 9 has three acts** (ledger §25) is reaffirmed, and Act
IV "Afterlight" remains the epilogue written as an act.

---

## Ruling 7 — Pressure is calibrated PER TRILOGY

**Ruled.** `T5` in Veil does not denote the same magnitude as `T5` in Loom. The
`pressure_before` / `pressure_after` scale is **calibrated within a trilogy**, not across
the saga.

**This is separate from, and compatible with, the per-thread question, which stays
open** — ledger §43. Per-trilogy calibration is about what a number *means*; per-thread is
about *whose* pressure it measures. Both can be true.

### What this settles

Ledger §43's saturation finding: 11 of 12 milestones in B06–B08 sit at `5 → 5`. Under this
ruling that is not necessarily a scale failure, because a Loom `5` is a Loom `5` and the
comparison to a Veil `5` was never meaningful. The flatness *within* Loom remains a real
observation and remains open under the per-thread question.

---

## Ruling 8 — Location assignments are DERIVED NOW, as provisional

**Ruled.** Ruling 1 of 2026-09-19 said **preliminary**, not **absent**. Derive the
assignments now and carry them; do not leave the fields unpopulated.

**The provisional status rides IN THE FIELD**, not in a separate note beside it. A reader
of the value must see its status without consulting another document.

### What this settles

The 2026-09-19 implementation read Ruling 1's "do not lock contested ground" as "leave
contested ground empty". That was the wrong reading. Tremé, Marigny, the French Quarter,
Bywater and the Red Lantern Faultline get their provisional assignment **in the field,
marked provisional**, like everything else.

---

## Ruling 9 — POV rotation is DERIVED as an initial proposal

**Ruled.** Derive each book's POV rotation from the baton pass in
`rules/saga_context_S1.json`, marked **initial proposal**.

**Weights remain authored.** Do not derive a weight from a count.

---

## Derived work queue

1. Vocabulary for `PR` and `EP` — `canon_rules.json` and the SID format. Ruling 6.
2. Derive the trilogy envelopes from the books beneath them.
3. Enforce declared exceptions. Ruling 5.
4. Derive `continuity_hooks` and `exit_state_locks` from `required_setups`.
5. Derive `entry_state` for B02–B09 from the preceding book's exit.
6. Derive `locations_in_play`. Ruling 8.
7. Derive POV rotation. Ruling 9.

`title`, `pov_targets` weights and B01's `entry_state` are **not** in this queue. They are
authored and stay authored.
