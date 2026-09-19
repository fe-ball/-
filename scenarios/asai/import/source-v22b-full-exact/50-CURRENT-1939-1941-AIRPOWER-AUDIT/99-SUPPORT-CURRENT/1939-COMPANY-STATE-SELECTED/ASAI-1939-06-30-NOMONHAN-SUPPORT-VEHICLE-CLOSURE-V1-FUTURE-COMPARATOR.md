# ASAI 1939-06-30 NOMONHAN SUPPORT / VEHICLE CLOSURE V1

Status: CURRENT-BRANCH PATCH / 1939-06-30 24:00
Scope: Nomonhan support mechanics before the July 1939 major ground offensive.
Rule: Do not convert Asai vehicle quality into a blanket increase in Japanese motorization. Count, quality, route capacity, ammunition, water, command and doctrine remain separate.

## 1. Historical bottleneck hierarchy retained

Nomonhan is a motor/logistics battle as much as a tank battle. The Japanese side faces:
- long road movement from the Hailar-side support area;
- sections of unimproved road that turn to bog under rain;
- acute potable-water shortage;
- scarce artillery ammunition relative to Soviet expenditure;
- Soviet numerical superiority in motor transport, armor and artillery;
- exposed, treeless terrain that makes guns, trucks and workshops vulnerable once located.

Asai does not erase any of these constraints.

## 2. Ground vehicle family — CLOSED

### 2.1 Heavy 6x4 cargo / ammunition / fuel / water trucks
Current parent: `asai-works-military-diesel-vehicles.md`.

- 1934-class 6x4 diesel baseline around 70 hp; Asai-influenced turbo variants are in the 80–90 hp class.
- Benefit is not higher road top speed. Primary benefit: loaded pull, reduced stalling, high-temperature / altitude compensation, lower mechanical dropout and better towing margin.
- Nomonhan-specific limitation: once a flooded track becomes a deep quagmire and the chassis sinks to the undercarriage, extra engine power does not solve the route problem.
- Dust filtration, cooling, bearings, oil handling and parts interchange are treated as part of the Asai vehicle-Q package.

CLOSED: the 1st Motor Transport Regiment / other heavy transport assets may contain a priority subset of Asai-influenced heavy trucks, but total truck count is not multiplied by turbo adoption.

### 2.2 Artillery tractors
This is the strongest vehicle application at Nomonhan.

- 5t / 6t / 8t / 13t diesel tractor families already exist historically.
- Asai low-pressure turbo / flat-rated and second-generation strengthened-transmission variants have been in military rollout since 1934–37.
- Priority recipients: motorized field artillery and heavy-artillery tractor elements.
- Benefits: sustained low-speed pull, hot-weather load margin, fewer tractor dropouts, faster recovery of guns from bad ground, more reliable displacement after firing.

CLOSED: do not increase gun range or shell stock. Improve the probability that a gun which exists can be moved, supplied and repositioned.

### 2.3 Recovery / workshop vehicles
Do not invent a new armored recovery fleet in 1939.

Use historical truck / tractor support assets with:
- turbo heavy truck or tracked tractor;
- winch / towing kit;
- shallow spare-part standardization;
- small mobile power;
- machine tools / drills / grinders / battery charging / lighting.

CLOSED: field repair and non-fire-zone recovery are materially better. Recovery under direct Soviet fire remains dangerous and often impossible.

## 3. Mobile GT utility sets — CLOSED

Current parents: `08-MILITARY-DELIVERY-LEDGER-1937-SUMMER.md`, Gate 75, `asai-works-gt-apu.md`.

Existing current anchors:
- by 1938 H1: cumulative small mobile-GT operational/evaluation population about 15–25 sets;
- small mobile units are tens to low-hundreds kWe class, not the 500 kW E4 fixed plant;
- large E4-class mobile/tractor sets remain exceptional.

### 3.1 1939 H1 national population — WORKING-CLOSED
Given 1938 H2 and 1939 H1 industrial ramp, set operational/evaluation population at **32–45 small mobile-GT sets** by 1939-06-30.
This is not a universal Army issue item.

