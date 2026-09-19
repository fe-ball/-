# ASAI WORLDLINE — E6 TWIN MISSION / ARMAMENT / HIGH-SPEED RELEASE CLOSURE V1
## 1939 lineage inheritance and 1940 service-configuration freeze

**Status:** AIRFRAME MISSION CONFIGURATION CLOSED / SERVICE-GUN MODEL AND EXACT 1940 THEATER ALLOCATION REMAIN SERVICE-LOCAL  
**Clock effect:** NONE — combat remains stopped at 1939-12-31 24:00.  
**Purpose:** Close the E6 Twin service configuration that remained open after E6REBASE1/E6COSTREBASE1, and carry the already-paid E5 high-speed light-strike / mission-bay / release-control lineage into a practical 1940 reconnaissance, interception, escort, courier and high-speed harassment system.

---

## 0. Central closure

1. **Common E6 Twin is a two-seat airframe.** Do not create a separate one-seat E6 Twin J fuselage merely because the J block is interception-biased. The rear station is retained for observer/navigation/radio/mission work; pure-J interception sorties may leave it unoccupied or use it for a controller/observer. E6 Single remains the separate one-seat branch; its later service-production status is controlled by E6SINGLE1 rather than by this Twin mission file.
2. **The common service airframe keeps the E5 lineage's central mission bay.** The service mass limit is **~0.40 t internal mission load**. The bay is centered close enough to the aircraft CG that ordinary 0–0.40 t mission changes remain within the normal trim/load-sheet envelope rather than requiring a new airframe.
3. **1940 fixed-gun envelope:** concentrated nose battery, structurally closed around **2×20 mm-class cannon + 4×7.7 mm-class guns**. Navy can use the already-production Type 99 20 mm family; exact Army cannon/feed identity remains a service-local integration item inside the same mass/recoil envelope. Later-war 20 mm×4 batteries are not backdated into 1940 merely because the airframe could eventually accept more.
4. **Mission-ready zero-fuel bookkeeping center:** **~3.50 t** including two crew, normal fixed-gun installation/ammunition allowance, radio/oxygen, oil and ordinary service equipment, but excluding mission-module load and usable kerosene. This is a weight-accounting closure, not a claim for a manufacturer placard empty weight.
5. **Normal service takeoff band:** **~4.25–4.60 t** depending mission. **Heavy external-fuel takeoff ceiling for ordinary service planning: ~5.05 t.** Higher combinations require a special load sheet and are not routine.
6. **High-speed release is not a new 1940 invention.** E5 has already flown a ~0.4 t light-strike mission in the 510–525 km/h weapon-configuration speed class and has paid release-delay, suspension, bomb-table, mission-bay and high-speed handling work. E6 requalifies separation and bay-door behavior at its local Mach/q envelope.
7. **E6 does not drop ordinary external bombs at clean maximum speed as standard doctrine.** High-speed attack uses the internal bay. External wing stations are primarily D320F fuel stations; external ordnance is a local/test exception because drag destroys the reason for using E6.
8. A **100 kg-class high-speed dispersal/harassment container** is closed as a 1940 service-equipment option. Detailed FRP carriage architecture, S6/S4/M1 bay adapters, 250 kg-class release qualification and the refined HSC-100F production center are controlled by `ASAI-E6-FRP-ORDNANCE-CARRIAGE-HIGHSPEED-STORE-CLOSURE-1939-1940-V1.md`.

---

## 1. Why two seats remain the common production choice

The military twin lineage was created around:
- pilot + observer/test/mission crew;
- radio/photo work;
- command reconnaissance;
- heavy-fighter/escort comparison;
- one-engine procedures;
- long-distance navigation;
- light strike.

By 1939 those are operational needs, not prototype instrumentation excuses. A one-seat J derivative would save some mass and frontal/canopy area, but it would:
- split a 144-airframe-class production program into another fuselage/canopy/control series;
- reduce long-range navigation/radio workload capacity;
- remove the observer/controller useful to local interception before mature radar/GCI exists;
- duplicate the separate single-seat question assigned to E6 Single (later closed for service production by E6SINGLE1).

Therefore common Twin production retains the two-seat structure. The J block remains faster because of propulsion/weight allocation, not because it receives a separate one-seat fuselage in 1940.

---

## 2. Common service mass bookkeeping

Central accounting coordinate:

| item | working mass |
|---|---:|
| mission-ready zero-fuel aircraft, two crew, fixed guns/ammunition allowance, normal radio/oxygen/oil | **~3.50 t** |
| normal internal fuel band | **~0.65–0.90 t** |
| photo/recon module | **~0.10–0.14 t** |
| internal strike load | **0–0.40 t** |
| D320F full installed pair | **~0.53–0.56 t** including fuel and installed tank/rack mass |
| normal service takeoff planning ceiling | **~5.05 t** |

The existing E6REBASE1 central JF `~4.40 t` remains valid as a representative mission load, not a single universal configuration.

### Representative JF configurations

| mission | internal fuel | mission load | external fuel | takeoff center | interpretation |
|---|---:|---:|---:|---:|---|
| fighter / escort | ~0.80–0.85 t | gun/radio only | none | **~4.30–4.35 t** | normal clean combat block |
| command/photo recon | ~0.82–0.88 | ~0.10–0.14 t camera | none | **~4.43–4.52 t** | routine deep-photo aircraft |
| normal light strike | ~0.62–0.70 | **~0.35–0.40 t** | none | **~4.47–4.60 t** | internal-bay strike; no D320F assumed |
| recon + nuisance load | ~0.78–0.82 | camera + **~0.08–0.12 t** ordnance | none | **~4.48–4.58 t** | photo mission can carry one small harassment store without becoming a bomber sortie |
| long recon | ~0.75–0.82 | camera | D320F full | **~4.88–5.02 t** | long-cover/recon block |
| long recon + nuisance | ~0.68–0.74 | camera + **~0.08–0.10 t** ordnance | D320F full | **~4.94–5.05 t** | reduce internal fuel to respect takeoff ceiling |
| high-value courier | ~0.70–0.80 | **~0.20–0.30 t** cargo | none | **~4.40–4.60 t** | prepared-hub trunk mission |

Do not combine full internal fuel + full D320F + 0.40 t bombs as a routine load. E6 inherits the E5 rule that fuel, payload, runway and landing weight are traded rather than stacked for free.

---

## 3. Fixed armament closure

### 3.1 Common structural envelope

The 1940 common nose is frozen around:
- **2×20 mm-class cannon**;
- **4×7.7 mm-class guns**;
- concentrated forward fire;
- no defensive turret in the standard airframe.

Reasoning:
- the E5 military lineage already moved from an interim four-rifle-caliber nose battery toward a later two-cannon provision;
- E6's closure speed shortens firing opportunities, so cannon effect is valuable;
- a 20 mm×4 late-war battery is not necessary to make the 1940 aircraft useful and would backdate later feed/ammunition maturity;
- keeping a common mass/recoil envelope lets Army/Navy fit their own approved weapon identities without redesigning the fuselage.

### 3.2 Role use

- **JF recon/courier:** fixed battery retained; units may reduce ammunition on exceptional range sorties.
- **JF heavy fighter/escort:** full normal ammunition allowance.
- **J interceptor:** same common nose envelope; specialized trials may substitute additional cannon only after a separate service weapon-release gate.

No generic dense-core 20 mm load is created by this file. Special ammunition remains a separately accounted program.

---

## 4. Internal mission bay closure

The central mission bay is a **~0.40 t-class internal load station** inherited from the E5 military requirement lineage.

It is used for interchangeable modules rather than dedicated fuselages:
- photo/camera and calibration equipment;
- normal 0.35–0.40 t light-strike load;
- one or two small high-speed harassment stores;
- high-value courier cargo;
- test instrumentation.

Design rule:
**high-speed mission stores are carried internally whenever possible.**

At E6 speeds the drag cost of hanging conventional bombs externally is disproportionate. The bay therefore uses short-duration opening/release rather than prolonged open-door flight. Exact door linkage and detailed separation drawings remain manufacturer-level, but the service requirement is closed: ordinary mission stores must leave cleanly in the qualified subcritical high-speed band without striking the fuselage/nacelles.

---

## 5. High-speed-release lineage — why it already exists by 1940

E5 has demonstrated for years that a turbine twin can arrive over a target much faster than conventional Army bombers and still carry a light attack load. That creates a persistent ordnance/test requirement:
- bomb suspension that does not distort or jam under higher q;
- release-delay measurement;
- stable separation from an internal/central station;
- ballistic tables for higher forward velocity;
- sight/release setting discipline;
- statistical post-drop calibration.

FIREOPTICS1 already closes the relevant institutional capability as FCS1 with limited FCS2 workflow/test support. Therefore E6 does not begin with a blank sheet.

