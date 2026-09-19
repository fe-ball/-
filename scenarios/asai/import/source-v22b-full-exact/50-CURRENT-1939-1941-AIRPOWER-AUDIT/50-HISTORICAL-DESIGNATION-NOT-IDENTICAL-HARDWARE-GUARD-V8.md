# HISTORICAL DESIGNATION != IDENTICAL HARDWARE GUARD — V8 IDENTITY1

> Session closure: 2026-09-05. This is the current V8 cross-service guard for historical Japanese designations that survive in the Asai worldline while hardware, installation, production state, service state, chronology, or even designation mapping differs. It complements `47/47A` and the exhaust-specific `49/49A`. This guard does **not itself** advance the combat clock; current chronological authority is REPLAY3 through **1939-06-27 24:00**.

## 0. Core rule

A historical designation is an **identity label**, not permission to copy the complete historical datasheet.

The worldline deliberately preserves historical names where lineage/mission remains recognizable. Therefore any historical vehicle/aircraft/engine with the same name must pass this sequence before its historical specification is used:

1. **designation identity** — does the code/name refer to the same lineage in this worldline at all?
2. **date / lot / sub-variant** — is the historical anchor from the same production state?
3. **visible configuration** — airframe, armor, gun, propeller, exhaust, cooling, engine installation, transmission, etc.;
4. **production state** — materials, bearings, heat treatment, tolerances, balancing, gauges, acceptance/QC;
5. **service state** — maintenance, spares, workshop/recovery, radio installation quality, mission preparation and operational availability;
6. **historical-anchor inclusion** — did the quoted historical performance already consume a later improvement (e.g. EX2 thrust exhaust)?
7. **allocation/adoption** — technical availability does not prove that a named unit has the modified lot.

If any answer differs, use the local V8 ledger rather than silently copying a historical figure.

## 1. Identity classes

- **ID0 — near-historical hardware:** historical headline specification may be used unless a local V8 file changes it; readiness/QC may still differ.
- **ID1 — same designation, installed-system delta:** recognizable historical vehicle, but propulsion/prop/exhaust/cooling/transmission/electrical installation differs.
- **ID2 — same designation, production delta:** nominal design is near historical, but material/process/QC/acceptance makes realized performance, life or variance different.
- **ID3 — same designation, service-state delta:** nominal vehicle can be historically similar while operational availability, repair cycle, radio/workflow or support differs.
- **ID4 — lot/variant split:** early/late or depot-retrofit states differ under the same broad designation; date/serial/lot is mandatory.
- **ID5 — designation remap/collision:** the code/name does **not** mean the same aircraft as in ordinary historical references. Historical data may be used only under the explicitly mapped historical-anchor name.
- **IDH — historical anchor only:** the historical type is retained as a comparison/calibration object; its complete historical performance must not be treated as the worldline production article without the H->C->M->E->P->I->A pass.

Multiple tags may apply to one item.

## 2. Mandatory Navy designation warnings

These are high-risk because normal aviation references encourage automatic code-name matching.

### A7M / A9M — highest-priority warning

- **Worldline A7M = Gaifu**, the earlier Navy carrier turboprop fighter line.
- **Historical A7M1/A7M2 Reppu is not worldline A7M.** When historical Reppu hardware/performance is used as an H-anchor, write **`historical A7M Reppu (worldline designation A9M)`**.
- The historical Reppu lineage, if it survives the requirement/procurement gate, is **A9M** in the worldline naming map.
- Therefore a bare `A7M2 = 628 km/h`, A7M2 mass, Ha-43 cooling, exhaust, etc. must never be read as a specification of worldline Gaifu.

### A8N / J2N

- **A8N = Sakufu**, Navy carrier jet fighter line. It is a worldline program, not a historical A8V/A7M substitute.
- **J2N = Hekireki**, Navy twin-jet interceptor competing under the same broad local-fighter requirement space as historical J2M Raiden. J2N is not shorthand for J2M and its data must never be inherited from Raiden.

