# ASAI WORLDLINE — E6 TWIN J/JF PERFORMANCE / FUEL / FRP DROP-TANK REBASELINE V1
## 1939 comparative-flight interpretation and 1940 service-production planning closure

**Status:** TECHNICAL H→A DESIGN REBASE CLOSED / MEASURED FLIGHT VALUES STILL TEST-LOCAL  
**Clock effect:** NONE — 1939/1940 combat clocks are not advanced by this file.  
**Purpose:** Remove the stale small-fleet E6 assumption that survived the E5 retro replay, propagate the current E6-M J/JF engine closure into an aircraft-level design calculation, and close a practical high-speed external-fuel family using the already-mature E5 drop-tank and Asai FRP manufacturing base.

---

## 0. Central verdict

1. The old `Twin 4 / Single 2 in 1940 -> 1941 limited production` bundle is a **pre-retro-replay planning residue**. It was created when E5 Twin itself was still treated as a ~10-aircraft technical population. It is not a valid planning scale after E5 was retro-replayed as a large operational fleet.
2. **E6 Twin and E6 Single are separated.** This file controls the Twin. The later E6SINGLE1 closeout supersedes the old research-only reading for the Single and closes it as a separate pure-J service-production interceptor/high-cover line.
3. E6 Twin JF is the practical main-block candidate. Pure-J remains useful as the speed / high-altitude / local-interception knife.
4. The current engine closure makes E6 Twin an approximately **0.74–0.80 Mm/h JF** and **0.80–0.83 Mm/h pure-J** central-design aircraft depending altitude; uncertainty in metal-wing drag-rise and exact aircraft geometry remains larger than engine-thrust uncertainty.
5. E5 drop-tank technology is already mature. E6 pays only aircraft-local load, flutter, separation, CG and high-q requalification.
6. For 1939–40, the rational molded external tank is **not CFRP**. The preferred immediate product is a **flax/hemp-epoxy molded shell with metal load fittings**, optionally using a thin sealed/glass local outer layer. Full structural GFRP waits on wet-strength/coupling maturity; scarce structural carbon fiber is reserved for applications where its specific stiffness changes the aircraft.

---

## 1. Mandatory parent anchors

### E5 aircraft inheritance
Current AIRPOWER6/retro replay anchors:
- representative E5 Twin pure-J loaded aircraft: **~3.8 t**;
- E5-J pair engine dry mass: **~0.79 t**;
- E5 Twin has already paid one-engine procedures, J/JF controls, radio/photo integration, mission fuel, drop-tank operation, servicing and field turnaround;
- E5-D200 is technically qualified by mid-1938 and service-evaluation PASS by late 1938.

### E6 engine anchors
Current E6-M engine-side authority:
- pure-J: **~850 kgf/engine** at the accepted non-Ni 870°C product point;
- selected Ni pure-J: **~900 kgf/engine** at 920°C, local higher-rating use still subject to product life/release;
- J dry mass: **~500–555 kg/engine, center ~525 kg**;
- JF long-life center: **~984 kgf/engine at 835°C**;
- JF candidate 850°C / 870°C engineering points: **~1,003 / 1,028 kgf/engine**, flight/rating release local;
- JF dry mass: **~610–690 kg/engine, center ~650 kg**;
- same-condition static comparison: JF gives about **+21% thrust and −17% TSFC** versus pure-J.

### Material anchors
Current material authority:
- selected flax/hemp-epoxy design composite: `E1 ~28.6 GPa`, density **~1.33 g/cm³**, design tensile strength **~122 MPa**;
- kerosene does not create the water-swelling problem of natural fiber; the outside still needs sealing against rain/humidity;
- molded FRP drop tanks are explicitly an early high-value manufacturing application because they are disposable, secondary structure and do not justify expensive sheet-metal labor;
- structural wet-strength GFRP is a **1941–43** maturity track, not the 1939 production center.

---

## 2. Weight rebaseline

The 3.8 t E5 Twin reference minus its ~0.79 t engine pair leaves **~3.01 t** of airframe + installation + crew + mission equipment + mission fuel at that representative loaded state.

