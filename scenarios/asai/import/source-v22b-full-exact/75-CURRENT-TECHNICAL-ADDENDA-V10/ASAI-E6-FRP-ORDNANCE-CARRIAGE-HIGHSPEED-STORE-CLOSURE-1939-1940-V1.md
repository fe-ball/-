# ASAI WORLDLINE — E6 TWIN FRP ORDNANCE CARRIAGE / HIGH-SPEED STORE CLOSURE V1
## 1939–1940 plant-FRP application to bomb-bay doors, store adapters, stabilizing fairings and dispersal carriers

**Status:** CLOSED DESIGN / 1940 SERVICE QUALIFICATION PATH  
**Clock effect:** NONE — combat remains stopped at 1939-12-31 24:00.  
**Purpose:** Refine E6MISSION1 using the already-closed Asai epoxy/plant-FRP capability. This file decides where FRP changes the ordnance system materially and where metal remains the rational choice.

---

## 0. Central closure

1. **Do not replace ordinary HE bomb bodies with FRP.** The steel body remains part of the bomb's structural and fragmentation function. FRP is used around the bomb, not instead of the normal bomb body.
2. **Use plant-FRP aggressively on expendable/non-primary aerodynamic structure:** bomb-bay doors/door skins, removable mission/store cassette fairings, selected high-speed tail/fairing sets, HSC dispersal-carrier shells, and D320F tanks.
3. **Keep concentrated-load hardware metal:** suspension hooks/lugs, release spines, hinge pins, local hardpoints and other concentrated-load fittings.
4. 1939–40 production material is **selected flax/hemp + Asai epoxy**, with sealed surfaces. Local glass veil may be used for abrasion/edge protection where supply allows. Broad wet-strength structural GFRP is not required; CFRP is specifically rejected for expendable stores.
5. The E6 internal mission bay is standardized around three service adapter families rather than one-off bomb installations:
   - **S6 small-store cassette:** up to six 50/60 kg-class stores, subject to the ~0.40 t bay mass limit;
   - **S4 medium-store cassette:** up to four 100 kg-class stores or HSC-100F carriers, subject to the same limit;
   - **M1 heavy-store cradle:** one 250 kg-class conventional service bomb.
6. Selected historical-service bomb classes are therefore expanded from the earlier HSR-50/100 wording to a service-specific HSR family:
   - Army: selected **50 / 100 / 250 kg-class** bombs;
   - Navy: selected **60 / 250 kg-class** bombs;
   - exact bomb marks remain service-local.
7. **HSC-100F becomes the common modular dispersal carrier** because a ~100 kg store is useful both as one reconnaissance nuisance load and as a four-position dedicated area-strike load. A larger dedicated FRP carrier is not standardized in 1940 because it gives up cassette commonality and requires another bay-volume/separation program for little gain.
8. E6 high-speed release remains an **area-effect / harassment / fixed-area attack capability**, not precision point bombing.

---

## 1. Why FRP changes the system, but not the bomb body

Asai has already released plant-FRP as an early-win process for:
- fairings / ducts / covers;
- selected fuel/external tanks;
- doors / floors / secondary panels;
- molded large secondary shapes.

Those are exactly the parts around an internal weapon installation that consume shaping labor but do not need to be metallic primary structure.

The useful split is therefore:

| part | 1939–40 material choice | reason |
|---|---|---|
| normal HE bomb body | steel / service-standard metal | structural body and terminal fragmentation function |
| suspension lug / release spine | metal | concentrated release and maneuver loads |
| stabilizing tail structural attachment | metal local fitting | local concentrated load |
| tail cone / stabilizer fairing where requalified | **flax/hemp-epoxy FRP** | repeatable smooth geometry, low metal demand, disposable |
| bay cassette tray/fairing | **plant-FRP / sandwich + metal lugs** | low inertia, modularity, fast shape changes |
| bay door skins / non-primary door panel | **plant-FRP / paper-sandwich hybrid** | low inertia and smoothness; existing 1938–39 secondary-structure capability |
| HSC carrier outer body | **flax/hemp-epoxy FRP** | expendable low-pressure molded shell; contents provide terminal effect |
| D320F | **flax/hemp-epoxy FRP** | already closed by E6REBASE1 |