### B6N / B7A

- **B6N Tenzan** is restored to the historical Nakajima lineage. Old `B6A Aichi Tenzan` material is superseded.
- **B7A Ryusei** remains Aichi's independent integrated attack design, not a Tenzan derivative.

## 3. Navy aircraft — same historical name, altered state

The detailed machine-readable treatment is in `50A` and exhaust state in `49A`. High-risk examples:

- **A6M1 / 12-Shi:** V8 first-flight article uses the Z-900N working engine path, three-blade constant-speed propeller from first flight and design-origin thrust-exhaust integration. Historical A6M1 configuration is not a direct copy.
- **A6M2:** basic lineage/mission remains Zero, but V8 A0 propulsion/prop/exhaust/cooling/test integration differs. Use the Zero rebaseline, not a bare historical performance sheet.
- **A5M4:** late new-build/major-overhaul exhaust state can differ; existing fleet is lot-dependent rather than blanket-upgraded.
- **B5N2:** old `historical individual exhaust -> E1=0` ruling is superseded. Historical working state is EX0 collector-ring; worldline later production may be EX2. Use date/lot.
- **D3A1, G3M2:** broadly historical mission/airframe, but later/new-build exhaust and production/QC states can differ.
- **E13A, F1M2, H6K5:** adoption is role/economics/lot dependent; do not assign a fleet-wide speed card simply because the technology exists.
- **G4M1, J1N1:** worldline new-production installation can reach EX2/EX3 years before the historical late-production change. Historical speed anchors must match weight/variant and exhaust state.
- **B6N1/B6N2, P1Y1:** same designation family does not mean same exhaust state. B6N2 and production P1Y already contain historical individual-stack improvement; full collector-to-stack credit cannot be repeated.
- **J2M2/3, N1K1-J/N1K2-J, H8K, A6M5:** historical production anchors already contain mature individual/thrust exhaust to a significant degree. Asai delta is residual integration/QC, not another full conversion.
- **D4Y:** DB601/Atsuta-derived exhaust begins near EX2; radiator/heat-recovery is a separate card.
- **B7A:** treat the historical production aircraft as already near EX2 unless stronger hardware evidence says otherwise; Homare realization is the larger worldline lever.

## 4. Army aircraft — same name, altered state

- **Ki-27:** basic airframe and armament remain historical, but late-production EX2 exhaust path plus engine/prop matching/QC/serviceability means a late worldline aircraft is not numerically identical to an early historical Ki-27. REPLAY3 has now closed the current Nomonhan 24th Sentai pool at **EX2 x15 / EX0 x4**; this named-unit closure must not be generalized to other sentai.
- **Ki-15-II / C5M1/2:** reconnaissance priority and new-engine installations can receive earlier exhaust integration; do not copy one variant's value into another.
- **Ki-43 / Ki-44 / Ki-45 Kai / Ki-46 / Ki-48 / Ki-49 / Ki-51:** historical lineage survives, but V8 installation/test/QC and, where closed, thrust-exhaust timing differs. Full speed cards are variant/state dependent.
- **Ki-61:** Ha-40/DB601-derived individual stacks are already near EX2; do not add a collector-to-stack card. More important V8 deltas are Ha-40 materials/production health plus separate radiator/heat-recovery work.
- **Ki-84:** earliest historical prototype collector state is a comparison shadow only. Production 631-km/h-class historical anchor already belongs to the individual-exhaust side; worldline 645-660 band is mainly Homare realization/QC/cooling plus residual EX3.
- **Ki-64:** current V8 meaning is the historical Kawasaki tandem-Ha-40 experimental heavy-fighter lineage. The old P-47-class single-engine turbo production concept under `Ki-64` is superseded and must not re-enter by name association.
- **Ki-76:** the worldline deliberately reuses/inherits the historical role/designation slot on an accelerated STOL liaison lineage. Do not import the historical service-entry date as a capability ceiling.

