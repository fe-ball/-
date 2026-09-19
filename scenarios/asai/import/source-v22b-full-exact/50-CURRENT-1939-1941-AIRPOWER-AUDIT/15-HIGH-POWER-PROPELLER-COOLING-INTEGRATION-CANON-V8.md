# HIGH-POWER PROPELLER / COOLING INTEGRATION — CANON V8 AIRPOWER4

## Status
**CANON for branch-neutral technology availability and integration sequencing through 1943Q1.**

This file does **not** reopen the already-audited 1937-39 Hamilton/constant-speed-propeller history.
Older V6/V7 material already established:
- Sumitomo Hamilton-family variable/constant-speed metal propellers;
- Nippon Gakki Army-side Hamilton production preparation;
- three-blade constant-speed adoption and production ramp;
- Asai drawing/tool/gauge/QC support;
- prior P0-P3 propeller-control/material work, including feathering/negative-torque work for later turboprop applications and experimental CFRP blades.

The new scope is only the step from that base to **1,800-2,200 hp-class piston engines, 3.3-3.6 m four-blade propellers, high-power governors/reduction gears, radial-engine cooling and oil-system integration**.

## 1. Historical anchors retained
Use the following as hard or strong historical anchors rather than inventing a new Japanese propeller industry:

- Sumitomo acquired Hamilton Standard variable-pitch rights and was prototyping by about 1937; Nippon Gakki prepared Army Hamilton production in 1938.
- Japanese propeller output rose to roughly 4,033 units in 1939, including about 1,466 Sumitomo and 2,567 Nippon Gakki units; roughly two-thirds of fixed/variable metal units in the cited 1939 requirement mix were three-blade.
- Sumitomo also acquired VDM rights in the late 1930s. Historical series use of VDM-family high-power propellers became important in the 1942+ period.
- A surviving Sumitomo/VDM four-blade Homare propeller associated with N1K has a diameter of 330.2 cm.
- A surviving Sumitomo/VDM four-blade Homare propeller associated with B7A has a diameter of 345.4 cm.
- Historical J2M2 used a roughly 3.3 m four-blade Sumitomo VDM constant-speed propeller; the preceding J2M1 electric pitch mechanism was considered unreliable and the J2M2 path changed to hydraulic actuation.
- USSBS judged the VDM type substantially more labor-intensive than the older Hamilton family, quoting roughly 70 percent more man-hours and noting alloy/operational difficulties. It also found that proliferation of many propeller sizes hurt capacity utilization.

Therefore V8 does not need a fictional 1940 invention of four-blade propellers. The divergence is earlier and better **qualification, control, standardization and reproducibility** for the high-power class.

## 2. New availability-state semantics
Do not say merely that a propeller "exists".

### `PA-D` — Propeller Available for Development
A hub/blade/governor/reduction combination can be run on a full engine and fitted to a development aircraft with an explicit power/rpm/speed limitation.
This can support prototype flight. It is not a service release.

### `PA-Q` — Propeller Installation Qualified
The specified engine-propeller-airframe combination has passed representative overspeed, vibration, pitch-change/governor, climb, high-speed and engine-out/control tests for a defined operational envelope.

### `PA-S` — Propeller Serial-Reproducible
The blade/hub/governor family, tooling, inspection gauges and acceptance procedure are frozen enough that accepted serial units can reproduce the qualified envelope.
`PA-S` does **not** mean unlimited national quantity.

Cooling/oil installation is tracked separately:

### `CI-D` — Cooling Installation Development
Ground and limited flight installation exists with instrumentation for cylinder-head temperature, oil inlet/outlet temperature/pressure, cowl pressure and climb/high-speed points.

### `CI-Q` — Cooling Installation Qualified
The installation closes representative hot-day climb, sustained high power, high-speed, ground/taxi and altitude oil-pressure cases without relying on a single hand-tuned prototype.

### `CI-S` — Cooling Installation Serial-Reproducible
Cowl baffling, duct/seal geometry, oil-cooler installation and acceptance checks are frozen for serial manufacture.

Engine `EA-*`, propeller `PA-*` and cooling `CI-*` states must all be stated for any later aircraft chronology.

## 3. V8 high-power propeller development path
### 1939H2 — pre-study
Branch-neutral and **closed**:
- Sumitomo/VDM licensing and foreign-design access already make a four-blade hub a known engineering object rather than a clean-sheet invention.
- Asai-supported work can begin on high-power blade-root stress, hub pitch-change loads, governor response, reduction-ratio matching, overspeed protection and torsional instrumentation.
- The intended class is initially 1,500-1,800 hp; 2,000+ hp is a growth envelope, not a 1939 production requirement.

State: no general `PA-D` for the 2,000 hp class yet.

