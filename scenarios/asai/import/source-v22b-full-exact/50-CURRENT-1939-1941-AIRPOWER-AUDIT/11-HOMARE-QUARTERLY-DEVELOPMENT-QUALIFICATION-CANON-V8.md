# HOMARE QUARTERLY DEVELOPMENT / QUALIFICATION CANON — V8 AIRPOWER3 HOMARE1

## Status / authority
This file closes the **branch-neutral engine-side Homare development path through 1943Q1** at quarter-level resolution.

It does **not** close:
- post-1943 combat history;
- monthly production quantities;
- theater fuel/lubricant availability;
- fleet-wide overhaul life or sortie reliability;
- final aircraft procurement/allocation;
- exact installed-aircraft performance.

Where this file conflicts with `07-HOMARE-DEVELOPMENT-SERVICE-PERFORMANCE-AUDIT-V8.md`, this file wins for:
1. quarter-by-quarter development state;
2. fuel/lubricant qualification sequencing;
3. the distinction between development-flight, service-qualified and series-repeatable engine availability;
4. the 1943Q1 branch-neutral technical-maturity checkpoint.

The purpose is to make later aircraft work mechanical: an airframe may only use a Homare state that actually exists at its design/flight date.

---

## 1. Historical anchor — CLOSED
Historical Homare development was already exceptionally rapid and must not be rewritten as a failed prewar design program.

Reference-history anchor:
- late 1939: next-engine concept work after Sakae 20 maturation;
- spring 1940: formal design begins;
- end March 1941: first engine test operation/performance test completed;
- end June 1941: first 300-hour durability test completed;
- early Homare: about 1,800 hp at 3,000 rpm and +350 mmHg boost;
- subsequent Model 20: about 2,000 hp at 3,000 rpm and +500 mmHg boost;
- September 1942: production release.

The later historical cliff was not one single defect. It combined:
- a shift from a 100-octane design premise toward roughly 88–92 motor-octane service fuel;
- domestic lubricant substitution;
- abnormal cylinder-temperature behavior;
- main connecting-rod bearing failures;
- high-altitude oil-pressure loss;
- intake-port casting/core deformation;
- distributor-case and supercharger-inlet geometry problems;
- vibration/service difficulty;
- worsening materials, labor and production conditions.

Therefore the V8 divergence remains: **similar design calendar and headline design output, but earlier alternate-condition qualification and much better prototype-to-series replication.**

---

## 2. Fixed physical severity — CLOSED
Use the Homare 20/21 family as approximately:
- 18 cylinders, two-row radial;
- bore × stroke: 130 × 150 mm;
- displacement: ~35.9 L;
- diameter: ~1.18 m;
- Homare 21 mass reference: ~830 kg;
- maximum-power speed: ~3,000 rpm.

Useful severity checks:
- mean piston speed at 3,000 rpm: ~15.0 m/s;
- 1,800 hp at 3,000 rpm corresponds to ~15.0 bar BMEP;
- 2,000 hp at 3,000 rpm corresponds to ~16.6 bar BMEP;
- 2,000 hp is ~55.7 hp/L.

These values explain why V8 cannot simply declare the engine easy because better bearings, oil tests or supercharger maps exist. Homare remains a compact, high-speed, high-BMEP 18-cylinder engine with severe crank, bearing, thermal, induction and manufacturing sensitivity.

Do not create a V8 power bonus merely from better technology. The principal gain is that a larger fraction of engines can safely realize the intended rating.

---

## 3. V8 intervention topology — CLOSED
### 3.1 Already available before formal Homare design
By 1940 Nakajima can draw on the Asai-derived domestic technology shelf for:
- knock mapping versus boost / ignition / mixture / intake temperature / fuel grade;
- water or water-methanol ADI test practice;
- corrected centrifugal-compressor maps;
- cylinder-by-cylinder thermal measurement practice;
- high-load multilayer bearing candidates and surface-treatment knowledge;
- crankpin roundness/roughness/grinding standards;
- oil aeration, pump-suction, filtration and altitude-related test methods;
- dynamic balancing and torsional-vibration instrumentation;
- master gauges, critical-dimension control, lot traceability and acceptance testing.

