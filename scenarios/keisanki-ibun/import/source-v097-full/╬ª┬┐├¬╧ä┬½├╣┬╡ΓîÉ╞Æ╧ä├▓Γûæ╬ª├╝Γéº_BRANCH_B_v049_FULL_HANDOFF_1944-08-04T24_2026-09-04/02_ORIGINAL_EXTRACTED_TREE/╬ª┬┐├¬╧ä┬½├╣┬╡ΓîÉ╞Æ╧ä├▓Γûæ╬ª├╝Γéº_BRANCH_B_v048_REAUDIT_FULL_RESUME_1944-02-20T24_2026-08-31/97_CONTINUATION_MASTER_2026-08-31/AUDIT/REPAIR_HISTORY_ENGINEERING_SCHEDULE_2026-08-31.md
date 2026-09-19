# REPAIR HISTORY / ENGINEERING SCHEDULE — 2026-08-30 to 2026-08-31

This is intentionally written as an **engineering schedule**.  The sequence of mistakes, reopened assumptions, tests and repairs is itself part of the branch methodology.  Do not compress it into a single final number and discard the path.

## Phase 0 — Resume integrity and branch contamination controls

**Problem.**  v048 contained a large valid knowledge base plus old settlement/runtime material from earlier branches.  Several files could silently reintroduce rolled-back results or later assumptions.

**Controls established.**

- semantic base remains **v048**;
- old `97_CONTINUATION_MASTER_2026-08-30` is preserved but is no longer the current load master after this re-audit;
- `96_SESSION_WORKING_2026-08-30` is audit material, not runtime authority;
- `99_LEGACY_UNTOUCHED` is provenance only unless revalidated;
- the rolled-back Sep-1943 “Second Midway” result is forbidden in current Branch B;
- Bengal planning references to secondary carriers do not imply combat deployment: actual Bengal combat hull deployment remains zero;
- technology-transfer cargo is split into information/documents, samples/small hardware, and full hardware; I-34 success does not duplicate full Jumo/HWK engines.

**Why it mattered.**  Without these guards, later calculations looked internally precise while importing force losses, doctrine, carrier locations or technical maturity from the wrong branch.

---

## Phase 1 — Marianas continuation exposed missing propagation

The session initially advanced the old 1944-06-15 frontier through provisional 16-21 June states.  That work found several modeling omissions:

- secondary-carrier decks were being treated too passively;
- aircraft/deck separation and cross-deck recovery were under-modeled;
- Marianas water aviation disappeared from the continuation ledger;
- runway-based Marianas aviation after 17 June was also accidentally suppressed from the ledger;
- Kongo-class employment needed to be derived from Yamamoto's fleet-decision intent, not copied from historical bombardment patterns;
- tank reliability/recovery/doctrine effects needed to propagate into daily usable vehicles rather than merely increase vehicle count.

**Decision.**  Rather than patch June locally, the simulation was rolled back to GALVANIC because the missing fortification/logistics/sensor effects originated before Tarawa.  The provisional June 16-21 packages are preserved in `QUARANTINED_DOWNSTREAM` and must not be loaded as current results.

---

## Phase 2 — Pre-GALVANIC fortification/logistics reopen

**Question.**  Why did Branch B island defense still resemble “historical garrison plus a small increment” despite years of better logistics, construction uptime and process control?

**Repair.**  Fortification was redefined as conversion of shipping + engineering plant + materials + labor into a base-defense system.  The pre-GALVANIC branch does **not** know anti-LVT/deep-island lessons yet; it simply builds the older concept more completely and robustly.

Engineering cargo explicitly includes mixers, compressors, drills, pumps, generators, welders, winches, tractors/dozers, trucks, sawmills/workshops, cement, steel, wire, timber, explosives/mines, phones/cable, pipe and protected fuel/water systems.

**Guard.**  No automatic giant cave networks or unsupported concrete fortresses.  Natural terrain/caves, drainage, entrances, blast walls, shelters and small magazines are allowed where geography supports them.

**Files.**  Runtime overlays 001-003.

---

## Phase 3 — GALVANIC air OOB, hardening, sensor and water-air repair

