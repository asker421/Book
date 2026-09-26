# V4 LINE-BY-LINE AUDIT — «Красная будка»

## Baseline
- Branch: `main`
- Frozen audit baseline: `d93e87211c98563ea551492aef771d0de1e20e86`
- Post-fix audited prose head: `94785a99409c27d8b1c07b740babea583865c695`
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
| 27.md | PASS | PASS | Historical addressing introduced with limits; loop example is generic; source question travels only with Asgar/service record |
| 28.md | FIXED | False callback to Mirena after the long slope stay corrected to the actual Ch26 exchange («можете говорить?» → «Могу»); full post-fix reread PASS |
| 29.md | PASS | PASS | Receiving-side/source, no universal year, RETRO-1 loop and 2014 access revealed only from Avelina/project record |
| 30.md | FIXED | Ch1/Ch8 mirrors verified; restored current-canon causality for automatic 2014→2039 selection and explicit open passenger record; post-fix reread PASS |

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

- Ch25–27: full literal line pass completed; no new objective defect found.

- Ch28–30: full literal line pass completed. Ch30 mirror dialogue/staging independently cross-checked against Ch1 and Ch8.

- Ch21–23 + Interlude IV: full literal line pass completed; no objective defect found. Ch23 domestic-memory callback traced to Ch1 line 55.

- Ch24–26: full literal line pass completed; no objective defect found.

- Ch28 defect fixed: recalled Mirena exchange did not match Ch26; replaced with the exact established question/answer.
- Ch30 canon gap fixed: 20.08/24.08.2014 are stated as automatically skipped for insufficient external geometry; 2039 is explicitly not selected by Avelina; final state now explicitly says RETRO-1 completed its return while Asgar's passenger record remains open.
- Final Ch30 mirror check against Ch1 and Ch8: staging, limb/step behavior, silent audio channel, Katya's actions, spatial deformation and disappearance all match without other-POV leakage.

- Ch27–30: full literal line pass completed; no objective defect found.

## Current result
- 30/30 chapters checked line by line.
- 4/4 interludes checked line by line.
- Objective defect clusters found during the literal/post-fix pass: 4.
  1. Ch7 — unsupported recalled Katya quote.
  2. Ch25 — archive/Olmer wording overclaimed absence of RETRO-1 lineage beyond available evidence.
  3. Ch28 — false recalled Mirena exchange after the long slope isolation.
  4. Ch30 — missing/blurred automatic 2014→2039 selection causality and open passenger-record state.
- All four defect clusters were repaired in `main`.
- Open objective defects in the audited categories: 0.

## Final line-by-line verdict
All 30 chapters and 4 interludes were re-read literally from the current corpus with previous PASS judgments ignored. One new objective continuity defect was found (Ch7 unsupported recalled quote), fixed, and rechecked against Ch1 and later callbacks. No other objective knowledge-provenance, future-knowledge, false-memory, ordinary-reaction, body/object-state, reveal-order, or sentence-logic defect remains known after this pass.

- Fresh-main final-block SHA recheck after concurrent edits: PASS — 27 `5c61f97c...`, 28 `db88dc00...`, 29 `01b8b493...`, 30 `87d06a4b...` are the blobs actually read in the completed audit.

- Ch21–23 + Interlude IV: full literal line pass completed; no objective defect found.

- Ch25 defect fixed: Olmer's «связи ... не существует» overclaimed beyond the archive evidence and conflicted with the later causal-loop reveal; changed to «связь ... не прослеживается».

## Completion

Literal line-by-line pass completed for all 30 chapters and all 4 interludes. Previous PASS judgments were not trusted as evidence. Every current prose file was re-identified by blob SHA after the post-fix phase.

### Repairs produced/confirmed by this pass
- Ch7: `caaf025d443a4e297b9a56ab525d1e43f8caba29` — replace unsupported Katya callback with the exact Ch1 line.
- Ch28: `e519cbbafc181634fe1444ac6130134f65b938aa` — correct the remembered Mirena exchange to the actual Ch26 question/answer.
- Ch25: `2d2d41b0def82d964ee2877f31e31ca76185dcc9` — change an absolute lineage denial to the evidence-bounded “не прослеживается”.
- Ch30: `e87849196695bdb36d50f1cad1e293aa8bcc9c99`, `94785a99409c27d8b1c07b740babea583865c695`, `20ba59ed003170630fc4c19b3e7eb64ff6593657` — restore/clarify automatic state selection, skipped 2014 states, 2039 causality and the still-open passenger record.