### 3.2 Still unique to Homare hardware
The shelf cannot know in advance:
- 18-cylinder mixture maldistribution;
- exact front/rear-row cooling interaction;
- master-rod/articulated-rod distortion and edge loading;
- Homare crankshaft torsional eigenmodes;
- full-engine reduction-gear behavior;
- steel-crankcase distortion/sealing behavior;
- exact intake-casting core deformation;
- aircraft-specific cowl, oil cooler, propeller and exhaust interactions.

These must still be discovered by rigs, complete engines and aircraft.

### 3.3 Correct V8 causal claim
V8 changes the **search order, instrumentation, alternate-condition preparation and production replication**.
It does not replace Homare development with foreknowledge of Homare-specific geometry.

---

## 4. Operating-map architecture — CLOSED PRINCIPLE
From formal design onward the engine program carries multiple operating maps rather than one nominal rating followed by emergency redesign.

Use four map families:

### F-P — premium design map
- approximately 100-octane-class fuel;
- used to establish maximum design capability and margin;
- ADI available above the relevant boost threshold.

### F-S — standard service map
- approximately 92-class fuel;
- ADI integrated from the start as part of the high-output system;
- main objective: retain ordinary rated/combat power with known limits, not duplicate premium margin everywhere.

### F-E — emergency low-grade map
- approximately 88–90-class fuel with ADI;
- known derating/boost-stop schedule;
- intended to preserve a healthy, predictable engine rather than nominally claim 2,000 hp.

### F-N — low-grade / no-ADI survival map
- major boost restriction;
- ferry, training, return-to-base or supply-emergency use;
- not normal maximum-combat operation.

Exact horsepower penalties for F-E/F-N are **not canonized** before the relevant full-engine tests. The older 15–25% derating figure remains only a broad working sensitivity band, not an automatic multiplier.

---

## 5. Lubricant architecture — CLOSED PRINCIPLE
Continue the V8 lubricant classes:
- `L-P Premium`: imported first-class or genuinely equivalent certified oil;
- `L-Q Qualified Domestic`: domestic mass-service aviation oil that passes V8 acceptance limits;
- `L-E Emergency`: substitute / unstable / doubtful-quality lots.

Key rule:

> Lubricant quality mainly changes allowable duration, bearing distress, oil-system margin and overhaul life. It does not automatically subtract a fixed percentage from instantaneous dynamometer horsepower.

A high-power setting may be physically achievable on L-E and still be prohibited by the service map.

---

## 6. Homare availability grades — CLOSED STATE MACHINE
Later aircraft files must distinguish these states.

### `EA-D` — development-flight engine available
The engine can safely power prototype/development aircraft under manufacturer support and restrictive inspection rules.
It need not yet be ready for squadron issue or broad production.

Minimum gates:
- stable complete-engine running;
- major vibration bands mapped;
- development endurance passed at relevant rating;
- known fuel/oil map for the test aircraft;
- installation-specific oil/cooling checks begun.

### `EA-Q` — service-qualified engine available
The model has a defined approved operating envelope for specified fuel/oil classes and has passed engine + installation qualification appropriate to service use.

### `EA-S` — series-repeatable engine available
Production lots can reproduce the qualified configuration with controlled variance.
This requires production-process evidence, not merely a successful prototype.

An airframe can fly on `EA-D` before `EA-Q` or `EA-S` exists.
This distinction is mandatory in later Reppu/N1K/B7A/C6N/P1Y work.

---

# 7. Quarter-by-quarter development closure

## 1939Q4 — concept architecture
### Engine program
- Sakae 20 maturation releases direct Nakajima team attention toward the next compact high-output radial.
- Homare concept work is active; no finished Homare hardware exists.
- 1,800 hp-class first objective and ~2,000 hp growth objective are reasonable program targets.

### V8 delta
Before detailed design, the team receives the relevant domestic technology shelf as **test/specification methods**, not a finished engine design.

Program requirement already includes:
- premium + standard + emergency fuel maps;
- ADI provision;
- explicit oil-class qualification;
- crank/bearing surface and dimensional acceptance planning;
- torsional/balance measurement points;
- production critical-to-function dimensions.

### Availability
- `EA-D = NO`
- `EA-Q = NO`
- `EA-S = NO`

---