## 5. Engines and propulsion — same designation is especially dangerous

- **Homare:** historical rated figures are useful design anchors, but historical failure to reproduce rated output, bearing/fuel/ignition/cooling problems and fleet variance are not automatically copied into V8. The large worldline gain on Ki-84/N1K/B7A/P1Y is often **realization of intended output**, not a fictional extra exhaust card.
- **Ha-40 / Atsuta:** same design lineage does not imply historical production failure/shortage. V8 metallurgy/process/QC changes can keep the line alive; therefore the historical Ki-100 conversion trigger is not automatically present.
- **Sakae / Ha-25:** do not grant a generic horsepower bonus. Ratings/whole-altitude maps remain variant-specific; V8 gains are mainly integration, exhaust where state-differential, matching, durability and repeatability.
- **Ha-43:** historical Reppu installation evidence is an installation anchor only. It must not be silently attached to worldline A7M Gaifu because `A7M` is a designation remap.

## 6. Ground vehicles / weapons

- **Type 97 Chi-Ha:** same tank designation, but ordinary 1938-39 V8 production center is **200 hp continuous / 220 hp short** Mitsubishi V12 + Asai low-pressure turbo/intake. Historical engine output/mobility is not a direct copy. Gun/armor doctrine remain broadly historical unless separately changed.
- **Type 95 Ha-Go:** mass line remains near historical ~120 hp naturally aspirated. Do **not** infer a blanket turbo conversion; special altitude/hot-weather/test branches are separate.
- **heavy 6x4 trucks / artillery tractors / workshop-recovery vehicles:** selected high-value vehicles can have turbo-diesel, filtration, transmission/cooling/QC and standardized support packages. Historical vehicle counts may remain useful, but historical availability/repair/towing performance is not automatically the worldline value.
- **Type 94/97 tankette/light armored class:** near-historical headline capability; no blanket turbo conversion. Production/QC/support may differ.
- **37 mm dense-core special AP:** the gun remains the historical gun; ammunition state is a separate controlled-inventory gate. By 1939-06-27 REPLAY3 has two **non-interchangeable** forward-issued test-combat stocks: infantry `AT-37` 48 rounds (4 guns x12) and tank-gun `TANK-37` 48 rounds (8 Ha-Go x6). Neither has field-combat validation yet.
- **flexible spall liner:** a vehicle retaining its historical designation may later receive the liner, but current REPLAY3 through 1939-06-27 still has **0 combat vehicle fitment**. Fit count and combat effect remain event/allocation gates.

## 7. Navy ships / carriers — headline performance cards do not move together

The generic ship guard in `50A` is tightened here. A historical ship name/class remains a hull/architecture anchor unless a local current audit closes a worldline change. Asai capability may improve machinery repeatability, auxiliary power, maintenance or design analysis without automatically changing displacement, shaft horsepower, maximum speed, aircraft capacity or combat resilience.

For carriers, never collapse the following into one number:

`historical hull/deck geometry -> installed machinery -> delivered/serviceable shaft power -> speed at actual displacement/sea state -> wind over deck (WOD) -> aircraft takeoff/landing envelope -> elevator/hangar/deck handling -> deck-ready aircraft -> sortie generation`

A gain at one stage does not automatically propagate through all later stages.

### Existing fleet carriers: Akagi / Kaga / Soryu / Hiryu

