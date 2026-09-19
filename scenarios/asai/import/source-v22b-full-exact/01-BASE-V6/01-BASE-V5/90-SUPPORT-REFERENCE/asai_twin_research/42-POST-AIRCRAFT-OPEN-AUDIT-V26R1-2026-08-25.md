# 航空再基底化後の未決着監査 — semantic v26 / machine v26r1 / 2026-08-25

## P0 — top-level blockers

**なし。** 航空の能力ロスター/主要機体技術帯はv26で再基底化済み。戦史再開前に全航空機をさらに一律再監査する必要はない。

## P1 — current technical work still worth doing

1. **史実基準戦闘機H→Aの続行**：隼・鍾馗等と敵側反応。攻撃/爆撃系はv26で別途閉鎖した。
2. **回転翼1942+**：中型レ号系、艦上係止/格納、ASW/救難。
3. **radio/radar reliability**：真空管、ferrite、epoxy sealing、電源、耐振動、EMI、QC、航空機/艦上稼働率。
4. **mine/sweeping**。
5. **survey/artillery meteorology/firing tables**。
6. **大型艦13号diesel・大鯨系別EH→EA、水上艦船型/高速艇の計算文化込み再監査**。
7. **潜水艦生産会計と任意次世代主機**。
8. **戦車1942+実開発史**：技術shadowはv25でclosed。
9. **E8/E9+ later-war propulsion**：要求が発生した場合。富嶽E8-Lは本稿のconditional aviation exceptionで、E9+一般技術を先取りしない。

## P2 — quantitative detail

- E5/E6/E7/E8 compressor maps, rpm/PR/bleed/IGV, restart MTBF。
- aircraft-specific prop diameter/rpm/tip Mach/gear ratio/negative-torque/feather life。
- **Fugaku 5,000shp reducer life and 5m prop hub/blade endurance**。
- **R2Y2 E6-L-J/JF installed mass and altitude thrust map**。
- **Ki-102 late armament optimization**。
- dedicated computer component count/weight/MTBF/I/O error/production quantity。
- optics production and exact sight/rangefinder details。
- wet-aircraft exposure/repair/slam fatigue。
- Type 91 response surfaces/tolerance。
- rotorcraft transmission/ground resonance/shipboard outfit。

## CONDITIONAL development/history gates

- AT-3/Ki-92: whether 1939 concept actually receives Nakajima/Army/government funding; prototype date; 4–6 first lot; 8–12 operational group.
- Fugaku: whether Project Z receives joint green-light; E7-L flight test timing; first prototype; 24/36-aircraft procurement; dedicated bases and actual missions.
- Kikka: only if a cheap/simple 500kg jet strike requirement opens.
- Ki-201: independent production only if Army organizational requirements outweigh Hekireki commonality.
- Tenka/new jet bomber: only if a later 2–3t / ~1,000km high-speed strike requirement opens.

## FROZEN history/OOB

1941-12-08以後の航空隊/艦隊/陸軍OOB、機種比率、実生産、配備、空襲/雷撃/急降下命中率、損耗、敵反応、富嶽/大型輸送の作戦使用は技術正本から分離したまま。

## Closed/rebased by v26

- E6 Kaifu role split.
- Ki-40 altitude-power/range correction.
- B6N/B7A/P1Y historical-role restoration and E6 selection.
- G5N/G8N/AT-3/Fugaku architecture separation.
- Sakufu speed/approach/catapult rebaseline.
- Army/Navy attack-bomber role map.
- jet strike branch deletion/selection through R2Y2.
- Fugaku technical envelope through propulsion, wing/gear/base, defense, crew and force-size design shadow.
