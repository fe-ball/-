---
title: "計算機異聞 Branch B v096 FULL HANDOFF — 1944-04-30T24:00 技術統合・太平洋/中国同期・地上配置次回ゲート"
version: v096
created: 2026-09-17
status: current-authority-overlay
base_package: v095 FULL HANDOFF 1943-11-24T18:00
current_cutoff: 1944-04-30T24:00
current_theater: GLOBAL / Central Pacific / Marianas-Palau / China / Indian Ocean-CBI
next_frontier: ground force deployment and its strategic/operational effects
---

# READ FIRST — v096

v096はv095フルパケを**全保持**し、2026-09-17セッションで議論・閉鎖した 1943-11-24以後〜1944-04-30 の作業線を現行authority overlayとして上積みする。

このv096では、旧zip内に残るv048〜v094由来の1944年working/legacyファイルを自動的な現行正本とはしない。**v096のCURRENT_AUTHORITYとV096_ADDENDUMに再掲された値だけが現行線**であり、旧1944ファイルは構造・感度・比較参照に限定する。

## 1. 現在の読み順

1. `00_CURRENT_AUTHORITY/00_READ_FIRST_V096_FULL_HANDOFF.md`
2. `00_CURRENT_AUTHORITY/02_SUPERSESSION_MAP_V096_FULL.md`
3. `00_CURRENT_AUTHORITY/CURRENT_BRANCH_B_V096_COMPACT_ACTIVE_CONTEXT_1944-04-30T2400.md`
4. `00_CURRENT_AUTHORITY/CURRENT_BRANCH_B_V096_STATE_1944-04-30T2400.json`
5. `V096_ADDENDUM_2026-09-17/03_SESSION_UPDATES/01_MASTER_TIMELINE_1943-11-24_TO_1944-04-30.md`
6. `V096_ADDENDUM_2026-09-17/03_SESSION_UPDATES/02_PACIFIC_CARRIER_AND_BASE_WAR_SETTLEMENT.md`
7. `V096_ADDENDUM_2026-09-17/03_SESSION_UPDATES/03_CHINA_WEST_AIR_HUMP_ICHIGO_SETTLEMENT.md`
8. `V096_ADDENDUM_2026-09-17/03_SESSION_UPDATES/04_TECH_INTEGRATION_AIR_RADAR_ELECTRONICS_SUBMARINE_1944-02-25.md`
9. `V096_ADDENDUM_2026-09-17/03_SESSION_UPDATES/05_MARIANAS_ARMY_NAVY_JOINT_DEFENSE_DEPLOYMENT_1944-04-30.md`
10. `V096_ADDENDUM_2026-09-17/03_SESSION_UPDATES/06_ALLIED_EXTRA_LOSSES_AND_GLOBAL_PRESSURE_LEDGER_1944-04-30.md`
11. `V096_ADDENDUM_2026-09-17/03_SESSION_UPDATES/07_OPEN_ITEMS_AND_NEXT_SESSION_GATE.md`
12. `V096_ADDENDUM_2026-09-17/03_SESSION_UPDATES/09_GROUND_DEPLOYMENT_NEXT_SESSION_BRIEF.md`

## 2. 現在時刻 1944-04-30 24:00 の中心状態

### 日本第一機動艦隊
- 翔鶴・瑞鶴・飛龍・蒼龍：4艦ともA級第一線、船体健在。
- 四空母航空隊：**280–300機 ready**級。
- 大鳳：1944-03-07就役相当、1944-04末は**B+**。単艦/小編成実戦可だが、四空母核心と完全同格になるのは5月共同演習後が中心。
- 五空母の物理航空系：**331–368機 mission-ready**級。戦闘機155–175、D4Y 78–92、B6N 72–86、その他15–25の作業帯。
- 大鳳のB7A流星：**8–14 ready**級の高価値sub-cell。D4Y/B6N主力を置換しない。
- 艦隊はTruk/Palau固定基地から切り離し、South Philippines〜Tawi-Tawi方面を中心に運用・訓練。基地を守るために主力空母を固定しない。

### Marianas共同防空
- 海軍航空ready：旧監査基準で96–120機級。そのうち戦闘機58–74。
- 現行枝で追加：飛行第59戦隊 Ki-44-II **24–28 ready**、飛行第11戦隊 Ki-84 **22–27 ready**。
- 1944-04下旬の戦闘機総ready：**104–129**、地域航空総ready：**142–175**、中心約155。
- Saipan/Tinianは海軍センサー・作図網を陸軍/海軍戦闘機が共用する共同防空正面。
- 海軍plot→陸軍連絡班→陸軍地上無線→戦隊のI/O遅延は3月訓練で中心1.5–3分級まで短縮。

