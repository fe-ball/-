# GT ADVANCED-BRANCH 1939 STATE CANON — V8 GTCORE1

> **AIRPOWER5 / GTCORE1 current authority for 1939-04-20 advanced GT subtechnology state.** This file answers a narrow but important question: which technologies later associated with E7/E8/E9 already exist as knowledge, rig work, or inherited hardware by the current checkpoint, and which coupling/qualification gates are still unpaid?
>
> Mandatory parents: `00A-MANDATORY-CHEAT-CAPABILITY-PREFLIGHT-CANON-V8.md`, `20-GT-E6S-JF-E7-E9-REBASE-CANON-V8.md`, `21-GT-LIFE-RATING-SEMANTICS-CANON-V8.md`.

## 0. Central verdict

Do **not** read E7/E8/E9 as invention dates. By 1939-04-20 Asai already knows and has paid meaningful hardware/test clocks for VSV/bleed, multiple-spool mechanics, turbine cooling, free-power turbines/fan backends, and reheat/variable-nozzle concepts. The remaining gates are subsystem-specific coupling, endurance, transient control and production yield.

The current 1939 state is therefore neither:

- `all advanced features are future ideas`; nor
- `an E9 flight engine already exists`.

It is a layered state: some later-generation ingredients are already productized, some are active component/subsystem rigs, and some are architecture-known but not yet integrated fired cores.

## 1. Readiness vocabulary used here

- **K** — answer/architecture known; no claim of hardware maturity.
- **R1** — component/cascade/spin/coupon hardware and measurement active.
- **R2** — subsystem/partial-stack/drive or thermal rig; repeated mapped testing possible.
- **R3** — integrated gas-generator/backend ground hardware.
- **R4** — flight-development release possible.
- **R5** — qualified product coordinate.
- **R6** — serial-reproducible/service-mature.

These labels describe the **specific subtechnology**, not the whole E-generation.

## 2. VIGV / bleed / multi-row VSV

### 2.1 Already productized before the advanced branch

- E5-S standard uses fixed IGV + one interstage bleed; high-flow trim may use variable inlet swirl.
- E6-S standard uses mechanically scheduled **VIGV + stage-4 bleed**.
- E6-M standard uses **VIGV + two staged bleed bands**.
- Hydro-mechanical scheduling is sufficient; computation is used to design the cam/orifice schedule and release map, not to place an electronic controller on the engine.

Therefore `variable geometry / bleed is a later E8 invention` is **false**.

### 2.2 1939 advanced state

The reincarnator architecture gate for multi-row VSV was open much earlier, and the 1935-37 U4/R2 design culture already treats VSV/bleed schedule and surge margin as design variables. By 1939:

- multi-row VSV cascade/mechanism and partial-compressor work = **R2**;
- PR8/E7-directed scheduling work = **R1-R2 active**;
- multi-row VSV is **not required on standard E6-M**, because VIGV + two bleeds already satisfies the PR7 product requirement with lower production/control tax.

This is a deliberate product simplification, not lack of capability.

## 3. True two-spool gas generator

### 3.1 What is inherited

Asai has years of independent-spool experience from free-power turbines, high-speed bearings, balancing, gears, lubrication, critical-speed/Campbell work and later the free-LP-turbine/aft-fan path. The architecture and the reason to use separate compressor spools are known well before E8.

### 3.2 1939 state

True two-spool **compressor gas-generator** work is kept distinct from a free power turbine or free-LP fan spool.

At 1939-04-20:

- architecture / split-PR studies = **K, mature**;
- concentric-shaft, bearing/seal, torsional/critical-speed and independently driven split-compressor rigs = **R1-R2**;
- full transient matching models are entering the stronger 1938-42 computation era but are not yet a fully paid product capability;
- an integrated fired true-two-spool flight gas generator = **NOT current / OPEN**.

Earliest integrated-core work may proceed on its own 1940-41 clock if a PR/operability requirement justifies it. It does **not** wait for an E8 calendar label, but it must pay the genuinely new coupling tax: concentric shaft/bearing/seal, inter-spool matching, start/acceleration, control and endurance.

## 4. Reheat / augmentation and variable-area nozzle

The idea gate is not a 1940s invention in this worldline. Once E4/E5 pure-jet flight exists, exhaust reheat is an obvious dedicated backend branch to a reincarnator who already knows the final architecture.

By 1939-04-20 the current engineering state is:

- tailpipe burner / flameholding / fuel-distribution component work = **R1-R2**;
- short-duration static reheat rear-end rig = **R2 active**;
- fixed enlarged and mechanically **two-position / variable-area nozzle** rig work = **R1-R2**;
- flight-qualified reheat package = **NOT YET R4**;
- exact augmentation percentage, pressure loss, nozzle schedule, hot-duct endurance and restart/stability envelope = **OPEN local audit**.

This closes the chronology needed by the high-speed research line: an E6-M reheat backend can plausibly be a 1940-41 flight-development item without inventing the concept then. It still requires flight qualification and does not create an operational aircraft automatically.

## 5. Free-power turbine, aft fan and front fan

### 5.1 Free-power turbine

Independent free-power turbine mechanics are **already a mature inherited branch** from stationary, pump, marine and turboprop work. They are not an E7 invention.

### 5.2 Aft fan

Aft fan is the lower-coupling-tax aviation fan architecture because it can retain the single-spool gas generator and add a separate free-LP turbine/fan spool.

