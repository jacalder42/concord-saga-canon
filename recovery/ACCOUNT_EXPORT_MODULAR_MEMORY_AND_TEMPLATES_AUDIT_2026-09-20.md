# Account Export Audit — Modular Memory System + Project Memory Templates

Status: RECOVERY / SOURCE AUDIT — NON-CANONICAL  
Date audited: 2026-09-20

Sources:
- `2025-12-12__Modular_memory_system_design__693c11db`
  - ID `693c11db-2468-832f-b50d-3b31a838e32c`
  - 98 turns / 39,692 words
- `2025-12-12__Project_memory_templates__693c0db7`
  - ID `693c0db7-8408-832e-8921-8f84339ada12`
  - 4 turns / 1,309 words

## Executive finding

These two conversations are the architectural bridge between the Dec. 10 Character Vault,
the Dec. 12 compression work, and the Dec. 13 GitHub/source-canon architecture.

They establish the durable principle:

**external canon is authoritative; ChatGPT memory is a working cache / operating spine.**

The longer Modular Memory conversation then stress-tests several implementations and
corrects its own early assumptions. Its final useful architecture is not “hot-swap giant
memory sets,” but:

- small persistent governance/invariant memory;
- external canonical storage;
- directive prompts that tell a work chat how to use loaded material;
- trilogy-scale EBCI workspaces for longitudinal comparison;
- book-scale workspaces for scene-level beats;
- downstream prose tools fed derived book/scene packets.

This is the conceptual ancestor of the later GitHub manifest/context architecture.

## 1. Project Memory Templates source

The four-turn source proposes five loadouts:

- Character Generation
- Structural / Plot Architecture
- Visual & Prompt Engineering
- Editorial / Analysis
- Prose Execution

It explicitly says:

> Project Memory ≠ Canon Archive  
> Project Memory = Active Working Set

and:

> Your canon lives externally.

### Disposition

**CURRENT / HISTORICAL ARCHITECTURE.**

The exact hot-swap mechanism is obsolete, but the separation of durable canon from active
reasoning context remains sound.

## 2. Scope separation produced the Modular Memory chat

The author correctly decides that memory-system design should move to a separate chat so
the current Character Vault can remain focused on character/faction cards.

The assistant generates the opening prompt for the new Systems Architect chat.

### Disposition

**PROCESS PROVENANCE.**

This directly explains why the Dec. 12 Modular Memory conversation exists.

## 3. External authority

The Modular Memory prompt itself says:

> Treat all canon as externally authoritative.

The assistant repeatedly converges on:

> External is authoritative; memory is a cache.

### Disposition

**CURRENT / CONFIRMED PROJECT PHILOSOPHY.**

Later GitHub architecture is the implementation of this principle.

## 4. Early “Frame Rooms” idea is superseded

The conversation explores separate chats as persistent Frame Rooms, then the author points
out the model cannot actually see those chats unless information is in memory/re-prompted.

The architecture is corrected toward:
- directive prompts;
- small memory spine;
- externally loaded material.

### Disposition

**SUPERSEDED IMPLEMENTATION / USEFUL PROCESS HISTORY.**

Do not revive “separate chats are authoritative memory modules.”

## 5. Trilogy → book workflow

The author explicitly proposes:

- separate EBCI chat for each trilogy so episodes can be compared across the trilogy arc;
- then each book gets its own chat for scene-level beats;
- scene beats then migrate to NovelCrafter / Sudowrite / etc.

The assistant agrees.

### Disposition

**HIGH-VALUE WORKFLOW PROVENANCE.**

This matches the later backup-chat strategy and explains why trilogy visibility was
considered important before splitting into books.

The modern repo/context system may reduce dependence on separate chats, but the
**reasoning scope** remains valuable:
trilogy for longitudinal EBCI coherence; book for execution detail.

## 6. What memory should contain

The source converges on a small stable spine:
- canon governance;
- invariant rules;
- identifier/schema definitions;
- how to interpret loaded context.

It rejects permanent memory storage of:
- full character bios;
- episode inventories;
- long canon cards;
- prose;
- large evolving matrices.

### Disposition

**CURRENT / CONFIRMED IN PRINCIPLE.**

The modern GitHub substrate is a better external implementation than the Notion-heavy
options considered in December.

## 7. Book bundle concept

The long source develops the idea that each book should have one authoritative context
bundle for prose generation, derived from higher-level canon rather than becoming a new
canon store.

### Disposition

**TRANSFERABLE / CURRENT.**

This maps well to current book contexts + manifests/derived packets.

The bundle should be generated from the substrate, not hand-maintained as a competing
authority.

## 8. Product/tool claims are historical

The conversation contains extensive discussion of then-current ChatGPT, Notion,
NovelCrafter, Sudowrite and context-window capabilities.

### Disposition

**PROCESS / SUPERSEDED WHERE PRODUCT-SPECIFIC.**

Do not treat 2025 product limitations as durable project rules.

## 9. Important connection to current recovery

These sources explain why the project accumulated multiple representations of the same
canon:
- full source;
- memory-safe card;
- EBCI packet;
- book bundle;
- prose packet.

Those are **different views for different tasks**, not automatically conflicting canon
generations.

During line review, classify an artifact by purpose before interpreting omissions.

## 10. Provenance tags reinforced

Use:
- FULL_SOURCE
- AUTHOR_ADJUDICATED
- DERIVED_TIER1
- MEMORY_SAFE_COMPRESSION
- CONTEXT_BUNDLE
- TEMPORAL_IMPLEMENTATION
- LATER_RULING

This prevents a one-page execution card from outranking the source it compressed.

## 11. Next source

Proceed to:
`2025-12-10__Character_Vault_Chat__6938daf6`

This is a major source:
- 672 turns;
- 296,996 words;
- primary-character 7-bundle material;
- antagonist packs;
- interaction chemistry;
- appearance/VFX;
- backstory/origin packages;
- repeated micro-audits and canon integration.

Because of its size, review it by **character/topic strata**, not as one undifferentiated
conversation.

Recommended pass order:
1. vault structure/provenance;
2. Seraphine/Lucien/Caro control cases;
3. Baz/Tahl;
4. Elisabet/Rex/Kade/Lacuna/Trip;
5. antagonists;
6. cross-character relationship/narrative assets;
7. drift/conflict index.

END AUDIT