### 1940H1 — component rigs
**Closed**:
- four-blade hub bench rigs;
- hydraulic governor/pitch-control rigs;
- blade-root/fatigue coupons and full-blade proof tests;
- propeller reduction/torsional instrumentation coordinated with Nakajima and Mitsubishi engine programs;
- oil leakage, seal, cold-start and rapid-rpm-change tests.

Asai's main value is test discipline, gauges, hydraulic-control knowledge and failure classification. It does not create a magically lighter or stronger foreign propeller.

### 1940H2 — full-engine development
**Closed as technically available for priority programs**:
- 1,500-1,800 hp-class full-engine runs with high-activity three/four-blade candidate hardware;
- first `PA-D` high-power four-blade sets can exist in small numbers;
- 3.3 m class is the lowest-risk fighter envelope;
- 3.4-3.5 m class begins for attack/carrier aircraft that can tolerate larger landing-gear geometry.

This is development hardware, not fleet production.

### 1941H1 — qualification family emerges
**Closed**:
- 3.3 m-class four-blade systems can enter `PA-Q` for a specified 1,600-1,800 hp installation after engine-specific vibration work;
- V8 priority high-power combat propellers use a **hydraulic governor path as the preferred baseline** rather than spending a major program cycle on an electric primary mechanism.

This is a V8 design choice enabled by Asai hydraulic/control experience and cross-program testing. It is not a claim that every historical VDM installation was hydraulic from the beginning.

### 1941H2 — 1,800 hp flight hardware / 2,000 hp growth rigs
**Closed**:
- 3.3-3.45 m / 1,800 hp-class development and priority qualification hardware is available;
- a limited serial-reproducible family can reach `PA-S` if a program orders it, but nationwide production quantity is not fixed;
- 3.5-3.6 m / roughly 2,000 hp-class hub, blade and reduction-ratio work is in full-engine qualification rather than basic feasibility.

### 1942H1 — practical Homare-class installation capability
**Closed**:
- 3.3-3.45 m four-blade / roughly 1,800 hp installations can be `PA-Q`, and selected families can be `PA-S`;
- 3.5-3.6 m / 2,000 hp development sets can be `PA-D` and move toward `PA-Q`;
- the technical ability to fit a B7A/N1K-class aircraft is no longer a dominant schedule blocker if the engine and airframe are ready.

### 1942H2-1943Q1 — 2,000-2,200 hp priority-prototype envelope
**Closed only as technology availability**:
- 3.6 m-class, low-prop-rpm four-blade installations for Homare 20/21 and early Ha-43-class power can exist as `PA-D` and selected `PA-Q` hardware;
- `PA-S` for a specific family is plausible only after that family is selected and its production tooling frozen;
- national quantities, supplier priority and fleet allocation remain branch-dependent.

## 4. Why 2,000-2,200 hp does not require an exotic propeller breakthrough
First-order disk-power loading provides a useful guard:

| nominal case | power | diameter | disk power loading |
|---|---:|---:|---:|
| J2M/N1K lower class | 1,800 hp | 3.30 m | ~157 kW/m^2 |
| B7A/Homare class | 1,825 hp | 3.454 m | ~145 kW/m^2 |
| Homare Reppu class | 2,000 hp | 3.60 m | ~147 kW/m^2 |
| Ha-43 Reppu class | 2,200 hp | 3.60 m | ~161 kW/m^2 |

The 2,200 hp / 3.6 m case is not an order-of-magnitude jump beyond historical 1,800 hp / 3.3 m practice.
The hard problems are instead:
- blade activity/profile and efficiency;
- pitch/governor authority;
- torsional and blade vibration;
- reduction-ratio selection;
- tip compressibility at high flight speed;
- hub/blade-root fatigue;
- manufacturing repeatability.

## 5. Large-diameter / low-rpm guard
For a Reppu-class first-order check:

### Homare installation
- engine ~3,000 rpm;
- special reduction around 0.422;
- propeller ~1,266 rpm;
- 3.6 m diameter;
- at ~620 km/h around 6 km, first-order helical tip speed is about 294 m/s, roughly Mach 0.93 under representative conditions.

### Ha-43 installation
- engine ~2,800 rpm working comparison point;
- reduction ~0.472;
- propeller ~1,322 rpm;
- 3.6 m diameter;
- at ~630 km/h around 6 km, first-order helical tip speed is about 305 m/s, roughly Mach 0.96.

These are **guard calculations, not CFD or final propeller efficiency values**.
They explain why the Homare low reduction ratio is a meaningful installation choice and why simply increasing rpm/diameter is not free.

## 6. Governor / pitch-control conclusion
V8 high-power fighter/attack-aircraft baseline:
- ordinary constant-speed regulation is already mature technology;
- the new challenge is fast, stable regulation of a larger four-blade assembly at higher torque and airspeed;
- high-power four-blade combat installations should preferentially use a hydraulic governor/pitch-actuation path with explicit overspeed/failure testing;
- electric actuation can remain an experimental/alternate path but should not be allowed to hold a major V8 fighter program if the hydraulic system is already qualified.

