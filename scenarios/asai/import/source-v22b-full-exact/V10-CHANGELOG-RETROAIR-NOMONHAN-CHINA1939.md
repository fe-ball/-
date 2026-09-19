# V10 CHANGELOG — RETRO AIRPOWER / NOMONHAN REVISED / CHINA 1939 COMPLETE

Major changes from V9:
- Rebased E5 Twin and Ki-42 from tiny evaluation populations to their 1937-39 operational procurement fleets.
- Closed 1938 retro aviation production/use and 1939 Q1/May10 state.
- Replayed Nomonhan as a delta from OLD V9 while carrying every old Asai effect forward.
- Revised Nomonhan terminal loss/readiness/withdrawal geometry; campaign result remains Soviet/Mongolian territorial/operational victory.
- Closed post-Nomonhan China REALLOCATION; corrected bad RETURN wording.
- Advanced China from 1939-06-20 through 1939-12-31: Shantou, East Shanxi, Changzhi counteroffensive, First Changsha, South Guangxi, Winter Offensive, Kunlun Pass.
- Restored pure-addition opportunity-cost effects: E5/Ki42 can release conventional recon/Ki-27 missions when actually reassigned.
- Closed E5/Ki42 auxiliary fuel/drop tanks.
- Closed Chi-Ha WET1 / 200-220 hp wet/heavy-mobility and First Changsha tank/engineer OOB.
- Closed mobile-GT winter heating/cold-start support through 1939.
- Added 1940 weapon appearance/fielding ledger as NEXT GATE only; combat clock remains 1939-12-31.
- Quarantined stale post-V9 working files, especially 1940 Q1 draft with obsolete small E5/Ki42 fleet volumes.

## DATAFIX1 — 2026-09-07

- Corrected `MACHINE-INTEGRITY-AUDIT-V10.json` file-count semantics: 763 manifest-target files / 765 final files / 762 inventory rows.
- Classified historical V7/V8/V9 manifest drift instead of rewriting legacy provenance files.
- Marked `PACKAGE-INVENTORY-V8.tsv` as an intermediate provenance snapshot; final V8 SHA-256 manifest remains the V8 snapshot authority.
- Preserved the post-V8-manifest `PACKAGE-STATE-V8.tsv` hash accepted by V9/V10 rather than forcing a rollback to the older V8 manifest hash.
- Explicitly treats `00-START-HERE-CURRENT.md` as a mutable alias whose old V8/V9 hashes are snapshot-only.
- No worldline fact, clock, OOB, production quantity, equipment-performance value, combat result, or next-gate decision changed.

## E6REBASE1 — 2026-09-07

- Removed the stale `E6 Twin 4 / Single 2` 1940 evaluation-only planning block inherited from the pre-retro small-E5-fleet assumption.
- Separated E6 Twin military productization from E6 Single research/evaluation.
- Propagated current E6-M-J/JF installed thrust/mass closure into a new aircraft-level H→A design calculation without claiming unrecorded measured flight-test values.
- Rejected the unsourced 14 m² conversational wing-area assumption; new performance calculations use an explicit 18.5–20.0 m² / drag / Mcrit sensitivity box.
- Closed E6 Twin central design estimates: J ~4.10 t / ~800–830 km/h class; JF ~4.40 t / ~740–795 km/h class; measured flight values remain local H→A.
- Closed a 300–350 L/side E6 external-fuel family, center `E6-D320F 320 L ×2`, using molded flax/hemp-epoxy with metal lugs and inherited E5 drop-tank handling/jettison practice.
- Rebased 1940 E6 Twin planning to 36–60 accepted aircraft, center ~48, JF 75–85%, with actual monthly production/allocation left to 1940 replay.
- No 1939 combat result, clock, E5/Ki-42 OOB, or E7 chronology changed.



## E6COSTREBASE1 — 2026-09-07

- Reconciled E6 Twin procurement with embedded E5/E6 engine-price models, a conventional twin airframe cost bridge, E5 procurement behavior and the T-1/T-2/T-3 capacity schedule.
- Engine-only E6-JF premium remains ~73–75% over E5-JF, but the mission-equipped whole-aircraft planning premium closes at only ~28–35% because airframe and mission-system costs are substantially common.
- Superseded the E6REBASE1 `36–60 accepted / center ~48 / JF 75–85%` pilot-production band.
- New procurement posture: **144 common E6 Twin airframes firm-order class + 72 option**; exact signing date and service split remain replay-local.
- New 1940 acceptance planning band: **120–156, center ~144; JF 85–90%**, with Q1/Q2/Q3/Q4 cumulative bands ~18–24 / 48–66 / 84–114 / 120–156.
- The first service aircraft remain heavily instrumented/proving aircraft, but are lead aircraft from an already-committed production series rather than a pre-adoption evaluation handful.
- E6 Single remains research/requirement-dependent and is not bundled into Twin production.
- No combat clock, 1939 outcome, E5/Ki-42 OOB, E6 aerodynamic performance or D320F technical value changed.
