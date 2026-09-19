# Branch B — WIO-6: October Indian Ocean / Cape / Madagascar drawdown / TORCH carrier deficit

Period: **1942-10-04 through 1942-10-24 inclusive**  
Status: **CENTER CLOSED through 1942-10-24; one strong named torpedo upper-tail ticket remains OPEN**  
Dependency: v066 WIO-5 + v063 Madagascar wallet + v050 authoritative Santo/FS clock.

## 0. Governing rules

- British countermeasures are charged **gross first**. Calendar assignment is booked even when maintenance, defects or transit reduce tactical output.
- **Full cost != full tactical effect**. No patrol, escort or transfer is assumed to create a contact or kill unless the geometry exists.
- An unaffordable bill is not erased. It must reappear as a delay, uncovered route, another theatre's loss of capacity, wear, or blood.
- Same hull on same day is never double-booked.
- No named counterfactual casualty is invented.
- Historical defensive measures already present at a historical attack are not applied a second time to rescue the same target.
- Historical duties that disappear because of Branch divergence are credited; the credit is not automatically converted into enemy losses.

## 1. Correction carried forward from v066: CAMILA was omitted

v066 closed WIO-5 at 5 ships / 26,906 GRT and cumulative 29 ships / 139,770 GRT. That omitted I-166's 1 October attack on **CAMILA, 1,201 GRT**.

CombinedFleet I-166 records that on 1 October, off Calcutta, I-166 shelled and damaged CAMILA; the burning merchant was beached and became a total loss. This is a confirmed historical loss and must be included in the ordinary-submarine ledger.

**Corrected WIO-5 increment:** 6 ships / **28,107 GRT**.  
**Corrected cumulative through 3 October:** 30 ships / **140,971 GRT**.

This is a bookkeeping correction, not a new Branch-extra loss.

Source anchor: CombinedFleet I-166 TROM, https://www.combinedfleet.com/I-166.htm

## 2. I-162: one loss, one expensive save

### 2.1 MANON — 7 October

CombinedFleet records I-162 torpedoing **MANON, 5,597 GRT**, carrying 7,100 tons of coal from Calcutta/Vizagapatnam toward Colombo. MANON sank; eight sailors were killed.

The Eastern Fleet October narrative dates the loss to 8 October, while the Japanese TROM gives 7 October. For individual-boat chronology the TROM date is retained; the source discrepancy is preserved.

**CENTER:** MANON remains sunk. No duplicate Branch bonus is added to an already successful attack.

Source anchors:
- CombinedFleet I-162 TROM, https://www.combinedfleet.com/I-162.htm
- Eastern Fleet October 1942 narrative, https://www.naval-history.net/xDKWD-EF1942-Introduction.htm

### 2.2 MARTABAN — 13 October

I-162 torpedoed **MARTABAN, 4,161 GRT** east of Ceylon. The bow was hit, two sailors were killed, fire broke out and the crew abandoned ship. The ship did **not** become a permanent merchant loss.

The rescue bill is real and is charged gross:
- aircraft search on 14–15 October;
- HMS ASTER takes MARTABAN in tow on 16 October at only 1–2 knots;
- HMAS LAUNCESTON participates in survivor recovery;
- because Trincomalee has no suitable tug, EMPIRE DEFIANCE escorted by NETRAVATI is ordered to assist;
- Australian official history records ASTER reaching Trincomalee with MARTABAN on 21 October and 61 of 64 crew ultimately rescued.

Through this block, the merchant hull is unavailable from 13–24 October inclusive: 12 calendar days × 4,161 GRT = **49,932 temporary GRT-days**. This is not permanent sunk tonnage and not the full repair bill.

Known minimum towing window: ASTER, **16–21 October = 6 corvette tow-days**. Rescue/search/support craft are booked as committed where identifiable, but no unsupported exact aircraft-sortie count is invented.

**CENTER:** MARTABAN survives. The torpedo already functioned and caused a damaging hit; submarine technical improvements do not convert the historical salvage operation into an automatic sinking.

Source anchors:
- CombinedFleet I-162 TROM, https://www.combinedfleet.com/I-162.htm
- RN War Diary, 17 Oct 1942, MARTABAN entry (Naval Historical Branch)
- Australian official history, chapter “On Australia’s Ocean Communications” (AWM RCDIG1070424)

