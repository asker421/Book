# V4 Independent Red-Team Audit

## Scope and source of truth

- Repository: `asker421/Book`
- Branch: `main`
- Start SHA fixed before reading: `273acaa9e479ae58d32459a3896ca14a678ef3e5`
- Audited artistic corpus: `chapters_v4/`
- Reading order: 01 → 02 → 03 → 04 → 04a → 05 → 06 → 07 → 08 → 08a → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 15a → 16 → 17 → 18 → 19 → 20 → 21 → 22 → 22a → 23 → 24 → 25 → 26 → 27 → 28 → 29 → 30
- Full files read: **34/34**
- Final audited artistic line count: **13,845**
- Previous audits / PASS files / worklogs were not used as evidence.

## Per-file ledger

| FILE | Lines | Continuity | Reaction | Asgar-name tic | Findings |
|---|---:|---|---|---|---|
| 01.md | 231 | PASS | PASS | FIXED (1) | redundant second «Асгар» in final phone-booth paragraph |
| 02.md | 443 | PASS | PASS | FIXED (1, concurrent; verified) | «Асгар ухватился за перила» → zero subject; full reread after main drift |
| 03.md | 355 | PASS | PASS | PASS | — |
| 04.md | 433 | PASS | PASS | PASS | — |
| 04a.md | 97 | PASS | PASS | PASS | — |
| 05.md | 569 | PASS | PASS | PASS | — |
| 06.md | 457 | PASS | PASS | PASS | — |
| 07.md | 559 | FIXED | PASS | PASS | callback contradicted 01.md: he had already asked the older man if he was okay |
| 08.md | 637 | PASS | PASS | FIXED (1) | «Асгар поднял руку…» → «Он поднял руку…» |
| 08a.md | 75 | PASS | PASS | PASS | — |
| 09.md | 537 | PASS | PASS | FIXED (1) | second «Асгар рассказал…» → «Он рассказал…» |
| 10.md | 551 | PASS | PASS | PASS | — |
| 11.md | 553 | PASS | PASS | PASS | — |
| 12.md | 465 | PASS | PASS | PASS | — |
| 13.md | 543 | PASS | PASS | PASS | — |
| 14.md | 269 | PASS | PASS | PASS | — |
| 15.md | 305 | PASS | PASS | FIXED (1) | «Асгар вернул трубку…» → zero subject |
| 15a.md | 271 | PASS | PASS | PASS | — |
| 16.md | 289 | PASS | PASS | PASS | — |
| 17.md | 337 | PASS | PASS | PASS | — |
| 18.md | 459 | PASS | PASS | PASS | — |
| 19.md | 479 | PASS | PASS | PASS | — |
| 20.md | 477 | PASS | PASS | PASS | — |
| 21.md | 659 | PASS | PASS | PASS | — |
| 22.md | 561 | PASS | PASS | PASS | — |
| 22a.md | 59 | PASS | PASS | PASS | — |
| 23.md | 383 | PASS | PASS | PASS | — |
| 24.md | 471 | PASS | PASS | PASS | — |
| 25.md | 391 | PASS | PASS | PASS | — |
| 26.md | 477 | PASS | PASS | PASS | — |
| 27.md | 329 | PASS | PASS | PASS | — |
| 28.md | 625 | PASS | PASS | FIXED (1) | second exact beat «Асгар посмотрел на узел» removed |
| 29.md | 267 | PASS | PASS | PASS | — |
| 30.md | 232 | PASS | PASS | FIXED (1) | second «Асгар провёл…» → zero subject |

## Objective continuity / knowledge / reaction findings

### RT-001 — FIXED — continuity / callback

- File: `chapters_v4/07.md`
- Pre-fix line: 465
- Pre-fix text: `Асгар вспомнил, как отступил, освобождая ему дорогу. Мог спросить, нужна ли помощь. Мог задержать на несколько секунд.`
- Conflict source: `chapters_v4/01.md` already contains `— Вам нормально? — крикнул Асгар.`, followed by the older man raising a hand and Asgar explicitly telling Katya that he called out and the man signaled he was okay.
- Why objective: chapter 7 framed asking whether help was needed as an unrealized action, but the action had already occurred on-page.
- Fix: `Мог спросить, нужна ли помощь.` → `Мог подойти, убедиться, что помощь не нужна.`
- Recheck: PASS against chapters 01 and 30.

No other unresolved continuity, knowledge-state, reaction, POV, reveal-order, physical-state, or time/age defect was found in the final corpus.

## Asgar-name / authorial automation fixes

Final corpus contains **7 verified reductions of redundant “Асгар” / repeated Asgar action beats** during this audit window:

