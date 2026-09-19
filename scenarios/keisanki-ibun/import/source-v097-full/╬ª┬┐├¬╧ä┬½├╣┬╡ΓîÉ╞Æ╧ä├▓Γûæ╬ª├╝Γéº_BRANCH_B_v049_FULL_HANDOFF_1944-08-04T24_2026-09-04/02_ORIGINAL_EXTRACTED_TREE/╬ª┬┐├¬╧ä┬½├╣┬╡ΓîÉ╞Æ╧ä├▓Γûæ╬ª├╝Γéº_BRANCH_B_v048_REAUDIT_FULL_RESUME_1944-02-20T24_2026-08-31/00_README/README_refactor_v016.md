# 計算機異聞 refactor v016 — 2026-08-24 pre-Ichigo data audit

v016 does not advance the scenario clock. It records the prerequisite audit requested before re-adjudicating the early-May 1944 No.1/Ichigo-equivalent operation.

## Canonical machine entrypoint

1. `06_RUNTIME/CURRENT_BRANCH_STATE_v001.json`
2. `06_RUNTIME/CURRENT_ANALYSIS_FRONTIER_1944SPRING_REAUDIT_v001.json`
3. `06_RUNTIME/PRE_ICHIGO_LAND_AIRFIELD_OOB_SHIPPING_NANJING_AUDIT_1944-04-25_v001.md`
4. `06_RUNTIME/CATCHPOLE_ENIWETOK_1944-04-18_24_SETTLEMENT_v001.md`
5. `06_RUNTIME/SESSION_2026-08-24_ROLLBACK_PACIFIC_CHINA_SETTLEMENT_v001.md`

## Current branch

Current analysis frontier remains **1944-04-25T00:00**.

v016 flags a major Burma OOB correction: historical 1944 Burma includes the 2d Division, but this branch has the 2d Division main body fixed in New Caledonia and contains no later Burma redeployment record. It therefore must not be double-counted.

The pre-Ichigo audit now treats land/airfield ownership, China/Burma OOB, shipping/inland transport and Nanjing rear substitution as prerequisites to operation sizing. Old 7–9 division and later ~14 division Ichigo analogs remain reference values only.