## 1940Q1 — formal design start
### Combustion / fuel
- formal chamber, compression, ignition and boost studies proceed around the premium rating;
- standard-fuel and ADI cases are specified simultaneously rather than deferred until a later crisis;
- cylinder-to-cylinder distribution is recognized as a future complete-engine gate.

### Bearing / crank
- available high-load bearing families narrow material search rapidly;
- crankpin finish, roundness, journal geometry and bearing-clearance measurement are declared critical dimensions from drawing issue.

### Lubrication
- a total lubrication schematic is produced, as historically, but V8 adds explicit pump-suction, aeration, pressure-loss and altitude-sensitivity test plans before flight.

### Supercharger / induction
- corrected compressor-map practice is applied to supercharger design;
- intake temperature and worst-cylinder mixture are explicit constraints.

### Vibration / reduction
- torsional measurement points and test procedures are designed into the prototype program;
- no natural frequency is assumed known in advance.

### Production
- design engineering and production engineering begin in parallel;
- intake-port geometry and casting-core location are tagged as critical-to-performance rather than ordinary foundry geometry.

### Availability
No complete engine yet.

---

## 1940Q2 — component-rig convergence
### Combustion / fuel
- single-cylinder or representative-cylinder firing work expands premium/standard fuel knock maps;
- ADI nozzle/flow concepts are compared;
- spark-plug heat range and ignition scatter are explicitly instrumented.

### Bearing / crank
- bearing rigs compare material/overlay candidates, oil temperature, clearance, surface finish and deliberately introduced misalignment;
- the program learns the difference between material failure and edge-loading/geometry failure before complete-engine endurance testing.

### Lubrication
- pump capacity alone is rejected as a sufficient safety criterion;
- suction depression, entrained air, scavenge return, oil heating and filter restriction receive separate rig cases.

### Supercharger / induction
- compressor efficiency and inlet geometry are mapped;
- mixture-distribution hardware remains provisional because the final 18-cylinder manifold still matters.

### Vibration / reduction
- component inertia data and reduction-gear test preparations mature;
- four-blade/high-power propeller rig work is a parallel enabling program, not part of Homare certification itself.

### Production
Critical-to-quality (`CTQ`) list is issued for at least:
- intake-port/core geometry;
- supercharger inlet geometry;
- crankpin roundness/roughness;
- bearing clearance/crush and rod geometry;
- gear tooth contact/hardness;
- impeller balance;
- ignition/distributor timing geometry;
- oil drilling/orifice geometry.

---

## 1940Q3 — prototype manufacture / supplier qualification
### Main change from reference history
The engine is **not** materially earlier, but more of the eventual production process is being proved alongside prototype manufacture.

### Bearing / crank
- crankpin process sheets contain measured finish/roundness limits;
- multilayer/overlay bearing candidates are available, but final Homare specification remains test-selected rather than predetermined by Asai.

### Lubrication
- complete-engine oil-flow targets are converted into component acceptance checks;
- pressure pickups are placed to identify where pressure is being lost rather than observe only one system pressure.

### Induction / production
- master/core gauges are prepared for critical intake passages;
- representative castings are sectioned/flow-checked to verify that the drawing survives foundry production.

### Vibration
- prototype instrumentation for crank/gear/engine vibration is prepared.

### Availability
Still no aircraft engine.

---

## 1940Q4 — first-engine assembly preparation
### Engine state
- first full engine(s) approach assembly/testing;
- supplier components such as the steel crankcase and ignition system remain real long-lead integration items.

### V8 guard
Do **not** pull first full operation into 1940 merely because component science is better. Reference history already executed the program at extraordinary speed.

### Fuel / oil
- premium and standard-fuel control schedules exist on paper/rig evidence;
- full 18-cylinder validation remains open;
- L-P/L-Q comparison oil testing is active.

### Production
At least one production-intent second-set of critical castings/parts should be built rather than allowing a unique hand-fitted prototype to become the only reference article.

---

## 1941Q1 — first full-engine running
### Historical anchor
First operation/performance test is centered around March 1941.
V8 may move individual subtests by weeks, but **central first-run timing remains Q1 1941**.

### Expected first-wave Homare-specific findings
Allow real problems:
- front/rear cylinder temperature scatter;
- mixture-distribution scatter;
- RPM/load-specific vibration bands;
- master-rod bearing edge-loading signatures;
- reduction/accessory resonances;
- oil return/pressure behavior that component rigs did not reproduce exactly.

