# 計算機異聞 refactor v013 — 2026-08-24 rollback / Pacific-China re-audit full package

v013 is a **session-continuation safety release** built from the complete v012 tree.

It preserves every v012 file, including the previously advanced Saipan/1944-summer and China forward-adjudication work, but marks those later states as **reference/provisional, not current branch continuation**, because the 2026-08-24 session corrected an upstream carrier-roster error and removed the old Sep-1943 Second Midway event.

## Current continuation entrypoints

Read in this order:

1. `00_README/NEXT_SESSION_HANDOFF_REFACTOR_v013.md`
2. `06_RUNTIME/CURRENT_ANALYSIS_FRONTIER_1944SPRING_REAUDIT_v001.json`
3. `06_RUNTIME/SESSION_2026-08-24_ROLLBACK_PACIFIC_CHINA_SETTLEMENT_v001.md`
4. `00_CONFIG/current_branch_overrides_v004.json`
5. `06_RUNTIME/PACIFIC_CENTRAL_1943_1944Q1_SETTLEMENT_v001.md` as pre-existing evidence, not blindly authoritative where overridden
6. `06_RUNTIME/CHINA_BURMA_CBI_1943_1944Q1_SETTLEMENT_v001.md` as pre-existing evidence, not blindly authoritative where overridden
7. `06_RUNTIME/CBI_AIR_LOGISTICS_TAX_1944-04_06_WORKING_SETTLEMENT_v001.md` for mechanism/band reuse only
8. v011 combat/platform execution layers

## Current branch frontier

**1944-04-11, immediately after the re-audited HAILSTONE-equivalent Truk raid.**

Next required event:
- re-audited CATCHPOLE / Eniwetok, working window Apr 18–22

Then:
- freeze Pacific late-Apr checkpoint
- return to early-May China No.1/Ichigo-equivalent launch
- synchronize back to sea for Palau/DESECRATE, likely mid/late May under the new clock

## Critical upstream corrections

- Old Sep-1943 Second Midway invasion removed.
- Japanese Sep-1943 core fleet carriers = Shokaku / Zuikaku / Hiryu / **Soryu**.
- Old 1944 “10 carriers” table omitted Soryu. Physical total after Taiho completion is **11 hulls** before later losses.
- GALVANIC delayed to Feb 1944.
- Marshall campaign delayed to late Mar 1944.
- Truk fleet-base downgrade occurs after Kwajalein; high-value mobile assets disperse before HAILSTONE equivalent.
- Five-Go closes with limited Guangyuan capture and no deep Chengdu pursuit.
- Burma main line remains mostly old-version: no U-Go; Myitkyina/North Burma emphasis rises.

## Do not do

Do **not** resume directly from:
- `CURRENT_ANALYSIS_FRONTIER_1944SUMMER_v001.json`
- old Saipan settlement as current state
- old China Hengyang forward adjudication as synchronized global state

Those remain useful evidence for later comparison, but must be re-audited after the corrected 1944 spring sequence catches up.

## Execution layer

v011 execution behavior remains authoritative unless explicitly superseded by current-branch overrides:
- separate detection/track/identify/allocation/fire-control/fire/hit
- separate existence/availability/readiness/mission set/effectiveness/allocation
- no nationality/year-label combat shortcuts
- no industrial teleportation for either side
- submarine and surface-combatant capability review remains mandatory when relevant
