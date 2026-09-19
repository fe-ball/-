# Branch B — WIO-2 Source Reconciliation v001

## Purpose
Keep source disagreements separate from model adjudication. A date/GRT discrepancy is not itself a Branch divergence.

## Merchant-loss normalization

- **Queen Victoria**: South African campaign list uses 4,937 GRT; CombinedFleet I-10 chronology uses 4,957. Working ledger retains **4,937** because the campaign's ten-ship total independently resolves to 50,656 GRT.
- **Goviken**: South African campaign list / RN situation reporting uses **4,854 GRT**; I-20 chronologies commonly give 5,063. Working ledger retains 4,854.
- **Express**: campaign/RN reporting uses **6,736 GRT**; CombinedFleet gives 6,737. Working ledger retains 6,736.
- **Alchiba**: working GRT **4,427**. Some campaign tables place the attack on 1 Jul. CombinedFleet I-10 chronology gives a precise **8 Jul 1755** attack after Hartismere earlier that day; use 8 Jul.
- **Steaua Romana**: working GRT **5,311**. I-20 chronology and campaign tables place the attack on **30 Jun**. Allied situation-report entries are not internally date-consistent; retain 30 Jun as boat-log working date and keep the Allied report-date issue as provenance noise.
- **De Weert**: attack/damage event is **1 Jul**; ship sank **3 Jul**. Charge the loss to WIO-2 and preserve both clocks.

## Failed-attack set
RN 6 Jul situation reporting explicitly lists:

- ROOKLEY — 30 Jun — unsuccessfully attacked / shelled but not sunk.
- DALLINGTON COURT — 30 Jun — torpedo attack failed.
- PHEMIUS — 2 Jul — unsuccessful; Japanese I-18 chronology identifies premature torpedoes.
- AGAPENOR — 6 Jul — unsuccessful; mechanism/boat not securely resolved in the current source set.

Only PHEMIUS presently has a failure mechanism securely matched to the Stage 3A torpedo-reliability improvement. DALLINGTON COURT remains a candidate but not a scored conversion.

## I-18 clock ticket
The retained source attribution gives DE WEERT on 1 Jul and PHEMIUS on 2 Jul. Position/time snippets can imply a demanding transit. Do not discard the source attribution, but do not infer exact I-18 track, speed budget or attack opportunity spacing until the event clocks/positions are reconciled from lower-level records.

Ticket: `I18_DE_WEERT_TO_PHEMIUS_TRANSIT_CLOCK_OPEN`.

## British response source anchors

- Royal Navy War Diary, early July 1942: four unsuccessful attacks; Catalina availability and patrol scheme; shortage of maintenance stores/marine craft; ACTIVE to Comoro Channel; request to send BIRMINGHAM plus six Eastern Fleet destroyers from Aden to Kilindini.
- uboat.net Allied warship chronologies: BIRMINGHAM + NIZAM + NORMAN + INCONSTANT + HOTSPUR + GRIFFIN + FORTUNE departed Aden 1 Jul and arrived Kilindini 8 Jul; DAUNTLESS/ACTIVE Operation THROAT and Mayotte capture; Mauritius/Devonshire movement chronology.
- Naval-History.Net WS convoy chronology: Mauritius relieved Shropshire on WS19 on 18 Jun and was relieved by Devonshire on 26 Jun; Devonshire escorted Bombay-detached ships arriving 1 Jul.
- HMS Ramillies chronology: under repair at Durban throughout July; sailed 6 Aug still without control of main/secondary armament.
- Historical RFA British Loyalty chronology: cargo salvage in June; divers considered refloat possible; ship not raised until Dec 1942, followed by lengthy repair.
- Evert Kleynhans, *The Naval War in South African Waters, 1939–1945*: late-June/early-July ten-merchant loss list and normalized tonnages.
- CombinedFleet Imperial Submarine chronologies for I-10, I-16, I-18, I-20: boat attribution and attack mechanism detail.

## Accounting warning
Historical countermeasures active before a historical loss are already embedded in that loss geometry. They are not a second Branch-only shield. Branch-specific effects require an actual Branch-specific force, timing, readiness or route difference.
