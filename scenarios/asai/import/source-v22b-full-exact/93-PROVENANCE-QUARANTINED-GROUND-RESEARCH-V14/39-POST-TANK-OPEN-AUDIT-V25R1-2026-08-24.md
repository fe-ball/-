# 計算機統合後の未更新・未決着監査 — semantic v25 / machine v25r1 / 2026-08-24

## 判定原則

v4の計算機統合以後に書かれた「次P0」「OPEN」「要確認」を、その後のv5–v24で実際に閉じたか再照合した。旧文書のOPEN表記をそのまま現行OPENへ足さず、後続正本で解決済みならCLOSED、技術成立は閉じたが個別値だけ残るものはP2、現行正準がなおA_old/再I待ちならP1として残す。

## P1 — 現在も意味のある未更新・未決着

1. **E6凱風Iと艦戦ロスター再生成**。`aviation-lineup` / `aviation-timeline` / `turboprop-fighter` はE5一一型をA_oldへ降格したが、E6本格凱風のH/C/M/E/P/I/Aをまだ閉じていない。旧一一/二一/三一年次・性能を現行ロスター/OOBの根拠にしない。
2. **史実基準機H→Aの続行**。零戦A0/A6M2/A6M3とF4F基準は再基底化済みだが、`historical-aircraft-rebaseline` が次段に置く陸軍軽戦/重戦（隼、鍾馗等）と、その後の敵側要求変更は未実走。旧「1941ピストン10機」はretrofit比較表であり、個別のcurrent Aへ順次置換する。
3. **TP完成機の個別I**。Ki-40、天山、銀河等は系列・帯があるが、機体別の重量内訳、高度別installed power、prop/gear、搭載、航続、冷却/吸排気まで同じ粒度では閉じていない。`turboprop-program` 自身もKi-40または天山の一段詰めを次作業として残す。
4. **深山/連山の生産・装備統合**。v24でpart-load/航続は修正済みだが、四発量産の治工具・熟練、生産規模、減速ギヤ×4の実重量/信頼性、防御配置、与圧重量、給油練度は未確定。
5. **回転翼1942+**。開戦前カ号/小型ヘリは閉じたが、中型レ号系中型回転翼機一型、艦上係止/格納、戦時ASW/救難運用は1942年以後の未監査枝。
6. **radio/radar reliability**。原理早期化でなく、真空管、ferrite、epoxy sealing、電源、耐振動、EMI、QC、艦上/航空機搭載の稼働率をAsai chainとして詰める論点が残る。
7. **mine / sweeping**。非磁性GFRP、磁気/電気 sensing、掃海器、艦艇側電装との交差を未監査。
8. **survey / artillery meteorology / firing tables**。計算サービスが測地・気象・射表生成と野戦運用にどこまで効くか未監査。
9. **大型艦13号diesel・大鯨系の別EH→EA、水上艦船型/高速艇の計算文化込み再監査**。旧v23 P1から後続v24で明示閉鎖されていない。
10. **潜水艦の生産会計と任意次世代主機**。battery/motor/yard年産、1,550t/1,850t shadow branches、最初から過給統合した次世代2-cycle主機は詳細OPEN。12/15kt線の成立条件ではない。
11. **戦車1942+の実開発史**。v25で75mm砲塔中戦車の技術成立shadowは閉鎖した。残るのは、敵情・戦訓・政策から実際に研究発注/要求確定/制式化/量産へ進む時期と仕様であり、**DEVELOPMENT-HISTORY CONDITIONAL OPEN**。shadow諸元をcurrent実在車として使わない。
12. **E8/E9+ later-war propulsion**。TIT940 cooling blade、Ni tail、E9+ postwar edgeは後期要求が発生した時点で再監査。

## P2 — 成立は閉じたが数値/実装を締めていない

- E5/E6/E7 compressor map実曲線、rpm/PR/bleed/IGV点、restart MTBF。
- 個別propeller径、rpm、tip Mach、gear ratio、negative-torque/feather/restart寿命。
- 専用計算器の部品点数、重量、MTBF、I/O誤差、量産数。
- optics各社の計算外注量、glass/grinding/inspection capacity、個別照準器/測距器。
- seaplane/flying boatのwet-exposure coupon、repair man-hours、slam fatigue。
- heavy Daihatsuの線図、ramp、浜条件別離岸、母船layout。
- Type 91の型別response surface、production tolerance、照準補助器の誤差帳簿。
- Chi-Ha/Chi-Heの実gear ratio、cooling airflow、turret motor rating、periscope exact optics。
- rotorcraftの主減速機寿命、ground resonance対策、艦上係止/格納詳細。

## HISTORY/OOB — 意図的に未決着

1941-12-08以後の航空隊/艦隊/陸軍OOB、機種比率、配備数、戦果・損耗、敵反応、雷撃/急降下命中率、水上航空基地配置、潜水艦作戦/損失/ASW、上陸実戦摩擦、戦車部隊戦果/教範成熟は技術正本から分離したまま。歴史を再開する際に技術P1を必要分だけ呼び戻す。

## CLOSEDと再確認した旧OPEN

専用/現場計算器の成立帯、射撃/光学、seaplane/flying boat、水陸両用system、Seiran/I-400残件、潜水艦quieting/trim/battery計算、E6/E7 part-load、Type 93/95/91/航空雷撃、Chi-Ha→Chi-Heはv24で技術P0閉鎖済み。v25で1939–45次期中戦車の条件付き技術shadowも閉鎖した（実開発史は未確定）。旧v23 P0-A〜Fを現行OPENへ重複登録しない。
