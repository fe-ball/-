# 計算機異聞 refactor v040 — Central Pacific airfield / water-air re-audit WORKING FULL

CURRENT authority is unchanged at **1944-01-01**. Working discussion clock remains **1944-02-02 09:30 Marshall local**; this revision does not advance time, it re-runs only the 2-Feb 04:30–09:30 air calculation.

v040 closes the missing regional aviation layer:
- US Tarawa/Makin/Abemama forward land-air network (historical end-Jan anchor 365 assigned-class aircraft).
- US PBY/PBM/PB4Y/PV search/ASW/Dumbo system and Curtiss/Mackinac tender support.
- Japanese Ebeye/Kwaj 952 AG float-recon node, Kyofu, Zuiun and legacy float aviation as subsets of existing totals.
- Japanese surrounding depth at Eniwetok, Ponape, Kusaie, Nauru, Wake, Truk, Saipan/Tinian and Midway, with same-day range/staging gates.
- Corrected first suppression morning v002 and corrected 09:30 Marshall OOB v002.

Key corrected poststate at 09:30: ~94 serviceable, ~46 fighters, ~10 Raiden, ~20 unique water-air aircraft, ~21 attack aircraft. Eniwetok retains ~10 land-attack serviceable center. US morning aircraft irrecoverable center ~16 across TF58 + Gilbert land-air; Japanese morning center ~39, cumulative since Jan31 night center ~43.

Load first:
1. `00_README/CURRENT_DISCUSSION_FRONTIER_v009.json`
2. `95_AUDIT/CENTRAL_PACIFIC_AIRFIELD_WATER_AIR_REAUDIT_2026-08-29_v001.md`
3. `06_RUNTIME/CENTRAL_PACIFIC_REGIONAL_AIRFIELD_NETWORK_1944-02-02T0430_WORKING_v001.json`
4. `06_RUNTIME/MARSHALL_WATER_AVIATION_NETWORK_1944-02-02_WORKING_v001.json`
5. `06_RUNTIME/US_GILBERT_FORWARD_LAND_AIR_1944-02-02_WORKING_v001.json`
6. `06_RUNTIME/FLINTLOCK_FIRST_SUPPRESSION_STRIKE_1944-02-02_WORKING_v002.json`
7. `06_RUNTIME/MARSHALL_AIR_OOB_1944-02-02T0930_WORKING_v002.json`
8. `06_RUNTIME/MARSHALL_SUBMARINE_CONTACT_LIAISON_1944-01-28_WORKING_v001.json`

Next exact action: 2-Feb late morning/afternoon second suppression cycle + submarine convergence, now under explicit Gilbert patrol/ASW pressure and with surviving Japanese water-air/search depth.
