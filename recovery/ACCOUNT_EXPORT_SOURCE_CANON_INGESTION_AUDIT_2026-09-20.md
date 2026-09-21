# Account Export Audit — Source Canon Ingestion Process

Status: RECOVERY / SOURCE AUDIT — NON-CANONICAL  
Date audited: 2026-09-20  
Source: `2025-12-14__Source_canon_ingestion_process__693ef473`  
Conversation ID: `693ef473-8b4c-83a8-a2f6-a43df5a38b22`  
Created: 2025-12-14  
Turns: 260  
Words: 78,633  
Source archive: author-supplied 2026-09-15 account-export TAR

## Executive finding

This conversation clarifies an important ambiguity but does **not by itself resolve** the
current `source_canon/` authority conflict.

The December conversation uses “source canon” as a **workflow concept**: authoritative raw
character materials are audited, conflicts are explicitly adjudicated, and distilled
Tier-1 GitHub files are produced. It does **not** establish the present
`source_canon/` directory as an authoritative repository layer.

In fact, the workflow repeatedly distinguishes:

1. raw source material that may contain multiple incompatible “FINAL CANON” labels;
2. an explicit precedence ruling by the author;
3. lossless consolidation / derived canon;
4. GitHub-ready Tier-1 output.

That is broadly compatible with the current repository rule that a source/archive location
is not automatically authority.

The internal stamp `FINAL CANON · LOSSLESS · EXPORT READY` in
`source_canon/characters/seraphine_full.md` therefore cannot be promoted solely from its
label. Its provenance and relation to the actual author-adjudicated Seraphine source set
still need to be established.

## 1. Opening workflow rule

The conversation begins with a strict ingestion posture:

- attached TXT files are treated as authoritative raw source material;
- no silent invention;
- conflicts are surfaced before consolidation;
- no canon files are produced until explicitly instructed.

### Disposition

**CURRENT / CONFIRMED PROCESS PRINCIPLE.**

This is essentially the ancestor of the current recover → reconcile → promote workflow.

## 2. “Authoritative raw source” did not mean every statement was canon

The first Lucien audit immediately finds incompatible source packages:
- multiple parent sets;
- sibling-status variance;
- district variance;
- class variance;
- multiple files self-labeled FINAL.

The assistant explicitly identifies a:

> “FINAL CANON” LABEL COLLISION — PROCESS CONFLICT

and refuses safe consolidation without a precedence rule.

### Disposition

**CRITICAL PROVENANCE FINDING.**

In December usage, “authoritative raw source material” means **the authoritative evidence
set to audit**, not “every line in every attached file is simultaneously governing canon.”

This is directly relevant to the modern `source_canon/` ambiguity.

## 3. Author adjudication created authority inside the source set

For Lucien, the author rules:

> “backstory file takes precedence. then review again for conflicts”

The assistant then records:

> Backstory_Lucien.txt takes full authority over all other Lucien source files.

Other self-declared FINAL labels are explicitly neutralized as:
- derived;
- subordinate;
- non-authoritative.

### Disposition

**CURRENT / CONFIRMED AUTHORITY MECHANISM.**

The decisive authority is the author's precedence ruling, not the presence of “FINAL
CANON” text inside a source artifact.

## 4. Derived canon vs source authority

The Lucien romance pack is accepted as:

> derived canon, not source authority.

The workflow repeatedly distinguishes:
- source authority;
- derived canon;
- output canon.

### Disposition

**CURRENT / HIGH-VALUE TERMINOLOGY RECOVERY.**

This supports maintaining separate provenance fields during line review rather than
flattening all recovered material into one canon tier.

## 5. “Lossless” has a specific historical meaning

The conversation uses “lossless” for consolidation/output that preserves all approved,
non-conflicting information from the adjudicated source set.

It does **not** mean:
- all historical variants remain active;
- every raw statement is canon;
- a file stamped LOSSLESS overrides later rulings.

### Disposition

**CURRENT / CLARIFYING.**

“LOSSLESS” is a fidelity claim about the approved source state at the time of export, not
a timeless authority claim.

## 6. “FINAL CANON” is explicitly shown to be unsafe metadata

The conversation repeatedly encounters multiple incompatible blocks labeled:
- FINAL CANON;
- TIER-1 FINAL;
- END — FINAL.

For Lucien, Baz, Caro, Elisabet and Rex, the workflow has to inspect duplication and
variant strata rather than trust those labels mechanically.

### Disposition

**CURRENT / CONFIRMED.**

This is strong evidence against resolving the present Seraphine `source_canon/` conflict
by reading the words “FINAL CANON” alone.

## 7. What the December workflow actually outputs

The conversation's intended destination is consistently:
- `canon/characters/`
- `canon/pov/`
- GitHub-ready Tier-1 character files.

For Lucien it produces/targets:
- Identity
- POV
- EBCI
- Appearance
- Render

The conversation does **not** describe a `source_canon/` directory lifecycle.

### Disposition

**NEW RECOVERY / IMPORTANT NEGATIVE EVIDENCE.**

The modern `source_canon/` directory appears to be a later repository architecture, not
the repository layer being defined by this December conversation.

