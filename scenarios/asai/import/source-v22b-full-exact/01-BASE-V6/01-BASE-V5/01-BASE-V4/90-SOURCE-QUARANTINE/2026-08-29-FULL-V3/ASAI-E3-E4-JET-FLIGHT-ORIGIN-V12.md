# 浅井世界線：E3→E4 初期GT航空実証の再試算 V12

## Status
- Purpose: E3/E4から最初のjet飛行実証がどう立ち上がるかを、現行v48 core authorityと強チート/K-A-Bルールに接続して再構成する。
- Engine parents: FIXED-UPSTREAM.
- E3 direct-jet thrust, E4 pure-jet mass, aircraft mass/drag/range: DERIVED / SENSITIVITY.
- Exact first-flight dates, military contract dates, airframe names: OPEN / WORLDLINE-PROBABLE windows only.

## 1. Upstream fixed parents
- E3 (1928–29 technical front): PR3.5, TIT ~690C, compressor efficiency ~0.80, gross specific work ~77 kJ/kg. Historical-worldline text places meaningful stationary/bench prototypes around 300–500 hp class.
- E4 (1931–33): PR4.5, TIT ~710C, design flow 6.7 kg/s. Shaft industrial product ~507 kW; robust industrial dry product 0.80–0.90 t; core life parent 250–450 h.
- E4 pure-jet pre-audit shadow: ~300 kgf at 6.7 kg/s; high-flow 7.2 kg/s branch ~330 kgf. This is not yet a product rating.
- Current v48 aviation framework explicitly permits an E4 dedicated jet demonstrator and treats E4 fan/free-turbine work as a rig-research candidate.

## 2. E3: why research starts here but autonomous jet aircraft does not
A first-order Brayton/nozzle sensitivity at PR3.5/TIT690C gives static specific thrust roughly 380–430 N per kg/s after allowing for early losses. If the 300–500 hp E3 stationary core corresponds to roughly 4–6 kg/s class flow, a direct-jet rear end is therefore about 160–250 kgf static thrust.

That is enough to measure and to partly offset a flight pod's drag, but not enough to justify building a dedicated autonomous aircraft around the heavy late-1920s core.

### E3 likely hardware
1. stationary gas-generator rig;
2. replaceable rear end: free-power turbine / fixed convergent nozzle / crude ducted-fan load;
3. thrust stand and fuel-flow / pressure / temperature / vibration instrumentation;
4. late-E3 or E3→E4 transition: one captive/flying pod on an existing multi-engine mother aircraft.

Working E3 flight-pod envelope:
- engine/pod hardware: ~0.7–0.9 t (SENSITIVITY, not parent spec);
- fuel/instrument/mount: ~0.15–0.25 t;
- thrust: ~0.16–0.25 tf;
- powered test run: ~10–20 min normally; the mother aircraft remains fully capable of landing with the GT shut down.

Purpose is not aircraft performance. It closes inlet distortion, altitude mixture/fuel scheduling, lubrication return, vibration, thermal shielding, shutdown, and flight-vs-ground thrust correlation.

## 3. E4 aviationized pure-jet module
The E4 0.80–0.90 t parent is a robust industrial shaft product including hardware unnecessary to pure-jet flight. Removing the independent output turbine/output machinery and redesigning auxiliaries for short-duration aviation use gives a working pure-jet dry allowance of ~0.58–0.70 t. With inlet/nozzle/mount/firewall/flight accessories, installed propulsion is ~0.68–0.82 t.

This is deliberately conservative relative to E5 because E4 still carries early robust construction.

Working E4 J0/J1:
- thrust: 300 kgf standard shadow; 330 kgf high-flow shadow;
- installed propulsion: ~0.68–0.82 t;
- TSFC sensitivity: ~1.0–1.15 kg/(kgf h);
- full-thrust fuel flow: ~300–380 kg/h.

## 4. First E4 flight sequence
### 4.1 Airborne pod / flying laboratory
The first E4 flight article should remain a pod on a proven multi-engine mother aircraft.
- module + test fuel + instrumentation: ~0.85–1.05 t;
- powered periods: 10–25 min;
- engine may be started before takeoff initially; airborne restart can be a later test rather than a first-flight requirement.

This pays the flight-environment gates without coupling them to a new airframe.

### 4.2 Dedicated clean single-engine demonstrator
Once the pod has established stable flight operation, a purpose-built clean aircraft becomes high-information rather than reckless.

Representative point:
- loaded mass: 1.75–1.90 t (central 1.80 t);
- wing area: 12–13.5 m2 (central 12.5);
- E4 thrust: 300–330 kgf;
- clean Cd0 sensitivity: 0.022–0.025;
- CLmax: ~1.5;
- internal fuel: ~275–350 L = ~220–280 kg kerosene-type fuel;
- no armament; pilot + instrumentation only;
- simplest first arrangement: nose intake / short central duct / tail nozzle. A side-intake future-form airframe is a separate later experiment.

Representative derived performance at 1.80 t / 12.5 m2 / Cd0 0.023:
- 300 kgf: ~451 km/h sea-level level-speed sensitivity;
- 330 kgf: ~476 km/h;
- stall ~141 km/h;
- liftoff target ~162 km/h;
- first-order ground roll ~1.07 km at 300 kgf, ~0.91 km at 330 kgf;
- full-thrust endurance with 240 kg fuel: about 42–48 min before reserve; practical instrumented sortie ~25–35 min with margin.