The result is not a miraculous weight reduction. The important gains are **shape repeatability, light-alloy/steel conservation, fewer skilled thin-sheet hours, and cheap iteration during separation trials**.

---

## 2. Internal bay adapter architecture

The ~0.40 t mission bay remains the controlling mass envelope. E6FRPORD1 closes the following ordinary load forms.

### 2.1 S6 — 50/60 kg small-store cassette

Normal compatible loads:
- Army: up to **6×50 kg-class** = ~0.30 t nominal store mass;
- Navy: up to **6×60 kg-class** = ~0.36 t nominal store mass.

Use:
- broad-area light attack;
- runway / dispersal / rail-yard nuisance attack;
- smaller-store ballistic-table work;
- service-specific mixed lots only when separately released.

The cassette's aerodynamic/non-primary tray structure may be molded plant-FRP, with metal suspension/release fittings.

### 2.2 S4 — 100 kg / HSC cassette

Normal compatible loads:
- up to **4×100 kg-class conventional stores** = ~0.40 t;
- up to **4×HSC-100F** provided actual accepted lot mass keeps total mission load at or below the ~0.40 t bay limit;
- camera + one HSC-100F is the routine reconnaissance-harassment combination;
- camera + two HSC-100F is available for shorter-radius deliberate armed reconnaissance when the load sheet permits it.

This is the most flexible E6 strike cassette and should be the production center.

### 2.3 M1 — 250 kg heavy-store cradle

Normal compatible load:
- **1×250 kg-class conventional service bomb**.

The 250 kg store does not fill the bay's mass allowance, but it consumes enough local volume/separation margin that E6FRPORD1 does not standardize an additional heavy store beside it. The unused mass margin can instead be spent on fuel, normal ammunition or other mission equipment.

---

## 3. HSR-F high-speed stabilizing / integration package

The earlier `HSR-50/100` concept is broadened into a service-specific compatibility family. `HSR` remains an **integration/release standard**, not a new explosive identity.

### 3.1 What FRP adds

For selected service bombs, the high-speed kit may include:
- a molded aerodynamic afterbody/tail fairing;
- repeatable stabilizer geometry;
- protective fairing around otherwise draggy attachment detail;
- plant-FRP non-load-bearing portions with local metal fittings;
- bomb-specific mass-property and ballistic requalification.

This is useful even though carriage is internal: after bay release the store immediately enters a Mach-sensitive free stream, and repeatable tail geometry reduces separation/ballistic scatter attributable to hardware variation.

### 3.2 Release bands

**Small/medium conventional stores — Army 50/100, Navy 60, HSC-100F:**
- normal qualified high-altitude release target: **~700–760 km/h TAS at ~7–9 km**;
- local Mach/separation tables remain store-specific.

**250 kg-class store:**
- initial 1940 service qualification band: **~650–720 km/h TAS at ~6–8 km**;
- expansion upward is a flight-test result, not assumed automatically from the smaller-store table.

Reason: the 250 kg bomb is structurally ordinary for the period, but its bay-clearance/separation transient is a larger-store problem and deserves its own release ladder.

---

## 4. HSC-100F — FRP modular dispersal carrier

### 4.1 Revised production center

`HSC-100F` remains a nominal **~100 kg-class** store.

Working production center:
- total accepted store mass: **~96–102 kg class**;
- FRP outer carrier + metal spine/fittings: **~12–18 kg class**;
- useful carried service payload: **roughly low/mid-80 kg to high-80 kg class**, depending the arsenal payload and service fittings.

This is intentionally not sold as a huge weight miracle. The important fact is that the container overhead stays modest while avoiding a fully metal aerodynamic shell.

The contained items are existing service small fragmentation/incendiary-type aerial stores selected by the Army/Navy arsenal. Their exact internal arrangement, fuze and arming details remain separate service-ordnance records.

### 4.2 Why 100 kg is the standard size

A ~100 kg carrier does three jobs with one production article:
1. **one-store reconnaissance nuisance load**;
2. **two-store armed reconnaissance load** when range is traded for area effect;
3. **four-position dedicated area-strike cassette** within the E6 ~0.40 t mission-bay class.

A 180–250 kg dedicated FRP dispenser would reduce inert fraction slightly, but it creates another bay adapter and separation program and loses the one-store reconnaissance use. Therefore it is not a 1940 standard requirement.

