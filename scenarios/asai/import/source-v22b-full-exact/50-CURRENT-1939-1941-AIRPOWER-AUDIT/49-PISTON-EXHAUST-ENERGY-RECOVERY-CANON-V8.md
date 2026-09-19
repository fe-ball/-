# PISTON EXHAUST ENERGY RECOVERY CANON — V8 EXHAUST1

> Session closure: 2026-09-05. This file is the current V8 authority for individual/ejector exhaust treatment on historical piston aircraft and supersedes any older binary reading of “individual exhaust exists -> Asai delta = 0” or “Asai knows thrust exhaust -> add the full collector-to-stack speed gain to every later aircraft.” This technical file does **not itself** advance the combat clock; current chronological authority is now REPLAY3 through **1939-06-27 24:00**.

> **IDENTITY1 cross-reference:** same-name / designation interpretation is controlled by `50-HISTORICAL-DESIGNATION-NOT-IDENTICAL-HARDWARE-GUARD-V8.md` / `50A`. In particular, bare `A7M` means worldline Gaifu; historical Reppu A7M data are worldline A9M anchors.

## 0. Core decision

Asai is not merely a vendor of a particular exhaust pipe. For military work it acts as a technology-transfer / consulting / test-method supplier: protected military-use IP is released to the services and manufacturers, with nozzle-area selection, back-pressure measurement, thrust-axis alignment, heat/support design, cooling-outlet interaction, acceptance gauges, endurance testing and production QC transferred with the hardware concept.

Therefore exhaust credit is **state-differential**, not binary.

- **EX0 — collector/common exhaust:** collector ring or common manifold; no meaningful rearward momentum recovery credit assumed.
- **EX1 — individual exhaust, non-integrated:** separate stubs/pipes exist, but rearward thrust recovery and installation integration are not yet demonstrated as the governing design objective.
- **EX2 — thrust individual/ejector exhaust:** rearward jet thrust is intentionally recovered; gross collector-to-stack gain is already substantially consumed.
- **EX3 — integrated exhaust-energy recovery:** EX2 plus nozzle-area/back-pressure optimization, flow direction, cowling/cooling-exit interaction, thermal/support life, production repeatability and flight/bench A/B closure.

### Mandatory double-count guard

1. If the historical performance anchor already uses an **EX2** production aircraft, do **not** add the full EX0->EX2 gain again.
2. Historical EX2 aircraft may still receive **EX2->EX3 residual** benefit, normally a small speed increment plus cooling, life and production-repeatability benefit.
3. Liquid-cooled DB601/Ha-40/Atsuta installations that already use effective individual exhaust stacks begin near EX2 for this ledger. Their larger Asai installation opportunity is partly a **separate radiator/heat-recovery card**; do not hide Meredith-type credit inside the exhaust card.
4. Late 1943-45 aircraft are already aerodynamically mature. Their total Asai low-altitude new-aircraft speed delta remains bounded by the existing late-war guard; exhaust is only one component.

## 1. Physical calibration retained

The validated legacy calculation remains useful as a **collector-to-good-thrust-stack shadow**, not as an automatic worldline increment.

- Zero A6M5 within-type historical comparison remains the primary Japanese calibration: net exhaust thrust about **120-195 N**, central about **160 N** for the calibrated Sakae installation.
- Simplified mass-flow scaling remains approximately **0.75 kg/s per 1,000 hp** at the relevant full-power condition when aircraft-specific data are unavailable.
- Exhaust thrust horsepower is `F * V`; it is an aircraft/flight-condition quantity, not a fixed engine attribute.
- Nozzle area is an optimization problem: excessive restriction can increase jet velocity while losing more shaft power to back pressure.

The following old “full EX0->EX2” speed shadows remain usable when the historical anchor is truly EX0:

| aircraft | full exhaust-only shadow |
|---|---:|
| Ki-27b | +5 to +8 km/h (legacy calc +5.4 to +8.3) |
| A6M2 | +6.4 to +10.1 km/h |
| Ki-43-I | +5.8 to +9.0 km/h |
| Ki-44-I | about +6.5 to +11 km/h |
| Ki-46-II | +7.6 to +12.4 km/h |
| Ki-48-I | +5.7 to +8.7 km/h |
| Ki-21-IIa | about +6 to +9 km/h |
| B5N2 | about +4 to +6 km/h |
| D3A1 | about +4 to +6 km/h |
| G4M1 early | +5.2 to +7.9 km/h |
| G3M2 | about +4 to +6 km/h |

