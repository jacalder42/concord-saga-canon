# Lived-in Louisiana language: diagnosis and proposal

**Date:** 2026-10-05
**Status:** PROPOSAL, non-canonical. Written at the user's direction in chat: *"there needs to be more lived-in language
present. For a story based in New Orleans and filled with natives, there is stark lack of Cajun and Creole influence and
dialect."* Nothing here is approved until the author answers §6.

**What this does not change:** no manuscript text, card, rule, packet or profile line. The merged B01's numbers come from
the manuscript at `1a8be36`, by script. No manuscript prose is quoted.

## 1. Diagnosis: the page

The merged B01 has 173,456 words, with dialogue from more than 30 Louisiana-born speakers. Native speech carries almost
no regional marker.

| Marker class | Uses in the book |
| --- | ---: |
| Louisiana French address and exclamations (*cher/sha, mais, ça, nonc, tante, parrain, nannan, bébé, Mon Dieu*, and others) | **2** (one *chère*, one *Tante*) |
| Cajun-English calques (*make groceries, pass a good time, get down* out of a car, *save the dishes*, *envie*) | **0** (the 6 uses of *get down* are literal) |
| NOLA greetings and set phrases (*where y'at, yeah you right, how's your mama and them, for true, lagniappe*) | **0** |
| NOLA place and civic words (*neutral ground*, *go-cup*, *Uptown/Downtown*, *second line*) | 41. **This is the one layer that is present** |
| Southern and Black New Orleans address (*baby, honey, sugar, Lord, y'all, Miss/Mr.* + first name) | about 330, mostly *Miss Tavie*. **Present, but generic Southern** |
| Nonstandard grammar in elders' speech (*he don't*, *I'd broke*) | a handful |

**What a reader hears:** New Orleans as a set of street names, foods and courtesies, spoken in neutral American English.
The courtesy layer works. The *voice* layer (what people say, how they greet, what they call each other at home, the
French that survives in Louisiana English) is missing.

## 2. Root cause: the stack

1. **The author's own 2025 direction never reached drafting.** On 2025-11-10 he wrote:
   - *"Seraphine should be cajun, while the New Orleans group is creole"*;
   - *"take care with regional dialects… we want to sound like we have local cred, not like we just arrived on the bus
     full of tourists"*;
   - *"Concord is not Disney World."*

   Source: `recovery/FOREIGN_LANGUAGE_AND_CULTURAL_REGISTER_SOURCE_RECOVERY_2026-09-30.md` §2. Q-FL1–8 recovered the
   rules for *foreign* languages. The Cajun/Creole split for the *native* cast became one line on honorifics in §12A.
2. **§12A frames all non-English as an outsider's tell.** It says sparing, a permission at moments of stress or
   tenderness. That fits Lucien's German. It does not fit a Tremé elder, for whom Louisiana English *is* the everyday
   register. §12A's own line, *"A local's own words are not foreign to them,"* points the other way, but nothing operates
   on it.
3. **No B01 prose packet carries a speech-community note** for any local character. A grep of `ebci/prose/B01/` for
   *Cajun*, *Creole*, *dialect* and *Louisiana French* finds 0. The drafters were never told who sounds like what.
4. **The phonetic-spelling rule was right, but no replacement was given.** §12A bans eye dialect and says to carry a
   voice by "rhythm, word choice and forms of address", but no packet lists the word choices.

## 3. Proposed: speech communities in Veil

Each community gets its own variety. **No single group is the only one marked as nonstandard.**

| Community | Who, on the B01 page | The variety | Carried by |
| --- | --- | --- | --- |
| **Acadiana Cajun / Black Creole family** | **Seraphine** (card: Abbeville; page: Lafayette, an open card-versus-prose item). Her family's elders, off-page or by phone | Cajun English with Louisiana French residue | *Mais* as a discourse marker; *cher/sha* (invariable, to children, clients, family); family titles (*Nonc, Tante, Mawmaw, Parrain, Nannan*); calques (*make groceries, get down, save the dishes, pass a good time*); exclamations under pressure. **She code-switches:** E03 already gives her a "work voice". At work she is neutral; the register comes out at home, with elders, tired or afraid |
| **Downtown Black Creole and Black New Orleans** | Miss Tavie, Mrs. Arceneaux, Mrs. Toussaint, Mr. Vidrine, Miss Hazel, the Tremé and Seventh Ward elders, Trip, Inez (to confirm) | New Orleans English of the Tremé and Seventh Ward. **English, not Kouri-Vini:** Creole French survives in names, Catholic practice, food and a few family words, not in sentences | Greetings (*where y'at*, asking after *your mama and them*); *by* for someone's house; *making groceries*; family titles (*Nannan, Parrain, Tante*); church and saint's-day life (already present: St. Roch, red beans Mondays, whitewashed tombs); habitual and completive grammar. **Grammar only with a sensitivity read** (§4) |
| **Yat (white and Italian working-class New Orleans)** | Sal Ferrara (Sicilian on the page); candidates: Vernice, Clement, Mr. Benoit | Yat | *Where y'at*, *dawlin'*, *yeah you right*, *cap* (to a man), *making groceries*, *lagniappe*, *neutral ground*. This keeps the regional marking from falling only on Black characters |
| **Northshore and Honey Island family** | Odile, Renée, Lorraine (Metairie) | **To confirm.** Is Odile's family Cajun-descended or not? | Settles whether her *chère* (the feminine form) stays, or becomes Cajun-invariable *cher* |
| **Outsiders** | Lucien, Baz, Elisabet, Caro | Unchanged (their tells) | Their *hearing* of local speech is a POV tool (§12A, LR-10). Lucien may misparse a greeting; Baz translates it for someone; Caro (Chicago) hears it as foreign |

## 4. Guardrails

All of these are already in force or recovered from the author.

- **No phonetic spelling.** Not *dem*, *zinc* for sink, or *ax*. Spell words standard, and carry the voice by word choice,
  word order, address and rhythm (§12A; the author's 2025 rule).
- **Real usage only**: no invented blends (LR-5).
- **No tourist set**: no *laissez les bons temps*, *who dat* or voodoo color. *Concord is not Disney World.*
- **Function, not decoration.** Each use is a greeting, a form of address, an exclamation, a ritual, a calque of habit,
  or the way someone names a place. A sentence that carries plot is said in plain English (LR-7, §12A).
- **Readers get it at once** (author, 2025-11-30). Meaning comes from context or a reply, never a gloss.
- **Readers from the community** before anything is final, extending Q-FL6 and Q-FL8: Cajun French and Cajun English;
  Black New Orleans English; Yat. **This is required for any grammatical feature.** Nonstandard grammar on the page
  without that check risks the caricature the author ruled out (*"No one is a caricature"*, 2025-11-15).
- **No quotas** *(ruled)*. Density stays a review-side watch item (Q-FL2). The watch item here is the reverse of the
  outsiders': **a local speaker with several lines and no regional marker is the flag.**

## 5. How it would be applied

1. **The stack (for B02 onward):**
   - add a §12B *Louisiana speech* to the writer profile: the communities, the guardrails, and §12A's *"a local's own
     words are not foreign"* made operative;
   - add a speech-community line to each local character's identity context;
   - add a speech-community note to each prose packet with local speakers.
2. **The merged B01.** It can be done in one of three ways:
   - (a) a **dialogue pass** over native speakers' lines only. No scene, plot or line function changes; the pass works
     on word choice, greetings, address and calques. A reviewed diff and a per-character change log go to the author;
   - (b) a **pilot of three or four chapters** first, so the author can judge the level by ear. Suggested: one chapter
     each for Seraphine at home or with family, a Tremé elder, Sal, and Odile;
   - (c) wait for the line pass after the author's read.
3. **Readers from the community**, before the B01 changes go final.

## 6. Questions for the author (Q-LL)

- **Q-LL1. Adopt the four-community map in §3?** (a) As proposed. (b) Change it. Seraphine's strand reads the 2025 line
  (*"Seraphine should be cajun"*) together with the 10-01 Q-FL4 answer (*"both registers, mostly forms of address"*), as
  Cajun-dominant with Black Creole family. Confirm or correct.
- **Q-LL2. How far, for B01?** (a) Lexical: address, greetings, exclamations, calques, set phrases. (b) Lexical plus
  word order and rhythm. (c) Lexical plus grammar (habitual and completive forms), only after a community reader.
- **Q-LL3. When, for B01?** (a) A pilot of 3–4 chapters now. (b) A full dialogue pass now. (c) At the line pass after
  the read. (d) B02 onward only.
- **Q-LL4. The stack:** add profile §12B and the packet notes now? (a) Yes. (b) After the pilot.
- **Q-LL5. Readers from the community:** (a) Commission them before B01 is final. (b) At the publication copyedit.