## 3. I-27: the strongest Branch-specific torpedo-failure ticket so far

### 3.1 EMPIRE BOWMAN — 18 October

Near Ras al Hadd, I-27 fired on **EMPIRE BOWMAN, 7,031 GRT**. CombinedFleet records **two torpedoes hitting amidships and neither exploding**. The RN October narrative independently records two dull blows amidships consistent with failed torpedoes.

This is qualitatively different from the many historical attacks that already succeeded. The geometrical-hit gate was already passed twice; the historical failure is squarely in the technical-function gate.

Stage 3A, however, explicitly does **not** adopt an absolute torpedo failure coefficient. Its q_run/q_fuze calculation is illustrative only. Therefore this event is not assigned a hard Branch probability.

Under the existing WIO working sensitivity convention only — treating 15%, 20%, 25% as hypothetical relative chances of removing each historical dud gate — the probability that at least one of two dud gates is removed is:

- 15% convention: `1 - 0.85^2 = 27.75%`
- 20% convention: `1 - 0.80^2 = 36.00%`
- 25% convention: `1 - 0.75^2 = 43.75%`

These are **not adopted model coefficients**. They only show that EMPIRE BOWMAN is a material upper-tail divergence candidate. Even a corrected detonation still leaves a separate damage-to-loss gate.

**CENTER:** EMPIRE BOWMAN survives.  
**OPEN:** `EMPIRE_BOWMAN_1942-10-18_OPEN_UPPER_TORPEDO_DUD_DAMAGE_OR_LOSS`.

No center extra GRT is posted.

Source anchors:
- CombinedFleet I-27 TROM, https://www.combinedfleet.com/I-27.htm
- Eastern Fleet October 1942 narrative.
- Stage 3A local authority: `BRANCH_B_SUBMARINE_REVALIDATION_STAGE3A_v001.md`, §5.

### 3.2 OCEAN VINTAGE — 22 October

I-27 torpedoed and sank **OCEAN VINTAGE, 7,174 GRT**, sailing independently from New York to Bandar Shapur with 9,300 tons of general cargo. An RAF crash launch towed the lifeboats toward Ras al Hadd.

**CENTER:** retained as historical loss. No additional Branch multiplier is applied.

Source: CombinedFleet I-27 TROM, https://www.combinedfleet.com/I-27.htm

### 3.3 Other October attack reports

Unsuccessful or unattributed cases such as GLENAFRIC, POINT CLEAR, CABERITA, and HAVFRU are not promoted without a defensible Japanese-boat identity and failure mechanism. HAVFRU's reported dud is retained as `UNATTRIBUTED_DUD_ATTACK_OPEN_IDENTITY`, not automatically assigned to I-27.

## 4. Ordinary IJN submarine ledger through 24 October

Corrected carry-in through 3 October: **30 ships / 140,971 GRT**.

WIO-6 permanent losses:
- MANON: 5,597 GRT
- OCEAN VINTAGE: 7,174 GRT

WIO-6 increment: **2 ships / 12,771 GRT**.

Corrected cumulative, 5 June–24 October: **32 ships / 153,742 GRT**.

MARTABAN is excluded from permanent-loss GRT and booked separately as temporary damaged capacity. EMPIRE BOWMAN remains an upper-tail ticket only.

**Branch-extra center direct merchant loss through 24 October remains 0 ships / 0 GRT relative to the historical outcomes represented by these attacks.**

The strategic divergence is now in where Britain must move scarce escorts, aircraft and carrier capacity to preserve those historical outcomes.

## 5. The Aden “reinforcement” is transient: Madagascar -> Aden -> Mediterranean

v066 carried the expectation that CROMER, CROMARTY and ROMNEY would reach Aden on 5 October and might close the surface A/S hole. The 5 October Mediterranean Fleet diary clarifies their destination: all three arrived at Aden **to join the Mediterranean Station**.

This changes the interpretation:

- Madagascar had prevented their earlier release.
- They reach Aden on 5 October, but are **not a free permanent Gulf-of-Oman A/S group**.
- The Mediterranean / El Alamein minewar claim takes them onward.
- By 22 October CROMARTY is already on passage toward Suez; the flotilla is being absorbed into the Mediterranean minesweeping problem immediately before the 23 October El Alamein offensive.

