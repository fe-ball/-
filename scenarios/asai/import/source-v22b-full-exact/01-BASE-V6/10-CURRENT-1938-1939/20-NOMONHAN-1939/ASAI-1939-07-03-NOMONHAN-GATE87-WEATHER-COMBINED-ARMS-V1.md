# ASAI 1939-07-02/03 NOMONHAN GATE 87 — WEATHER / RECON / COMBINED-ARMS CLOSURE V1

Status: CURRENT-BRANCH PATCH
Time closed through: 1939-07-03 24:00
Parents:
- ASAI-1939-07-01-NOMONHAN-AIR-RECON-CLOSURE-V1.md
- ASAI-1939-06-30-NOMONHAN-SUPPORT-VEHICLE-CLOSURE-V1.md
- 16-DENSE-CORE-AMMUNITION-MILITARY-IMPACT-1937.md
- asai-works-tank-early-computation-materials-rebaseline-1928-41.md

## 0. Governing rule: weather-window elasticity, not weather cancellation

Asai-derived aviation improvements do not create visibility through cloud, rain, darkness or dust.
They do change whether a short usable weather window can be exploited.

Count separately:
1. transit/climb compression from faster aircraft;
2. endurance/alternate margin where engine/mixture mapping actually supports it;
3. launch readiness and turnaround from QC, maintenance and ground power;
4. staggered/overlapping reconnaissance because more aircraft are mission-ready;
5. photo-to-map turnaround after recovery.

Do not apply a generic `all-weather +X%` multiplier.

### Ki-15-II anchor
Relative to Ki-15-I historical reference:
- maximum speed about 510 vs 480 km/h;
- climb to 5,000 m about 6m49s vs 8m27s;
- nominal range remains about 2,400 km in commonly cited specifications.

Operational implication: on a typical local/deep reconnaissance leg, the minimum usable daylight/weather opening can be several minutes shorter, and a sortie can launch later into a clearing without automatically losing the recovery margin. This is useful in 20–60 minute marginal windows but cannot rescue a 20 m-visibility thunderstorm or darkness.

## 1. Historical July 2 weather anchor

4th Tank Regiment battle report:
- daytime: clear/hot;
- weather worsens toward evening;
- rain begins after about 18:00;
- by about 22:00 black cloud and severe storm; visibility only around 20 m;
- major thunderstorm immediately before the tank breakthrough aided concealment.

Drea tactical study:
- around 19:40 a Japanese reconnaissance pilot reports Soviet withdrawal and urges rapid pursuit;
- pilot visibility/accuracy is degraded by cloud and rain;
- the resulting night pursuit/attack becomes fragmented and poorly coordinated.

CLOSED: Asai does not remove this weather sequence.

## 2. July 2 reconnaissance decision gate

### 2.1 Earlier-day reconnaissance is stronger
By July 1–2 the worldline has:
- 4 operational Ki-15-II in the Hailar/front reconnaissance pool plus 2 rear reserve/evaluation aircraft;
- stronger photo/index processing;
- better aircraft readiness;
- reliable ground electrical support at the photo/intelligence cell.

Therefore daytime July 2 reconnaissance is scheduled with overlapping sweeps rather than relying on one late report.

CLOSED working effect:
- an afternoon sweep before the rain confirms that substantial Soviet armor/artillery and vehicle activity remains on/behind the east-bank positions;
- this does not identify every gun or prove enemy intent;
- it creates a recent contradictory intelligence anchor against any later claim of a general Soviet withdrawal.

### 2.2 19:40 withdrawal report remains
The historical late report still occurs in substance.
Rain has already begun and light is failing.

CLOSED:
- report content remains `enemy appears to be withdrawing / rapid pursuit may trap them`;
- reliability is explicitly tagged LOW-MODERATE because of weather and conflict with the earlier sweep;
- no photo product capable of resolving the issue exists before darkness.

### 2.3 No magic second confirmation sortie
A faster Ki-15-II cannot create daylight after the 19:40 report. With sunset around 20:00 and weather worsening toward the 22:00 storm, a fresh visual/photo confirmation cannot reliably return before Yasuoka's decision cycle.

CLOSED:
- no definitive second-sortie correction before the 21:00 attack order;
- the gain is not `report corrected`, but `report believed less absolutely`.