- Historical post-modernization hull, flight-deck, hangar, elevator, shaft-line and main-plant geometry remain the default anchor unless an explicit refit audit changes them.
- Asai QC/metrology can improve turbine/boiler repeatability, bearing life, auxiliary machinery, electrical reliability and maintenance turnaround. That is primarily **ID2/ID3**, not a free increase in rated shaft horsepower.
- Do not add a generic knot bonus from better turbine quality. High-speed ships are subject to the approximate cube-law relation between required propulsive power and speed; a modest power gain normally buys only a small speed change, and propeller/cavitation/hull resistance remain gates.
- Do not turn better aircraft serviceability into a larger physical hangar or elevator. Air-group inventory, serviceable aircraft, deck-ready aircraft and sortie rate are separate ledgers.
- A heavier/larger worldline carrier aircraft is not automatically compatible merely because it carries a Navy designation. Elevator planform/load, hangar clearance, flight-deck strength, arresting loads, deck run and WOD must pass locally.

### Shokaku-class and other new-build carriers

- Because design/construction overlaps the Asai period, historical Shokaku-class data are a strong **H anchor**, not proof that every detail is unchanged.
- Conversely, Asai capability does not automatically alter displacement, 34-knot-class speed, range, elevator dimensions, hangar volume, armor/protection, air-group capacity or build date. Each requires a design-freeze / yard / procurement audit.
- Improvements most likely to enter without redefining the class are production/QC, electrical distribution, auxiliary machinery, instrumentation, fire pumps/ventilation and maintainability; even these need adoption timing.

### Light / small carriers: Hosho / Ryujo and later light-carrier conversions

- Small hulls are particularly constrained by stability, topweight, freeboard, deck area, elevator geometry and aviation-fuel/ordnance arrangement.
- Better machinery or aircraft does not create free deck area or stability margin. Any added radar, AA, fire protection, fuel or larger aircraft consumes weight/volume/topweight.
- Do not infer fleet-carrier sortie generation from nominal aircraft count.

### Low-speed converted / merchant carriers, including Taiyo-class type conversions

- The current large-marine canon explicitly supersedes the old shortcut that a ~21-knot converted carrier plus GT boost automatically becomes a fleet carrier.
- GT boost can be studied as a **short-duration WOD aid** only after installed shaft power, intake/exhaust trunks, reduction gear/clutch, shaft torsion, salt MTBO, fuel and 30-60 minute operating window are paid.
- Even if a few knots become technically available, protection, subdivision, elevator/hangar geometry, deck cycle, aviation-fuel safety, seakeeping and sustained fleet speed do not automatically improve.

### Carrier machinery / WOD / GT guard

- Apr20 1939 current state contains shore marine-GT qualification functions but **no automatic large-surface-ship GT installation**. Carrier boost remains a future requirement/procurement gate under `42-MARINE-GT-1939-04-20-STATE-CANON-V8.md`.
- GT bare-engine power-to-weight is never sufficient evidence. Installed mass/volume includes reducer, clutch, intake separation/filtering, exhaust trunk, fuel, controls, spares and structural work.
- WOD is ship speed plus ambient wind component along the deck; a theoretical speed increment is not automatically available on every launch/recovery course or sea state.
- A WOD gain does not automatically increase maximum aircraft takeoff weight unless deck run, propulsive acceleration, landing/recovery envelope and structural handling also close.

### Carrier capacity and sortie-generation guard

For any carrier OOB, keep at least these states separate:

`physical stowage capacity -> actually embarked inventory -> serviceable inventory -> deck/hangar spotted state -> launchable package -> recovered/rearmed/refueled package -> repeat sortie rate`

Asai aircraft QC may improve the **serviceable** term. It does not directly enlarge physical stowage, elevator throughput or deck parking. Workshop tooling can shorten some maintenance cycles, but fueling, weapon handling, elevator movement, spotting and deck-clearance procedures remain independent bottlenecks.

### Shipboard weapons, electronics and damage control

- Better metallurgy/QC does not silently increase naval-gun range, rate of fire, armor penetration or director accuracy. Gun, ammunition/fuze, mount, director/radar and crew drill are separate cards.
- Radar/electrical capability does not prove shipboard fit, quantity, antenna position or doctrine. Each ship/class requires an installation/adoption gate.
- Better pumps, wiring, emergency generation, seals and materials can improve damage-recovery potential, but do not grant USN-style damage-control outcomes automatically. Compartmentation, aviation-fuel arrangements, fire mains, redundancy, training and doctrine remain decisive.

