# SESSION HANDOFF — 2026-09-05 / V9 SESSION CLOSE

This file captures all decisions made after the packaged V8 checkpoint (1939-08-22 24:00). It is the first authority for resuming the next chat unless a later file in this directory explicitly narrows a value.

## Current world clock by theater
- NOMONHAN: combat campaign CLOSED through 1939-08-31 stabilization/central stop. Post-battle procurement and force-rebuild consequences remain future-flow items.
- CHINA: replay caught up through **1939-06-20 24:00**. Next combat gate is **1939-06-21 Swatow/Shantou operation**, with the North China Wutaishan fourth phase concurrently active.
- GLOBAL/INDUSTRIAL: 1939-04-20 company state remains the physical/organizational base; uranium/nuclear research is now explicitly recognized as an early research branch but not an industrial enrichment capability.

## Highest-priority new authorities
1. `01-NOMONHAN-CLOSURE-CANON-V9.md`
2. `02-NOMONHAN-LOSS-LEDGER-V9.tsv`
3. `03-NOMONHAN-AIR-SPECIAL-AMMO-CORRECTION-V9.md`
4. `03A-NOMONHAN-AIR-SPECIAL-AMMO-WORKING-V9.tsv` — machine-readable companion to 03
5. `04-NOMONHAN-REINFORCEMENT-PIPELINE-V9.md`
6. `04A-NOMONHAN-REINFORCEMENT-PIPELINE-V9.tsv` — machine-readable companion to 04
7. `05-NOMONHAN-ACTOR-LESSONS-THREAT-ESTIMATE-V9.md`
8. `07-CHINA-CROSS-THEATER-ALLOCATION-GUARD-V9.md`
9. `08-CHINA-CATCHUP-1939-04-20-06-20-V9.md`
10. `08A-CHINA-1939-06-20-STATE-V9.tsv`
11. `09-NEXT-GATE-SWATOW-1939-06-21-V9.md`
12. `11-G3M-CHONGQING-EX-STATE-CLOSEOUT-V9.md` / `11A...tsv`
13. `12-NOMONHAN-SPECIAL-AMMO-PRODUCTION-FLOW-CLOSEOUT-V9.md` / `12A...tsv`
14. `13-NOMONHAN-AVIATION-STOCKFLOW-CLOSEOUT-V9.md` / `13A...tsv`
15. `14-URANIUM-SYSTEM-BALANCE-CLOSEOUT-V9.md` / `14A...tsv`
16. `15-RIKEN-ISOTOPE-RESEARCH-CLOSEOUT-V9.md` / `15A...tsv`
17. `10A-ACTIVE-OPEN-ISSUES-V9.tsv` — current active/deferred session queue; file 10 retains full issue history

Package-level current control overlays are `../TERMINOLOGY-AND-SUPERSESSION-GUARD-V9.tsv` and `../DECISION-INTENT-INDEX-V9.tsv`; the V7 decision-intent index is provenance/fallback only.

## Critical no-backflow rules
- Historical Aug22-31 Japanese pocket annihilation MUST NOT be recopied. The worldline main body escaped through the altered corridor and Fui/Tomii staged withdrawal.
- Ki-27 EX2 adoption is an absorbing state; late-1938 new production is already largely EX2 and overhaul can convert EX0→EX2. Do not freeze OPEN mixtures for months.
- Capability != adoption, but non-adoption also does not auto-persist.
- TANK-37 and AT-37 special ammunition are distinct complete cartridges. Old V8 forward stocks 192/576 are superseded by 288/912 Aug19. TECHCLOSE4 formalizes the minimum flow: cumulative accepted/forwarded by Aug19 is at least TANK-37 322 and AT-37 936; exact factory gross output remains unasserted.
- Do NOT apply an aggregate "Nomonhan penalty" to China. The historical China baseline already includes historical China→Manchuria transfers. Subtract only worldline-specific additional transfers actually sourced from China.
- Conversely, post-Nomonhan saved manpower/equipment first becomes Home/Manchuria reserve or retained capital. Do NOT instantly add it to China unless actual reassignment is established.
- 1939 Army aviation redeployment to Manchuria mixed emergency Nomonhan use with a pre-existing 1939 air arm reorganization/Manchurian strengthening plan. Do NOT assume all September northbound air units remain in China merely because the campaign ended early.
- E4 China photo-recon capability was not shown to be stripped for Nomonhan. Ki40/E5 x2 were evaluation assets pushed into combat, not China-line aircraft; therefore no China subtraction and no E5 development delay are imposed.

## Campaign-level Nomonhan result
- Soviet/Mongolian side achieves the territorial/operational objective: contested/claimed area secured.
- Japanese main body avoids the historical annihilation. This is still a Japanese limited operational defeat, not a Japanese victory.
- Kwantung Army remains dissatisfied and prepares a September return offensive, but the very need to rebuild/concentrate gives Tokyo time to impose a no-new-offensive order around Aug30-31. No major September reattack is launched in the main branch.
- Soviet side does not pursue deeply into Manchuria; after securing the claimed line, it stabilizes and probes rather than opening a new strategic invasion.

## Nomonhan working terminal figures
- Japanese total human loss: ~12.4k center (combat ~10.6k, disease/noncombat ~1.8k).
- 23rd Division total loss: ~7.35k center; badly damaged but organizational skeleton preserved rather than historically destroyed.
- Soviet total human loss: ~22.5k center; Mongolian ~0.5k.
- Japanese First Tank Group: 38 irreversible tank/tankette losses center; ~50 physical survivors/recoverables; ~35-37 ready by late Aug; 3 Chi-Ha remain.
- Japanese artillery irreversible losses: ~42 guns center (range ~38-46), substantially below historical ~72-class loss.
- Japanese aircraft irreversible campaign loss: ~135-145 all-cause band; Soviet ~220-230 all-cause band. Use separate combat-only/all-cause definitions when formalizing.
- Retained high-value human capital vs history: provisional +0.95k to +1.5k officers/NCOs/specialists. DO NOT compound this until the planned 1941-end audit.