### Coverage proof
Repository head when this proof table was captured: `86ddf374e8388f80604e6b06a4f58648cf06b545`.

| File | Blob SHA | Lines |
| --- | --- | ---: |
| 01.md | 1d2a1f5013c2793c842c994269bf1c4f48725dcd | 232 |
| 02.md | 1345f8342520adcd6789baa3fdb7366bdc5b2063 | 443 |
| 03.md | e8b137a44c17a8511707fda59199e426eab645df | 355 |
| 04.md | 56273392f5ff4a00024501a3f5407c934afd8ee5 | 433 |
| 04a.md | 5e7050dd2de1eb9effc4390ccbb168cb1910ece6 | 98 |
| 05.md | ca87f1e18ffab55880264af9e9edffbb35ae7131 | 569 |
| 06.md | aa7eda7b6c9d9f027b77833ec8f39f1d5c31da54 | 458 |
| 07.md | 3f1b20eee68f4f3639ec53427a48207579787a71 | 559 |
| 08.md | 68d31fdd80cd0a6ed904b777384c3fba3fab658e | 638 |
| 08a.md | 8f8d1637a2f268f48f44553378635d96458c8f8d | 76 |
| 09.md | 1fbff633b8397bbc3681e06a8bc8be89ea74eb42 | 537 |
| 10.md | 3e69a1114c0bfad9b1a91dead6cf947de2327000 | 551 |
| 11.md | 52fcc9b2d6d0597c30a082c1fcb64fd252592cf5 | 553 |
| 12.md | c2f2b467565730745f3729279c0ab179d7fdd65e | 465 |
| 13.md | a33df876d0d85cc5e76793a96b5e721acb8f1ef1 | 543 |
| 14.md | 5253928e793dcc1c4ae6d504ab9047d0640d82d8 | 269 |
| 15.md | a26553bed5247e481db4f2bd82b83374820133cc | 306 |
| 15a.md | 57fd5c868e8f1bc3c6d062f0170aefd96e4c322a | 271 |
| 16.md | ba8c4102c77ed1f52f352311ed8551f9c7084c36 | 290 |
| 17.md | 98def3f92eb7611c1c9ffdbde72d676b78f7fdc4 | 337 |
| 18.md | a70eb12610a5fe25ad4e62b85f6912915d2f8afe | 459 |
| 19.md | 1b44719bbd98dd85d1187ac88804edf4c834c8c7 | 480 |
| 20.md | 5fbf3af86f9c8ac91f24684489a430ae85ce79c5 | 477 |
| 21.md | af5bf5c1a37bcdd5abe16e3b71bc340a63b4fd8f | 659 |
| 22.md | b29db8df71ee4dedd6fe3130f8cf166e0bd4db7f | 561 |
| 22a.md | 514e60e47c367ade220665188a7a42c4f9c74d3d | 60 |
| 23.md | 79e5337a44713cbf23d243cbac7e9ca8e353c13a | 383 |
| 24.md | 98af1cd35e946d712b4fb90dcdcb816968f5cb82 | 471 |
| 25.md | b1acc8264f67cfd227b6aaa1c25f03275bbc8837 | 391 |
| 26.md | 9bab3e8a66e9f26616029b8fe38067f4400efd1a | 477 |
| 27.md | 5c61f97c67d978b69ec56e80f3e10c8f567a1643 | 330 |
| 28.md | db88dc008ec8cea82f3be450f539d47584837139 | 627 |
| 29.md | 01b8b493929ad73478c90c7a3eaec1ddf7c23ab7 | 268 |
| 30.md | c478ac950e3e7298e397c73230907f761b7459e0 | 233 |

Total audited corpus: **34 files / 13,859 lines**.

### Final status
All 34 current prose files are accounted for by blob SHA and line count. Open objective defects in the audited categories: **0 known**. Any later prose edit invalidates the affected file's PASS until that new blob is re-read.