## 3. Effect on Yasuoka's decision

Yasuoka still decides to attack on the night of 2–3 July.
Reasons retained:
- operational plan already favors rapid action;
- fear that Soviet forces may escape;
- Japanese doctrine/command culture is unchanged;
- storm/night appears to offer concealment.

But the attack is framed as a rapid attack against a partially withdrawing but still organized enemy, not a simple pursuit of a collapsing force.

CLOSED command delta:
- tank regiments are ordered to retain phase-line/axis discipline as far as communications allow;
- known/presumed antitank and artillery belts from daytime reconnaissance are passed to artillery and tank commanders;
- attached artillery receives prepared target areas before darkness;
- infantry/artillery support is not deliberately discarded merely to maximize pursuit speed.

Hard limit:
- radio density and tactical combined-arms doctrine remain weak;
- once tanks diverge in darkness/storm, command still degrades badly.

## 4. Route, fuel and support mechanics before the assault

Historical 4th Tank Regiment lessons explicitly state:
- a roughly 20 km wetland west of Jiangjunmiao was insufficiently reconnoitered/prepared and caused major delay;
- fuel support was insufficient, leaving little fuel after the night attack;
- tanks were used too independently from infantry/artillery.

Worldline deltas already available:
- selected heavy truck/tractor mechanical-ready fraction +5–8 percentage points;
- routine workshop turnaround 15–25% shorter;
- better route/logistics records and engineering support;
- stronger towing and recovery margin;
- no increase in total road width or total fuel stocks by fiat.

CLOSED for July 2:
- wetland delay is reduced, not erased; support elements arrive roughly 1–2 hours less late than matched history on the central working branch;
- bogging/recovery consumes less fuel and fewer vehicles;
- fuel trucks themselves suffer fewer mechanical dropouts;
- 4th Tank Regiment enters the night action with a materially better reserve margin, sufficient to preserve one controlled post-assault reposition/withdrawal cycle for more vehicles.

No blanket fuel-economy percentage is assigned.

## 5. Artillery integration in rain/night

Prepared fires benefit from Asai-derived survey, firing-table, lot-control and target indexing even when observation becomes impossible.

CLOSED:
- before the storm, several likely AT/artillery areas are pre-registered;
- initial approach receives more coherent suppressive/preparatory fire than matched history;
- in the first phase, scarce shells are wasted somewhat less;
- after tanks leave planned axes or penetrate beyond the registered belt, fire support loses effectiveness because communications and observation remain weak.

This is a first-belt advantage, not Soviet-style continuous combined-arms control.

## 6. Tank OOB and ammunition

### 6.1 Chi-Ha share
Historical 3rd Tank Regiment included only about 4 Type 97 Chi-Ha among a force dominated by Type 89 mediums.
Worldline prior closure replaces part of the Type 89 share without increasing overall armored establishment.

CLOSED opening strength:
- 11–13 Type 97 Chi-Ha in the Yasuoka armored force, central 12;
- replacement is primarily at the expense of Type 89s;
- Chi-Ha retains the low-velocity 57 mm infantry-support gun and is not converted into a true AT tank.

6–8 Chi-Ha carry removable hemp/hair spall-liner trial panels.
Effect: lower crew injury risk from non-penetrating/partial-penetrating internal spall; no increase in penetration resistance or tank survival after a full 45 mm penetration.

### 6.2 Ha-Go propulsion
Standard Ha-Go remains 120 hp naturally aspirated.
A limited Manchurian high-temperature/high-altitude compensation subset may be present, but no fleet-wide 140–145 hp conversion exists.
Benefit is readiness/flat-rating, not higher headline top speed.

### 6.3 Dense-core tank-gun ammunition
Current technical parent permits special dense-core AP for the Type 94 37 mm tank gun as a MEDIUM-value branch, but its lower muzzle velocity makes it distinctly weaker than the Type 94 AT-gun program.

CLOSED for Nomonhan:
- a small tank-gun-compatible special-AP batch has been qualified before July 1939 after the Zhanggufeng anti-armor validation cycle;
- 120–180 special rounds are allocated to selected Ha-Go crews, generally only several rounds per tank;
- this is a separate cartridge/round from the Type 94 AT-gun reserve and is not deducted one-for-one from the AT-gun 37x165R stock;
- use is reserved for difficult frontal/oblique AFV shots at close to moderate range;
- no exact penetration mm figure is canonized.

