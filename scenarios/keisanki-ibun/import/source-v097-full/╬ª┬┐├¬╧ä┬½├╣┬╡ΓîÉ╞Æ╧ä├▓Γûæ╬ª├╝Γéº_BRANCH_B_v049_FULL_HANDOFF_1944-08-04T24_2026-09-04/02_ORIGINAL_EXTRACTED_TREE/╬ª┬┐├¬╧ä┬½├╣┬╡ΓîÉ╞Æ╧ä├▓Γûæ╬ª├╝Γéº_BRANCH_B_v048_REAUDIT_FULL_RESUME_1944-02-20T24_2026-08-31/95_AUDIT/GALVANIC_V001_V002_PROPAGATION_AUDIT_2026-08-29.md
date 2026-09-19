# GALVANIC v001 -> v002 propagation audit — 2026-08-29

status: FINAL_PROPAGATION_AUDIT

This audit records the authoritative deltas introduced by the full sortie-to-closeout re-audit and where they are propagated.

| Topic | old v001 / retained assumption | final v002 current state | downstream consequence |
|---|---|---|---|
| Nauru | omitted from reopened tactical sequence | Wasp + Princeton suppress Nauru 11/23; useful lower-priority damage sink; limited night staging recovers by early Dec | US sorties are split; Japanese multi-TG recognition improves; no free Marshall-wide US suppression |
| First carrier hit | Independence hit later | Independence torpedoed D-1 evening 11/23 | US vigilance rises before D-Day; historical Liscome Bay D+4 geometry is broken |
| Liscome Bay | sunk | survives | CVE support remains intact at Makin; later US CVE wallet increases |
| Cowpens | campaign-out | operational | US light-deck wallet is materially better than old settlement |
| Lexington CV-16 | temporary/light-moderate damage | torpedo + 1-2 bombs on 11/26; major mission-kill/repair into Mar-1944 band | US fast-carrier strength at 1944-01-01 is lower than old settlement |
| Yorktown CV-10 | not material | one bomb/near-miss; limited ops next day, near-normal ~11/29 | short-lived deck-cycle debt only |
| Soryu | fully operational survivor | two bombs, mission-kill, survives; Truk/home-yard repair; unavailable at year-end | Japanese first-line operational core at 1944-01-01 is Shokaku/Zuikaku/Hiryu, not four |
| Two-way carrier battle | Japanese one-way strike, no material US counterstrike | real 11/26 two-way carrier battle | both sides gain equal-carrier battle experience; Japanese experienced strike-cadre debt is explicit |
| Kinsei Zero | effectively absent through late Nov | 18-22 carrier-ready, center 20 on 11/26 | modestly improves Japanese escort/CAP; forces mixed Kinsei/Zuisei after-action doctrine |
| Japanese air losses | old 28-34 for 115-aircraft strike | ~60-75 irrecoverable across full carrier battle | still much thicker than historical late-1943 Japan, but strike leadership/navigation losses bind |
| US air losses | minor | ~40-50 irrecoverable | material but recoverable under superior US replacement/rescue depth |
| Tarawa defender quality | 4,500-4,700 combat | 2,600-2,900 first-line + 700-1,000 limited armed support | prevents construction/labor personnel from being treated as SNLF infantry |
| Tarawa landing | historical-like reef problem | 11/24 tide is independently resolved; later LCVP/LCM use measured lanes during high-water window | first wave harsh, later logistics much better; final US casualties ~1,900-2,300 |
| Japanese first-night ground reaction | limited/old sequence | organized 350-450-man + 3-4 Type 95 counterattack, then infiltration | real first-night pressure but mobile reserve is spent |
| Early surface raid | 11/23-24 nuisance raid possible | removed for lack of forward named hulls | no unit spawning from total fleet inventory |
| Actual surface raid | unnamed/later unclear | Hatsuzuki/Suzutsuki/Hamakaze/Fujinami, 11/26-27 stand-off Type-93 raid | Franks DD-554 sunk; Fujinami damaged; no prolonged SG gun battle |
| Submarine high-value hit | Liscome Bay / later oiler | I-175 misses D-Day CVE opportunity; torpedoes Pierce APA-50 on 11/27 and is damaged | no automatic CVE/oiler kill; named repair clocks close |
| 12/4 Kwajalein raid | historical mass raid broadly reusable | mass Kwajalein/Roi strike not realized; limited outer-Marshall raid/recon under strong cover | surviving Japanese carrier fleet-in-being constrains US attack allocation |
| Secondary Japanese carriers | easy to omit | Junyo/Hiyo/Ryujo/Zuiho explicit rear-deck/cross-deck/regeneration pool | Soryu orphan aircraft and post-battle deck congestion can be absorbed without inventing fresh crews |

Current propagation files:
- `06_RUNTIME/GALVANIC_BRANCH_B_1943-11_SETTLEMENT_v002.md`
- `06_RUNTIME/GALVANIC_FINAL_OUTCOME_LEDGER_1943-11_12_v001.json`
- `06_RUNTIME/GALVANIC_DAMAGE_REPAIR_REGEN_LEDGER_1943-11_1944Q1_v001.json`
- `06_RUNTIME/GALVANIC_AIRCRAFT_AFTER_ACTION_LESSONS_1943-12_v001.md`
- `06_RUNTIME/BRANCH_B_1943H2_YEAR_END_SETTLEMENT_v002.md`
- `05_WARTIME/CHECKPOINT_1943-12-31T24_BRANCH_B_v003.json`
- `06_RUNTIME/BRANCH_B_YEAR_END_GUARD_1944-01-01_v002.json`
- `00_CONFIG/current_branch_overrides_v011.json`

Retained v001 files are not deleted. Their authority is explicitly superseded so provenance is preserved without allowing old results to leak back into runtime.