**Problem.**  Regional air strength and base allocation had arithmetic inconsistency, and “airfield suppression” was too close to “air system erased.”

**Repair.**

- corrected regional 23 Nov center to 166 physical / 134 serviceable aircraft;
- separated land fighters, attack aircraft, legacy recon/water-air, Kyofu and Zuiun;
- treated revetments by protection class rather than a flat survival multiplier;
- distinguished aircraft loss from survival of mechanics, fuel, workshops, communications and repair parties;
- kept lagoon/water-air facilities as separate target systems;
- retained Kinsei Zero shore allocation centered at zero.

**Consequence.**  U.S. first suppression could heavily degrade the network without sterilizing it.  Surviving search/attack capacity forced repeat work and altered U.S. deck allocation.

**Files.**  Runtime overlay 004 and the corrected v002 air-OOB file in overlay 006.

---

## Phase 4 — Secondary-carrier domain trace

**Problem.**  “Plan mentions western/Indian Ocean use” had drifted toward “secondary carriers were actually deployed there,” and carrier hull position was being conflated with air-group location/readiness.

**Repair.**  Hull-by-hull 1943 trace closed for Junyo, Hiyo, Ryujo and Zuiho.  Bengal combat deployment = zero.  By GALVANIC they form a rear-deck support system, not free aircraft added to the first-line strike.

Functions: CAP rotation, search, ferry, emergency recovery, orphan-aircraft collection and limited second strike.  First-line Kinsei Zero allocation remains small and prioritized; late Zuisei Zero remains the main fighter.

**Consequence.**  Carrier warfare thereafter uses hull location / air-group location / deck readiness / mission assignment separately.

**Files.**  Runtime overlay 005.  Earlier trace-resume package is preserved under diagnostic audit only.

---

## Phase 5 — GALVANIC Pass A diagnostic -> adaptive-U.S. runtime rule

A fixed-U.S. “Pass A” was run only to measure sensitivity of hardened bases.  It showed that the same historical-style first strike did not sterilize the Branch-B network.  A U.S. adaptive “Pass B” then reallocated sorties, CAP/sweep/escort effort and repeat suppression.

**Critical policy change.**  The fixed/non-adaptive U.S. path was retired as an actual scenario.  From this point onward the United States always adapts naturally to observable evidence, with normal delays, mistakes and friction.

The Pass A JSON remains in overlay 006 as an accident/sensitivity record but is explicitly excluded from runtime load semantics.

---

## Phase 6 — Tarawa day-by-day rerun

### 24/25 Nov night

Branch B's improved shelters, local communications, ammo dispersion and assembly routes allow a more coherent 430-530-man counterattack with 5-6 Type 95 tanks.  Red 2/3 connection is locally disrupted for roughly 1.5-3 hours, but U.S. Sherman/75-mm/illumination/DD fire restores the bridgehead.

### 25 Nov

U.S. adapts: the priority becomes preventing Red 2/3 reconnection from being cut again, then systematic strongpoint reduction with tank + engineer + direct fire + naval observation.  Japanese island-wide C2 degrades while local cells remain effective.

### 26 Nov carrier battle

New Tarawa support demand and properly modeled rear decks alter the carrier task state.  Japanese first strike rises from the old ~160-165 to ~178-188 through reduced first-line CAP/search burden—not by adding the whole secondary-carrier pool to the strike.  Soryu's old two-hit campaign-out center is replaced by a one-hit + near-miss degraded-but-recoverable center.

### 26/27 Nov surface action

Because Tarawa remains a valuable active target, the Japanese DD raid logically shifts from Makin toward Tarawa support waters.  Four DD immediate first salvo is corrected to **24 Type 93 torpedoes**, not the old 28-32.  One U.S. DD loss remains centered, but the historical name Franks is not inherited without individual OOB closure.

### 27-29 Nov closeout

Makin ends without copying Tarawa's defensive density.  I-175's old Pierce hit is removed; survival/repair state changes downstream.  Tarawa organized resistance collapses 28 Nov evening/night and secure follows 29 Nov morning.  U.S. casualties are materially higher, but U.S. combined-arms reduction becomes more efficient with each day.

