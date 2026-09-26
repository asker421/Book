# V4 Independent Red-Team Audit

## Scope and source of truth

- Repository: `asker421/Book`
- Branch: `main`
- Start SHA fixed before reading: `273acaa9e479ae58d32459a3896ca14a678ef3e5`
- Artistic-corpus SHA after all audited prose fixes, before ledger-only commits: `1c1529db6fb1e200ef89e82e0ecd98ba27ec8615`
- Audited artistic corpus: `chapters_v4/`
- Reading order: 01 → 02 → 03 → 04 → 04a → 05 → 06 → 07 → 08 → 08a → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 15a → 16 → 17 → 18 → 19 → 20 → 21 → 22 → 22a → 23 → 24 → 25 → 26 → 27 → 28 → 29 → 30
- Full files read: **34/34**
- Final audited physical line count: **13,845** (blank lines included; terminal split pseudo-line excluded)
- Previous audits / PASS files / worklogs were not used as evidence.
- Every artistic file changed during this audit was reread in full after its edit: **01, 02, 07, 08, 09, 15, 28, 30**.

## Per-file ledger

| FILE | Lines | Continuity | Reaction | Asgar-name tic | Findings |
|---|---:|---|---|---|---|
| 01.md | 231 | PASS | PASS | FIXED (1) | redundant repeated name removed in phone-booth paragraph |
| 02.md | 443 | PASS | PASS | FIXED (1) | `Асгар ухватился за перила.` → zero subject |
| 03.md | 355 | PASS | PASS | PASS | — |
| 04.md | 433 | PASS | PASS | PASS | generic safety wording `Не входите` is not the removed old motif `Не входи` |
| 04a.md | 97 | PASS | PASS | PASS | — |
| 05.md | 569 | PASS | PASS | PASS | — |
| 06.md | 457 | PASS | PASS | PASS | — |
| 07.md | 559 | FIXED | PASS | PASS | callback contradicted chapter 01: Asgar had already asked the older man whether he was okay |
| 08.md | 637 | PASS | PASS | FIXED (1) | redundant `Асгар поднял руку…` → `Он поднял руку…` |
| 08a.md | 75 | PASS | PASS | PASS | — |
| 09.md | 537 | PASS | PASS | FIXED (1) | second same-paragraph `Асгар рассказал…` → `Он рассказал…` |
| 10.md | 551 | PASS | PASS | PASS | — |
| 11.md | 553 | PASS | PASS | PASS | — |
| 12.md | 465 | PASS | PASS | PASS | — |
| 13.md | 543 | PASS | PASS | PASS | right-knee injury origin confirmed |
| 14.md | 269 | PASS | PASS | PASS | right-knee injury continuity confirmed |
| 15.md | 305 | PASS | PASS | FIXED (1) | `Асгар вернул трубку…` → zero subject |
| 15a.md | 271 | PASS | PASS | PASS | — |
| 16.md | 289 | PASS | PASS | PASS | — |
| 17.md | 337 | PASS | PASS | PASS | — |
| 18.md | 459 | PASS | PASS | PASS | right-knee residual stiffness confirmed |
| 19.md | 479 | PASS | PASS | PASS | left-eyebrow scar origin confirmed |
| 20.md | 477 | PASS | PASS | PASS | item transfer into bag / jacket tracked |
| 21.md | 659 | PASS | PASS | PASS | — |
| 22.md | 561 | PASS | PASS | PASS | RETRO-1 task / passenger-state reveal order holds |
| 22a.md | 59 | PASS | PASS | PASS | — |
| 23.md | 383 | PASS | PASS | PASS | callbacks verified against prior on-page sources |
| 24.md | 471 | PASS | PASS | PASS | — |
| 25.md | 391 | PASS | PASS | PASS | bag contents and new field kit tracked |
| 26.md | 477 | PASS | PASS | PASS | scar / ageing / self-recognition continuity holds |
| 27.md | 329 | PASS | PASS | PASS | historical addressing introduced as prior real contact, not arbitrary date selection |
| 28.md | 625 | PASS | PASS | FIXED (1 action-beat repetition) | second exact beat `Асгар посмотрел на узел.` removed |
| 29.md | 267 | PASS | PASS | PASS | Source / passenger record / loop reveal order holds |
| 30.md | 232 | FIXED | PASS | FIXED (1) | right-knee gait continuity corrected in two loci; one redundant name removed |

