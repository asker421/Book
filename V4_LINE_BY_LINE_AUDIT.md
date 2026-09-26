# V4 LINE-BY-LINE AUDIT — «Красная будка»

## Baseline
- Branch: `main`
- Frozen audit baseline: `d93e87211c98563ea551492aef771d0de1e20e86`
- Corpus: `chapters_v4/`, 30 chapters + 4 interludes.
- Previous PASS statuses are ignored for this audit.

## Rule
Every narrative statement, thought and line of dialogue is checked as potentially wrong until supported by the text already available to that POV/character.

Checks:
1. knowledge provenance;
2. future/other-POV leakage;
3. unsupported memory/callback;
4. repeated discovery of known facts;
5. ordinary first reaction / natural dialogue;
6. character voice/motivation;
7. body/object/injury/time/location continuity;
8. RETRO-1 capability/reveal order;
9. accidental author omniscience;
10. prose logic / sentence-level absurdity.

## Status

| File | Status | Findings |
| --- | --- | --- |
| 01.md | PASS | 232 lines: young-Asgar reactions mundane; older-Asgar seed observational only; no future knowledge |
| 02.md | PASS | 443 lines: date/disappearance verified through phone, Katya, guard, records; Katya/Rauf stay evidence-bounded |
| 03.md | PASS | 355 lines: CCTV provenance and memory contamination handled explicitly; no overclaim from enhanced image |
| 04.md | PASS | 433 lines: family/Rauf responses risk-first and ordinary; no mechanism knowledge beyond phone statements |
| 04a.md | PASS | 98 lines: service discovers passenger only post-close; older-man trace remains unresolved |
| 05.md | PASS | 569 lines: entry decision voluntary and contested; 2039 disbelief/verification sequence is mundane |
| 06.md | PASS | 458 lines: ordinary identity recovery; institutional verification precedes acceptance; memories self-contained |
| 07.md | FIXED | 559 lines: unsupported stadium callback replaced with exact established Ch1 line; post-fix local reread PASS |
| 08.md | PASS | 638 lines: Katya/service reactions stay knowledge-bounded; 2039 hook uses observable geometry only |
| 08a.md | PASS | 76 lines: model-side knowledge sourced from telemetry and Asgar's report; no purpose/identity leak |
| 09.md | PASS | 537 lines: post-fix memory provenance clean; doctor/Inessa remain evidence-bounded |
| 10.md | PASS | 551 lines: Martin labels hypotheses and provenance; no causal overclaim or future-knowledge leak |
| 11.md | PASS | 553 lines: routines/memories grow on-page; archive-work dialogue preserves exact-speech discipline |
| 12.md | PASS | 465 lines: safety/evacuation and entry decision remain voluntary; source terminology already established |
| 13.md | PASS | PASS | Local first contact, calendar verification and survival reactions remain mundane; right-knee injury tracked |
| 14.md | PASS | PASS | Local route/safety knowledge is earned; temporal-anomaly label comes only from machine protocol |
| 15.md | PASS | PASS | Protocol provenance investigated on-page; identity/cause/purpose remain explicitly unknown |
| 15a.md | PASS | PASS | Mirena handoff is explicit; Asgar-reported facts retain attribution; operator cannot choose for him |
| 16.md | PASS | PASS | Mirena knowledge fully sourced by handoff/service telemetry/Asgar report; external scene remains invisible to her |
| 17.md | PASS | PASS | Arved/Tayra first-contact reactions are risk-first and skeptical; no genre acceptance |
| 18.md | PASS | PASS | Sayma separates prior testimony, source chain, retelling and hypothesis; remembered water exchange traced to Ch1 |
| 19.md | PASS | 480 lines: integration/conflict/accident reactions mundane; unexplained utility fault not blamed on Asgar |
| 20.md | PASS | 477 lines: separation option presented neutrally; Mirena refuses to choose for him; Asgar's choice is earned |
| 21.md | PASS | PASS | arrivals office and Tessa explicitly separate Asgar claims from measurements/model; endpoint and return purpose remain unknown |
| 22.md | PASS | PASS | Project-purpose reveal is sourced from newly raised project archive; Mirena admits prior ignorance; conflict remains human |
| 22a.md | PASS | PASS | Similar pre-close signal grouped statistically only; older man remains unidentified; Asgar report kept separate |
| 23.md | PASS | PASS | Tessa/Asgar explicitly correct overstatement about finished separation; source uncertainty and service limits preserved |
| 24.md | PASS | PASS | Olmer verifies local facts first; Asgar identifies provenance of every RETRO claim; Baku memories are self-contained |
| 25.md | PASS | 391 lines: red-form lineage explicitly separated from physics/provenance; archive prevents desired inference |
| 26.md | PASS | 477 lines: survival continuity coherent; stadium-self hypothesis remains contaminated/uncertain and first description is preserved |
| 27.md | PENDING | — |
| 28.md | PENDING | — |
| 29.md | PENDING | — |
| 30.md | PENDING | — |

## Findings log

- 01–05 + Interlude I: full literal line pass completed; no objective defect found.

- Ch7 defect fixed: invented recalled quote «Главное — чтобы ты приехал» had no prior textual source; replaced with established Ch1 quote «Тогда не тяни. И воду не забудь, пожалуйста».

- Ch9–12: literal line pass completed; no new objective defect found.

- Ch13–15 + Interlude III: full literal line pass completed; no objective defect found.

- Ch16–18: full literal line pass completed; suspicious Ch18 water callback verified against Ch1 and is genuine.

- Ch16–20: full literal line pass completed; no objective defect found.

- Ch19–21: full literal line pass completed; no objective defect found.

- Ch22–24 + Interlude IV: full literal line pass completed; no objective defect found.

- Ch21–26 + Interlude IV: full literal line pass completed; no objective defect found.