Important physical point:
E6 high-altitude TAS looks extreme, but dynamic pressure is not equally extreme. Around 8–8.5 km, a ~790 km/h TAS E6 is only about **~500–520 km/h equivalent airspeed class**. That is close to the E5 weapon-configuration speed already used as the lineage calibration point. E6 still pays Mach/separation work, but not a wholly new load-factor universe.

---

## 6. High-speed release envelope

### 6.1 Standard high-altitude release

The preferred E6 harassment / area-strike mode is:
- prepared target folder or clearly identified area target;
- high-altitude level or very shallow flight;
- **~700–760 km/h TAS class at roughly 7–9 km** for normal high-speed release;
- transient bay opening;
- immediate clean acceleration/egress after release.

This is deliberately below the clean JF maximum rather than a claim that every store can be thrown out at 793 km/h on day one.

The reason the band is useful is survivability, not precision. At those altitudes the dynamic-pressure class is similar to E5's already-paid high-speed attack work, while enemy piston fighters face a much worse closure/second-pass problem.

### 6.2 Lower-altitude boundary

Do **not** copy the 7–9 km TAS number to sea level. Low-altitude q rises sharply. Low-level and shallow-dive attack retains a lower aircraft-specific release limit and is not the preferred E6 role.

### 6.3 Accuracy doctrine

High-speed level release does not become precision bombing merely because the tables are better.

Use it for:
- airfield surfaces/dispersal areas;
- rail yards and sidings;
- truck parks / supply areas;
- exposed artillery or troop concentrations;
- known fixed installations where area effect matters.

Point bridges, individual vehicles, ships maneuvering at sea and other small targets still need a different attack geometry or a different weapon/sight solution.

---

## 7. HSR conventional-bomb compatibility family

**Working technical designation:** `HSR` — High-Speed Release compatibility family.

E6FRPORD1 broadens the earlier shorthand `HSR-50/100`: Army 50/100/250 kg-class and Navy 60/250 kg-class selected service bombs are the current integration families. The 250 kg store uses its own lower initial release-speed ladder.

This is **not a new explosive filling** and does not replace ordinary Army/Navy bomb identities. It is an aircraft/ordnance integration standard for selected service bombs in the currently released size family:
- low-drag carriage geometry inside the E6 bay;
- qualified suspension/release hardware;
- stable tail/configuration accepted for the E6 release band;
- bomb-specific high-speed ballistic/drop tables;
- release-delay and lot acceptance control.

The exact service bomb mark remains Army/Navy-local. Explosive fillings and fuzes remain service-arsenal identities unless a separate chronological ordnance file changes them.

Routine E6 strike combinations may use up to the **~0.40 t bay mass limit**; ordinary high-speed reconnaissance normally carries much less.

---

## 8. HSC-100F high-speed dispersal / harassment container

**Working technical designation:** `HSC-100F`  
**Status at 1939-12-31:** TECHNICALLY PLAUSIBLE / LATE-1939 QUALIFICATION OR 1940-Q1 SERVICE RELEASE BAND; no retroactive 1939 combat credit without an event ledger.  
**1940 role:** service-equipment option for E5/E6-family high-speed area harassment, with E6 local separation requalification.

### 8.1 Mass / construction class

- total carrier mass: **~95–115 kg class**;
- majority of carried mass is existing small fragmentation/incendiary-type service payload selected by the arsenal;
- aerodynamic outer carrier/fairing: molded flax/hemp-epoxy;
- metal suspension/load spine and local fittings;
- contained service stores and their arming/fuze identities remain controlled by the Army/Navy arsenal records.

The refined FRP/store architecture is controlled by E6FRPORD1. The FRP logic is the same as D320F:
- expendable secondary object;
- low-pressure molds;
- saves light alloy and skilled thin-sheet labor;
- easy to reshape as E6 separation testing advances;
- no justification for scarce CFRP.

### 8.2 Mission use

Normal E6 uses:
- **one HSC-100F** with camera fit for routine nuisance/harassment reconnaissance;
- **two HSC-100F** with camera fit for shorter-radius deliberate armed reconnaissance when the load sheet permits;
- **S6:** up to six 50/60 kg-class conventional stores;
- **S4:** up to four 100 kg-class or HSC-100F stores inside the ~0.40 t bay limit;
- **M1:** one 250 kg-class conventional store with its separate release ladder;
- long-range D320F + camera + one ~100 kg nuisance store is permitted only with reduced internal fuel inside the ~5.05 t takeoff ceiling.

HSC is an **area-effect convenience**, not a magical anti-armor or precision weapon. It exists because high-speed reconnaissance repeatedly exposes valuable but broad targets for which one small area-effect release is worth carrying even when the main mission is information collection.

