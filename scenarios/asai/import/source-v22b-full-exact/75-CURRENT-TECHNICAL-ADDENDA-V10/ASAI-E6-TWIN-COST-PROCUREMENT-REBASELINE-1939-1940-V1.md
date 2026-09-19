# ASAI WORLDLINE — E6 TWIN COST / PROCUREMENT REBASELINE V1
## Relative acquisition economics, E5 precedent, and 1940 service-production posture

**Status:** COST H→A REBASE CLOSED / EXACT CONTRACT QUOTES AND 1940 MONTHLY ACCEPTANCE REMAIN REPLAY-LOCAL  
**Clock effect:** NONE — the combat clock remains 1939-12-31 24:00.  
**Purpose:** Test whether the E6 Twin procurement posture left after E6REBASE1 is institutionally and economically consistent with the already-closed E5 operational fleet, current E6 performance, embedded Asai cost models, and the turbine-capacity schedule.

---

## 0. Central verdict

1. The E6REBASE1 `36–60 accepted / pilot-production` working band is **too conservative and is superseded**.
2. E6 Twin is not a new propulsion concept being offered to a service with no turbine experience. The services already operate a large E5 Twin fleet, predominantly JF, with established field maintenance, one-engine procedures, kerosene supply, radio/photo mission integration and mature external-fuel practice.
3. The embedded engine cost model makes an E6-JF engine pair roughly **+73%** more expensive than an E5-JF pair at family-scale production, but engines are not the whole aircraft. After common airframe and mission-equipment cost is restored, the useful planning premium for a mission-equipped E6-JF Twin is only about **+28–35%** over a comparable E5-JF Twin.
4. That premium buys a change from the E5 operational speed class into the current E6-JF **~0.74–0.80 Mm/h** design class, while retaining a practical JF mission radius and the already-paid E5 drop-tank/field-service doctrine.
5. The internal E5 procurement record shows that the services did not behave as timid evaluators once the aircraft proved useful: after the first ten E5 Twin airframes, a 36-airframe firm order, a 24-airframe option, then a 72-airframe second tranche followed; by 1939-05-10 cumulative E5 production reached 98 and April alone produced 16.
6. Therefore the rational 1939-12-31 procurement posture is **service production with concurrent operational proving**, not “evaluate a handful and decide in 1941.”

---

## 1. Cost-source semantics

The package contains two useful cost-model anchors:

- `01-BASE-V6/01-BASE-V5/01-BASE-V4/90-SOURCE-QUARANTINE/2026-08-29-FULL-V3/ASAI-GT-FRONT-SCALE-RATING-PRODUCTS-V14-COST.xlsx`
- `01-BASE-V6/30-ASAI-CURRENT-AUDITS/ASAI-EPOXY-FRP-CAPABILITY-LEDGER-V2-COST.xlsx`

They are used here for **relative design costing**, not as a claim that a dated Army/Navy contract has already been signed at those exact yen values. No newer current file supplies a conflicting E5/E6 engine-price table.

All yen below are nominal contemporary-yen planning values. `k¥` means thousand yen.

---

## 2. Engine acquisition delta

The embedded GT cost workbook gives the following production-price centers:

| engine product | low-rate current band | single-type mass | family-scale mass |
|---|---:|---:|---:|
| E5-J | 34–46 k¥ | 28 k¥ | 23 k¥ |
| E5 aft-fan / JF analogue | 47–62 k¥ | 40 k¥ | 33 k¥ |
| E6-M J | 65–86 k¥ | 56 k¥ | 45 k¥ |
| E6-M aft-fan / JF | 80–105 k¥ | 70 k¥ | 57 k¥ |

Twin-engine pair comparison:

| block | single-type-mass pair | family-scale pair | delta vs E5 |
|---|---:|---:|---:|
| E5 J | 56 k¥ | 46 k¥ | — |
| E6 J | 112 k¥ | 90 k¥ | +100% / +96% |
| E5 JF | 80 k¥ | 66 k¥ | — |
| E6 JF | 140 k¥ | 114 k¥ | **+75% / +73%** |

The engine-price increase is real. It is also the wrong number to use as the aircraft-price increase.

---

## 3. Whole-aircraft cost bridge

The embedded composite/airframe cost workbook provides a useful twin-engine aircraft analogue:

- 25-aircraft small series: conventional-riveted equivalent about **170 k¥**, with an engine allocation about **72 k¥**;
- 100-aircraft mass series: conventional-riveted equivalent about **158 k¥**, with an engine allocation about **60 k¥**.