### Capital ships and other surface combatants

- Yamato/A-140 central path remains historical-style all-steam machinery; improved No.13 diesel knowledge does not automatically reopen diesel main propulsion.
- Destroyer/cruiser GT additions remain conditional. Existing high-speed ships receive small maximum-speed returns from modest added power, while intake/exhaust/reduction/shaft integration costs remain large.
- Historical hull count and commissioning schedule remain default unless yard capacity, material allocation, procurement decision and construction event are separately replayed. Industrial efficiency is not permission to conjure extra hulls.

The detailed machine-readable cautions are in `50A`; the current technical authority for large marine GT is `42` plus `99-SUPPORT-CURRENT/1939-COMPANY-STATE-SELECTED/asai-works-surface-ship-large-marine-rebaseline-1934-41.md`.

## 8. Use rule for OOB / combat replay

When a historical OOB says `N x Ki-27`, `N x B5N2`, `N x Chi-Ha`, etc., retain the **count** unless the replay changes procurement/attrition, but do not automatically inherit the historical configuration mix or ready rate.

For each counted item:

`historical inventory count -> worldline lot/config mix -> operational/serviceable -> forward deployed -> combat used`

This is the same separation already used for equipment allocation. A technical delta never creates a named-unit retrofit count by itself.


## 8A. Fire-effect chain guard — same hardware name can still produce a different firing/bombing result

Historical designation identity is not enough to copy historical **hit probability, bombing dispersion, first-round hit rate, torpedo attack accuracy or AA effectiveness**.

For any combat-effect calculation, resolve:

`observation -> sight/sensor -> input/estimate -> calculation/correction -> indication -> boresight/stabilization -> mount/release -> ammunition/ballistics -> crew execution -> environment -> effect`

A same-named Ki-27, Ki-21, Chi-Ha, Type 94 37 mm gun, carrier or naval gun can retain its historical main hardware while the Asai worldline changes calibration, boresight, production/QC, ballistic tables, release timing, photo-target workflow or fire-control follow-up. Conversely, an upstream computation capability does **not** prove that a new reflector/gyro sight, director, radar or automatic release system was adopted.

Before copying a historical fire-effect number, consult `51-FIRE-CONTROL-SIGHTING-BOMBING-INTEGRATION-CANON-V8.md` / `51A`. In particular:

- same gun caliber does not imply same ammunition, sight state or firing dispersion;
- same aircraft/bomb load does not imply identical bombing concentration;
- same sight architecture with better calibration does not justify a generic fixed hit-rate multiplier;
- later historical reflector/gyro/director benefits may not be added again if the historical performance anchor already contains them;
- better reconnaissance target folders and better weapon-sight workflow are separate stages and must not be double counted.

## 9. Cross-reference / precedence

- General historical-vehicle delta: `47-1939-04-20-HISTORICAL-VEHICLE-DELTA-CANON-V8.md` / `47A`.
- Exhaust-specific state differential: `49-PISTON-EXHAUST-ENERGY-RECOVERY-CANON-V8.md` / `49A`.
- Fire-control / sighting / bombing-effect chain: `51-FIRE-CONTROL-SIGHTING-BOMBING-INTEGRATION-CANON-V8.md` / `51A`.
- Naval ship/carrier headline-performance guard: Section 7 here; marine-GT current state `42`; large-marine technical rebaseline under `99-SUPPORT-CURRENT/1939-COMPANY-STATE-SELECTED/`.
- This file / `50A` is the **identity and historical-datasheet guard**. Where it flags ID5 remapping, its designation interpretation controls bare-name readings.
- Local aircraft/engine rebaseline remains authoritative for the actual numerical A-state.
- Procurement, production quantity, OOB allocation and combat use remain chronological/event gates.