**Files.**  Runtime overlays 006-011.

---

## Phase 7 — Post-GALVANIC learning, Marshall network and Soryu recovery

**Soryu.**  The lighter 26 Nov damage removes the old long Japan repair clock.  Soryu is centered back in first-line service in mid-Dec 1943.  Hull recovery does not restore lost veteran aircrew; deck availability and strike-cadre debt remain separate.

**Japanese learning.**  Tarawa yields evidence that ammo dispersion, communications and shelters work, but shallow beach-line defense is eventually dismantled.  Lessons propagate in stages; no perfect survivor AAR or future knowledge.

**Fortification expanded.**  Sensor/C2 becomes part of the fortress: radar, DF/RI, visual posts, plot, phone/radio, backup power, spares and mobile water-air reconnaissance.  A-grade nodes can create useful warning and staged fighter readiness without becoming U.S.-style precision GCI.

**Network.**  Taroa/Maloelap, Kwajalein/Roi, Wotje, Mili, Jaluit and Eniwetok are modeled as a distributed system, with Ponape/Kusaie staging support.  Kusaie can become a limited staging strip through better construction, not a magically large fighter base.

**U.S. learning.**  Tarawa drives more reconnaissance, fire, boats, engineers and ammunition, but each addition competes for DD ASW/picket duty, carrier CAP/search, beach throughput, lanes, fuel and command bandwidth.  Congestion is an explicit U.S. bottleneck.

**Files.**  Runtime overlays 012-013.

---

## Phase 8 — FLINTLOCK information war and four-carrier battle

From 16-31 Jan, Japanese warning develops through submarine/traffic/DF/air-water reconnaissance chains; radar helps preserve local warning and sortie generation but does not detect carriers at impossible ranges.  The U.S. retains Kwajalein direct assault as the center plan, with D-Day later than historical due to changed air/naval wallets.

Soryu's recovery means the Japanese first-line carrier force is Shokaku, Zuikaku, Hiryu and Soryu.  On 2 Feb, fresh contact and observed U.S. mission cycling satisfy a real strike-quality GO gate.  A carrier cross-strike occurs one day earlier than the old branch line.

Centered effects include Cabot campaign-out, Intrepid temporary deck interruption, Hiryu mission damage, Soryu light damage, and heavy Japanese carrier-aircrew debt.  The following maritime rebaseline corrected a bookkeeping typo: cumulative Japanese carrier-air irrecoverable center **56 -> 86**; the combat result itself did not change.

**Files.**  Runtime overlays 014-016.

---

## Phase 9 — FLINTLOCK approach and D-Day

4-5 Feb are modeled as regeneration/reallocation, not another free full-rate carrier day.  A Japanese submarine mission-kills one LST-class ship but its identity/cargo remain open rather than being used to force a particular tank/LVT loss.  U.S. suppression reduces Marshall local air and radar/C2 without erasing all distributed warning.

D-Day is fixed at **6 Feb 1944** after weighing diminishing bombardment returns against submarine/air exposure.

Ground combat separates Roi, Namur and Kwajalein.  Recent corrections to radar, AA, communications, ammunition dispersion, local reserves, vehicles and water-air all apply, but no untraced Japanese tank force is created.  Namur's historical giant ammunition/torpedo-warhead secondary explosion is not automatically inherited because Branch-B blast separation changes the physical setup.

U.S. mass helps, but more LVT/LST/engineers also create beach/route queues that U.S. traffic control must actively manage.

Roi falls fastest; Namur remains harder; Kwajalein persists through D+2.  Kwajalein is formally secure on 9 Feb.

**Files.**  Runtime overlays 017-021.

---

## Phase 10 — U.S. force, death and amphibious ledgers

### Force delta

U.S. ground manpower/OOB remains close enough to historical FLINTLOCK structure that the assault plan does not need to be rebuilt solely for infantry quantity.  Differences are mainly cadre/replacement quality and naval/air task wallets.

### Death ledger

