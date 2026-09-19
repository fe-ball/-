# ASAI AVIATION DECISION-INTENT GUARD V1
Status date: 1939-09-01
Purpose: preserve why aircraft exist, what decision each one supports, and when production is rational.

## 1. Mandatory causal fields for every new aircraft/block

Before adding or advancing an aircraft, record all of:

1. **Problem owner** — Asai, Army, Navy, civil customer, or joint technical bureau.
2. **Problem to solve** — range, landing, reconnaissance, interception, material qualification, maintenance, etc.
3. **Why an aircraft is needed** — why bench/ground/donor-airframe testing is insufficient.
4. **New variables introduced** — propulsion, structure, mission equipment, controls.
5. **Attribution/backout path** — how failure can be assigned and how the program can fall back.
6. **Capability allocation** — what is bought with the performance dividend: speed, fuel, payload, protection, field length, life.
7. **Productization level** — research, military technical prototype, service-evaluation batch, limited series, mass series.
8. **Customer ecosystem** — fuel, spares, maintainers, fields/decks, manuals, mission equipment.
9. **Superseded alternative** — what is deliberately not being built.
10. **Next physical gate** — a test or measured event, not a historical calendar year.

If these are not present, do not create a new aircraft or production decision.

## 2. Historical-year prohibition

Historical dates are calibration/reference only.

Never delay or advance a worldline aircraft because:
- "jets historically appeared around 1940";
- "a 14-Shi requirement historically occurred in 1939";
- "turbofans historically came later";
- "a named historical aircraft entered service in year X".

Use instead:
- prior prototype first-flight date;
- accumulated flight hours;
- unresolved failure modes;
- engine/core qualification;
- factory/tooling state;
- military/customer requirement;
- support-system readiness.

## 3. Research frontier versus product shelf

Research may advance continuously E5→E6→E7.

A product may deliberately remain E5 if:
- its mission does not benefit from E6 enough;
- E5 has known life/maintenance;
- fuel/field/customer requirements favor simplicity;
- stable tooling/manuals are more valuable than peak performance.

A new research generation is **not** a reason to block a useful production block.

## 4. Performance-dividend rule

Never default a technical improvement to maximum speed.

Explicitly choose among:
- speed;
- climb;
- fuel/radius;
- payload;
- armor/protection;
- reliability/TBO;
- low-speed/field performance;
- production margin.

Record the choice.

## 5. Fuel→landing causal guard

If range is increased by added fuel, recalculate:
- takeoff weight;
- landing/rejected-mission weight;
- stall/approach speed;
- brake/gear/arresting energy;
- go-around margin;
- runway/deck requirement.

Do not award range without paying landing and structure consequences.

## 6. STOL lineage guard

The small TP/STOL family exists because:
- turbine fuel substitution is useful;
- practical customers need rough/short-field operation;
- heavier fuel/range configurations create landing-energy pressure;
- low-speed engineering needs a dedicated school.

Do not collapse:
- P1 practical sale aircraft;
- P2 purpose-designed STOL evolution;
- Material No.1 structural A/B aircraft;
into one object.

## 7. Aft-fan guard

The aft-fan is an early, intentional architecture:
single-spool gas generator + free LP turbine + aft fan.

It is chosen partly to reuse free-power-turbine knowledge and avoid making an early front-fan/multi-spool architecture the central path.

Therefore:
- aft-fan research begins in the mid-1930s, not after E6;
- E5 aft-fan flight is a 1937 event in current canon;
- 1938 is durability/mission/maintenance maturation;
- E6 aft-fan inherits the architecture rather than reinventing it.

Do not describe it as having "no added mechanism": the LP/fan spool is real.

## 8. Military-requirement stages

Distinguish:

- **R — company research**
- **M — military technical requirement/prototype**
- **S-eval — service/development evaluation batch**
- **S — service/adoption production requirement**

An aircraft can be military-requirement hardware without having a service designation or mass-production order.

Do not downgrade Stage M aircraft to "company research" merely because the final tactical role is open.

## 9. Production gate

Production does not wait for technology to stop evolving.

A block may be frozen when:
1. mission value exists now;
2. catastrophic failure modes are acceptably bounded;
3. configuration is stable enough for tooling/manuals;
4. customer ecosystem exists;
5. the block has a useful expected production/service life.

Use pilot/service-evaluation batches between prototype and mass series.

## 10. Material-lineage guard

New material is introduced by attributable steps:
coupon/joint
→ secondary parts
→ low-speed full-airframe A/B (Material No.1)
→ high-q aircraft (Material No.2)
→ only validated blocks migrate into products.

Do not award a complete composite airframe because a coupon or low-speed test succeeds.

## 11. Authority rule

When a later summary conflicts with this guard:
- preserve measured physical facts from the later gate if they are not causally dependent on the bad interpretation;
- supersede the interpretation/status wording;
- document the exact line being superseded;
- do not silently delete old files.

This guard is intended to keep future package compression from destroying decision intent.
