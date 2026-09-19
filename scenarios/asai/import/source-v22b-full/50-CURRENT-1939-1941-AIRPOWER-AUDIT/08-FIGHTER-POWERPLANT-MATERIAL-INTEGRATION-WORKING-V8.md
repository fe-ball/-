# FIGHTER POWERPLANT / MATERIAL INTEGRATION — WORKING V8

> Working synthesis. Local engine/aircraft canons override this file when more specific.

## Purpose

Connect engine, propeller, exhaust, cooling, materials and aircraft requirements without applying independent maximum bonuses.

## Fighter integration chain

For each fighter:

1. select actual engine/model/date and availability grade;
2. close propeller diameter/blade count/governor/reduction/vibration;
3. close cowling/cooling/oil/exhaust installation;
4. close aircraft mass/CG/structure;
5. calculate speed/climb/range/turn/stall;
6. decide how technical margin is reinvested in the adopted configuration.

## Common failure of naive rebaseline

Do not do:

`historical fighter + better engine hp + exhaust speed + propeller speed + material weight saving + computation speed bonus`

as independent additions.

A stronger engine may require:

- larger propeller;
- stronger gear/wing/engine mount;
- more cooling;
- more fuel;
- heavier armament;
- larger tail;
- increased drag.

Material saving may be reinvested rather than appear as lower loaded weight.

## 1939–41 fighter families

### A6M

Design already benefits from:

- strong Sakae/Z-900 class integration;
- 3-blade constant-speed propeller from first flight;
- thrust exhaust from design origin;
- better calculation/test/QC.

Do not later add those again.

### Ki-43

Initial clock remains near history. Redesign loop can converge more efficiently. Production configuration should evaluate thrust exhaust and improved propeller/engine integration from the start.

### Ki-44

High wing loading/high power makes propeller, cooling and landing/handling more important. Thrust exhaust is standard design card by production.

### Ki-61

Liquid-cooled installation begins near EX2 exhaust; radiator/duct recovery is the larger remaining opportunity. Do not treat it as if it had a radial collector-ring deficit.

### J2M

Formal requirement remains Sep 1939; deeper pre-design is possible. High-power radial integration must still pay cooling/propeller/landing-speed gates.

## Materials

Use certified material/process only. Do not replace all aluminum structure with CFRP merely because coupons exist. CFRP in 1939 is application-limited and expensive.

## Adoption

The adopted fighter may spend gains on:

- speed/climb;
- range;
- protection;
- armament;
- structural/landing margins;
- radio/oxygen;
- serviceability.

Therefore technical shadow performance is not automatically the service airplane.