Replacing propulsion without pretending the rest of the aircraft becomes free gives:

| block | calculation | normal loaded working band |
|---|---|---:|
| E6 Twin J | `3.80 - 0.79 + 1.05 + local E6 install allowance` | **4.00–4.20 t**, center **4.10 t** |
| E6 Twin JF | J block + ~0.25 t engine dry delta + rear duct/structure/CG allowance | **4.30–4.55 t**, center **4.40 t** |

This does **not** claim that every E5 and E6 mission carries identical fuel/weapon load. It is the correct first-order loaded-mass inheritance for aircraft-performance closure.

For the JF mission block, a usable internal kerosene target of **~0.85–0.95 t** (~1.05–1.18 m³) is retained as the design center because it closes a useful ~400–500 km routine combat/recon radius without external fuel. Exact cell geometry remains drawing-level.

---

## 3. Airframe aerodynamic working closure

No current V10 source closes an E6 Twin wing area. The old conversational `14 m²` figure therefore has **no authority and is rejected**.

A conventional-runway high-speed twin at the loaded masses above is closed for calculation with this sensitivity box:

| item | working band | central calculation |
|---|---:|---:|
| wing area | **18.5–20.0 m²** | **19.0 m²** |
| aspect ratio | **6.0–6.6** | **6.25** |
| Oswald efficiency | 0.78–0.82 | 0.80 |
| clean `Cd0`, J | 0.0245–0.0275 | **0.0255** |
| clean `Cd0`, JF | 0.0265–0.0305 | **0.0275** |
| straight-metal-wing drag-rise onset | **M 0.68–0.72** | **M 0.70** |
| landing `CLmax` | **1.8–2.0** | 1.8 conservative calculation |

At the central 19.0 m² wing:
- J 4.10 t wing loading: **~216 kg/m²**;
- JF 4.40 t: **~232 kg/m²**;
- JF with a full D320F pair at ~4.95 t: **~260 kg/m²**.

This remains a conventional prepared-runway aircraft. The engine does not magically make it STOL.

---

## 4. Engine/airframe calculation method

The performance sheet uses:
- ISA atmosphere;
- the current PR~7 / 14-stage E6-M gas-generator closure;
- current J and JF static thrust/TSFC points reproduced by cycle calculation;
- ram/inlet recovery and net exhaust momentum in flight;
- parasite + induced drag polar;
- explicit smooth drag rise after the straight-metal-wing critical-Mach band;
- no hidden afterburning/reheat;
- no 850/870°C JF higher rating in the central service calculation.

The model reproduces the current static anchors at sea level:
- J: **~853 kgf**, TSFC **~0.799 kg/(kgf h)**;
- JF: **~984 kgf**, TSFC **~0.650 kg/(kgf h)**.

The principal remaining uncertainty is therefore aircraft aerodynamics, not whether the engine has ~500 or ~1,000 kgf thrust. The old ~500 kgf E6-M engine anchor is already superseded upstream.

---

## 5. Central clean-aircraft performance

### 5.1 Level maximum speed — calculated design values, not claimed flight-test records

| altitude | E6 Twin J, 4.10 t | E6 Twin JF, 4.40 t |
|---:|---:|---:|
| sea level | **~800 km/h** | **~744 km/h** |
| 3,000 m | **~827** | **~772** |
| 6,000 m | **~830** | **~793** |
| 8,500 m | **~818** | **~793** |
| 10,000 m | **~806** | **~783** |

Sensitivity over plausible mass/drag/Mcrit corners:
- J: roughly **760–830 km/h sea level**, **790–860 km/h around 6 km**;
- JF: roughly **700–770 km/h sea level**, **740–825 km/h around 6–9 km**.

Interpretation:
- pure-J remains the high-specific-thrust speed knife;
- JF does **not** lose a fixed 5–10%. Its penalty varies with speed because the free-aft-fan gives excellent static/low-speed thrust but lower specific thrust as forward velocity rises;
- both variants eventually run into straight-metal-wing compressibility/drag-rise before engine static thrust becomes the sole limiter.

### 5.2 Climb

Central best-rate calculation:

| item | J | JF |
|---|---:|---:|
| initial best ROC | **~29–30 m/s** | **~26–27 m/s** |
| time to 3 km | ~1.9 min | ~2.1 min |
| time to 6 km | **~4.4 min** | **~4.9 min** |
| time to 8 km | ~6.7 min | ~7.5 min |
| time to 10 km | ~9.9 min | ~11.2 min |
| service ceiling, ~0.5 m/s ROC criterion | **~13.5 km** | **~12.9 km** |

The old qualitative statement `JF climb is better` remains correct **at takeoff/low speed**, where JF has the higher static T/W. At the best sustained climb speed, pure-J can overtake it because the JF fan backend gives up specific thrust and carries ~0.25–0.30 t extra mass. The two claims describe different parts of the envelope and are no longer to be conflated.

### 5.3 Acceleration

Central clean-aircraft full-power calculation:
- J, sea level, 300→600 km/h: **~38 s**;
- JF, sea level, 300→600 km/h: **~43 s**;
- at 6 km: roughly **~71 s J / ~79 s JF**.

These are ideal clean-aircraft calculations before unit/weather/turbulence allowances.

### 5.4 One-engine return

With a conservative dead-side/asymmetric drag increment:
- one-engine sea-level best climb at representative return weight: **~7–9 m/s**;
- one-engine maximum level speed: roughly **~470–495 km/h**;
- one-engine service ceiling: **~6.5–7.5 km** depending weight/backend.

Thus the original military requirement `return on one engine` is comfortably retained rather than merely theoretical.

---

## 6. Runway / landing closure

With central wing area and conservative `CLmax=1.8`:
- JF 4.40 t stall: **~163 km/h**;
- representative lighter return mass 3.7–3.9 t: **~149–153 km/h**;
- full D320F takeoff near 4.95 t: **~173 km/h** stall;
- liftoff target at ~1.15 Vs: approximately **187 km/h clean JF / ~199 km/h full external-fuel JF**.

First-order ideal ground-roll calculation gives about:
- clean JF: **~0.42 km**;
- full D320F: **~0.55 km**.

For actual 1939–40 operations, spool response, runway roughness, wind, brake/tyre limits, pilot margin and obstacle clearance require a substantial operational factor. Use a planning band around:
- clean prepared-field takeoff: **~0.55–0.70 km ground run class**;
- full external-fuel prepared-field takeoff: **~0.75–0.95 km class**;
- rough/wet/short fields require a local restriction and are not implied safe by this calculation.

---

## 7. Internal-fuel range closure

For the JF mission block, central planning uses:
- usable internal kerosene: **~0.90 t**;
- climb/taxi allowance to the high-altitude cruise band: **~0.12–0.14 t**;
- protected reserve/descent/combat allowance: **~0.20 t**;
- economical high-altitude cruise: **~530–550 km/h at ~8–9 km**;
- clean-aircraft `L/D` around the specific-range optimum: **~10–10.5**;
- flight/part-load JF TSFC sensitivity: **~0.75–0.90 kg/(kgf h)**. The current static 0.649 value is not copied directly into a cruise Breguet calculation.

Resulting internal-fuel cruise-equivalent distance after climb/reserve allocation:
- **~0.87–1.04 thousand km**, central ~0.95 thousand km.

Practical round-trip mission planning after routing, station/combat allowance and reserve:
- routine recon/escort/interception radius: **~400–480 km class**;
- lighter photo/courier profiles can trade mission load/station time for more reach.

The J speed block, with roughly 0.65–0.75 t internal fuel, is naturally shorter-legged: approximately **~300–380 km routine combat-radius class** depending mission load.

---

## 8. E6-D320F molded FRP drop-tank family

### 8.1 Why a new tank size is justified
E5-D200 is already mature and can be used for initial E6 trials. E6, however, is faster and its JF mission block can exploit more fuel without becoming thrust-starved. A direct copy of D200 leaves too much range capability unused.

The rational E6 standard design band is **300–350 L per tank**. `320 L` is the central engineering point, not a sacred capacity.

**Working designation: E6-D320F**