## Objective continuity / knowledge / reaction findings

### RT-001 — FIXED — continuity / callback

- File: `chapters_v4/07.md`
- Pre-fix line: 465
- Pre-fix text: `Асгар вспомнил, как отступил, освобождая ему дорогу. Мог спросить, нужна ли помощь. Мог задержать на несколько секунд.`
- Conflict source: `chapters_v4/01.md` already contains `— Вам нормально? — крикнул Асгар.`, followed by the older man raising a hand and young Asgar explicitly telling Katya that he called out and the man signaled he was okay.
- Why objective: chapter 7 framed asking whether help was needed as an unrealized action, but that action had already happened on-page.
- Exact fix: `Мог спросить, нужна ли помощь.` → `Мог подойти, убедиться, что помощь не нужна.`
- Recheck: PASS against chapters 01 and 30.

### RT-002 — FIXED — physical continuity / gait

- File: `chapters_v4/30.md`
- Pre-fix loci: lines 21 and 43.
- Pre-fix text: `Левая ступня легла осторожнее правой.` and `Левая нога отзывалась осторожностью, накопленной за два года пути…`
- Conflict source:
  - `13.md`: fall and abrasion are explicitly on the **right knee**; Asgar later keeps weight on the left and extends the right leg.
  - `14.md`: the **right knee** hurts more after the platform incident.
  - `15.md`: the **right leg** is still being pulled under the bandage.
  - `18.md`: the **right leg / knee** still stiffens after sitting.
- Why objective: chapter 30 explicitly attributed a two-year learned cautious gait to the wrong side before any new left-foot injury occurred.
- Exact fixes:
  - `Левая ступня легла осторожнее правой.` → `Правая ступня легла осторожнее левой.`
  - `Левая нога отзывалась осторожностью, накопленной за два года пути…` → `Правая нога отзывалась осторожностью, накопленной за два года пути…`
- Note: the **left** foot later turns inward acutely in chapter 30 only after the spatial distortion; that event remains unchanged and is not the source of the earlier two-year gait habit.
- Recheck: PASS against chapters 13, 14, 15, 18, 01 and the remainder of 30.

### Defect totals

- Objective defect classes found: **2**
- Defective loci: **3**
- Continuity / physical-state: **2 classes**
- Knowledge-state defects: **0**
- Reaction defects: **0**
- POV/reveal-order defects: **0 unresolved**
- CRITICAL unresolved: **0**
- MAJOR unresolved: **0**

## Asgar-name / authorial-automation fixes

### Name-only fixes: 6

1. `01.md`: redundant second `Асгар` in the final phone-booth paragraph → pronoun / zero-subject construction.
2. `02.md`: `Асгар ухватился за перила.` → `Ухватился за перила.`
3. `08.md`: `Асгар поднял руку ей навстречу.` → `Он поднял руку ей навстречу.`
4. `09.md`: second `Асгар рассказал…` in the same paragraph → `Он рассказал…`.
5. `15.md`: `Асгар вернул трубку на рычаги.` → `Вернул трубку на рычаги.`
6. `30.md`: second `Асгар провёл по ней ладонью…` in the same paragraph → zero-subject construction.

### Additional repeated action beat: 1

- `28.md`: the exact action `Асгар посмотрел на узел.` was repeated a few lines later with no new beat; the second instance was removed.

No chapter contained a cluster of multiple confirmed **name-only** tic defects after contextual review. The six name-only fixes are singletons across chapters 01, 02, 08, 09, 15 and 30. Raw occurrence count was highest in 08, 21, 13, 09/28 and 19, but raw frequency was not treated as evidence where the name was needed to disambiguate multiple male subjects or restore focus.

## All prose edits made in this audit