Therefore this source cannot be used to claim that the current directory was intended to
be authoritative.

## 8. Seraphine's role in this conversation

Seraphine is initially used as the reference implementation for the desired Tier-1 output.

The author supplies raw GitHub links to Seraphine Appearance, EBCI, Render and later POV
files as structural targets for Lucien.

### Disposition

**CURRENT / HISTORICAL PROVENANCE.**

This shows that by December 14, Seraphine already had a richer canonical implementation
that served as the template for other Tier-1 characters.

It also explains why the present repo's missing Seraphine EBCI is suspicious and worth
recovery.

## 9. Current `source_canon/seraphine_full.md` conflict

Current repository state:

`source_canon/README.md` says:
- NON-AUTHORITATIVE;
- redundancy/contradiction allowed;
- Extract → Reason → Distill → Archive/Discard.

But `source_canon/characters/seraphine_full.md` contains internal block stamps such as:

> FINAL CANON · LOSSLESS · EXPORT READY

### What this source resolves

It resolves the **semantic interpretation**:
- “FINAL CANON” labels inside historical artifacts are not self-authenticating;
- “LOSSLESS” does not override later author rulings;
- source materials can contain incompatible FINAL labels;
- explicit author precedence + distilled Tier-1 output is the actual promotion mechanism.

### What this source does NOT resolve

It does not establish:
- when `seraphine_full.md` was created;
- which raw Seraphine files it consolidated;
- whether its blocks exactly represent the author-adjudicated Seraphine state;
- whether it was intentionally placed in `source_canon/` as a temporary source after
  later repo restructuring;
- whether every fact in it remains compatible with current Seraphine Tier-1 files.

### Disposition

**AUTHORITY CONFLICT NARROWED, NOT CLOSED.**

Do not promote `seraphine_full.md` wholesale.

Instead, audit it fact-by-fact against:
1. the full historical Seraphine source conversation(s);
2. current `canon/characters/SeraphineIdentity.md`,
   `SeraphineAppearance.md`, and `SeraphineRender.md`;
3. later explicit author rulings.

## 10. Identity-file construction problems are visible in this source

The latter part of the conversation shows repeated correction cycles:
- Caro ID initially generalized/invented details and had to be rebuilt;
- Elisabet ID was under-resolved and revised;
- Rex required explicit author authorization before inventing missing details;
- the Tahl ID file became the schema reference.

### Disposition

**HIGH-VALUE PROCESS WARNING.**

A file can be structurally Tier-1 and still contain extraction errors.

Therefore current Tier-1 files deserve respect as governing substrate, but their historical
provenance should still be audited where known conflicts exist.

## 11. Caro provenance warning

This source is especially useful for Caro because it documents a failed ID pass followed
by correction.

Historical names/packages inside the conversation include multiple Caro identity attempts
before the corrected output.

### Disposition

**RECOVERY LEAD.**

When Caro receives a dedicated line review, use the final corrected author/source-backed
pass, not earlier generated IDs from the same conversation.

## 12. Lucien provenance is unusually strong

Lucien receives:
- explicit source conflict audit;
- direct author precedence ruling;
- second conflict audit after ruling;
- worldview sanity check;
- POV construction;
- EBCI;
- Appearance;
- Render;
- compatibility review.

Current `canon/characters/LucienID.md` closely preserves the adjudicated identity package:
- Vienna / Alsergrund;
- Adélie Mercier-Kael;
- Karl Kael;
- Elena;
- upper-middle academic household.

### Disposition

**CURRENT / CONFIRMED.**

Lucien is a strong candidate for a “migration succeeded” control case when comparing
historical source → current Tier-1.

## 13. Recommended authority model after this audit

For this December ingestion generation, interpret evidence as:

**A. explicit author ruling in conversation**
→ controls conflicts.

**B. adjudicated source file/block**
→ authoritative for the scoped character fact set at that date.

**C. generated Tier-1 output verified against A/B**
→ intended GitHub canon artifact.

**D. derived canon**
→ valid only within its approved scope and cannot silently override A/B.

**E. raw variant / self-labeled FINAL block without precedence**
→ historical evidence, not governing merely because of its label.

This model is compatible with the present repository's broader authority rules.

## 14. Immediate action

No Tier-1 canon rewrite is warranted from this audit alone.

Recommended follow-up:
1. keep `source_canon/` unresolved at directory level for now;
2. stop treating the internal `FINAL CANON` stamp as evidence that
   `seraphine_full.md` overrides the README;
3. add a targeted **Seraphine provenance audit** to the work queue;
4. locate the historical Seraphine construction source(s) in the 72-conversation corpus;
5. compare their adjudicated output line-by-line against `seraphine_full.md` and current
   Tier-1 Seraphine files;
6. recover the missing Seraphine EBCI only after that comparison.

## 15. Next source

Next recommended audit:

`2025-12-13__System_memory_backup_export__693e5...` (exact archive ID to be taken from
the TAR inventory).

Why:
- it immediately precedes the December canon-ingestion work;
- it should reveal what project memory was believed to contain before Tier-1 extraction;
- it may identify source conversations/files for Seraphine and other systems;
- it is likely to clarify which assets were being backed up because they were vulnerable.

END AUDIT
