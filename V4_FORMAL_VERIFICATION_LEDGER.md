# V4 Formal Verification Ledger

Baseline main commit: `59c4ade1ae36fa640c0c9ec049c62c160d0cdc27`

Purpose: formal sequential verification of chapters_v4/01.md–30.md after continuity fixes.

For every substantive dialogue beat, reveal, inference, memory, habit, identity claim, technical claim, and emotional reaction, verify:
1. Knowledge provenance: PERSONALLY OBSERVED / TOLD / DOCUMENTED / INFERRED / HYPOTHESIS / NEW ORDINARY MEMORY.
2. Reveal order: no future-canon fact appears early.
3. Memory provenance: no detail is framed as previously established unless it was established; new ordinary memory must read as new memory, not callback.
4. Human reaction: response matches what this person plausibly knows and how much evidence they have.
5. Repeat-question logic: repeated questions must be explicit re-checks or seek a new layer of answer.
6. State continuity: time, injuries, objects, clothing, relationships and decisions carry correctly across chapter boundaries.

Status legend:
- PASS: no substantive issue found under this verification pass.
- FIXED: issue found and repaired; adjacent chapters rechecked.
- REVIEW: potentially subjective prose/psychology issue, not a continuity violation.

| Chapter | Status | Findings | Fix commit | Recheck |
| ---: | --- | --- | --- | --- |
| 1 | PASS | Opening knowledge/reaction chain and 2014/30 mirror verified; no unsupported callback | — | Ch30 opening cross-check PASS |
| 2 | PASS | Katya/Rauf/operator reactions remain evidence-bounded; no premature mechanism knowledge | — | Ch1/3 boundary PASS |
| 3 | PASS | CCTV/investigation dialogue preserves uncertainty; memory contamination explicitly controlled | — | Ch1/2 and Ch30 mirror PASS |
| 4 | PASS | Voluntary risk decisions, Katya resistance, Rauf caution and operator limits all provenance-safe | — | Ch3/5 boundary PASS |
| 5 | PASS | Entry decision remains Asgar's; Katya explicitly rejects shared responsibility; no future knowledge leak | — | Ch4/6 boundary PASS |
| 6 | PASS | 2039 identity verification is mundane/evidence-based; family-photo memory is locally grounded | — | Ch5/7 boundary PASS |
| 7 | PASS | Katya/family/archive knowledge develops from lived history and verified records; no premature mechanism claims | — | Ch6/8 boundary PASS |
| 8 | PASS | 2039 mirror matches Ch30; source concept introduced with explicit limits; family reactions remain human | — | Ch7/9 + Ch30 mirror PASS |
| 9 | FIXED | Inessa knowledge leak, Asgar age-memory reset, and unsupported stair memory repaired | e25abe6; 68447b3; d9dbadf | Full post-fix reread PASS |
| 10 | PASS | Martin keeps hypotheses separate from evidence; Inessa remains safety-bounded; no knowledge leak | — | Ch9/11 boundary PASS |
| 11 | PASS | Archive/translation work explicitly preserves source provenance; routines grow on-page | — | Ch10/12 boundary PASS |
| 12 | PASS | Safety decisions and entry choice remain voluntary; source question is already established | — | Ch11/13 boundary PASS |
| 13 | PASS | Locals verify threat/date before accepting Asgar's story; no anomaly expertise is assumed | — | Ch12/14 boundary PASS |
| 14 | PASS | Local survival knowledge remains local; 12m disagreement is observed, not interpreted as future canon | — | Ch13/15 boundary PASS |
| 15 | PASS | Temporal-anomaly protocol origin is derived on-page from machine archive; operator explicitly lacks prior knowledge | — | Ch14/16 boundary PASS |
| 16 | PASS | Mirena knowledge comes from explicit handoff/service telemetry; date choice and sensing limits remain bounded | — | Interlude III + Ch15/17 boundary PASS |
| 17 | PASS | Ar locals treat Asgar as an unverified risk; Arved checks claims before integration | — | Ch16/18 boundary PASS |
| 18 | PASS | Sayma separates source, retelling, translation and hypothesis; 'return to first door' exposed as later borrowing | — | Ch17/19 boundary PASS |
| 19 | PASS | Stadium-man resemblance remains weak personal hypothesis; scar and visual traits are previously grounded | — | Ch18/20 + Ch1/3 cross-check PASS |
| 20 | PASS | Stay/continue choice is informed and voluntary; Mirena, Tayra and Arved do not decide for Asgar | — | Ch19/21 boundary PASS |
| 21 | PASS | Tessa uses only local measurements + Asgar reports; no access to operator project knowledge; endpoint remains unknown | — | Ch20/22 boundary PASS |
| 22 | PASS | Project-purpose reveal occurs only after explicit archive lookup; post-close mass check and empty-module design match canon | — | Ch21/23 + Interlude IV boundary PASS |
| 23 | PASS | Asgar corrects his own overstatement; Mirena separates confirmed infrastructure facts from unknowns | — | Ch22/24 boundary PASS |
| 24 | PASS | Olmer treats claims as unverified testimony; local checks precede trust; new Baku memories read as ordinary new recall | — | Ch23/25 boundary PASS |
| 25 | PENDING | — | — | — |
| 26 | PENDING | — | — | — |
| 27 | PENDING | — | — | — |
| 28 | PENDING | — | — | — |
| 29 | PENDING | — | — | — |
| 30 | PENDING | — | — | — |