1. `01.md` — redundant name removed in the final phone-booth paragraph.
2. `02.md` — redundant subject name removed before `ухватился за перила`.
3. `07.md` — false callback `Мог спросить, нужна ли помощь` corrected to an unrealized action that actually remained available.
4. `08.md` — redundant name replaced with pronoun in the 2039 return scene.
5. `09.md` — repeated name replaced with pronoun inside one paragraph.
6. `15.md` — redundant name removed before returning the receiver.
7. `28.md` — duplicate `Асгар посмотрел на узел` action beat removed.
8. `30.md` — redundant name removed in the corridor-distortion paragraph.
9. `30.md` — first pre-2039 gait reference corrected from left to right.
10. `30.md` — “two years of cautious gait” reference corrected from left to right.

## Physical-state ledger result

PASS after fixes:
- phone / documents tracked;
- bag from Ar tracked;
- Bertram tool tracked;
- Tobin figure tracked;
- right-knee injury has an on-page cause and remains the long-term gait side;
- left-eyebrow scar has an on-page cause and remains;
- the later left-foot turn in chapter 30 is a new acute event after spatial distortion, not a two-year-old injury;
- hair / beard / ageing and weight loss are causally developed during long isolation;
- bag, jacket/documents and walking stick are left at the Source before the 2014 opening and do not reappear on Asgar in the stadium scene;
- Keeper’s black monitoring band remains on Asgar and is covered by his sleeve before the 2014 contact.

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
- Source is an artificial receiving node in the Solar System, not Earth;
- historical addressing uses real prior RETRO-1 contact states, not arbitrary calendar selection;
- full causal loop is not explained before chapter 29;
- chapter 29 reconciles independently developed physics with RETRO-1’s historically inherited concrete configuration.

## Mandatory adversarial rechecks

- `01 ↔ 30`: **PASS** — door/wall geometry, older Asgar’s exit, young Asgar stepping aside, eye contact, gait, look back at booth, `Вам нормально?`, raised hand, turn behind corner, and young Asgar’s later entry align.
- `08 ↔ 30`: **PASS** — older Asgar appears physically **outside** the booth in the 2039 hall; spatial stretching, silent intercom, Katya’s door movement, reaching hands, table bleed-through, white wall and disappearance align from both POVs.
- `22 ↔ 29`: **PASS** — empty module, service volume, post-closure mass check, persistent passenger record and return-to-receiving-side model remain consistent.
- `27 ↔ 29`: **PASS** — historical addressing is reuse of a real previous contact and is not upgraded into arbitrary date selection.
- `29 ↔ 30`: **PASS** — 2014 is opened first; 2039 appears only after the 2014 contact; the common geometry is limited; after the 2039 failure RETRO-1 completes its return and the ending accelerates without a new workaround branch.
- Callbacks rechecked: `Тогда не тяни…` and `просто сидели, разговаривали` both have prior on-page sources.
- Exact removed old motif `Не входи`: **absent**. Ordinary contextual forms such as `Не входите` / `не входить` are not the removed motif.
- Removed old canon names/elements checked: **absent** in the artistic corpus.
- Required final line: **PASS** — `Асгар смотрел на неё ещё несколько секунд.`

## Main-drift handling

- Start SHA was frozen before the full read.
- Artistic edits were made sequentially on `main`.
- Every changed artistic file was reread in full before the audit continued.
- After the artistic corpus reached `1c1529db6fb1e200ef89e82e0ecd98ba27ec8615`, `main` advanced by ledger/CI-only commits. The compare showed only `.github/latest_v4_release_run.txt` and `V4_INDEPENDENT_RED_TEAM.md`; both changed files were read in full before this ledger correction. No unreviewed artistic-file drift remained.

## Final status at ledger preparation

- Chapters closed: **30/30**
- Interludes closed: **4/4**
- Files read completely: **34/34**
- Lines checked: **13,845**
- Objective continuity/knowledge/reaction defect classes found: **2**
- Defective loci fixed: **3**
- Name-only Asgar-tic fixes: **6**
- Additional repeated Asgar action-beat fix: **1**
- CRITICAL unresolved: **0**
- MAJOR unresolved: **0**
- Final adversarial recheck: **PASS**
- Status: **READY**

The repository SHA must be read after committing this ledger because the ledger update itself changes `main`.
