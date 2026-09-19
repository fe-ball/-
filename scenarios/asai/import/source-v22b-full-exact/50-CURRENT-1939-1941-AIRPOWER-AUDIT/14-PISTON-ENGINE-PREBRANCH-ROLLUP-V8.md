# PISTON ENGINE PRE-BRANCH ROLLUP — V8 AIRPOWER4 AIRFRAME1

## Purpose
This file is a short machine/handoff bridge from detailed engine work to later aircraft/procurement work.
It does not choose the 1943+ war branch.

## Current engine-side closure
### Homare
- concept: late 1939;
- formal design: 1940Q1;
- first running: 1941Q1;
- first 300-hour endurance: 1941Q2;
- alternate-fuel/domestic-oil/bearing/altitude closure: 1941H2;
- 10/12 development-aircraft availability: 1942H1;
- formal main production window: 1942Q3;
- 20/21 qualified good-engine availability: late 1942–1943Q1;
- 1943Q1 good-engine center near 6.1 km: ~1,640–1,650 hp, broad ~1,600–1,680; ~1,700 is upper favorable case, not default.

### Ha-43
- pre-study: 1940Q3;
- formal design: 1941Q1;
- first complete engine: 1942Q1 central;
- base-engine development-flight availability: late 1942–1943Q1 plausible for a selected program;
- service qualification / production: not closed before replaying priority and war conditions;
- remote-turbo/Ru path is separate from the ordinary mechanically supercharged fighter-engine path.

## Mandatory aircraft-use fields
Any aircraft performance/procurement calculation using these engines must specify:
1. date;
2. engine model/configuration;
3. `EA-D / EA-Q / EA-S` state;
4. fuel map (`F-P / F-S / F-E / F-N`);
5. lubricant class (`L-P / L-Q / L-E`);
6. installed cooling/oil/propeller qualification state.

## Branch boundary
Safe to continue technical analysis without combat replay:
- prototype engine/airframe integration where requirement date is already established;
- propeller/cowl/oil-cooler feasibility;
- production-process readiness;
- alternate-engine comparison at a requirement gate.

Do not close without replay:
- 1943+ monthly engine/airframe output;
- frontline reliability/TBO distribution;
- theater fuel/oil quality;
- procurement quantities and priority allocation;
- requirement changes driven by combat after the branch point.


## AIRPOWER4 aircraft handoff
The engine-side closure above is now connected to the airframe side in files 15-18.

Key added state:
- 3.3-3.45 m high-power four-blade propeller installations are technically qualified by the 1942 Homare-aircraft window;
- 3.6 m / 2,000-2,200 hp installations exist as development/selected qualification hardware by late 1942-1943Q1, but serial priority remains open;
- B7A can provide direct Homare + large-four-blade carrier-airframe integration data from 1942Q2;
- N1K1-J first flight is technically robust in 1942Q4, center Oct-Nov on the current V8 path;
- N1K2 redesign can be active by 1943Q1 but its first flight is post-branch working only;
- Reppu-equivalent 1941 predesign is canon, while the formal 1942 requirement, engine selection and post-1943 flight/procurement outcome remain replay-dependent.

Read next:
1. `15-HIGH-POWER-PROPELLER-COOLING-INTEGRATION-CANON-V8.md`
2. `16-PREBRANCH-HOMARE-HA43-AIRFRAME-INTEGRATION-CANON-V8.md`
3. `17-PREBRANCH-AIRFRAME-INTEGRATION-STATE-LEDGER-V8.tsv`
4. `18-1943Q1-PISTON-AIRFRAME-TECHNICAL-SNAPSHOT-V8.md`
5. `19-1942-REQUIREMENT-PROCUREMENT-REPLAY-GATE-V8.md`