1. `01.md`: second redundant `Асгар` in the final phone-booth paragraph → pronoun / zero-subject construction.
2. `02.md`: `Асгар ухватился за перила.` → `Ухватился за перила.` This change arrived concurrently on `main`; the whole file was reread and the change was verified.
3. `08.md`: `Асгар поднял руку ей навстречу.` → `Он поднял руку ей навстречу.`
4. `09.md`: second `Асгар рассказал…` in the same paragraph → `Он рассказал…`.
5. `15.md`: `Асгар вернул трубку на рычаги.` → `Вернул трубку на рычаги.`
6. `28.md`: duplicate action beat `Асгар посмотрел на узел.` repeated a few lines later → second beat removed.
7. `30.md`: second `Асгар провёл по ней ладонью…` in the same paragraph → zero-subject construction.

No chapter contained a cluster of multiple confirmed name-tic defects after contextual review; the confirmed fixes were singletons. Raw name frequency was highest in chapters 08, 21, 13, 09/28 and 19, but raw frequency was not treated as evidence of a tic when names were needed for male-subject disambiguation or focus recovery.

## Physical-state ledger result

PASS after full read and final cross-check:
- phone / documents tracked;
- Ar bag tracked;
- Bertram tool tracked;
- Tobin figure tracked;
- right-knee injury persists and later resolves;
- left-eyebrow scar has an on-page cause and remains;
- later left-ankle injury / cautious gait remains consistent into the stadium return;
- hair / beard / weight loss are causally developed during the long isolation;
- items left at the Source before the 2014 opening do not reappear on Asgar in the stadium scene;
- Keeper’s black monitoring band remains on Asgar and is covered by the sleeve before the 2014 contact.

## RETRO-1 / reveal-order result

PASS:
- autonomous module;
- service interior;
- phone as service channel;
- passenger not intended;
- full mass reconciliation after door closure;
- intermediate exits do not close passenger record;
- Emergency Support physically on Earth in 2744;
- Mirena receives service telemetry / voice but does not see the external world;
- no direct channel from Support to Source;
- Source is the receiving node in the Solar System, not Earth;
- historical addressing uses real prior RETRO-1 contact states, not arbitrary calendar selection;
- causal loop is not fully explained before chapter 29;
- chapter 29 reconciles independent physics development with RETRO-1’s historically inherited concrete configuration.

## Mandatory adversarial rechecks

- `01 ↔ 30`: **PASS** — exit posture, young Asgar stepping aside, eye contact, cautious gait, look back at booth, `Вам нормально?`, raised hand, turn behind corner, and young Asgar’s entry align.
- `08 ↔ 30`: **PASS** — older Asgar appears physically outside the booth in the 2039 hall; spatial stretching, silent intercom, Katya’s door movement, reaching hands, table bleed-through and disappearance align from both POVs.
- `22 ↔ 29`: **PASS** — empty module, service volume, post-closure mass check, persistent passenger record and return-to-source model remain consistent.
- `27 ↔ 29`: **PASS** — historical addressing is introduced as reuse of a real previous contact and is not upgraded into arbitrary date selection.
- `29 ↔ 30`: **PASS** — 2014 opening uses the stated limited common geometry; subsequent 2039 contact follows available historical states; after failure, RETRO-1 closes its return and the ending accelerates without a new workaround branch.
- Callbacks checked: `Тогда не тяни…` and `просто сидели, разговаривали` both have prior on-page sources.
- Exact banned old motif `Не входи`: **absent**. The unrelated grammatical forms `Не входите` / `не входить` were not treated as the removed motif.
- Removed old canon names/elements checked: **absent** in the artistic corpus.
- Required last line: **PASS** — `Асгар смотрел на неё ещё несколько секунд.`

## Main drift handling

During the audit `main` advanced several times. Each drift was compared against the last audited head:
- CI-only changes to `.github/latest_v4_release_run.txt` were inspected.
- A later one-line change to `chapters_v4/02.md` was detected; `02.md` was reread in full and re-audited before continuing.
- No unreviewed artistic-file drift remained at ledger preparation.

## Final status at ledger preparation

- Chapters closed: **30/30**
- Interludes closed: **4/4**
- Objective continuity/knowledge/reaction defects found: **1**
- Objective continuity/knowledge/reaction defects unresolved: **0**
- Verified Asgar-name/action-tic fixes: **7**
- CRITICAL unresolved: **0**
- MAJOR unresolved: **0**
- Final adversarial recheck: **PASS**

The final repository SHA must be read after committing this ledger because including the ledger itself changes `main`.
