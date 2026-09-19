# Channels and Resonance States — Proposal

**Prepared:** 2026-09-19 · **Status:** proposal. Nothing here is ruled.

---

## 1. What I expected to find, and what is actually there

I flagged `VT` and `LT` appearing in both `controlled_vocab.res_states` and
`invariants.channels` as a category error — a channel filed as a state. On reading the
channel rules, that is not what it is.

`rules/Channels/CHANNELS_OVERVIEW.md`, Authoritative Canon, defines:

- **MT** — Mortal Technology, the human-built information and communication layer
- **VT** — **Veil-Touch**, *metaphysical boundary contact*
- **LT** — Luminous Thread, post-Mending only

`VT` is named for a contact event. `RES: VT` is not the channel sitting in a state
field; it is the field in a condition of boundary contact. Mechanica §33 agrees —
its `VT` entry reads "Metaphysical boundary interaction," and its `LT` entry
"Post-Mending prismatic filtration · Ascendant-only perception."

**The decisive evidence is `MT`'s absence.** If the three channels had been filed into
`res_states` by mistake, `MT` would be there too. It is not — and it should not be,
because a phone call is not a condition of the emotional field. The two tokens in
`res_states` are exactly the two channels whose use *is* a field condition.

The recovered packet reads the same way: `Resonance State: RUPTURE → VT-BRUSH`, with
the anchor "FIRST AND ONLY VT BRUSH IN VEIL TRILOGY." That is an episode recording
that contact happened, not that a channel was in use.

---

## 2. So the collision is narrower than it looked

There is a real distinction — channel as medium versus field condition — but it is
already expressed, in two different places:

| Concept | Where it lives now | Example |
| --- | --- | --- |
| Which channel a text uses | `grids/supplement_deployment.csv` → `channel_MT_VT_LT`; `grids/milestones_payoffs.csv` → `channel` | a Chronicle piece runs on `MT` |
| Whether the field made channel contact | ECID `RES` | `S1.T1.B3.A3.E14` records `VT` |

The ECID has no channel field and does not need one: at episode level, channel contact
*is* the state. A supplement needs a channel field because a supplement is a text
travelling on a medium, which is a different question.

**Recommendation: do not split the vocabulary.** The tokens are shared because the
concepts are related, the same way `FUN` and `SLICE` are shared between `MODE` and
`payoff_tags`. The field decides which is meant, which is the convention already ruled
for this repository.

---

## 3. What to do instead — make the structure visible

The flat list is what made this look like an error. Group it so the two kinds are
legible without renaming anything:

```json
"res_states": ["CALM", "BLOOM", "SHARD", "RUPTURE", "NODE", "VT", "LT"],
"res_states_kind": {
  "field_condition":  ["CALM", "BLOOM", "SHARD", "RUPTURE", "NODE"],
  "channel_contact":  ["VT", "LT"]
},
"channels": {
  "MT": "Mortal Technology — human-built information and communication layer",
  "VT": "Veil-Touch — metaphysical boundary contact",
  "LT": "Luminous Thread — post-Mending only"
}
```

The flat list stays, so nothing that reads it breaks. The grouping is additive and
carries the distinction into the data rather than leaving it in prose.

---

## 4. Rules that follow once the kinds are named

Each of these is enforceable only because the grouping exists, and each is already
canon somewhere in prose:

1. **Era gates.** `LT` is post-Mending only (`LT_RULES_POST_MENDING.md`:
   "Applies To: Post-Mending World Only"). `VT` persists in every era but is sealed
   until Tahl's breach in Veil (escalation curve: "VT: sealed until Tahl breach").
2. **Channel separation applies to contact states too.** `MT ≠ VT ≠ LT` is the core
   law. One episode cannot record both `VT` and `LT` contact.
3. **`VT` scarcity is already quantified.** The Supplement Text Architecture Bible caps
   VT Glimpses at 10–12 across nine books, and the Veil packet says "first and only."
   A contact-state counter is checkable; a field-condition counter would be meaningless.
4. **The Post-Mending envelope permits both.** `CALM · BLOOM · NODE · VT · LT`,
   forbidding only `SHARD` and `RUPTURE` — grounded in `VT_RULES.md` §9 ("VT persists
   as boundary contact · remains distinct from LT · VT does not evolve into LT") and
   §7.4 ("no new shards or ruptures").

None of these can be expressed against a flat list of seven equivalent tokens.

---

## 5. Options I considered and rejected

**Remove `VT` and `LT` from `res_states`, add a `CHANNEL` ECID field.** Rejected: it
contradicts Mechanica §33, which is authoritative under §5.2 and defines both as
resonance states with their own entries. It would also leave `E14` with nowhere to
record that the brush happened — the episode's whole point.

**Rename the states to disambiguate** — `VTC` for contact, `LTF` for filtration.
Rejected: still a Mechanica amendment, and it breaks the tie between the state and the
channel it names, which is the part that carries meaning.

**Leave it entirely alone.** Rejected: it is what let a Post-Mending envelope get
drafted without `LT`, the era's own signature state. The distinction needs to be in the
data, not only in the reader's head.

---

## 6. One drift found on the way

`canon_rules.json` glosses `MT` as `mortal_media_channel`. `MT_RULES.md`, Authoritative
Canon, defines it as **Mortal Technology** — "the human-built information and
communication layer," phones and infrastructure, not media as such. The JSON gloss is a
paraphrase that narrows it.

Worth correcting while the block is being edited. Small, but the gloss is what a future
reader will hit first.

---

## 7. For you to rule

1. Adopt the grouping in §3, or split after all?
2. Confirm the four rules in §4 as validator checks. Each is canon in prose already;
   this only makes them enforceable.
3. `VT` era gating: sealed until Tahl's breach, then available in every later era — or
   is it narrower than that?
4. Correct the `MT` gloss to Mortal Technology (§6)?
