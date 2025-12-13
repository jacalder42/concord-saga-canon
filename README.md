# Concord Saga Canon (Starter Template)

This repository is intended to store **non-prose** canon substrate for the Concord Saga:
- **/rules**: JSON rules, invariants, validation checks, trilogy envelopes
- **/canon**: Markdown canon explanations (tier-1 cards, codex, trilogy summaries)
- **/grids**: CSV grids (structure + telemetry)
- **/book_context**: per-book JSON context (skeletons initially)
- **/act_overlays**: per-act JSON overlays (skeletons initially)
- **/templates**: reusable templates for audits and bundles (generated artifacts should NOT be edited directly)

## Workflow
1. Update source files in /rules, /canon, /grids.
2. Generate compiled artifacts (Act Prose Bundles, Milestone Packets) into /templates or a separate /compiled folder.
3. **Do not** store prose, scene text, or dialogue here.

## Naming Conventions
- Book IDs: `B01`..`B09`
- Trilogy IDs: `T1` Veil, `T2` Neon, `T3` Loom
- Acts: `A1`..`A3`
- SIDs: `S1.T{trilogy}.B{book}.A{act}.E{episode}` (episodes live in grids, not filenames)

> NOTE: This is a starter scaffold. Replace TODO blocks deliberately; avoid freehand drift.