### Marianas地上装甲
- 第9戦車連隊：物理81両をMarianasへ移送。
- Saipan：中心53両（新砲塔チハ20 / 旧砲塔チハ18 / 九五式15）、combat-ready **42–49**。
- Guam：中心28両（新砲塔7 / 旧砲塔3 / 九五式18）、combat-ready **20–26**。
- Chi-He / Chi-Nu相当 / Ho-Niを自動追加しない。
- 戦車は一斉突撃ではなく、1–3両/3–6両級の掩蔽・側射・局地予備cellとして運用する。

### Palau
- 3/30–31 DESECRATE ONE後、基地航空は大損害を受けたが主力4空母は不在で生存。
- 日本航空損失55–68不可逆、米艦載機23–30不可逆の作業帯。
- 商船/補助艦7–10沈没級、8–13損傷級。大型油槽船の大半と工作艦明石は事前退避成功中心。
- 第14師団：**4/18までにPalau到着**を現行線とする。陸海軍混成の要塞正面化。
- Palauの戦車の正確な両数・Peleliu/Babeldaob等への配分はOPEN。

### Truk
- 2/17–18 HAILSTONE前に主力艦隊と高価値補助艦の相当部分を退避。
- Branch HAILSTONE：米不可逆28–36機、日本100–125機、輸送/補助艦10–14沈没級＋10–18損傷、燃料6–9千t級喪失。主力戦闘艦は退避。
- 以後Trukは艦隊泊地から、**ISR / 潜水艦 / 航空中継 / 補修 / 通信**基地へ格下げ。

### Marshall / FLINTLOCK
- 1/30、日本4空母は米上陸支援systemへ125–135機級の一撃。日本35–43機不可逆。
- 米側：APA1 sunk/CTL、LST級1沈没、APA2隻中〜大破、CVE1 heavy mission-kill、旧式BB1隻一時任務低下、米戦闘機10–15不可逆の中心線。
- Kwajalein/Roi-Namur：Attu→Tarawaの戦訓を反映した分散・代替C2・小規模夜間浸透。戦車増殖は無し。
- Branch Kwajalein/Roi主戦闘：米casualty約1,950–2,450、死亡/MIA390–480級。Kwajalein本島組織抵抗は2/4午後〜夕刻中心。
- Eniwetok：守備3,900–4,300級、米casualty1,450–1,800、死亡/MIA330–420、Parryまで2/24夕〜25未明中心で終了。

### China west / Hump / Ichi-Go
- Five-Go後、成都深追いはせず、Hanzhong–Guangyuanをactive pressure frontとして維持。
- 飛行第22戦隊Ki-84は漢中主配置・広元前進運用を維持。第59/11戦隊のMarianas移動で西部を空洞化しない。
- 1944-04-25相当の西部航空：物理90–115、通常即応68–86。戦闘機38–48、Ki-45 6–8、Ki-48/Ki-51 14–18、偵察6–9級。
- 西部地上：**2.3–2.8個師団相当 / 45–58k級**を維持し、中国側5–7有効師団相当を固定。
- 西部航空圧力による米中側の高優先物流税は春に**450–700t/月**級。航空燃料・防空飛行・分散260–420t、部品等90–150t、その他修理/AA/通信。
- 一号相当：湖南へ新規10–12個師団を中心、四川追撃なし。西部2–3個師団相当と合わせ、実質12–15個師団級の二軸圧力。
- 1944-04末は物理集積・鉄道輸送・工兵/渡河材・車両/砲弾stockpile段階。

### 潜水艦 / Penang / ASW
- Penang/Sabangは「潜水艦基地」だけでなく、日独の比較試験・技術中継・運用標準化拠点。
- I-8/U-511→RO-500等の経験から、通信短文化、哨戒区deconfliction、トリム再計算、静粛化後再聴音、故障/電池/機関統計が横展開。
- cm波警戒はなお弱点。Schnorchel標準化なし。ドイツ由来電気魚雷は比較試験であり九五式の一律代替ではない。
- 潜高：4月末**6隻実戦**、7–8隻目は戦力化境界。
- 伊400：単艦戦闘readyだが温存。伊401は4月就役、5–6月ready gate。
- MAD対応航空：25–40機、3–5個分遣隊級。広域探索→datum→MAD局地確認→攻撃→shore handoffを制度化。

## 3. 1944-02-25 技術統合状態