- architecture / drive principle = inherited and mature;
- E5 aft-fan hardware/flight possibility remains a **local installed-product audit**, not a forbidden future branch;
- E6-M-JF installed engine-side authority remains **950-1,000 kgf at the accepted 835 C long-life center**, with higher-TIT capability shadows handled by files 20-21;
- actual aircraft adoption/flight chronology is separate from engine capability.

### 5.3 Front fan / true low-BPR

By 1939:

- fan aerodynamics and component rigs = **R1-R2**;
- drive alternatives (second spool vs geared drive) are known;
- integrated front-fan flight engine = **OPEN**, because drive architecture, concentric shaft/gear, inlet/duct, control and transient matching must be paid together.

Thus E7 can expand front-fan work without “inventing turbofan” in 1942. The 1939 difference between aft and front fan is **integration tax**, not knowledge.

## 6. Turbine cooling / hot-section progression

### 6.1 Already paid/productized

By E4/E5 the worldline already has:

- fabricated hollow cooled rotor blades;
- deliberate vane/rotor/root/seal cooling budgets;
- flow-proof inspection of cooling circuits;
- diffusion/aluminizing-type protection where useful;
- creep/oxidation/thermal-cycle test infrastructure;
- NDT, lot traceability and hot-section teardown feedback.

Therefore `air-cooled turbine blade = later E7/E8 technology` is **false**.

### 6.2 1939 advanced state

What advances toward E7-E9 is degree and integration:

- more staged vane/rotor/root/disk cooling = **R1-R2 active**;
- cooling-passage geometry x flow x metal-temperature x life parameter work = **R1-R2**, strongly amplified by 1938-40 computation;
- E7 ~900 C component/hot-section rigs = active per current E7 schedule;
- E8 ~940 C and E9 ~1000 C are **not** granted as 1939 product TITs; their remaining gates are passage/yield, metal-temperature map, thermal fatigue, disk/root duty, endurance and manufacturing scatter.

The cheat changes start order and search efficiency; it does not erase the local material/process clock of a genuinely new passage/alloy/joining route.

## 7. Higher-PR compressor front

At 1939-04-20:

- PR7 E6-S/M = product/qualification front;
- PR8 E7 = component/partial-stack/rig work in the current schedule;
- PR9-10 E8-directed stage-loading/matching/VSV design work may already exist as **K/R1**, because the required average stage ratio is not radically above E6; full compressor qualification is not yet claimed;
- PR11-12 E9 = benchmark/architecture direction, not a 1939 integrated compressor claim.

Again: the generation label is a coordinate read from the moving front, not a permission date to begin work.

## 8. 1939-04-20 compact state table

| branch | 1939 state | current reading |
|---|---|---|
| E6-S VIGV + bleed | **R5/R6 product-side** | standard architecture |
| E6-M VIGV + 2 bleeds | **R4/R5** | current all-axial PR7 operability solution |
| multi-row VSV | **R2** | active advanced compressor subsystem; not needed on standard E6 |
| true two-spool gas generator | **R1-R2** | shaft/bearing/split-compressor work; integrated fired flight core open |
| free-power turbine | **R5/R6 inherited** | stationary/marine/TP basis |
| aft-fan backend | **R3-R5 family-dependent** | E6-M-JF installed authority accepted; E5-J/JF local installed product CLOSED in file 23 |
| front-fan / true low-BPR | **R1-R2** | component/drive branch; integrated flight product open |
| reheat / variable nozzle | **R2** | static short-duration rear-end development; flight qualification open |
| hollow/cooled turbine blade | **R5/R6 inherited** | not a future invention |
| advanced staged cooling | **R1-R2** | E7+ component rigs / process-yield work |
| PR8 compressor | **R1-R2** | E7 component/rig front |
| PR9-10 directed work | **K/R1** | E8-directed stage/matching studies; no full qualified compressor claim |

## 9. What this changes in the current audit

1. File 02's `1939 E7 component/rig` schedule remains valid **for integrated E7 core maturity**.
2. It must not be read as saying VSV, two-spool, cooling, fan or reheat ideas begin in 1939-42.
3. HS-3 / transonic research may use an E6-M reheat flight package once the **backend flight gate** closes; it need not wait for E7.
4. E8/E9 R&D clocks are distributed across their subtechnologies and begin before the mature E8/E9 coordinate years.
5. No procurement, aircraft adoption or post-1943 production result is created by this subsystem capability ledger.

## 10. Remaining engine-side hard opens after GTCORE1

The broad E-family capability semantics are now substantially closed. Remaining local engine audits are:

- E5 pure-J / aft-fan installed product audit is **CLOSED in file 23**; next work is aircraft-local altitude/mission integration and E6-S/reheat local product closure;
- E6-S-J local installed package is **CLOSED in file 25/25A**; remaining E6-S-J work is measured flight map, R5 service qualification/TBO and any later derivative;
- E6-M-JF higher-rating engineering ladder/free-LP thermal duty is **CLOSED in file 26/26A**; product endurance/TBO and aircraft flight release remain open;
- E6-M reheat/variable-nozzle installed engineering map is **CLOSED in file 27/27A**; wet endurance/relight/flight release remain open;
- any chosen true-two-spool or front-fan integrated engine;
- E7-E9 product-specific installed maps when a real product/requirement is selected.

These are **local product audits**, not reasons to reopen the v38-v46 capability basis.