**CENTER:** do not retain the Cromer group at Aden merely to save EMPIRE BOWMAN or OCEAN VINTAGE. Doing so would shift real risk into the Mediterranean and would be a free substitution.

This is the clean cross-theatre chain:

`Madagascar demand -> delayed A/S release -> brief Aden transit/reinforcement -> Mediterranean minewar consumes the same hulls`.

Source anchor: Mediterranean Fleet Admiralty War Diary, 5 Oct 1942, Fourteenth Minesweeping Flotilla.

## 6. HERO and TETCOTT continue to be the Mediterranean payment

HERO and TETCOTT remain used on the Aden/Red Sea route during this block. TETCOTT continues escort movements through 24 October; the historical rescue of OCEAN VINTAGE survivors occurs just beyond this cutoff.

WIO-6 gross removal from Mediterranean availability:
- 4–24 October: 21 days each × 2 = **42 destroyer-days**.

These are historical gross cross-theatre burden, not Branch-extra. They matter because the Mediterranean is simultaneously approaching El Alamein and TORCH.

## 7. Persian Gulf convoy system still leaves a structural hole

The RN October narrative records 24 convoy movements in the Persian Gulf structure and states that **about 50% of trade entering the Persian Gulf remained unescorted**, principally because no suitable assembly port existed for overseas arrivals.

Therefore the British are not granted an imaginary fully escorted Ras al Hadd screen after 5 October. The loss of OCEAN VINTAGE while sailing independently remains compatible with the actual defensive architecture.

This also explains why the enormous gross A/S bill can coexist with continuing losses: the network is buying partial coverage, not invulnerability.

Source: Eastern Fleet October 1942 narrative.

## 8. Cape U-boat emergency consumes the released reserve

From 7 October German U-boats open a severe offensive off the Cape. The Eastern Fleet monthly narrative gives **about 15 ships / 100,000 tons sunk between 7 and 13 October**; the later Proceedings summary describes 13 ships sunk in the outbreak. Both figures are retained as a source discrepancy; no Branch-extra German kill is fabricated.

The practical effect is unambiguous: destroyers that might otherwise form an Indian Ocean reserve are sucked into South African waters.

### 8.1 Known minimum gross destroyer assignment, 4–24 October

Calendar-assignment bookkeeping only; this is **not** operational-effectiveness time:

- ARROW + ACTIVE, held at Cape from 7 Oct: 2 × 18 = **36 DD-days**
- NIZAM + FOXHOUND, Cape/refit pool from 7 Oct: 2 × 18 = **36 DD-days**
- EXPRESS + CATTERICK, ordered south and sail 13 Oct: 2 × 12 = **24 DD-days**
- NEPAL, reaches Durban/Cape pool 18 Oct: 1 × 7 = **7 DD-days**

Known minimum: **103 gross destroyer assignment-days** through 24 October.

NIZAM/FOXHOUND refit and machinery limitations mean these days do not imply full tactical availability. FORTUNE is deliberately omitted from the quantified minimum while her boiler-cleaning/availability clock remains less clean. NAPIER/INCONSTANT/BLACKMORE are not double-counted into the Cape pool during this block because they are still paying the Madagascar MD1 escort bill.

Source: Eastern Fleet Proceedings, 10 Oct–6 Nov 1942.

### 8.2 Branch-specific credit: no ILLUSTRIOUS escort back to Kilindini

Historically HOTSPUR and DERWENT left Durban on 15 October escorting ILLUSTRIOUS to Kilindini and arrived on 20 October: 2 ships × 6 inclusive days = **12 destroyer-days** of historical duty.

Branch ILLUSTRIOUS is mission-killed in the Mediterranean and is not in Durban. That specific escort task does not exist.

**Branch credit:** **12 gross DD-days of local availability**.

This credit is not mechanically subtracted from the 103 above because it is a different hull/location duty line, and it is not converted into an invented U-boat kill. It simply means the carrier loss removes one historical escort obligation as well as removing carrier capability.

Source: Eastern Fleet October narrative, destroyer movements.

## 9. Catalina cascade: Cape demand reaches back to Ceylon