No-Guadalcanal does not mean every historical Guadalcanal death becomes a free 1944 soldier.  Branch-B Santo/New Caledonia and especially the much costlier MI battle offset a large part of the raw total.  Specialist categories are separated: general infantry, NCO/officer cadre, surface-fleet sailors, carrier/deck crew, aircrew.

### Amphibious wallet

A major correction: CATCHPOLE has a **dedicated** reserve amphibious wallet of **106 amtracs + 17 amphibian tanks**.  It does not wait for FLINTLOCK's 4th Marine/7th Division LVT fleet to be repaired.  Tarawa's LVT survivors also are not simply added to Eniwetok.

Tarawa's final LVT state is re-audited as much healthier than historical because the favorable tide/lane plan reduces prolonged reef-shuttle abuse; that benefit is preserved for later 2nd Marine rebuilding, not duplicated into CATCHPOLE.

**Files.**  Runtime overlays 022-024.

---

## Phase 11 — Post-FLINTLOCK next-operations split

HAILSTONE and CATCHPOLE are separated into distinct wallets.  HAILSTONE main force is fixed at:

Wasp / Yorktown / Essex / Intrepid / Bunker Hill + Belleau Wood / Monterey / Cowpens = **5 CV + 3 CVL**.

Princeton and Langley plus Sangamon/Suwannee/Chenango support CATCHPOLE.

The old HAILSTONE/CATCHPOLE outcomes are reopened.  The date-generation logic survives after re-audit: HAILSTONE centered on 20 Feb; Engebi on 21 Feb.  Dates after Engebi remain open and must respond to captured intelligence and actual resistance.

Eniwetok has ~3,380-3,540 defenders and nine traced Type 95 tanks, three per main island.  No local operational radar is created without a shipment trace.  Short-warning improvements are redistribution, alternate command, camouflage, registered fires and tank concealment—not a new Peleliu-style cave network.

**Files.**  Runtime overlay 025.

---

## Phase 12 — HAILSTONE Day 1 / CATCHPOLE approach to 20 Feb T24

Truk's defense is modeled as a prepared base system: radar + visual + RI/DF + weather + plot + radio/telephone + staged fighter readiness + AA fire direction + independent water aviation.  It receives strategic/operational warning and does not stand down after a single negative search.

High-value mobile targets evacuate: first-line carriers stay west, Hiryu leaves after emergency repair, Akashi and major oilers/tenders receive priority.  Therefore HAILSTONE does **not** inherit the historical shipping-massacre geometry.

On 20 Feb the U.S. still wins the daylight air battle through better fighters, repeated deck cycles and mass, but at higher cost.  Japanese first-hour ground-air massacre is avoided; U.S. shifts more sorties into deliberate runway/radar/plot/power/fuel/maintenance suppression.

At dusk, Truk still has a degraded warning/base system and 13-19 attack/recon/water-air night-capable aircraft.  The Japanese night counterstrike gate remains open with only sector-quality cueing.

At Eniwetok, passage minefields consume 2.5-4 hours of schedule margin but do not cancel the 21 Feb Engebi landing.  The defenders are fully alerted; 3-5 local aircraft remain serviceable and the nine Type 95 tanks remain traced and hidden as local reserves.

**Files.**  Runtime overlay 026.

---

# Current engineering frontier

**1944-02-20T24.**

Next exact work items:

1. Truk 20/21 Feb night Japanese air/submarine counterstrike using actual stale/sector cue quality;
2. HAILSTONE Day 2 only after resolving the night and the fixed-system repair/damage state;
3. Eniwetok 20/21 night air/submarine interference;
4. 21 Feb Engebi assault from the actual mined-passage, fire-support, local-air, tank and short-warning defense state;
5. decide Eniwetok Island / Parry sequencing only after Engebi results and captured intelligence.

# Downstream quarantine

The old v048 continuation through June and the session's provisional Marianas 16-21 June packages are preserved because they contain useful OOB, doctrine and accident-history information.  They are **not** current results.  The GALVANIC/FLINTLOCK/HAILSTONE upstream changes can alter carrier availability, trained aircrew, submarine states, construction lessons, U.S. learning and support wallets; therefore those later Pacific events must be rerun causally.