Both imply a reusable conventional twin non-engine anchor around **98 k¥**. This is a costing bridge, not an exact E5 invoice.

For E6, add a local **8–15 k¥** working allowance for the higher-q inlet/nacelle detail, stronger brakes/tyres/local structure, acceptance instrumentation and high-speed production/QC burden. Common mission equipment is carried as **20–40 k¥** because radio/photo/armament fit varies by role and is substantially common between the comparison aircraft. E6MISSION1 subsequently closes the common two-seat mission architecture, ~0.40 t internal bay and high-speed-release family; this cost band remains adequate and is not multiplied into a separate new-aircraft penalty.

### Family-scale mission-equipped planning model

| item | E5 Twin JF | E6 Twin JF |
|---|---:|---:|
| engine pair | 66 k¥ | 114 k¥ |
| common twin airframe/non-engine anchor | 98 | 98 |
| E6-specific high-q/acceptance allowance | — | 8–15 |
| common mission equipment working allowance | 20–40 | 20–40 |
| **total planning band** | **184–204 k¥** | **240–267 k¥** |

Central comparison with a 30 k¥ mission kit and 12 k¥ E6 local allowance:

- E5 Twin JF: **~194 k¥**;
- E6 Twin JF: **~254 k¥**;
- absolute premium: **~60 k¥/aircraft**;
- whole-aircraft premium: **~31%**.

Across the reasonable mission-kit sensitivity, the whole-aircraft premium is approximately **+28–35%**.

This is the correct order-of-magnitude decision variable. A service is not choosing between a 100% more expensive E6 aircraft and an E5; it is choosing whether roughly thirty percent more acquisition cost is worth the operational step.

---

## 4. Fuel-money and operating-cost interpretation

The embedded GT cost model uses joint aviation GT distillate around **¥0.095/L** and kerosene density around **0.8 kg/L**.

At the E6REBASE1 JF center:

- 0.90 t internal fuel ≈ 1,125 L ≈ **¥107** of fuel;
- D320F usable external fuel 490–505 kg ≈ 613–631 L ≈ **¥58–60**;
- internal + full D320F fuel value ≈ **¥165–167**.

Thus direct fuel purchase price is negligible beside a ~250 k¥ aircraft acquisition price. Fuel still matters operationally because of transport, storage, sortie-generation and theater tonnage; it does **not** justify a tiny E6 procurement block on purchase-price grounds.

Exact E6 maintenance yen/hour is not closed here. The correct qualitative accounting is nevertheless bounded:

- E5-JF has already paid the organizational cost of an aft-fan/free-spool/governor backend, field kerosene, turbine-shop practice and one-engine twin procedures;
- E6 adds tighter axial-compressor/hot-section/balancing and high-speed airframe QC requirements;
- the 835°C JF point is explicitly the long-life production center, so the aircraft must not be assigned a fictitious “experimental jet = disposable engine” penalty.

Until an overhaul-cost ledger is closed, use **acquisition + spare-engine burden** as the conservative cost discriminator and keep maintenance cost OPEN rather than inventing a historical early-jet penalty.

---

## 5. What the extra money buys

Current E6REBASE1 aircraft calculation, measured-flight numbers still local:

- JF normal loaded mass center: **4.40 t**;
- JF long-life thrust center: **984 kgf/engine @835°C**;
- clean maximum-speed center: **~744 km/h sea level; ~793 km/h around 6–8.5 km**;
- 6 km climb: **~4.9 min**;
- internal-fuel routine radius: **~400–480 km**;
- D320F practical long-cover/recon radius: **~650–800 km**;
- one-engine return remains operationally useful.

The E5 fleet already supplies the doctrine, trained maintainers, kerosene chain, mission kit and drop-tank handling. E6 therefore buys primarily a **large performance and survivability step**, not a brand-new operating ecosystem.

At a central ~60 k¥ acquisition premium, 144 E6 Twin aircraft cost about **¥8.64m more** than buying 144 comparable E5 Twin JF aircraft under the same planning model. Total E6 acquisition at the central ~254 k¥ figure is about **¥36.6m** for 144 aircraft.

The premium is large enough to matter to procurement, but far too small to explain a six-aircraft or forty-eight-aircraft caution regime once the service configuration flies successfully.

---

## 6. Industrial capacity test

Current GT capacity anchors:

- T-1 sustainable: **600–750 cores/year**;
- T-2 after qualification/maturity: **+450–650/year**, maturity 1939Q4–1940H1;
- T-3 after qualification/maturity: **+800–1,200/year**, maturity 1940H2;
- T-AUX remains the specific JF fan/free-turbine/governor/package bottleneck rather than raw factory floor area.

A 1940 E6 Twin acceptance band of **120–156 aircraft** requires:

- installed engines: **240–312**;
- with a 20–25% acceptance/operational spare allowance: roughly **288–390 flight-grade engine packages**.

Even before T-3 reaches mature output, this is a plausible minority share of the expanding T-0/T-1/T-2 core envelope. It is not free: flight-A yield, T-AUX, instruments, mission equipment, brakes/tyres and partner-airframe learning can still throttle the line. But the old 36–60-aircraft ceiling is not imposed by core arithmetic.

Airframe precedent is also important: E5 output reached **16 completed aircraft in April 1939**. A 120–156 E6 acceptance year asks for roughly a 10–13/month annual average, with a slower Q1 and a 12–16/month H2 run rate. That is a transition/ramp problem, not a fantasy mass-production assumption.

---

## 7. Procurement behavior rebaseline

The E5 order history is the strongest internal behavioral evidence:

- first 10 E5 Twin completed by 1938-06-30;
- **36-airframe firm order** on 1938-06-30;
- **24-airframe option exercised** 1938-10-31;
- **72-airframe second production tranche firm** on 1938-12-15;
- total military follow-on commitment at 1938 year-end: **140 airframes** plus two development prototypes;
- cumulative completed: 76 by 1939-03-31, **98 by 1939-05-10**;
- a further **36-aircraft JF operational block** was ordered 1939-06-02.

That institution has already demonstrated the behavior relevant to E6: once usefulness is demonstrated, it buys production capacity ahead of perfect long-term knowledge.

E6 has **less basic operational uncertainty than E5 had when those orders were placed**. The fundamental turbine-twin, JF backend, field servicing, fuel, drop-tank and mission-system questions are inherited.

Therefore the 1939-12-31 planning posture is revised to:

### Procurement commitment posture
- immediate service-production target: **144 common E6 Twin airframes firm-order class**;
- attached follow-on option: **72 airframes**;
- exact signing date/allocation between services remains a 1940 replay event unless an upstream dated order is later found;
- the option is a rate/defect/allocation hedge, not a “do we believe in E6 at all?” hedge.

### 1940 accepted-aircraft planning band
- **120–156 accepted E6 Twin**, center **~144**;
- JF: **~85–90%**;
- pure-J: **~10–15%** specialized high-speed/high-altitude/local-interception block;
- E6 Single remains outside the **Twin** production count. E6SINGLE1 later closes a separate pure-J serial-production plan; do not use this Twin cost file to keep the Single research-only.

### Rational ramp
- Q1 cumulative: **~18–24**;
- Q2 cumulative: **~48–66**;
- Q3 cumulative: **~84–114**;
- Q4 cumulative: **~120–156**.

The first 12–24 aircraft still perform service proving. The semantic correction is that they are **lead aircraft from an already-committed service-production series**, not a tiny evaluation batch whose success is required before the military dares to place a real order.

---

## 8. Operational-release guard

Aggressive procurement does not mean magical combat deployment.

Keep the following separate:

1. **order/commitment** — can occur while service trials continue;
2. **factory acceptance** — aircraft and engines pass production acceptance;
3. **unit conversion/training** — crews and maintainers qualify;
4. **combat allocation** — a theater receives the aircraft;
5. **mission release** — armament/external-fuel/high-altitude configurations are individually cleared.

Therefore no mass E6 combat wing is retroactively placed in China on 1940-01-01. But once Q1/Q2 conversion and local allocation gates pass, a normal operational unit—and later more than one—may appear without waiting for a fictional 1941 first-adoption decision.

The 1941 decision becomes: **how much more E6, what J/JF mix, which theaters, and when to transition toward the next E-generation**, not “whether to begin limited E6 production.”

---

## 9. Supersession

This file supersedes the following E6REBASE1 planning values wherever they conflict:

- `36–60 accepted in 1940, center ~48`;
- `JF 75–85%`;
- `pilot-production` as the main procurement characterization;
- `1941 scale/role decision` if interpreted as the first real adoption decision.

It does **not** supersede the E6REBASE1 aircraft performance, weight, wing-area sensitivity, D320F construction, range or E-generation semantic closure.

**E6 TWIN COST / PROCUREMENT REBASE CLOSED — V1**