### 3.2 Nomonhan allocation by 1939-06-30 — CLOSED
Allocate **5–7 small mobile-GT utility sets** to the Nomonhan / Hailar support chain by the end of June, because Manchurian field use is a high-value match for the product.

Central role split:
- 2: field workshop / recovery / maintenance;
- 1: artillery / signal headquarters power and battery charging;
- 1: water-pumping / purification support;
- 1: forward aviation ground support / lighting / charging / workshop;
- 0–2: reserve / medical / engineer rotation.

Large E4 400–500 kWe mobile plant:
- forward combat area: **0**;
- Hailar / major rear workshop: **0–1 possible**, not required for combat calculations.

## 4. Power + heat use — CLOSED AS DERIVATIVE, NOT A NEW VEHICLE TYPE

There is no need to create a separate fictional `heat-source truck`.

A small GT utility set already produces:
- electric power;
- compressed-air potential;
- a large high-temperature exhaust stream.

Current technical parent also accepts simple exhaust-heat cogeneration for warming.
Therefore fit **2–3 Nomonhan utility sets** with simple exhaust-to-air / exhaust-to-water heat-recovery attachments.

Use in July–August:
- hot water and sanitation;
- warming lubricating oil / difficult engines at cold dawn;
- parts washing / drying;
- workshop heat for repair processes;
- medical / engineer utility heat.

Do **not** treat this as a major troop-heating advantage during the main July summer offensive.
Its cold-start value rises toward September and is much larger in a true Manchurian winter.

## 5. Water support — CLOSED

Nomonhan water scarcity is source + purification + transport constrained.

Mobile power can:
- keep pumps and purification gear operating;
- support lighting / repair of the water unit;
- charge pumps / communications / ancillary equipment.

It cannot:
- make saline sources potable without adequate purification capacity;
- create water where no suitable source exists;
- increase tanker/container count automatically;
- keep a road open when mud closes it.

Therefore water-delivery reliability improves locally, but `water shortage solved` is prohibited.

## 6. Artillery mechanics and computation — CLOSED

Current parent: `asai-works-survey-artillery-meteorology-rebaseline-1935-45.md`.

By 1939 the Asai effect includes:
- calibration records;
- survey / coordinates;
- met-message reduction and time tagging;
- firing-table integration;
- transcription / version checks;
- observation-correction workflow.

Nomonhan application:
- Type 90 / other motorized batteries benefit most from tractor + calculation integration;
- prepared and observed fire reaches useful correction faster;
- scarce ammunition is wasted somewhat less in ranging / transcription errors;
- motorized batteries can displace somewhat more reliably after firing, reducing exposure to counterbattery fire.

Hard limits retained:
- no blanket hit-rate multiplier;
- obsolete / short-range guns remain short-ranged;
- Soviet artillery mass and shell volume remain superior;
- infantry-artillery liaison and command doctrine do not become Soviet-style combined-arms doctrine.

## 7. Nomonhan local mechanical delta at 1939-06-30 — WORKING-CLOSED BANDS

These are local support bands, not theater-wide universal bonuses.

- eligible heavy truck / tractor mechanical ready fraction: **+5 to +8 percentage points** in Asai-exposed elements;
- routine field-workshop repair turnaround: **15–25% shorter** for repairable mechanical/electrical faults that reach a workshop;
- motorized battery displacement time on passable track: **about 10–15% shorter / more reliable**;
- prepared-fire correction cycle: modest improvement; in favorable observed missions, one correction/ranging step may be avoided, but no universal percentage is assigned;
- water/pump/purification uptime: improved locally, with route and tanker capacity still dominant.

Do not sum these percentages into a casualty multiplier.

## 8. July 1939 consequence gate

The July offensive must include, separately:
1. tank quality / Chi-Ha share;
2. 37 mm dense-core AP;
3. artillery tractor and firing-solution quality;
4. motor-transport reliability;
5. mobile power / workshop / recovery;
6. water and ammunition bottlenecks;
7. Soviet artillery / armor / vehicle mass;
8. Japanese command / combined-arms limitations.

Expectation: Asai support makes the Japanese July attack more sustainable and reduces mechanical self-attrition. It does not by itself remove the Soviet quantitative and combined-arms advantage.