These values are not procurement or fleet-performance statements.

## 2. 1937-40 early-adoption canon

### Ki-27 Type 97 fighter

- Historical baseline: **EX0 collector/manifold**.
- Asai path: 1937 flight/bench comparison; thermal, support and nozzle work continues; **late-production 1938 onward moves to EX2**, with existing aircraft eligible for overhaul retrofit rather than instant fleet conversion.
- Exhaust-only worldline delta for an EX0 aircraft converted to the mature early stack: **about +5 to +8 km/h**, central about +6 to +7.
- Do not turn this into a “super Ki-27.” The main late-1930s worldline advantage also includes accepted-output and serviceability/repeatability, not only clean-air maximum speed.
- The 24th Sentai force-allocation gate is now closed by REPLAY3 at **EX2 x15 / EX0 x4** for the current Nomonhan unit pool. This is a named-unit/date closure, not a national ratio.

### Ki-15-II / C5M

- High-speed reconnaissance makes exhaust thrust unusually valuable per unit installation tax.
- Ki-15-II new production may enter with **EX2/early EX3** after the long prototype-to-production interval; physical exhaust shadow **about +6 to +9 km/h**.
- C5M1 may remain mixed due small production and timing.
- C5M2 is a separate Sakae-powered installation; 1940 new production should normally consider **EX2 standard**, physical shadow roughly **+5 to +8 km/h** if compared to an EX0 installation.

### A5M4

- Historical installation is EX0-class exhaust-ring/collector architecture.
- Single-row engine makes retrofit technically easy, but remaining service life limits economic priority.
- Late new production / major-overhaul aircraft may receive EX2; full physical shadow **about +5 to +7 km/h**.
- No blanket retrofit of the entire surviving A5M fleet.

### B5N2 correction

- **SUPERSESSION:** older V8 wording that treated B5N2 as already historical individual-thrust exhaust and therefore assigned `E1 = 0` is withdrawn.
- The historical Sakae installation is treated here as **EX0 collector-ring** unless a stronger primary installation drawing overturns this closure.
- The old physical shadow **about +4.3 to +6.2 km/h** is therefore restored as a valid EX0->EX2 comparison.
- Worldline adoption is progressive: initial production may retain EX0; later B5N2 production can move to EX2 as the naval standardization package matures.

### D3A1

- Historical baseline remains EX0 collector-ring class.
- Physical exhaust-only shadow **about +4 to +6 km/h**.
- Initial production may remain EX0; later production can standardize EX2. The fixed-gear aircraft remains drag-heavy, so the gain does not change its tactical category.

### A6M1/A6M2

- Historical A6M2 baseline is EX0; existing Zero rebaseline already closes the Asai design path correctly.
- Worldline A0 uses **EX2/EX3 from design integration**, not a post-production fantasy retrofit.
- Full exhaust-only shadow **+6.4 to +10.1 km/h** is permitted when comparing to a true EX0 A6M2 anchor.
- A6M5 historical EX2 performance may not receive that full gain again.

### Ki-21-IIa / G3M2

- Ki-21-IIa: Ha-101 redesign is a natural EX2 integration gate; full shadow about **+6 to +9 km/h**.
- G3M2: historical EX0 collector architecture; new-build/major-overhaul adoption from 1939-40 is plausible; full shadow about **+4 to +6 km/h**.
- For long-range aircraft, part of the useful benefit may be retained as cruise-power/fuel/thermal margin rather than headline top speed.

## 3. 1940-42 standardization generation

By this period the design/test method has diffused to the Army/Navy and major makers. On a new high-speed air-cooled design, failure to evaluate thrust exhaust now needs an explicit reason.

