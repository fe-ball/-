# 計算機異聞 refactor v047 — Branch B land+vehicle integration / GALVANIC ground rollback

CURRENT authority time remains **1944-01-01**. The authority revision advances to `CHECKPOINT_1943-12-31T24_BRANCH_B_v005` only because the Tarawa ground node was corrected and propagated. WORKING discussion clock remains **1944-02-06 18:00 Marshall local**; v047 does not advance the war clock.

## What v047 fixes

v046 correctly restored artillery, mortar, direct-fire, fortification, tactical communications, engineer plant and ammunition-process effects, but compressed tanks and other vehicles into a small generic uptime note. v047 restores the full vehicle layer:

- Type 95/97, tankettes/armored cars, trucks/prime movers, recovery/workshop and engineer vehicles are separate families.
- Running gear, suspension, clutch/transmission, cooling/lubrication, production QC, spares and repair/recovery can differ from historical Japan.
- Gun energy, armor, crew ergonomics, radio count, physical hull count, fuel and terrain do not improve without their own trace.
- The 72-hour 1.3-1.6x effective-reappearance band is limited to suitable maintained mobile formations. Bombarded atolls use 1.1-1.3x and only for reachable, repairable vehicles.

`JAPANESE_LAND_COMBAT_INTEGRATED_SYNTHESIS...v001` is the single load point. It orders adjudication as physical OOB -> serviceable/crewed state -> maturity -> terrain/supply/suppression -> damage classification -> repair/reappearance -> casualties/timing.

## GALVANIC rollback result

Tarawa was reopened to the 24-November pre-landing node because the mandatory vehicle/OOB/reappearance inputs were absent from the previous closeout.

- Japanese Type 95: 14 physical; 6-9 contact-capable after suppression; 4-5 in the first-night counterattack; 2-4 later mobile firepoints.
- US M4A2: 14 physical; 8-11 ashore by first night; 6-8 operational.
- US Tarawa casualties: KIA/MIA 620-770; WIA 1,530-1,780; total 2,150-2,550, center about 2,350 (old center about 2,100; delta about +250).
- Organized resistance ends 28-November evening to 29-November noon, centered 29-November morning.
- US capture of Tarawa/Makin and the carrier, surface and submarine outcomes remain unchanged after dependency review.

The consolidated Allied-death-tally reservation is now partially applied to GALVANIC only. Other prior ground events, including the already-realized 6-Feb Flintlock first-day cost, remain reserved; do not copy Tarawa's delta to them.

## Load first

1. `00_README/CURRENT_DISCUSSION_FRONTIER_v014.json`
2. `06_RUNTIME/JAPANESE_LAND_COMBAT_INTEGRATED_SYNTHESIS_1932_1944_WORKING_v001.json`
3. `06_RUNTIME/JAPANESE_LAND_VEHICLE_ARMOR_LINEAGE_1932_1944_WORKING_v001.json`
4. `06_RUNTIME/ALLIED_DEATH_TALLY_RETROACTIVE_LAND_HARDWARE_RESERVATION_1941_1944_WORKING_v002.json`
5. `06_RUNTIME/FLINTLOCK_DDAY_DECISION_AND_LANDING_1944-02-06_WORKING_v003.json`
6. `06_RUNTIME/PARALLEL_THEATER_STATE_1944-02-06T1800_WORKING_v001.json`

Next exact action: resume from 6-Feb 18:00 and adjudicate 7-9 Feb Kwajalein/Roi-Namur ground reduction with the integrated land+vehicle system active prospectively.