This is already a striking 1931–33 research speed, but it is not a useful fighter: low thrust margin, long takeoff, short endurance, no payload.

## 5. E4 twin universal military-style testbed
A second aircraft branch should not chase speed. It should make the propulsion system look like a contemporary twin universal aircraft and provide reusable military-system space.

Representative point:
- loaded mass: 3.6–4.0 t (central ~3.8 t);
- wing area: ~26–28 m2;
- two modular nacelle stations;
- 2 x E4 pure jet: 600–660 kgf total;
- clean-ish test Cd0 ~0.028–0.031;
- two crew, cameras/radio/test ballast/optional dummy armament;
- generous fuel volume and accessible nacelles.

Representative 3.8 t / 27 m2 / Cd0 0.029:
- 600 kgf total: ~381 km/h;
- 660 kgf total: ~403 km/h.

Thus E4 pure-jet twin is NOT a speed wonder. Its value is system evidence: twin-engine installation, nacelle swaps, one-engine shutdown behavior, fuel/control duplication, camera/radio/weapon-bay integration, maintenance access, and customer familiarization.

The same center-fuselage/wing-box testbed can support different nacelle families over time rather than one literal universal engine mount:
- E4 shaft/free-turbine propulsive unit;
- E4 pure-jet pod;
- E4 crude aft-fan experimental pod;
- later E5 replacements.

## 6. E4 aft-fan: rig first, not first dedicated aircraft
Because E4 already possesses a free-power-turbine line, the protagonist can investigate fan propulsion before any historical turbofan date. However a first-order 500 kW-class free-turbine/fan calculation only yields a few hundred kgf of fan thrust unless a large cold mass flow is paid.

Working E4 aft-fan experimental envelope:
- static total thrust plausibly ~350–400 kgf class (SENSITIVITY only);
- complete propulsion likely approaches ~0.9–1.0 t once fan, duct, support and free turbine are included;
- therefore thrust gain over 300–330 kgf pure jet is not yet enough to compensate weight/diameter on a small autonomous aircraft.

Conclusion: E4 fan belongs on the ground rig and, at most, on the reusable twin flying testbed/pod. E5 is the proper first serious flight/product audit. This matches the current v48 framework without invoking a historical-date ceiling.

## 7. Worldline implementation implied by the numbers
### 1928–29 / E3
WORLDLINE-PROBABLE:
- Asai already knows the pure-jet / shaft / fan continuum conceptually.
- Rear-end comparison rigs are built while E3 remains a stationary prototype.
- Direct jet is recognized as technically real but too heavy/low-TW for a useful autonomous aircraft.
- A mother-aircraft pod program is authorized because it buys altitude/inlet/control evidence cheaply.

No military service-aircraft program is implied.

### 1929–31 / E3→E4 transition
WORLDLINE-PROBABLE:
- standardized flight-pod mounts, fuel/control lines and telemetry/instrument panels are created before the mature E4 engine;
- E3/transitional articles may be flown as captive pods;
- military technical observers can see data, but the program remains Asai-led R&D.

### 1931–32 / early E4
WORLDLINE-PROBABLE:
- E4 pure-jet module flies first as a pod;
- after stable flight operation, the clean single demonstrator is authorized;
- first dedicated jet aircraft is a research/record machine, not a service prototype.

### 1932–33 / mature E4
WORLDLINE-PROBABLE:
- clean E4 demonstrator reaches roughly mid-400-km/h class and proves a propellerless high-speed path;
- reusable twin universal testbed begins military-system work even though its E4 jet performance is merely contemporary;
- fan/free-turbine experiments remain rig/pod work;
- Army/Navy interest is therefore funding/access/requirements study, not immediate adoption.

The crucial institutional result is that by the time E5 appears, Japan is not asking whether a jet can fly. It already has flight data, trained test pilots, pod/nacelle practice, fuel/control/maintenance procedures, and two airframe philosophies ready to accept the new engine.

## 8. What changes when E5 arrives
Do not close E5 here, but the direction is forced:
- clean demonstrator receives 430–470 kgf-class E5 and enters ~550–600 km/h sensitivity territory;
- the twin universal testbed can replace nacelles rather than create a new institution from zero;
- E5 aft-fan is now worth a real installed/flight audit;
- this is where military joint high-speed / recon / interceptor interest can become a product decision.

## 9. Closure state
CLOSED/KEEP:
- E3 begins the aviation evidence chain as ground/rear-end research, not as a useful autonomous jet aircraft.
- E4 is the first credible autonomous jet-flight generation.
- sequence: ground rig -> mother-aircraft pod -> clean dedicated demonstrator -> reusable twin systems testbed.
- E4 fan is research/pod, not yet the main autonomous aircraft branch.

DERIVED WORKING:
- E3 direct-jet ~160–250 kgf;
- E4 pure-jet dry ~0.58–0.70 t, installed ~0.68–0.82 t;
- E4 clean single ~1.8 t / 300–330 kgf / ~450–475 km/h;
- E4 twin testbed ~3.8 t / 600–660 kgf / ~380–405 km/h.

OPEN:
- exact first-flight calendar date;
- exact mother-aircraft type;
- exact E4 pure-jet installed mass and TSFC product audit;
- exact clean-airframe drag and altitude thrust map;
- E5 replacement chronology and first military contract.
