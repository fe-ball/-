# NAVAL COMPUTATION / FIRE-CONTROL INTEGRATION CLOSURE — V9 TECHCLOSE1

## Status

**NAVAL DESIGN-COMPUTATION METHOD: CLOSED.**  
**SHIP FIRE-CONTROL MATURITY AXIS: CLOSED (FCS0-FCS4 from V8 51/51A).**  
**SHIP INTEGRATION-DEPTH AXIS: CLOSED AS R0-R3 TAXONOMY.**  
**1939 CLASS-LEVEL R-BASELINES: CLOSED by TECHCLOSE2. INDIVIDUAL EXCEPTIONS, later refits, radar/director adoption and wartime equipment changes remain event/type gated.**

This file restores a distinction that was present in earlier naval work but not represented in the current V9 routing. TECHCLOSE2 also applies `05-CHEAT-DISTANCE-AND-TRANSFER-GUARD-V9.md` and the class ledger `07A-NAVAL-FCS-CLASS-LEDGER-V9.tsv`.

## 1. Two independent axes

`FCS0-FCS4` describes the maturity of the fire-control chain itself. It answers: how sophisticated is the sight/calculator/director/gyro/electrical/analog assistance?

`R0-R3` describes how deeply that change is integrated into a ship. It answers: how much of the ship installation was actually changed?

V9 adopts the following integration-depth taxonomy:

- **R0 — calibration/function package:** calibration, boresight/function tables, acceptance/QC, procedural package; little structural/electrical alteration.
- **R1 — transmitters/wiring/synchronization:** electrical angle/data transmission, wiring, repeaters/synchro coordination and related power/interface work.
- **R2 — directors / AA FCS / switchboard:** director and fire-control equipment changes plus target-allocation/switchboard and associated integration.
- **R3 — complete architecture + structural foundations:** new-build or major-refit integration in which foundations, routing, power, spaces and system architecture are designed around the equipment.

R-level is not a quality score and is not interchangeable with FCS level. A technically mature FCS3 subsystem can be absent from a ship, or only partly integrated. A ship may have deep R3 infrastructure around a historically modest subsystem.

## 2. 1938-40 dedicated computation

The older computation work is retained only for the following current technical ruling: fixed-function mechanical/electromechanical/electrical continuous-analog modules for large-ship or AA test use are technically plausible in the 1938-40 band. This does not mean a modern general-purpose computer is installed aboard ship, and it does not assign the equipment to any class.

V8 51/51A remains the current authority on fire-control interpretation. Capital-ship main battery has a smaller relative gain because historical mechanical fire control is already strong. Medium-caliber AA has larger potential benefit from continuous tracking, angle transmission, follow-up, fuze setting and reset-delay reduction. 25mm-class weapons retain mount/feed/traverse limits. Torpedo fire-control may gain from target-motion, gyro-angle and transmission/QC.

## 3. Design computation and refit

Computation can accelerate weight/trim/stability cases, shafting and vibration work, machinery/propeller matching, structural comparisons and post-test redesign. It does not create free shaft horsepower, knots, range, deck capacity, weapon rate of fire, radar fit or hull count.

For propulsion, `42-MARINE-GT-1939-04-20-STATE-CANON-V8.md` controls physical Apr20 execution. The promoted large-surface-ship and small-craft parents supply detailed design baselines but remain subordinate to later local V8/V9 state rulings.

## 4. Ship/class closure rule

TECHCLOSE2 closes class-level 1939 integration baselines from already-paid modernization/new-build windows and prior naval decisions. Use `07-NAVAL-FCS-CLASS-CLOSEOUT-V9.md` / `07A...tsv`. These class baselines do not assign future hardware: function-specific FCS maturity remains controlled by 51/51A.

A later individual-ship refit/damage/event can override the class baseline. Do not infer shipboard radar/director fit from aircraft electronics or computation progress. Antenna, power, spaces, director interface, production quantity, training and doctrine remain type/date adoption gates.

The Navy's routine design/gunnery work is CD3 autonomous by 1936-39; Asai is a CD2 machine/method/support supplier. This permits the Navy to retain and improve the tools without treating each ship as a CD0 reincarnator project.