The Cape emergency also consumes flying-boat margin.

- Three Catalinas from the East African pool are ordered to South Africa; the first movement suffers a forced landing on 13 October, and an operational three-aircraft Saldanha detachment is built.
- To replace the East African loss, **three Catalinas are moved from Ceylon to Mombasa on 13 October**.
- Separately, the existing three-aircraft Persian Gulf detachment from Ceylon remains committed to convoy/A/S work.

Gross WIO-6 commitment bookkeeping, not sortie count:
- Persian Gulf detachment, 4–24 Oct: 3 × 21 = **63 aircraft commitment-days**.
- South Africa detachment, 13–24 Oct: 3 × 12 = **36 aircraft commitment-days**.
- Ceylon -> Mombasa backfill, 13–24 Oct: 3 × 12 = **36 aircraft commitment-days**.

The specific Persian Gulf detachment therefore reaches **156 cumulative commitment-days** from 3 Sep through 24 Oct (93 carried in through 3 Oct + 63 in WIO-6).

Again, commitment-days are not assumed to be sorties. The cascade matters because the Cape emergency pulls the reserve chain all the way back to Ceylon.

Source: Eastern Fleet October 1942 narrative.

## 10. Madagascar: heavy fleet bill collapses, logistics/health bill remains

By early October the Army is firmly established and most of the naval task is complete. On 5 October Senior Officer Force M turns over duties; BIRMINGHAM and GAMBIA return to Kilindini, and MANXMAN has already left on 4 October.

Therefore the old high Madagascar battle-fleet charge is **not** continued indefinitely. This is a genuine release.

But the residual bill is substantial:

- The 29th Independent Brigade has deteriorated badly from malaria; reports run as high as **55 new cases per day**. Instead of proceeding directly to India, the brigade is routed to Durban for recuperation. The daily case figure is not multiplied into a fabricated exact casualty total.
- Convoy MD1 consists of DUNERA, DILWARA and EMPIRE PRIDE, leaving Tamatave 18 October.
- Escort: DAUNTLESS, NAPIER, INCONSTANT, BLACKMORE.
- EASTERN PRINCE is excluded because of engine-room defects.
- BLACKMORE is so overdue for boiler cleaning that her endurance is impaired and special oiling arrangements are required.

Gross 18–24 October booking through this cutoff:
- 3 troopships × 7 days = **21 troopship-days**.
- DAUNTLESS 7 cruiser-days + three destroyers × 7 = **28 escort hull-days**.
- 29th Brigade: **7 brigade-days unavailable for India** through the cutoff, with the larger recuperation debt carried forward OPEN.

Source: Eastern Fleet October 1942 Appendix III / Madagascar Operations.

## 11. TORCH: the unpaid carrier bill now has operational geometry

Historical Home Fleet planning shows VICTORIOUS and FORMIDABLE leaving the Clyde together on 30 October to join Force H for Operation TORCH. Historical FORMIDABLE's November air group is about **42 aircraft**.

Branch state:
- FORMIDABLE: sunk 5 Apr.
- INDOMITABLE: sunk 5 Apr.
- ILLUSTRIOUS: mission-killed at Pedestal.
- HERMES: not a modern fleet-carrier substitute and remains tied to the Indian Ocean system.

FURIOUS is not a free substitute. Her historical TORCH role includes direct Oran air support; using her to fill FORMIDABLE's covering slot removes that capability elsewhere.

**WIO-6 planning center:**
- `TORCH_FORCE_H_CENTER = VICTORIOUS_ONLY_MODERN_FLEET_CARRIER`
- `FORMIDABLE_SLOT_UNFILLED = ~42-aircraft historical carrier-air-group scale`
- TORCH remains executable.
- No TORCH casualty is posted before the 8 November operational geometry is actually run.

This is the first large unpaid bill that has escaped the Indian Ocean and reached a named future operation.

Source anchors:
- Home Fleet War Diary, 30 Oct 1942, TORCH departures.
- Formidable November 1942 air-group reconstruction, Armoured Aircraft Carriers.

## 12. Japanese payment: I-30 is lost on 13 October

Japan also pays in this block.