Chi-Ha 57 mm dense-core remains non-central and is not credited.

## 7. July 2/3 battle result

### Historical best-data comparison anchor
Common best-data summaries give roughly:
- 73 Japanese tanks engaged;
- about 41 disabled/lost during the July 3 fighting, with about 13 irrecoverable and many others repaired in field/rear shops;
- about 70 tank-regiment personnel killed across 3rd/4th Tank Regiments.
Exact accounting differs by source and recovery date.

### Worldline combat mechanics
Positive Japanese deltas:
- enemy withdrawal report is treated as uncertain rather than absolute;
- better route/fuel state;
- support elements less late;
- first-belt artillery preparation;
- larger Chi-Ha share;
- limited special AP for Ha-Go and strong dense-core AP in attached AT units;
- better mechanical recovery;
- July 3 clear-weather reconnaissance can warn more reliably of Soviet counter-moves.

Retained Soviet advantages:
- 45 mm AT and tank guns can still kill every Japanese tank type at practical ranges;
- Soviet armor/artillery mass is larger;
- Japanese tank radios/combined-arms control remain inadequate;
- Japanese infantry cannot keep pace with armor at Soviet motorized speed;
- Chi-Ha 57 mm remains poor for tank-vs-tank combat;
- storm/night still fragments units.

### CLOSED outcome through July 3 24:00
- Yasuoka armored attack still fails to reach the operational objective / create the intended encirclement.
- Japanese tanks penetrate some forward positions and inflict somewhat greater local AFV/gun losses, but Soviet defense and counterattack stop the thrust.
- Japanese tank disabled/lost count: **30–35 central band** instead of matched-history ~41 best-data.
- irrecoverable Japanese tanks by the immediate post-battle accounting: **8–10** instead of ~13.
- additional tanks can be returned to action by field/rear workshops over July 3–6 because recovery and repair are stronger.
- tank-regiment KIA reduction: **about 15–25** central band; wounded reduction smaller because spall/recovery converts some fatalities into wounds.
- Soviet/Mongolian AFV additional mission-kills attributable to the worldline package: **+5 to +8** over matched history on the Yasuoka/east-bank front, not counting unrelated west-bank Soviet losses.

Do not read these as a strategic victory.

## 8. July 3 air/weather follow-on

4th Tank Regiment weather report: July 3 is generally clear and combat movement is not weather-limited; temperature reaches roughly 32 C.

Therefore worldline aviation advantage switches from `weather-window elasticity` to ordinary repeated reconnaissance/attack support:
- Ki-15-II can fly multiple sweeps with reduced interception exposure;
- photo/intelligence processing improves the warning of Soviet armored concentrations;
- bomber target preparation is somewhat better for fixed/located positions;
- no automatic fighter gunnery bonus.

Ki-36 direct-cooperation detachment is still in transit and receives no July 2–3 credit.

## 9. Consequence gate for July 4–9

Because Japanese armor is damaged but not wrecked to the same degree, the historical July 9 dissolution/withdrawal of the Yasuoka tank detachment is no longer automatic.

OPEN EVENT for next gate:
- how many of the 30–35 disabled tanks return by July 4–6;
- whether Soviet pressure and artillery losses force withdrawal anyway;
- whether Kwantung Army retains the tank regiments as a local mobile reserve rather than dissolving them immediately;
- whether better Japanese armor survival induces another over-aggressive attack and thereby gives back the advantage.

## 10. Weather-window rule for later Nomonhan aviation

Use this rule from Gate 87 onward:
- weather visibility/ceiling is a hard gate;
- performance affects the minimum exploitable opening and recovery margin, not visibility itself;
- faster climb/transit and preserved endurance matter most in brief 20–60 minute clearings;
- higher mission-ready fraction permits staggered coverage and a better chance that an aircraft is already airborne when a gap opens;
- ground GT power/maintenance matters because an aircraft that is mechanically ready can launch immediately when the window appears;
- if the target is hidden by solid cloud or visibility falls below safe identification requirements, effect = zero regardless of engine performance.