### V8 difference
These appear as categorized measurements rather than a generic “engine unreliable” result.
Root-cause work begins immediately by subsystem.

### Power
- ~1,800 hp-class development output is legitimate;
- headline power is not increased merely because diagnosis is better.

### Availability
- bench-development state only;
- `EA-D = NO` until endurance and installation gates are sufficiently closed.

---

## 1941Q2 — first 300-hour endurance closure / 2,000 hp branch
### Historical anchor
The first 300-hour durability program completed by the end of June 1941; the subsequent 20-series reached ~2,000 hp/+500 mmHg class.

### V8 interpretation
The central date need not move. The gain is that more useful knowledge has accumulated by the same date:
- bearing wear is correlated with actual crankpin finish and deflection;
- oil aeration/temperature/pressure traces are retained by configuration;
- worst-cylinder CHT/mixture is tracked;
- vibration maps are tied to RPM/load/propeller inertia;
- production-intent parts are compared with prototype parts.

### Bearing revision
A plausible V8 sequence is:
1. viable multilayer material already available;
2. endurance reveals Homare-specific edge loading/deflection;
3. journal surface quality and bearing end relief are revised;
4. soft-overlay selection is finalized from Homare data.

Thus the historical search for a viable bearing solution is shortened, but an engine-specific geometry revision still occurs.

### Fuel
- premium 1,800/2,000 hp development points are demonstrated;
- F-S standard-fuel full-engine qualification is still in progress rather than assumed equivalent.

### Availability
- `EA-D` becomes plausible for tightly supported engine/aircraft development late in Q2 or Q3, depending on installation.
- `EA-Q = NO` for broad service.
- `EA-S = NO`.

---

## 1941Q3 — alternate-fuel / domestic-oil full-engine closure
This is one of the largest V8 divergences.

### Fuel / thermal
If Army/Navy policy imposes lower-octane fuel in 1941 as in the reference history, Nakajima is **not beginning from zero**.
The service change activates an existing test branch.

Full-engine work still finds Homare-specific distribution issues, but the solution space is already known:
- revise ADI distribution/atomization;
- reshape carburetor-to-supercharger flow route;
- correct worst-cylinder mixture;
- adjust spark-plug heat range and ignition schedule;
- define fuel-grade-specific boost stops.

The historical abnormal cylinder-temperature episode is therefore reduced from a broad redesign crisis to a qualification/tuning problem, although failures during test remain plausible.

### Bearing / oil
- L-Q domestic oil is run deliberately at hot/high-load conditions;
- bearing end relief, crankpin finish and overlay revisions are frozen only after L-Q testing;
- oil chemistry cannot be solved by geometry, so poorer L-Q lots may still shorten life.

### High-altitude lubrication
Asai-derived practice makes high-altitude oil-pressure loss a named hazard before aircraft service.
Bench simulation of suction/aeration is used, but flight remains necessary because installation attitude, tank head and cooling affect the real system.

### Availability
- `EA-D = YES` for selected development aircraft with specified fuel/oil and manufacturer support.
- `EA-Q` remains installation/model dependent.

---

## 1941Q4 — flight/installation qualification and production drawing stabilization
### Lubrication
A high-altitude flight oil-pressure anomaly is still allowed.
The V8 difference is response speed:
- pressure pickup data distinguish pump-suction/aeration from bearing leakage;
- oil quantity, tank head, scavenge return, pickup geometry, restrictors and cooling are changed selectively;
- fixes are re-run against L-Q oil, not only premium oil.

### Vibration / propeller
Aircraft propeller inertia and cowl/accessory configuration may expose modes not seen on the bench.
No zero-vibration assumption is allowed.
Dangerous operating bands are identified and hardware/control changes made where required.

### Production drawings
Production-intent revisions explicitly lock:
- critical intake-port/core profiles;
- supercharger inlet geometry;
- distributor/ignition alignment;
- crankpin surface/roundness;
- bearing geometry/clearance;
- oil-system drillings/orifices;
- balance limits and acceptance method.

### Branch neutrality
Whether war/sanctions have already worsened fuel/oil supply changes which map is operationally important, but does not change the engine-side fact that alternate maps now exist.

---

