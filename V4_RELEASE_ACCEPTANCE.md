# V4 RELEASE ACCEPTANCE — «Красная будка»

## Baseline

Literary release-candidate baseline: `89d95ceb75124fa2c4e471454a654f0c58f4f8fc`.

This ledger records final publication acceptance against the active V4 corpus (`chapters_v4/`, 30 chapters + 4 interludes). Any later prose change invalidates PASS for that file until rechecked.

## Gates

A chapter/interlude may be marked PASS only after:
- cold-read of the full current blob;
- prose/dialogue/tic check;
- character voice and motivation check;
- knowledge/reveal-order check;
- physics/staging/time/body/inventory check;
- setup/payoff and neighboring-scene check where applicable.

Final release requires:
- all 30 chapters + 4 interludes PASS;
- CRITICAL = 0;
- MAJOR = 0;
- adversarial second pass on all modified files and cross-book hotspots;
- active canon/document drift = 0;
- final build QA against the final literary SHA.

## Chapter status

| Chapter | Status | Notes |
| --- | --- | --- |
| 1 | PASS | Cold-read: opening, Katya dialogue, older-Asgar seed, staging and prose clean |
| 2 | PASS | Cold-read: operator/Rauf/Katya reactions and first return clean |
| 3 | PASS | Cold-read + prior full verification: evidence discipline and memory contamination clean |
| 4 | PASS | Cold-read: Asgar/Katya conflict remains morally frictional; service limits clean |
| 5 | PASS | Cold-read: entry decision voluntary; physical risk established; no coercive rewrite |
| 6 | PASS | Cold-read: 2039 identity/administrative sequence and family-memory grounding clean |
| 7 | PASS | Cold-read: Katya reunion, archive reactions, early 2039 hook and emotional continuity clean |
| 8 | PASS | Cold-read: Katya/Asgar conflict, source terminology, 2039 geometry and dialogue realism clean |
| 9 | PASS | Cold-read: Inessa/doctor post-fix dialogue, grief/search sequence, memory provenance and prose clean |
| 10 | PASS | Release cold-read / current-blob cross-check clean |
| 11 | PASS | Release cold-read / current-blob cross-check clean |
| 12 | PASS | Release cold-read / current-blob cross-check clean |
| 13 | PASS | Release cold-read / current-blob cross-check clean |
| 14 | PASS | Release cold-read / current-blob cross-check clean |
| 15 | PASS | Release cold-read / current-blob cross-check clean |
| 16 | PASS | Release cold-read / structure / voice / physics cross-check clean |
| 17 | PASS | Release cold-read / structure / voice / physics cross-check clean |
| 18 | PASS | Release cold-read / structure / voice / physics cross-check clean |
| 19 | PASS | Release cold-read / structure / voice / physics cross-check clean |
| 20 | PASS | Release cold-read / structure / voice / physics cross-check clean |
| 21 | PASS | Release cold-read / structure / voice / physics cross-check clean |
| 22 | PASS | Release cold-read/current-blob acceptance clean across prose, voice, motivation, knowledge, physics and continuity |
| 23 | PASS | Release cold-read/current-blob acceptance clean across prose, voice, motivation, knowledge, physics and continuity |
| 24 | PASS | Release cold-read/current-blob acceptance clean across prose, voice, motivation, knowledge, physics and continuity |
| 25 | PASS | Release cold-read: archive provenance, loop foreshadowing and prose clean after causal-line fix |
| 26 | PASS | Release cold-read: survival progression, body state and stadium-man hypothesis/memory contamination clean |
| 27 | PASS | Rechecked after source-message fix: question now travels only as part of Asgar/service record; historical addressing fair-play and prose clean |
| 28 | PASS | Release cold-read/current-blob acceptance clean; final canon, prose, staging, knowledge and payoff checks passed |
| 29 | PASS | Release cold-read/current-blob acceptance clean; final canon, prose, staging, knowledge and payoff checks passed |
| 30 | PASS | Release cold-read/current-blob acceptance clean; final canon, prose, staging, knowledge and payoff checks passed |

## Interludes

| Interlude | File | Status |
| --- | --- | --- |
| I | 04a.md | PASS |
| II | 08a.md | PASS |
| III | 15a.md | PASS |
| IV | 22a.md | PASS |

## Defects found in this release run

Release-run defects found and fixed: Ch27 impossible direct message to source; Ch30 canonical final-line regression; Ch30 Asgar knowledge leak about elapsed 2039 time; Ch30 duplicated Katya beat; stale final-beat documentation. All modified fiction files received adversarial recheck. Active canon drift scan: 0 hits.


## Final acceptance

- Literary corpus: READY.
- 30 chapters: PASS.
- 4 interludes: PASS.
- Open CRITICAL defects: 0.
- Open MAJOR defects: 0.
- Active canon/document drift: 0.
- Final literary SHA: `983fa961152cf636063d4117c64710eaf0b5f37e`.
- Publishing workflow run: `36258292411` — SUCCESS.
- Release-line lock: PASS.
- Approved-cover lock: PASS.
- EPUB artifact: built and uploaded.
- Publishing package: built and uploaded.
- PDF metadata: PASS (`Красная будка`, `Аскер Исмайлов`).
- DOCX metadata/timestamps: PASS.
- Package SHA256 manifest: PASS.
- EPUB structure/navigation/final line: PASS.
- Interior PDF visual spot-check (first/final page): PASS.
- Build output: 77,074 words, 385 pages.
- Physical-print hold: calculated interior spine is 19.25 mm while approved wrap artwork uses 21.5 mm. Confirm final paper stock/binding spine with printer before sending the wrap to press.
