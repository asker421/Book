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
| 16 | PENDING | — | — | — |
| 17 | PENDING | — | — | — |
| 18 | PENDING | — | — | — |
| 19 | PENDING | — | — | — |
| 20 | PENDING | — | — | — |
| 21 | PENDING | — | — | — |
| 22 | PENDING | — | — | — |
| 23 | PENDING | — | — | — |
| 24 | PENDING | — | — | — |
| 25 | PENDING | — | — | — |
| 26 | PENDING | — | — | — |
| 27 | PENDING | — | — | — |
| 28 | PENDING | — | — | — |
| 29 | PENDING | — | — | — |
| 30 | PENDING | — | — | — |

## Findings log

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