## 1942Q1 — pilot/pre-series production
### Production gate
This quarter is dominated by proving that engines built as a process, not as engineering prototypes, reproduce the design.

Required V8 production controls:
- intake/core master gauges;
- foundry process checks and sectioned/sample castings;
- sample intake flow testing;
- crank/bearing/gear go/no-go and measurement records;
- hardness/case-depth checks where applicable;
- dynamic-balance acceptance;
- corrected dynamometer maps by engine serial/lot;
- lot traceability back to critical castings/bearings/gears;
- explicit rework/quarantine path.

### Critical consequence
The historical production-engine mystery “does this engine actually make the specified power?” should become a **lot-detection event**, not a fleet-wide diagnostic surprise.
A malformed intake-core lot can still occur; it is detected and quarantined much earlier.

### Availability
- 1,800 hp-class 10/11/12-series `EA-D`: YES for development-aircraft allocation.
- `EA-Q`: emerging for specific installations.
- `EA-S`: pilot/pre-series only.

---

## 1942Q2 — development-aircraft grade becomes routine
### 10/11/12-series
A good, correctly supplied engine can reasonably realize approximately:
- takeoff: ~1,780–1,825 hp class;
- near 6 km: ~1,500–1,560 hp class.

These are **good-lot realization bands**, not a claim that every field installation always delivers them.

### Fuel/oil
Service manuals now specify combinations rather than one nominal horsepower number:
- F-P + L-P/L-Q;
- F-S + ADI + L-P/L-Q;
- emergency derated schedules for inferior fuel/oil.

### Aircraft interface
A new prototype aircraft needing ~1,800 hp can receive a credible development engine without waiting for 1943.
The airframe still owns:
- cowl pressure recovery;
- oil-cooler sizing;
- exhaust routing;
- propeller match;
- local vibration;
- fuel/ADI tank and control integration.

### Availability
- 10/12 `EA-D = YES` routinely for priority development programs.
- 10/12 `EA-Q = installation-dependent YES`.
- 10/12 `EA-S = LIMITED / pilot-series`.

---

## 1942Q3 — formal series release window
### Historical anchor
Reference production release was September 1942.

### V8 central closure
Keep formal main-production release in **1942Q3, center August–September**.
Do not move mass production into 1941.

A one-quarter advantage is permissible only as limited pre-series acceptance, not as mass output.

### Production quality
The principal V8 claim is variance control:
- low-output engines caused by intake-core or inlet-geometry deformation are much less likely to escape as accepted full-rated engines;
- bearing distress is traceable to material/finish/clearance lots;
- an engine that misses its corrected rating is reworked, derated or rejected rather than counted as nominally identical.

### 20/21-series
2,000 hp-class development/qualification continues in parallel.
Do not assume every 20/21 engine is series-mature just because the design rating has been demonstrated.

### Availability
- 10/12 `EA-S = YES`, initially with normal early-series caution.
- 20/21 `EA-D = YES` for selected programs as individual qualified engines become available.

---

## 1942Q4 — early-series stabilization / 2,000 hp qualification
### 10/12-series
The early series should no longer show the reference-history scale of unexplained engine-to-engine power scatter under intact production conditions.
Failures still occur, but they are more often identifiable by subsystem/lot.

### 20/21-series
Working engine-side envelope for good development/qualification engines:
- takeoff/emergency: ~1,900–2,000 hp depending on map, fuel/oil and qualification status;
- near 6 km: ~1,580–1,650 hp during the transition toward the 21-series service configuration.

The exact series designation at a given aircraft program date must be checked; do not use “Homare 21” as a generic name for every 2,000 hp development engine.

### Aircraft implication
A late-1942 fighter prototype can legitimately expose **airframe** limitations rather than being dominated by a chronically underperforming one-off engine.
This does not eliminate cowl/oil-cooler/propeller problems or the aircraft’s own landing gear/aerodynamic issues.

---

## 1943Q1 — branch-neutral technical-maturity checkpoint
This is the last point this file closes strongly without requiring the 1943 combat/production branch.

### What is now technically available
For a good, qualified 20/21-series configuration with suitable fuel/oil and a competent installation:
- takeoff/emergency class: ~1,950–2,000 hp;
- low-altitude rated power remains ~1,800+ hp class;
- near ~6.1 km: **center ~1,640–1,650 hp**, broad good-engine band ~1,600–1,680 hp;
- ~1,700 hp at ~6 km is an upper favorable case, not the default center.