- 新兵器の早期投入より、既存装備の**I/O統合**がBranch差の本体。
- 電探の物理探知距離差は史実比+5–15%級。性能ばらつき30–40%減、初期稼働率相対+15–25%、校正誤差30–50%減。
- 1943–44第二世代では、複数観測の平滑化、距離変化率、異常値排除、目標番号管理、レーダー距離＋光学方位融合が実用化。
- 米SG/CIC、fighter direction、5in/38＋VTの総合優位は維持。日本は一群の迎撃・再捕捉・引継ぎを大きく改善するが、多数raid連続管理はなお劣る。
- 大型艦電子系は主射撃盤を置換せず、気象・初速・砲身摩耗・弾薬ロット等の残差補正、戦術作図、電探I/Oを担当。
- 大鳳は建造時から1943–44型電源/配線/作図/CAP指揮を統合できる最初の空母だが、艦隊統合訓練時計は省略しない。
- 写真/ISRは撮影間隔・重複率・接合・座標化・前回比較が成熟。高価値物資の増減を追う。
- COMSECは内容復元を遅らせるが、traffic analysis / HFDF / reconnaissanceは残る。

## 4. Allied追加損失・拘束の要点（1944-04-30まで）

### Branch固有の大損失
- RN：Indomitable / Formidable 永久喪失。
- USN：Enterprise / Hornet / Saratoga 永久喪失（ただしWaspは史実損失を回避して生存）。
- Port Moresby / Midway / Santo / New Caledonia主要部をBranch特有の形で喪失。
- Five-Go：中国軍107–137k戦闘損失。
- GALVANIC以後：Essex/Belleau Wood/Lexington等の長期mission-kill、amphibious shipping追加損害。

### 恒常的なAllocation / Flow tax
- Indian Ocean 1942-09〜1943-11 Branch-only追加：商船20–55k GRT沈没＋10–25k GRT長期修理、36–65 ship-months、37–64 escort/ASW hull-months、6–12 patrol squadron-months、7–13 heavy-unit-months。
- Hump/China：春時点450–700t/月の高優先物流税。西部に戦闘機50–70 ready級＋補充/ferry 35–50級を継続拘束。
- Oceania：日本がSanto/New Caledonia/Port Moresbyを保持するため、Fiji/Tonga/NZ/Australiaが史実ほど完全な後方地域にならず、戦闘機・哨戒・工兵・沿岸防備・輸送予備を貼り付ける。
- Indian Ocean：U-Go深部侵攻はないため英印軍の戦闘損耗は減るが、健康な日本印度洋systemによりIndia/Burma/Ceylon/Bengal/Persian-routeの広域拘束は維持。
- Europe/Soviet波及は「援助崩壊」ではなく、同じ欧州圧力を維持するためのescort rotation圧縮、strategic reserve erosion、Lend-Lease delivery delay、人的/装備予備の追加消費として扱う。

## 5. Branch mixing guard

- v095内の古い1944年working FLINTLOCK / Marianas / initial setupファイルは、**構造・感度参照のみ**。日付・戦果・OOBを自動継承しない。
- 特に旧 `Army fighter allocation 0 in Marianas` は現行枝で**撤回**。第59戦隊Ki-44、第11戦隊Ki-84の共同防空投入がcurrent。
- 旧Soryu損傷/修理線は使用しない。現行会話線では11/21後の4空母は船体健在で推移。
- 旧FLINTLOCK D-Day 2/6等は使用しない。現行線は1/31上陸。
- 旧HAILSTONE/Palau戦果はcurrent会話線の再演算値で上書き。
- 未来装備の前借り禁止：烈風、Ki-67本格実戦、Ki-100、ジェット等を4月末の通常戦力へ数えない。

## 6. 次の再開点 — 地上の配置とその影響

次チャットの主論点は**「1944-04-30時点の地上兵力配置と、それが連合側/枢軸側の戦略予備・作戦選択へ与える影響」**。

優先順：
1. Marianas：31軍、各師団/旅団、Saipan/Tinian/Guam/Rota/Paganの実配置、工兵/砲兵/戦車/海軍根拠地隊、地下化工事進捗。
2. Palau：第14師団、海軍根拠地隊、Peleliu/Babeldaob/Angaur等の配分、戦車数、飛行場・港湾・地下化。
3. Truk/Ponape/Kusaie：海軍/陸軍守備、航空/潜水艦/補修機能と地上防御の役割分担。
4. China：湖南一号投入10–12師団＋漢中/広元2.3–2.8師団相当の同時配置、守備代替、南京政府部隊、戦区別拘束。
5. Burma/India/Indian Ocean：U-Goなしでも健康な日本印度洋systemが英印陸海空軍をどこまで拘束するか。
6. Oceania：Port Moresby / Santo / New Caledonia保持がFiji/Tonga/NZ/Australiaのfree strategic reserveをどこまで削るか。
7. これらを統合し、1944年春の**Free Strategic Reserve ledger**を米陸軍、英印軍、RN、USN、商船、輸送航空で作る。

ここを閉じるまで、Marianas本戦・一号発動・欧州追加死傷の最終数値化は進めない。