### 4.3 Normal target class

HSC remains appropriate for broad, exposed targets:
- airfield dispersal / service areas;
- rail yards / sidings;
- truck parks and supply concentrations;
- exposed troop/artillery concentrations;
- similar fixed-area targets.

It is not the default answer for a bridge, ship, individual vehicle or other small point target.

---

## 5. FRP bomb-bay doors and cassette structure

The E6 high-speed internal-release concept benefits directly from Asai's pre-existing door/fairing/sandwich capability.

Closed architecture:
- door skins / non-primary door panel: plant-FRP or plant-FRP/paper-sandwich hybrid;
- hinge axes, local actuator pick-ups and hardpoints: metal;
- removable S6/S4 cassette fairing/tray: plant-FRP/sandwich with metal load fittings;
- ordinary service inspection concentrates on edge sealing, local bond damage, hardpoint condition and door alignment.

Operational consequence:
- lower door/cassette inertia helps keep bay exposure transient;
- smooth molded inner/outer surfaces make separation geometry more repeatable;
- damage to a removable cassette need not ground the airframe structure itself;
- new store shapes can be trialed by changing molded adapters rather than rebuilding the central fuselage.

No new E6 zero-fuel-weight headline is created: the saving sits inside the existing ~3.50 t mission-ready bookkeeping uncertainty rather than being double-counted as a new performance bonus.

---

## 6. Standard 1940 E6-JF ordnance menus

| mission | normal internal load | planning meaning |
|---|---|---|
| R | camera ~0.10–0.14 t | normal reconnaissance |
| RH1 | camera + **1×HSC-100F** | routine armed reconnaissance / nuisance option |
| RH2 | camera + **2×HSC-100F** | shorter-radius deliberate armed reconnaissance; load-sheet dependent |
| S-small Army | **6×50 kg-class** | ~0.30 t broad-area light strike |
| S-small Navy | **6×60 kg-class** | ~0.36 t broad-area light strike |
| S-medium | **4×100 kg-class** | maximum ordinary ~0.40 t conventional internal strike |
| S-dispersal | up to **4×HSC-100F** | maximum modular area-effect strike within bay mass limit |
| S-heavy | **1×250 kg-class** | larger single-store attack; separate lower release ladder initially |
| LRH | D320F + camera + **1×HSC-100F**, reduced internal fuel | long reconnaissance + nuisance release; remains inside ~5.05 t takeoff ceiling |

No routine configuration stacks full internal fuel + full D320F + the full 0.40 t strike load.

---

## 7. Chronology

### 1937–38
- E5 pays the basic internal light-strike, suspension, release-delay and bomb-table school.
- plant-FRP doors/fairings/tanks move from limited to selected serial use.

### 1939 H1
- recurring E5 high-speed reconnaissance/attack makes a small internal area-effect carrier an obvious ordnance requirement rather than an E6 surprise.
- S6/S4-style interchangeable carrier logic and molded expendable fairings are credible development work.

### 1939 H2
- HSC-100F technical qualification and FRP high-speed tail/fairing trials are plausible on E5-calibrated q levels.
- closed 1939 combat records receive no automatic backflow from this planning inference.

### 1940 Q1
- E6 local S6/S4/HSC separation and high-Mach release tables qualify with lead service-production aircraft.
- Army 50/100 and Navy 60 kg-class HSR service release can proceed with the lead units.

### 1940 Q1–Q2
- M1 / 250 kg-class E6 separation ladder qualifies separately at the lower initial high-speed band.

---

## 8. Setting guards

1. Existing Army/Navy bomb identities remain separate unless an adapter/release table explicitly bridges them.
2. Better release tables do not create precision bombing.
3. FRP does not make conventional HE bomb bodies lighter for free; the body remains service-standard metal.
4. The mission-bay mass limit remains ~0.40 t.
5. High-altitude TAS release numbers are not copied to low altitude.
6. HSC payload effect comes from existing service submunitions; E6FRPORD1 changes the carrier/integration system.
7. No closed 1939 combat outcome is changed by this 1940 service-qualification closure.

**E6 TWIN FRP ORDNANCE CARRIAGE / HIGH-SPEED STORE CLOSURE — V1**