The historical Homare 21 reference rating around 1,625 hp at ~6.1 km remains the hard anchor; V8’s upper realization comes from better compressor/induction/mixture/production realization, not a new nominal 2,200 hp rating.

### What “mature” means here
By 1943Q1 V8 may canonize:
- a technically mature engine specification exists;
- the critical production process is known;
- correctly equipped plants can reproduce good engines;
- standard-fuel/ADI and domestic-oil operating schedules are known;
- the engine can be allocated to new prototype/service-trial aircraft without treating it as an experimental science project.

Do **not** canonize yet:
- national monthly output;
- percentage of all engines meeting the best band;
- fleet-wide TBO;
- theater sortie reliability;
- whether L-P/L-Q fuel/oil actually reach each unit;
- which aircraft receives priority;
- whether labor/material degradation begins, and when.

Those are 1943+ history/NC inputs.

---

# 8. Subsystem closure by 1943Q1

## 8.1 Fuel / combustion / ADI — CLOSED ENGINE-SIDE
Closed:
- multiple fuel maps are designed from 1940 rather than improvised after the fuel crisis;
- 92-class + ADI is a deliberate service branch;
- lower-grade operation has defined boost restrictions;
- worst-cylinder thermal/knock behavior drives the limit.

Open later:
- actual fuel-grade distribution by theater/date;
- whether premium stocks are concentrated on particular units.

## 8.2 Main rod / crank / bearing — CLOSED DEVELOPMENT MECHANISM
Closed:
- viable high-load bearing material/surface families exist before Homare;
- Homare-specific edge loading/deflection still appears in testing;
- crankpin finish, end relief/geometry, overlay and clearance are solved as an integrated tribology problem;
- production inspection prevents gross process drift from being invisible.

Open later:
- life under degraded oils/material substitutions;
- field maintenance quality.

## 8.3 Lubrication — CLOSED DESIGN / QUALIFICATION METHOD
Closed:
- oil flow, suction, aeration, temperature, scavenge and altitude behavior are separate test gates;
- L-P/L-Q/L-E operating classes exist;
- high-output duration can be restricted by oil class without changing the nominal engine rating.

Open later:
- service TBO and failure rate under actual 1943+ supply.

## 8.4 Supercharger / induction — CLOSED NEAR-TERM PATH
Closed:
- mechanical supercharging remains the ordinary Homare path;
- corrected maps and inlet/port geometry are production-controlled;
- mixture distribution is validated by worst cylinder;
- a malformed intake-core lot is treated as a manufacturing defect, not accepted as normal Homare behavior.

Open later:
- exact 21/22/23 variant timing by application;
- turbo mission branches.

## 8.5 Vibration / reduction — CLOSED METHOD, INSTALLATION-SPECIFIC RESULT
Closed:
- torsional modes must be measured;
- bench + propeller-inertia + aircraft tests are separate gates;
- dangerous bands and balance tolerances are recorded.

Open later:
- final vibration map for each propeller/airframe combination.

## 8.6 Production replication — CLOSED AS PRIMARY V8 DIVERGENCE
Closed:
- prototype drawings are not sufficient for series acceptance;
- CTQ geometry, flow, finish, hardness, balance and corrected output are lot-controlled;
- engine serial/lot records are tied to field returns.

Open later:
- how well factories retain this process under 1943+ manpower/material/bombing conditions.

---

# 9. Acceptance policy — CLOSED METHOD / NUMBERS WORKING
Do not accept a production Homare solely because it runs and reaches takeoff rpm.

Each full-rated production engine should have an acceptance record including:
1. corrected power at specified test points;
2. oil pressure/temperature and scavenge behavior;
3. worst-cylinder temperature spread;
4. vibration/balance limits;
5. ignition/mixture checks;
6. leak/consumption checks;
7. serial linkage to critical bearing/crank/casting/gear lots.

Working disposition logic, **not a historical specification**:
- full-rating acceptance: engine reaches the specified corrected map within the program’s measurement/tolerance band and passes all thermal/oil/vibration limits;
- limited-rating disposition: engine is mechanically healthy but misses a high-rating gate; it may be reworked or explicitly derated;
- reject/rework: unexplained power deficit, critical vibration, bearing distress, oil instability or CTQ geometry failure.