## Nomonhan hidden-capital interpretation
The worldline repeats the China pattern: better reconnaissance/withdrawal timing prevents encirclement and annihilation. Hence Japanese loss ratio improves strongly while absolute Soviet deaths do not necessarily rise. The largest long-run delta may be preservation of officers, NCOs, tank crews, artillery observers, radio personnel, mechanics/recovery teams, medical staff and instructor candidates.

## Soviet threat perception
- Soviet command recognizes a costly but successful operational victory, not Japanese weakness.
- Actual exchange ratio is worse for the Soviets than they are likely to understand immediately. Soviet/Japanese wartime loss estimates are biased; the main branch assumes Zhukov does NOT know the true ~2:1 Japanese-favorable combat-loss ratio.
- What is observable: Japanese tactical toughness, rapid technical adaptation, improved AT effectiveness, aircraft quality, recovery/maintenance, high-grade reconnaissance, and—most importantly—successful escape from an intended operational encirclement.
- Working Soviet conclusion: Japan is a high-cost dangerous opponent that can be defeated with concentrated artillery/air/armor/logistics, but cannot be treated as a stagnant second-rate army. Re-evaluate this in 1941 when European-war force transfers become relevant.

## Post-Nomonhan Japanese lesson split
- Kwantung aggressive staff: "direction was right; quantity and artillery were insufficient" rather than mechanization despair.
- 6th Army: prepare at army scale; preserve reserves and avoid local piecemeal rescue.
- 23rd Division field perspective: reconnaissance alone cannot compensate for insufficient artillery/AT/transport.
- Armor community: tank-alone breakthrough failed, but tanks as mobile reserve/extraction cover worked; demand better guns, recovery, communications, medium tanks and successors.
- Tokyo/GHQ: primary lesson is command/control and preventing a field army from independently creating a national war.
- Soviet side: deepen interdiction/second blocking line; do not allow Japanese withdrawal clock.

## Uranium/nuclear research branch (future revisit)
- Natural-U strategic retention by Aug1939 is now a formal scenario-system balance: **55-65 t-U, center 62 t-U**, split at center into 27 feed +14 metal/process +9 military +4 research +8 overseas/in-transit. It is not Home-Islands-only and not an empire-wide geological resource total.
- Protagonist strategy: use contemporaneously legitimate heavy-metal/materials/isotope-science reasons to make institutions fund resources and capabilities whose later value he knows.
- RIKEN cooperation can plausibly begin before formal wartime military atomic programs: isotope analysis/material purity/radioactivity/nuclear physics, later small isotope-separation research.
- 1939-40 Asai contribution is strongest in enabling technologies: vacuum, precision machining, seals/bearings, rotordynamics, pumps/compressors, special materials, measurement, power/control and mechanized calculation.
- "Enrichment research exists" is allowed; "industrial enrichment production capability exists" is NOT.
- No kg-scale enriched uranium or practical bomb program is canonical at Aug1939.

## China catch-up
- Suixian-Zaoyang overlapping campaign was missing from V8 and has been backfilled for Apr20-May24.
- Japanese basic map outcome remains historical-like: temporary offensive penetration, no decisive Chinese main-force encirclement, orderly Japanese withdrawal, Chinese territorial recovery.
- Working Japanese loss there: ~2,235 combat casualties center (KIA ~585, WIA ~1,650), ~9-10% below the historical internal ~2,468 baseline.
- 1939-05-25 to 06-20: 11th Army recuperates; Wutaishan operations continue in North China without decisive guerrilla annihilation; Chongqing strategic bombing continues; Shantou assault force is detached from 104th Division and sails on Jun20.
- China-wide worldline usable military-capital delta remains in the existing +5k to +8k CEQ family; by Jun20 a larger share is ready/deployable than immediately after Nanchang/Suixian-Zaoyang.

## TECHCLOSE4 bookkeeping closures
- China/Chongqing G3M EX-state: CLOSED-CONSERVATIVE for Jun20 replay. Credit EX0-equivalent headline performance plus existing reliability/QC effects; selective EX2 presence is possible but unquantified and receives no speed credit absent named lot evidence.
- Nomonhan special 37mm flow: CLOSED through Aug25 at lower-bound production/inspection/forwarding level. Factory monthly gross output/reject rate remains deliberately unasserted.
- Nomonhan aviation stock-flow: CLOSED-CAMPAIGN-SUFFICIENT from retained named-unit anchors and the Aug19-22 bridge; future exact sentai/day arithmetic is local only.
- Uranium system balance: CLOSED-SCENARIO-MACRO at Aug31 center 62 t-U; geography/legal-title detail remains local.
- Asai-RIKEN isotope research: CLOSED through Aug31 1939 at laboratory research scale; future scale-up/funding/apparatus decisions are later gates.

## Next exact gate
**1939-06-21 Shantou/Swatow landing and exploitation**, processed together with:
- Wutaishan fourth-phase close (Jun19-22),
- the temporary gap in 104th Division's Guangdong security line caused by detaching the Goto force,
- actual allocation/adoption state of landing craft, radios, vehicles, aviation and Asai-derived reliability improvements.
