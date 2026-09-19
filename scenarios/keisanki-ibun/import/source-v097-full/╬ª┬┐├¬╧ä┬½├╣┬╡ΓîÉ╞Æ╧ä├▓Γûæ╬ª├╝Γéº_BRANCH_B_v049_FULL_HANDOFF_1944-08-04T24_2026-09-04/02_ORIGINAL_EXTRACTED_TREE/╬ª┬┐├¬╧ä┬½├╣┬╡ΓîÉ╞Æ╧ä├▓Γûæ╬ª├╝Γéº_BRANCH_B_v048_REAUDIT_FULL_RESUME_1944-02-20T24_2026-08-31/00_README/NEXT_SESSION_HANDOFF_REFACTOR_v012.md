# 次回引継ぎ — refactor v012

## 最重要の時刻整理

canonical restart: `CHECKPOINT_1944-04-30T24_v004` = 1944-05-01 00:00。

current global analysis frontier: **1944-07-14 24:00**。Saipan organized defense終了までPacificを確定している。

Chinaについては `CHINA_ICHIGO_ANALOG_1944-05-27_08-06_FORWARD_ADJUDICATION_v001.md` に8/6 Hengyangまでの局地先行裁定があるが、これはglobal current timeではない。Europe/Pacific/production stateを8/6へ自動進行させない。

## 最初に読む

1. `06_RUNTIME/CURRENT_ANALYSIS_FRONTIER_1944SUMMER_v001.json`
2. `06_RUNTIME/MARIANAS_SAIPAN_1944-06-11_07-14_SETTLEMENT_v001.md`
3. `06_RUNTIME/1944SUMMER_JAPAN_US_FORCE_REGENERATION_WORKING_LEDGER_v001.md`
4. `06_RUNTIME/CBI_AIR_LOGISTICS_TAX_1944-04_06_WORKING_SETTLEMENT_v001.md`
5. `06_RUNTIME/CHINA_ICHIGO_ANALOG_1944-05-27_08-06_FORWARD_ADJUDICATION_v001.md`
6. `05_WARTIME/CHECKPOINT_1944-04-30T24_v004.json` and its combat support pointers
7. `06_RUNTIME/WEAPONS_AUDIT_1944-04-30_v001.md`
8. `06_RUNTIME/AIR_COMBAT_RESEARCH_1944SPRING_v001.md`

## 現在の未完了タスク

ユーザーが次に見たいのは **1944-07～10月の月次配備・修理復帰・戦力化台帳**。

必須対象:
- IJN CV/CVL: existing core, Unryu, Amagi, Katsuragi; completion vs work-up vs combat readiness
- BB: Yamato, Musashi, Nagato, Kongo-class repairs
- CA/CL: especially Ibuki heavy-cruiser completion/work-up
- fleet DD: Yūgumo/Akizuki lines and repair returns
- kaibokan/subchaser: convoy-ASW line and its indirect release of fleet DD
- submarine/Kō-class/I-400 readiness and repair
- oilers, repair ships, fleet logistics support
- aircraft: late Zuisei Zero, Kinsei Zero, Raiden, N1K2-J, D4Y/B6N, P1Y, Saiun, Zuiun, Ki-84, Ki-67; production→acceptance→training→allocation→ready
- carrier pilot/crew pipeline and experienced-cadre transfer cost to Unryu/Amagi
- trucks/artillery tractors/recovery vehicles and AFV acceptance/repair return
- US parallel: TF58 air groups, Lee fast-BB repair, CVE/DD/engineers, new hull work-up/transit

Do not use commissioning date as combat-ready date for either side.

## preliminary force-regeneration bands to audit, not blindly inherit

7/14 Japanese:
- main carrier hulls5 intact; Unryu C, Amagi C/D
- carrier-air physical370～430 / carrier-qualified320～370 / first-line integrated280～330
- major fast/heavy BB effective5～6
- heavy cruisers16～17 + Ibuki C
- fleet DD ready43～49

8/15 working:
- Unryu C+～B-, Amagi C+
- carrier-air physical410～470 / qualified350～410 / first-line300～360
- BB ~6
- CA17～18 + Ibuki B
- DD47～53

9/15 working:
- Unryu B, Amagi B-, Katsuragi C
- carrier-air450～520 / qualified390～450 / first-line330～390
- BB6～7
- CA18 + Ibuki B+
- DD49～55