Central pair:
- nominal: **320 L ×2 = 640 L**;
- usable: **~610–625 L**;
- kerosene: **~490–505 kg**;
- fineness ratio: ~5.2;
- body length: **~2.6 m**;
- maximum diameter: **~0.50 m**;
- wetted area: **~3.6 m² per tank**.

### 8.2 Material and construction
1939–40 production center:
- molded selected flax/hemp-epoxy shell;
- nominal skin **~1.5–1.7 mm**;
- molded circumferential stiffening ribs / fuel baffles to prevent empty/part-empty shell buckling;
- local thicker laminate at suspension points;
- metal filler/vent fittings, release lugs and load spreaders;
- sealed outer surface against rain/humidity;
- thin/local glass veil may be used at abrasion/high-load zones when available, but continuous structural glass is not required.

Do **not** use full CFRP. It buys little in a disposable tank while consuming the scarce material that matters for thin high-speed primary structure.

### 8.3 Mass
At 1.6 mm and 1.33 g/cm³, the raw laminate skin is about **7.7 kg/tank** at the central geometry.

After local reinforcement, ribs/baffles, sealing and fittings:
- tank body: **~12–15 kg each**;
- pair tank bodies: **~24–30 kg**;
- scaled rack/plumbing/jettison hardware: **~17–23 kg/pair**;
- complete empty installed pair: **~42–53 kg**, center ~**46 kg**.

Thus a full D320F pair adds roughly **~0.53–0.56 t** to takeoff mass and puts a central JF near **~4.93–4.98 t**.

The primary payoff is not a miraculous weight cut versus a very thin aluminum tank. It is:
- saving strategic light alloy;
- avoiding skilled thin-sheet welding/forming labor;
- making an expendable object in low-pressure molds with less-skilled labor;
- rapid geometry iteration for the high-speed aircraft.

### 8.4 Structural sanity check
For one full tank around 0.26–0.27 t:
- 3.5 g carried operational limit with 1.5 ultimate factor gives approximately **13–14 kN ultimate inertial load per tank**;
- metal lugs/load spreaders therefore dominate local attachment design.

Fuel/slosh pressure is much less demanding for the laminate membrane:
- ~0.5 m fuel head at 1 g: ~4 kPa;
- ~3.5 g equivalent: ~14 kPa; ultimate ~21 kPa;
- simple hoop membrane stress at 1.6 mm / ~0.25 m radius is only a few MPa, far below the ~122 MPa material design tensile coordinate.

Therefore **buckling, local lug load, impact/handling damage, bonding quality and jettison separation**, not raw tensile strength, govern the tank design.

### 8.5 Drag and retained-tank performance
Calibrating from mature E5-D200 operational penalties and scaling for the larger/high-q E6 installation gives a subcritical pair increment around:
- `ΔCd ~0.0025–0.0040`, central ~0.0032;
- higher local penalty near the upper carried Mach band from rack/interference/compressibility.

At a ~4.95 t JF takeoff state, central retained-tank calculation gives:
- sea-level maximum: **~700 km/h**;
- 6 km: **~740 km/h**;
- 8.5 km: **~735–740 km/h**;
- time to 6 km: **~6.1 min**.

Relative to clean JF, the retained pair costs roughly **40–60 km/h** at high speed. Doctrine is therefore unchanged from E5: external fuel is for transit/radius and is jettisoned before deliberate high-speed combat when fuel state permits.

### 8.6 Range with D320F
Using the same conservative climb/reserve accounting and a tank-dragged cruise segment followed by clean flight after jettison:
- cruise-equivalent distance: **~1.48–1.77 thousand km**, central ~1.6 thousand km;
- practical long-cover/recon radius: **~650–800 km class** after routing/station/reserve;
- light ferry/transfer one-way planning: **~1.6–1.9 thousand km class** without inventing a 2,400 km routine combat envelope.

---

## 8.7 Mission/armament authority added by E6MISSION1

Aircraft mission-bay mass, crew, fixed-armament envelope and high-speed ordnance release are now closed by:
`75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-E6-TWIN-MISSION-ARMAMENT-HIGHSPEED-RELEASE-CLOSURE-1939-1940-V1.md`.

