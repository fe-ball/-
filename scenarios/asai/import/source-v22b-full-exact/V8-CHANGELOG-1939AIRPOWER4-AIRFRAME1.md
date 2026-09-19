# V8 CHANGELOG — 1939AIRPOWER4 AIRFRAME1

## Scope
AIRPOWER4/AIRFRAME1 continues the piston-aviation audit without advancing the combat clock.
Source package: `ASAI-WORLDLINE-HANDOFF-2026-09-03-FULL-V8-1939AIRPOWER3-HOMARE1`.

## Main closure added
1. Confirmed that the package already contained substantial 1937-39 Hamilton/constant-speed propeller work; AIRPOWER4 does not duplicate or re-invent it.
2. Added high-power 1,800-2,200 hp propeller availability states `PA-D / PA-Q / PA-S` and cooling-installation states `CI-D / CI-Q / CI-S`.
3. Closed branch-neutral four-blade progression:
   - 1939H2 high-power pre-study;
   - 1940 component/full-engine rigs;
   - 1941 3.3-3.45 m / ~1,800 hp qualification path;
   - 1942 3.3-3.45 m practical Homare-class installation;
   - late 1942-1943Q1 3.6 m / 2,000-2,200 hp development/selected qualification path.
4. Preferred hydraulic governor/pitch actuation for V8 high-power combat-aircraft four-blade installations while preserving historical technology ancestry.
5. Preserved VDM production burden: Asai/QC can reduce reject/rework and type proliferation but does not erase intrinsic machining/man-hour cost.
6. Kept CFRP propeller work experimental; no early mass composite fighter propeller.
7. Connected propulsion to aircraft chronology:
   - J2M high-power prop/governor/cooling precursor;
   - B7A direct Homare + ~3.45 m carrier-airframe integration in 1942;
   - N1K1-J technically robust first-flight window in 1942Q4, current center Oct-Nov;
   - N1K2 redesign initiation around 1942Q4-1943Q1, later first flight still branch-sensitive;
   - Reppu-equivalent persistent 1941 predesign, but no automatic historical 1942 formal requirement;
   - Homare and Ha-43 Reppu installation paths remain parallel conditional branches.
8. Added explicit 1942 requirement/procurement replay gate so later technical readiness is not mistaken for a predetermined war-derived aircraft program.

## New authority files
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/15-HIGH-POWER-PROPELLER-COOLING-INTEGRATION-CANON-V8.md`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/16-PREBRANCH-HOMARE-HA43-AIRFRAME-INTEGRATION-CANON-V8.md`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/17-PREBRANCH-AIRFRAME-INTEGRATION-STATE-LEDGER-V8.tsv`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/18-1943Q1-PISTON-AIRFRAME-TECHNICAL-SNAPSHOT-V8.md`
- `50-CURRENT-1939-1941-AIRPOWER-AUDIT/19-1942-REQUIREMENT-PROCUREMENT-REPLAY-GATE-V8.md`

## Existing files updated
- root START-HERE files;
- `PACKAGE-STATE-V8.tsv`;
- `PRECEDENCE-2026-09-03-FULL-V8.tsv`;
- Shiden file 04 to use the tighter AIRPOWER4 N1K1-J integration window;
- fighter working file 08 to defer propeller chronology to file 15 while retaining numerical performance anchors;
- piston-engine rollup file 14 to hand off into files 15-19;
- state-machine file 10 to replace the stale "next carrier-fighter audit" pointer with the new 1942 requirement/procurement replay boundary.
- session-delta file 09 with an AIRPOWER4 supersession notice while preserving its original rollover text as provenance.

## Branch guard retained
AIRPOWER4 does not fix:
- historical-equivalent 17-Shi requirement date/text in this worldline;
- Ki-84-equivalent requirement existence/date;
- 1943+ first-flight/service dates that depend on those requirements;
- engine/propeller/airframe production quantities;
- carrier availability;
- frontline TBO/reliability distributions;
- wartime fuel/oil/material allocation;
- combat-derived program priority/cancellation.

## Combat clock
No combat-history advance.
Current revalidated combat checkpoint remains `1939-04-20 24:00`.