This does not imply modern electronic propeller control.

## 7. Cooling / cowl / oil integration
A good engine does not eliminate the installation problem.

Every high-power radial aircraft must close:
1. cylinder-head temperature distribution, not only average CHT;
2. front/rear row airflow balance;
3. cowl pressure recovery and exit-area control;
4. oil-cooler flow and pressure drop;
5. ground/taxi and low-speed climb heat rejection;
6. high-speed cooling drag;
7. exhaust routing/fire/heat effects;
8. propeller slipstream interaction with cowl inlet;
9. oil-pressure behavior at altitude and maneuver load.

Asai instrumentation and test planning can reduce the number of blind iterations, but cannot guarantee that a novel cowl works on the first flight.

## 8. Cooling fan is an installation choice, not an Ha-43 property
The Ha-43 family could be equipped with a 14-blade cooling fan, but not every installation used one.
Historical later **A7M2 Reppu / Ha-43** installation evidence (**worldline Reppu designation A9M; not worldline A7M Gaifu**) shows that adequate cooling could instead be obtained with a redesigned open cowl and separate intake/oil-cooler scoops.

V8 rule:
- use a fan when compact inlet area, ground/climb cooling, extension-shaft geometry or aircraft packaging makes it worthwhile;
- do not automatically charge every Ha-43 fighter the fan's weight/drag/power cost;
- equally, do not delete a fan until ground/climb hot-day `CI-Q` testing proves the fanless cowl.

## 9. Production guard — VDM is not free
Even after technical qualification, VDM-family production remains expensive.

Historical USSBS evidence indicates:
- roughly 70 percent more man-hours than the older Hamilton-family type;
- difficulties from suitable steel-alloy shortages;
- many propeller sizes reduced plant utilization.

V8 Asai effects can reduce:
- drawing errors;
- fixture/gauge inconsistency;
- reject/rework rate;
- balance/pitch-setting variance;
- uncontrolled proliferation of nearly identical parts.

V8 does **not** erase the intrinsic machining/assembly labor of a more complicated propeller.

Recommended but not yet procurement-canon standardization:
- one 3.3 m high-power fighter family;
- one ~3.45 m attack/carrier family where geometry demands it;
- one 3.6 m 2,000+ hp growth family;
- common governor, hydraulic, inspection and blade-root standards where feasible.

Exact standardization depends on which 1942 programs are actually ordered.

## 10. CFRP / composite guard
Prior P3/CFRP blade work remains experimental.

Do **not** use CFRP blades as the mainstream solution for 1941-43 Homare/Ha-43 aircraft.
The high-power branch closed here assumes conventional metal blades/hubs unless a later dedicated material program explicitly promotes an alternative after fatigue, erosion, moisture, repair and mass-production qualification.

## 11. Aircraft inheritance map
### J2M
Provides early Navy experience with:
- high-power radial fighter cowl;
- extension-shaft torsion/cooling problems;
- 3.3 m-class four-blade propeller;
- governor reliability;
- cooling fan / oil-cooler trade.

Not every J2M solution transfers directly: its extension-shaft geometry is unusually specific.

### B7A
Provides the first especially valuable direct dataset for:
- Homare 11/12;
- ~3.45 m four-blade propeller;
- carrier-aircraft landing-gear/ground-clearance constraints;
- prolonged high-power attack-aircraft cooling.

### N1K1-J
Provides fighter-specific data for:
- Homare 11 then 20/21 class;
- ~3.3 m four-blade propeller;
- high-angle climb and fighter transient cooling;
- interaction between large propeller and long mid-wing landing gear.

### Reppu-equivalent
Inherits the above but moves to:
- ~3.6 m diameter;
- lower prop rpm / higher absorbed power;
- larger wing/folding/gear geometry;
- separate Homare and Ha-43 cowl/cooling/reduction solutions.

Reppu therefore is an integration escalation, not a first encounter with four-blade propellers.

## 12. Branch boundary
Closed before combat replay:
- high-power four-blade technology availability by class/state;
- hydraulic-governor preference;
- 3.3/3.45/3.6 m development sequence;
- the need for separate engine/prop/cooling qualification;
- branch-neutral J2M/B7A/N1K inheritance paths.

Remain open until requirements/procurement/war branch is replayed:
- exact national propeller quantities after 1942;
- which family receives `PA-S` priority first;
- final Reppu engine/propeller selection;
- raw-material allocation;
- service failure rates and replacement-stock sufficiency.

## Source-basis notes
External historical anchors audited 2026-09-03 include Yamaha Motor's history of Nippon Gakki/Sumitomo propeller production; the USSBS *Japanese Aircraft Industry* propeller section; Smithsonian National Air and Space Museum Sumitomo four-blade Homare propellers; J2M family technical histories; and Ha-43 installation histories. These anchors establish historical technology and production burden; the V8 timing deltas above are causal worldline judgments, not quoted historical dates.