Use that file for the ~0.40 t internal mission bay, two-seat common airframe, HSR-50/100 compatibility, HSC-100F harassment container and mixed D320F/camera/nuisance load-sheet rules. It does not change the performance/fuel numbers above except through the explicitly listed mission weights.

## 9. 1940 production rebaseline — superseded by cost/procurement closure

The previous `Twin 4 / Single 2` 1940 block remains superseded. E6REBASE1 initially replaced it with a `36–60 accepted / center ~48` pilot-production working band.

Subsequent whole-aircraft cost and capacity reconciliation shows that this second band is also too conservative. Current procurement authority is:

`75-CURRENT-TECHNICAL-ADDENDA-V10/ASAI-E6-TWIN-COST-PROCUREMENT-REBASELINE-1939-1940-V1.md`

Current 1939-12-31 planning posture:
- service-production commitment target: **144 common Twin airframes firm-order class + 72 option**;
- 1940 accepted Twin: **120–156 aircraft, center ~144**;
- JF share: **~85–90%**;
- pure-J share: **~10–15%** specialized block;
- installed engines: **240–312**;
- with ~20–25% spare/acceptance allowance: **~288–390 flight-grade engine packages**.

Current ramp:
- Q1 cumulative: **~18–24**;
- Q2 cumulative: **~48–66**;
- Q3 cumulative: **~84–114**;
- Q4 cumulative: **~120–156**.

These remain planning bands, not retroactively asserted monthly delivery facts. The exact contract date, Army/Navy allocation, monthly acceptance, unit conversion and combat deployment remain replay-local.

E6 Single remains outside this **Twin** production count. E6SINGLE1 subsequently closes its own 96-firm/+48-option service-production posture and 84–108 / center ~96 1940 acceptance plan.

---

## 10. Service/adoption interpretation

E6 Twin is no longer a `pilot-production candidate` in the sense of adoption uncertainty.

Correct planning status at the 1939-12-31 gate:
- **E6 Twin JF: A — service-production main-block candidate, concurrent service proving**;
- **E6 Twin J: B — specialized service-production / interception-high-altitude block**;
- **E6 Single: superseded here by E6SINGLE1 — A/B separate land-interceptor/high-cover service-production line**.

The first 12–24 E6 Twin aircraft can still carry a heavy service-test burden, but they are lead aircraft from an already-committed production series. Production commitment, factory acceptance, unit conversion and combat allocation remain separate ledgers.

No E6 combat wing is retroactively created on 1940-01-01. Once training/allocation gates pass during 1940, however, normal operational units are allowed without waiting for a fictional 1941 first-adoption decision.

---

## 11. E-generation semantic guard

Nothing in this file changes the current E-family semantics:
- `E1…E9` remain technology-generation/front coordinates;
- after higher generations mature, labels such as `E4-equivalent` / `E5-equivalent` may denote lower-rated service/capability products made with newer mature processes where interfaces permit;
- `C/N/M/E` are local operating-rating labels, not technology generations;
- flight-A / flight-B / ground-mobile etc. are production/acceptance bins.

Therefore E7 research does not automatically terminate E6 aircraft or E6 production, just as E6 did not terminate E5 products.

---

## 12. Supersession / replay guard

This file supersedes only the stale E6 planning interpretation in the 1940 weapon gate where it says:
- `Twin 4 / Single 2` as the whole 1940 E6 block;
- E6 Twin cannot progress beyond service evaluation until a 1941 limited-production decision;
- any statement that treats the E6 Twin as if its military lineage still starts from a tiny experimental E5 fleet.

It does **not** alter:
- 1939 combat outcomes;
- 1939 E5/Ki-42 OOB already closed;
- E6 measured flight-test numbers not explicitly present in the replay ledger;
- the 1939-12-31 combat clock;
- E7 chronology.

**E6 TWIN PERFORMANCE / FUEL / FRP REBASE CLOSED — V1; PROCUREMENT QUANTITIES SUPERSEDED BY E6 COST/PROCUREMENT REBASE V1**