| aircraft | historical early state | Asai worldline state | full EX0->EX2 shadow | note |
|---|---|---|---:|---|
| Ki-43-I | EX0 | EX2/EX3 at production | +5.8 to +9 | existing A0 speed band retained; surplus may be reinvested |
| Ki-44-I | EX0 | EX2/EX3 at production | ~+6.5 to +11 | existing ~596-600 A0 interpretation retained |
| Ki-45 Kai | EX0 early | EX2/EX3 with redesign | ~+6 to +10 | historical late batches prove thrust-exhaust suitability |
| Ki-46-II | EX0 historical II baseline | EX3 standard | +7.6 to +12.4 | historical later Ki-46 individual-exhaust gain is strong external calibration |
| Ki-48-I | EX0 probable | EX2 likely | +5.7 to +8.7 | exact historical manifold hardware remains OPEN |
| Ki-49-I/IIa | EX0 | EX2/EX3 at production | ~+5 to +8 | historical later individual ejectors support suitability |
| G4M1 early | EX0 | EX2/EX3 at production | +5.2 to +7.9 | historical 1943 individual-stack adoption is late catch-up, not Asai invention |
| J1N1 | EX0 historical early | EX2 then EX3 by production | ~+6 to +9 | by 1941 new nacelle design, omission is unlikely without a reason |

## 4. Low-speed / special-role and already-mature installations

### Ki-51

- EX0 historical baseline; EX2/EX3 is technically worthwhile, physical shadow **about +4.5 to +6.5 km/h**.
- A0 should normally reinvest some margin into protection, cooling, rough-field life and serviceability rather than cashing every km/h into maximum speed.

### E13A

- Early historical production is treated as EX0; later historical individual stacks demonstrate suitability.
- Worldline can move EX2/EX3 into early production.
- Physical full shadow **about +3.5 to +5.5 km/h**.

### F1M2

- EX0/concentrated exhaust class; EX2 technically possible, physical shadow **about +3.5 to +5.5 km/h**.
- Adoption priority is medium/low because float/airframe drag dominates; later new builds are better candidates than a fleet retrofit.

### H6K

- H6K4 EX0; physical shadow **about +3 to +4.5 km/h**.
- H6K5 engine-change gate can justify EX2, physical shadow **about +4 to +6 km/h**.
- Four engines do not make the percentage speed gain four times larger; the propulsive baseline scales too. Retrofit economics remain weak on older H6K4s.

### H8K

- Historical production installation is treated as **EX1/EX2**, not EX0.
- Therefore do **not** add a full +5 to +8 km/h collector-to-stack shadow to historical H8K performance.
- Asai residual EX2->EX3 speed credit: **about +1 to +3 km/h central**, with thermal balance, stack life, nacelle cooling and inter-engine repeatability as the larger practical benefit.

### D4Y / Ki-61

- DB601-derived Atsuta/Ha-40 installations already use effective separate exhaust stacks; historical performance anchors start near **EX2**.
- Full collector-to-stack credit is prohibited.
- Asai residual EX2->EX3 speed credit: **about +1 to +3 km/h central, +4 sensitivity**.
- Radiator duct pressure/heat recovery is a **separate card** and may be materially more important than the residual exhaust card.

## 5. 1942-44 historical catch-up boundary

From 1942-43 the historical Japanese industry itself becomes an EX2 user on many new high-speed aircraft. The Asai delta changes character from “technology exists years early” to “first prototype starts with a mature implementation, later modification cycles disappear, and EX3/QC residual remains.”

### P1Y1 Ginga

- Early prototype/concentrated installation to historical production individual stacks is treated as an EX0/1 -> EX2 catch-up.
- If comparing an early EX0-like installation, full physical shadow is **about +6 to +10 km/h**.
- Historical production performance already contains much of EX2; Asai residual from a production EX2 anchor is **about +2 to +4 km/h**, with Homare realization/reliability more important overall.

### B6N

- B6N1: concentrated/single-exit installation retains a full EX0/1->EX2 opportunity, **about +5 to +8 km/h** physical shadow.
- B6N2: historical multiple rearward stubs already explicitly recover some forward thrust; historical B6N2 performance is therefore EX2-containing.
- Asai production B6N1 can adopt EX2 early; B6N2 moves toward EX3. Residual from historical B6N2 anchor: **about +2 to +4 km/h**.

### B7A

- Historical exhaust state is **EX1.5/EX2 probable**, confidence B pending stronger hardware documentation.
- Do not add a full EX0->EX2 shadow to historical production speed.
- Asai residual: **about +2 to +4 km/h**, while Homare realization remains the larger worldline lever.

### J2M