Do not invent a universal fixed ±3% acceptance tolerance until contemporary Nakajima/Asai measurement capability is separately audited.

---

# 10. Reliability / life guard — CLOSED
The historical 300-hour development endurance test is **not the same thing as a 300-hour frontline TBO**.

Before the 1943 branch is played, do not assign one canonical service life such as “Homare = 200 h”.
Service life depends on:
- fuel map used;
- oil class;
- emergency-boost frequency;
- cooling installation;
- dust/contamination;
- maintenance labor and spares;
- production lot;
- mission cycle.

The correct V8 early-1943 claim is qualitative but strong:

> Under intact L-P/L-Q supply and controlled production, Homare no longer has to be treated as intrinsically unable to hold its qualified rating. Under degraded supply/production, the same design can still deteriorate sharply.

This is deliberately compatible with later NC/war branching.

---

# 11. Aircraft-interface gates through 1943Q1 — CLOSED SEMANTICS
### By 1942Q2
A priority new aircraft may receive a credible ~1,800 hp-class Homare `EA-D` engine.
This does not mean the aircraft is service-ready.

### By 1942Q3-Q4
10/12-series engines are series-repeatable enough to support real aircraft-development programs.
A late-1942 fighter prototype using Homare 11-class power is therefore plausible without assuming constant engine failure.

### By 1942Q4-1943Q1
Selected ~2,000 hp-class 20/21 development/qualification engines can support prototypes and service trials.
A program requiring these engines must still reserve actual engines and complete its own propeller/cooling/oil/exhaust integration.

### Mandatory future rule
For every aircraft, write separately:
- `engine_model/date`;
- `engine_availability_grade (EA-D / EA-Q / EA-S)`;
- `fuel_map`;
- `oil_class`;
- `installed qualification state`.

Do not use one generic “Homare 2,000 hp” token.

---

# 12. Turbo branch — BOUNDED, NOT MAINLINE
Homare turbo work remains historically grounded and V8 can begin integration earlier because Asai turbo/control/oil-system experience exists.

However the turbo branch is not permitted to distort ordinary Homare maturation.
Keep separate:
- ordinary mechanically supercharged Homare used by the majority of fighter/attack programs;
- mission-selective turbo Homare for high-altitude reconnaissance/interception.

A turbo engine requires a second aircraft-level qualification path for:
- exhaust collectors;
- turbine/wastegate;
- ducting/intercooling where used;
- fire protection;
- altitude fuel/boost control;
- installation mass/drag/maintenance.

Do not count turbo availability as ordinary Homare `EA-Q`.

---

# 13. Canon summary
The Homare path through 1943Q1 is now:

`late-1939 concept`
-> `1940Q1 formal design with multi-fuel/oil/production test architecture`
-> `1941Q1 first running`
-> `1941Q2 300-hour / 1,800 hp closure and 2,000 hp development branch`
-> `1941H2 full-engine low-octane/domestic-oil/altitude/bearing closure`
-> `1942H1 pilot/pre-series and development-aircraft availability`
-> `1942Q3 formal main production window`
-> `1942Q4 early-series stabilization + 2,000 hp qualification`
-> `1943Q1 technically mature, reproducible good-engine specification exists`.

The key counterfactual is **not earlier headline horsepower**.
It is that the problems Nakajima historically encountered after the very successful prototype program are encountered earlier, classified correctly, tested against alternate fuel/oil, and incorporated into production controls before they become an opaque fleet-wide cliff.

---

## Source basis used for this closure
Primary/high-authority anchors:
- Ryoichi Nakagawa & Sotaro Mizutani, “Engine Fuels and Lubrication Systems at Nakajima Aircraft Co. from 1936–1945,” SAE Technical Paper 881610 (1988), DOI 10.4271/881610.
- Ryoichi Nakagawa, *From Aircraft to Automobiles and Automotive Electronics: Remembrances of an Internal Combustion Engineer*, SAE SP-826 (1990).
- Smithsonian National Air and Space Museum collection records for Nakajima Homare 12 and Homare 21 engines.

Secondary cross-checks are used only where the primary records do not provide a specific aircraft/model chronology.