---

## 9. Mission-performance consequences

### Reconnaissance

A 0.10–0.14 t camera module plus one ~0.10 t nuisance store adds mass but almost no sustained external drag because both are internal. The speed penalty after the bay closes is therefore small; the main costs are:
- climb;
- fuel/radius;
- landing weight;
- brief release disturbance.

This is exactly why the nuisance-load concept is attractive on E6: a reconnaissance aircraft can remain a reconnaissance aircraft rather than becoming a slow externally bomb-loaded strike configuration.

### Light strike

At ~0.35–0.40 t internal ordnance, use reduced internal fuel. Working radius remains approximately **~300–380 km class** until a dedicated strike-specific flight map closes it. This mission is shorter-legged than D320F reconnaissance but far harder to intercept than the E5 normal 0.4 t attack.

### Long recon + harassment

With D320F, camera fit and one ~0.10 t internal nuisance store, reduce internal fuel to keep takeoff near/below ~5.05 t. Working mission radius becomes approximately **~550–700 km class** rather than the clean long-recon 650–800 km band.

The conceptual value is not bomb tonnage. It is the ability to make a deep reconnaissance pass impose an additional air-defense/logistics cost whenever a suitable broad target lies on or near the route.

---

## 10. 1937–40 development chronology

### 1937 H2
E5 weapon/mission-bay flight work establishes high-speed suspension, release-delay measurement and representative 50–100 kg-class store separation as a recurring program rather than a one-off demonstration.

### 1938 H1–H2
E5 light-strike and bombsight/release-table workflow mature enough for service use. Higher-speed release problems become an ordinary test/QC subject. FRP manufacturing matures in parallel on non-primary structures and disposable objects.

### 1939 H1
Area-effect / nuisance-store requirement is formally credible: E5 reconnaissance repeatedly finds airfields, rail/logistics parks and troop concentrations that are too broad to justify precision attack but valuable enough that a small opportunistic release has utility.

### 1939 H2
100 kg-class streamlined dispersal-container and HSR bomb-compatibility trials can occur using the E5 q/suspension school. Treat late-1939 technical qualification as plausible, but do not inject unrecorded effects into closed 1939 battles.

### 1940 Q1
E6 local high-Mach/bay/separation requalification and service tables. The weapon family may enter unit service with the lead service-production aircraft rather than wait for a 1941 adoption decision.

---

## 11. Service-release matrix at 1939-12-31 planning gate

| configuration | JF | J | status |
|---|---|---|---|
| two-seat common airframe | YES | YES | CLOSED |
| 2×20 mm + 4×7.7 mm-class common nose envelope | YES | YES | AIRFRAME ENVELOPE CLOSED; exact service gun identity local |
| camera/command-recon module | YES | limited/optional | CLOSED |
| 0.35–0.40 t internal light-strike load | YES | possible but not priority | CLOSED MASS/CG ENVELOPE; bomb marks local |
| HSR Army 50/100 + Navy 60 kg-class high-speed compatibility | YES | YES | 1940-Q1 SERVICE-RELEASE PATH |
| HSR 250 kg-class service bomb | YES | possible but not priority | 1940-Q1-Q2 SEPARATE RELEASE LADDER |
| HSC-100F ~100 kg-class harassment container | YES | YES | LATE-1939/1940-Q1 TECH/SERVICE GATE |
| D320F + camera | YES | not preferred | CLOSED JF MAIN USE |
| D320F + camera + ~100 kg nuisance store | YES with reduced internal fuel | not preferred | CLOSED LOAD-SHEET ENVELOPE |
| full D320F + full 0.40 t strike + full internal fuel | NO routine | NO routine | PROHIBITED STACKING |

---

## 12. No-backflow / no-magic guard

This closure does **not**:
- change any closed 1937–39 combat result;
- create precision bombing at 700+ km/h;
- create radar/GCI;
- give every reconnaissance sortie a bomb load;
- make external bombs drag-free;
- make full fuel + full bombs + full drop tanks a free combination;
- backdate later 20 mm×4 fighter batteries;
- change Army/Navy explosive fillings or fuze identities without a separate chronological ordnance authority.

It closes the system-level fact that the military, after years of E5 high-speed light-strike/recon operations, enters 1940 with a credible high-speed internal-release school. E6FRPORD1 now controls the FRP door/cassette/tail-fairing architecture, S6/S4/M1 load families and refined HSC-100F carrier.

**E6 TWIN MISSION / ARMAMENT / HIGH-SPEED RELEASE CLOSURE — V1**