- J2M1 may be treated as the earlier concentrated/less-developed installation.
- Historical J2M2/3 already uses individual thrust-augmentation exhaust and is an EX2 anchor.
- A hypothetical EX0->EX2 shadow is roughly **+7 to +11 km/h**, but this is **not** an allowed addition to historical J2M2/3 speed.
- Existing worldline J2M **600-605 km/h class** is retained; its delta is re-attributed to **EX2->EX3 (~+2 to +4), installation/cooling/vibration/QC**, not a second full exhaust card.

### N1K1-J / N1K2-J

- Historical N1K1-J enters service with individual stacks: EX2-class baseline.
- N1K1-J Asai residual: **about +2 to +4 km/h**.
- N1K2-J is a still more mature EX2 airframe; residual exhaust speed credit is **about +1 to +3 km/h**.
- Existing worldline N1K2-J **600-605 km/h** band is retained; the larger delta is primarily Homare output realization, cooling/fuel/ignition/quality and aircraft repeatability, not a full new exhaust conversion.

### Ki-84

- Earliest historical prototype used collector exhaust; later prototypes/production used individual stacks. This is a valuable within-lineage EX0->EX2 transition.
- Full early-prototype EX0->EX2 physical shadow: **about +7 to +12 km/h**.
- In the Asai worldline, Ki-84 should begin prototype installation with EX2/EX3 knowledge already available; there is little reason to repeat the historical collector first step.
- **Critical guard:** the 631 km/h-class historical production/handbook anchor already belongs to the individual-exhaust side. Do not add +7 to +12 to 631.
- Existing worldline Ki-84 **645-660 km/h** band is retained. Exhaust residual from a historical production anchor is only **about +2 to +4 km/h**; the main delta is Homare rated-output realization, fuel/ignition/cooling/bearing health, propeller matching and production repeatability.

### A6M5 / historical A7M Reppu (worldline A9M) / other mature late new designs

- A6M5 historical speed already includes EX2; full A6M2 collector-to-stack credit may not be repeated.
- Historical A7M Reppu (worldline A9M) and comparable late new high-speed air-cooled designs are presumed to evaluate individual thrust exhaust from the outset unless documentation says otherwise; worldline residual normally **about +1 to +3 km/h** plus thermal/life/QC benefits.

## 6. Historical diffusion model

Working canonical chronology:

- **1935-36:** Asai bench program; nozzle/back-pressure/direction/thermal-support test method develops.
- **1937-38:** Ki-27 / Ki-15 / A5M-class flight A/B tests. Effect is proven, but Asai’s insistence on integrated thermal/nozzle/cooling closure delays blanket standardization.
- **1938 late-1940:** selected late-production aircraft and new designs adopt EX2; military-use IP/test practice diffuses through service and manufacturers.
- **1940-42:** on a new high-speed air-cooled military aircraft, thrust exhaust becomes a normal design card; omission needs a role/cost/installation reason.
- **1942-43:** historical Japanese industry itself catches up to EX2 on multiple types. Asai advantage shifts toward first-prototype maturity and EX3.
- **1944+:** large collector-to-stack worldline delta largely disappears on new high-speed types; residual is small speed, thermal margin, life, QC and service-average performance.

## 7. Deployment/procurement guard

This file closes **technical availability and aircraft-design interpretation** only.

It does not automatically determine:

- how many Ki-27s in a named sentai have EX2 on a particular date;
- retrofit orders or depot throughput;
- combat sortie strength;
- procurement quantities;
- whether a low-priority legacy aircraft is actually modified.

Those are force-allocation/history gates. REPLAY3 has now paid this named-unit gate: **24th Sentai Ki-27 = EX2 x15 / EX0 x4** for the current Nomonhan pool. Other sentai/date mixes remain separate allocation gates.

## 8. Supersessions

1. **B5N2 `historical individual exhaust -> E1=0` is superseded.** Treat historical B5N2 as EX0 collector-ring for current calculations unless stronger primary hardware evidence overturns this file.
2. **Late-war full-card repetition is prohibited.** A6M5, J2M2/3, N1K1-J/N1K2-J, production Ki-84 and comparable EX2 historical anchors receive only residual EX2->EX3 exhaust credit.
3. Existing late-war worldline performance bands are not automatically reduced; where retained, their attribution shifts toward engine rated-output realization / cooling / fuel / ignition / QC, with exhaust only a residual component.
4. Liquid-cooled Ki-61/D4Y do not receive a new collector-to-stack card; Meredith/radiator recovery remains separate.