These are conversation-level provisional ranges. Close them from hull-by-hull/month-by-month evidence before using them as final force tables.

## 戦略窓の仮説

- late Jul～early Aug: Japanese surface-action recovery window. Heavy surface units return faster than carrier-air integration while Lee's fast-BB layer still repairs.
- late Aug～mid Sep: likely best combined relative Japanese window if no prior major battle. Existing carrier air materially rebuilt, Unryu/Amagi limited use, Ibuki/DD/BB stronger.
- Oct onward: US damaged units/new hulls and Marianas base network accelerate; B-29 clock becomes increasingly serious.

This does NOT imply Japan should automatically fight. Fleet-in-being itself creates US CAP/search/escort/fuel task load. Yamamoto can choose limited logistics harassment while preserving core fleet, or intervene conditionally if Guam/Tinian creates divided US groups, fuel/rearm windows, weather, thin screens, or other positive-EV contact.

## Saipan settlement reminders

- US operational victory, not historical double victory.
- Japan carrier main force and large part of carrier aviation survive.
- Yamamoto ends main fleet-battle phase 6/18 PM; no historical 6/19 mass carrier suicide.
- US branch irreversible air loss through6/18 center~125; TF58 recovers but not instant.
- Lee fast BB 7→4 immediate effective before repairs.
- Saipan organized defense ends 7/14 24:00; US combat casualty center~20.3k.
- Guam/Tinian dates not yet closed.

## CBI / China reminders

CBI: direct exchange and transport-tax accounting must both be used. A US aircraft destroyed in China can induce India assembly/ferry/Hump/parts/fuel hours; US industry is huge but theater logistics and specialist crews are finite. Japan also pays scarce experienced aircrew and forward aviation consumption.

China: 8/6 Hengyang outcome is a frozen forward local branch. It is valuable as a likely continuation but must not overwrite unprocessed world synchronization. Nanjing has become a materially stronger administrative polity; committed personnel include true believers, anti-Chiang/anti-Communist nationalists, professional administrators, vested interests and double-track actors. Stronger Nanjing improves Japanese rear administration while also growing its autonomous state consciousness.

## 強制的な対称判定

- detection→track→identify→allocate→fire-control acquisition→fire→hit are separate for both sides.
- 15 US carriers are not one perfect organism; TG mission state, fuel, deck cycles, CAP/search/ASW/CAS, fatigue and pilot replacement matter.
- Japanese improvements do not grant magic hit rates, armor, AA immunity or march speed.
- US mass production does not teleport combat-ready crews, ships or aircraft into theater.
- lower casualty strategy has a price somewhere else.
- no local event should silently freeze or auto-advance remote theaters.

## Europe / other-theater skeleton that must be synchronized later

- Overlord: 1944-06-06 five beaches; direct D-Day capability ~100～103 historical; D+8～30 buildup92～98, logistics buffer85～93. Post-D-Day Normandy campaign not yet fully adjudicated.
- Italy: no Anzio; spring offensive breaks Gustav with more orderly German withdrawal; Rome still German 5/31; center fall June15～25 working skeleton.
- Eastern Front: Sevastopol falls ~May10～12; Axis saves a few thousand more; Soviet regeneration debt persists and ~50～55k extra troops remain Far East.
- Burma: Myitkyina airfield capture May20, emergency runway May22, normal-ish airlift May23; Japan avoids historical Imphal disaster and can consolidate Chindwin while North Burma remains under pressure.

## 実行層

v011 combat execution rules remain authoritative:
- load `COMBAT_ADJUDICATION_CONTEXT_v002.md`
- `WEAPON_PLATFORM_CAPABILITY_INDEX_v001.json`
- `COMBAT_PLATFORM_MATRIX_v001.json`
- `NOVEL_WEAPON_ADJUDICATION_POLICY_v001.json`
- FORAGER-type Gate must still review CARRIER / AIRCRAFT / SURFACE_COMBATANT / SUBMARINE
- use `weapon_systems` for branch-original systems
- final combat output requires `combat_resolution_ready=true`

潜水艦と水上艦は通常profile tagから独立して能力候補をレビューする。`weapon_systems` へ未登録分岐兵器を明示すること。