I-30 returns from the Yanagi mission, reaches Singapore on 13 October, departs after cargo handling, strikes a British mine three miles east of Keppel Harbour and sinks. **13 crew are lost; 96 are rescued.** Some cargo is salvaged, but the Würzburg radar model is destroyed and its drawings are rendered unusable.

Branch submarine machinery/reliability improvements do not remove this event. The causal chain is outdated codes/navigation information and a British minefield, not the technical reliability gate being audited for patrol endurance or Type 95 torpedoes.

**CENTER:** I-30 loss retained.  
Future technology-transfer effects remain a separate ticket; no broad “radar penalty” is fabricated in WIO-6.

Source: CombinedFleet I-30 TROM, https://www.combinedfleet.com/I-30.htm

## 13. WIO-6 center close — 24 October 1942

### Merchant/submarine account
- v066 correction: +CAMILA 1,201 GRT to prior block.
- WIO-6 permanent losses: **MANON + OCEAN VINTAGE = 2 ships / 12,771 GRT**.
- Corrected ordinary IJN submarine cumulative: **32 ships / 153,742 GRT**.
- Branch-extra center direct merchant loss: **0 ships / 0 GRT**.
- MARTABAN: saved, but at least **49,932 temporary GRT-days** through cutoff plus rescue/tow/air burden.
- EMPIRE BOWMAN: strongest named upper-tail Branch-extra case; center survival retained.

### British resource/tradeoff account
- CROMER group: not a permanent Aden reinforcement; Mediterranean minewar takes the hulls onward.
- HERO+TETCOTT: **42 Mediterranean destroyer-days removed** in this block.
- Cape emergency: known minimum **103 Eastern Fleet destroyer assignment-days** through cutoff, with tactical availability lower than calendar assignment for refitting/defective ships.
- Branch-specific canceled Illustrious escort duty: **+12 DD-days local availability credit**, no automatic combat effect.
- Catalina cascade: **63 PG + 36 South Africa + 36 Ceylon-backfill commitment-days** in block.
- Madagascar MD1: **21 troopship-days + 28 escort hull-days + 7 brigade-days** through cutoff, plus open malaria recuperation debt.
- TORCH: FORMIDABLE historical ~42-aircraft slot remains unfilled at center.

### Japanese account
- I-30 lost with 13 dead; Yanagi technology cargo partially compromised.

### Interpretation

Britain has not yet produced a clean Branch-extra merchant rescue or casualty in WIO-6 center, but its defense is now visibly **triage rather than reserve management**:

1. Madagascar releases hulls.
2. Mediterranean/El Alamein immediately absorbs the minesweepers.
3. German U-boats at the Cape absorb destroyers and Catalinas.
4. Persian Gulf still cannot escort roughly half of incoming trade.
5. Japanese I-27 exploits that structural gap and sinks OCEAN VINTAGE despite the gross defensive bill.
6. The modern-carrier deficit cannot be solved inside the theatre and rolls into TORCH.

No theatre is allowed to become safer merely because another one was made thin. Every transfer remains visible in the ledger.

## 14. Open tickets for WIO-7A

Open at **1942-10-25**:

- `EMPIRE_BOWMAN_1942-10-18_OPEN_UPPER_TORPEDO_DUD_DAMAGE_OR_LOSS`
- `HAVFRU_DUD_ATTACK_OPEN_IDENTITY`
- `MARTABAN_REPAIR_AND_RETURN_TO_TRADE_OPEN`
- `MADAGASCAR_29TH_BRIGADE_RECUPERATION_DEBT_OPEN`
- `CAPE_U_BOAT_EMERGENCY_CONTINUES_OPEN`
- `SOUTH_ATLANTIC_DESTROYER_LOANS_CONTINUE_OPEN`
- `TORCH_FORMIDABLE_SLOT_UNFILLED_OPEN_GLOBAL`
- `I30_YANAGI_TECHNOLOGY_LOSS_FUTURE_EFFECT_OPEN`
- `I162_EARLY_NOV_ENGINE_ABORT_NEXT_BLOCK`
- `I166_NOVEMBER_SEVENTH_PATROL_NEXT_BLOCK`
- Preserve v050 Santo/FS authority and prevent double-use of Japanese hulls.

Next hard operational boundary: **25 Oct–20 Nov**, including TORCH on 8 Nov and the Branch FS close on 20 Nov.