## Interludes verification

| Interlude | File | Status | Findings |
| --- | --- | --- | --- |
| I | 04a.md | PASS | Service discovers unplanned living mass only after door closure; unknown earlier man remains unresolved observation |
| II | 08a.md | PASS | Service can model Asgar's mass contribution but does not yet know project purpose or safe passenger separation |
| III | 15a.md | PASS | Mirena receives explicit handoff; Korvin enforces informed choice and operator knowledge limits |
| IV | 22a.md | PASS | Early 2014 trace is linked only as similar registration; witness account remains a separate source and identity is unresolved |

## Findings log

- Ch22: PASS — empty autonomous module, service volume, post-door mass registration and self-return are revealed only after Mirena/engineers reopen the old project.
- Interlude IV: PASS — pre-closure anomaly is grouped by measurement only; the older man remains an unresolved observation, not an identified Asgar.
- Ch23: PASS — Asgar explicitly corrects his own summary where it overstates the state of separation work; source/infrastructure uncertainty is preserved.
- Ch24: PASS — Olmer verifies environment and logs before accepting any larger story; newly surfaced domestic Baku details are presented as fresh ordinary memories, not callbacks.

- Ch19: PASS — scar creates a plausible resemblance cue only; sedina/hudoba were already observed in Ch1 and explicitly recalled in Ch3.
- Ch20: PASS — Mirena presents both real options without steering; Tayra states her preference openly; Arved does not expel Asgar.
- Ch21: PASS — Tessa distinguishes local measurement, model inference and Asgar's terminology; she does not know project purpose, source location or operator-side mechanics.

- Ch16: PASS — Mirena's service knowledge is fully sourced by Interlude III handoff and live contour data; she cannot see the outside scene or select dates.
- Ch17: PASS — Tayra/Arved verify danger, calendar and identity claims rather than treating time travel as established fact.
- Ch18: PASS — Sayma preserves provenance at every step; the legendary return-home ending is explicitly a later textual borrowing, not prophecy.
- Interlude I: PASS — first detection of extra living mass is shown operationally after closure; no design interpretation is available yet.
- Interlude II: PASS — model subtraction of Asgar's mass is not confused with knowing why the apparatus was designed or how to separate him safely.
- Interlude III: PASS — Mirena's knowledge and ethical operating frame are transferred on-page.

- Ch13: PASS — Radmila/Damir/Nazar treat Asgar as an unknown person in a dangerous environment and verify calendar claims rather than adopting them.
- Ch14: PASS — all technical behavior comes from local survival practice and direct measurements; ~12m disagreement is merely observed.
- Ch15: PASS — `temporal anomaly` reveal is source-traced from a surviving civil protocol; identity and causation remain explicitly unknown.

- Ch10: PASS — Martin labels resemblance vs causation and keeps Asgar's testimony separate from research conclusions.
- Ch11: PASS — source-provenance discipline is explicit; no unsupported biographical callback found.
- Ch12: PASS — operator and Inessa state uncertainty; Asgar's question about the source follows directly from Ch8.

- Ch7: PASS — Katya's 25-year knowledge is lived experience; institutions still verify rather than believe.
- Ch8: PASS — external 2039 materialization, silent acoustics and spatial collapse directly match Ch30; source is defined without implying construction site or selectable date.
- Ch9: FIXED/rechecked — Inessa now asks what Asgar means by transition; doctor treats non-aging as already known; unsupported stair callback removed and replaced with locally grounded family-photo memory.

- Ch4: PASS — operator states uncertainty instead of promises; Katya/Rauf reactions remain ordinary and bounded by observed risk.
- Ch5: PASS — Asgar's decision to enter is explicitly his; Katya says not to frame it as a joint decision.
- Ch6: PASS — institutional identity checks precede acceptance; the older son's inability to stay still for a photo is anchored to the displayed blurred family photo, not an unsupported callback.

- Ch1: PASS — older Asgar visual/gait/gesture and spoken mirror checked directly against Ch30.
- Ch2: PASS — no character accepts the time anomaly beyond available evidence; operator's surprise at the unknown man is preserved.
- Ch3: PASS — Rauf distinguishes camera evidence from Asgar's claims; image enhancement is explicitly treated as unreliable for identification.

