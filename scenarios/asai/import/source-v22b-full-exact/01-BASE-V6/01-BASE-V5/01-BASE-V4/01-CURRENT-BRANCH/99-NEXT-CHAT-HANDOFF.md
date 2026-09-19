# NEXT CHAT HANDOFF — 浅井世界線 / 1937-07-27

## 現在位置

- current branch time: **1937-07-27 ~04:30**
- latest CLOSED gate: `35-1937-07-26-27-GUANGANMEN-CONVOY-DELAY-GATE.md`
- next OPEN gate: **Q-035 — 1937-07-27 daytime → 1937-07-28 attack opening**
- next task: 最後通牒、撤兵期限、居留民退避、北支駐屯軍の攻撃部署、28日の南苑/西苑等への攻撃開始をevent-by-eventで監査する。

## 広安門gateの確定点

- 歩兵第2聯隊第2大隊系の最終移動は豊台から**26台truck**。
- 16:00頃の通過予定に対し、主力は1時間以上遅れた。
- source wordingは道路上の低速/故障ではなく **「豊台出発が遅れた」**。よって浅井turbo/heavy-vehicle reliabilityでは遅延を自動消去しない。
- 16:00頃に先遣側は一度開門許可を得ているため、定刻到着なら事件sequenceが変わった可能性は実在する。ただしcurrent branchではpremise不足なのでcounterfactual sensitivityのみ。
- 17:40頃再開門命令、18:20頃入門開始、門閉鎖と分断戦闘はCLOSED-SAME。
- first fire時に何台入っていたかはsource-sensitive。exact ordinalはOPEN-detail。
- 22:20頃、日本側は断片情報から翌27日正午攻撃命令を出す。
- 27日04:30頃、より完全な情報、松井介入、28日正午までの最後通牒、居留民退避未完等から攻撃開始を一時延期。

## 次gateで必ず監査する浅井差

1. **motorized readiness**
   - 浅井系重車両/砲牽引車は全軍置換ではない。
   - ただし増援部隊の重貨物車、砲牽引、整備ready fractionは史実より良い。
   - 28日以降の本格作戦では、同じ編制でも落伍率・砲の到着状態・補給tempoへ差が出始める可能性がある。

2. **砲兵計算体系**
   - 1937年時点ですでに計算、射表、測地、観測修正、射撃諸元処理、QCが史実より成熟。
   - 7/20の宛平砲撃は威嚇・懲罰目的が強く、任務目的が効果上限だったため大戦果化しなかった。
   - 本格的準備砲撃、対砲兵、集中射、射撃転移ではminor扱いせず再評価する。

3. **航空**
   - 日本史実機は1937夏までheadline性能は概ね史実。浅井計算導入で故障整理、耐久、冷却、整備、図面/QCが改善。
   - mass aviation GTはまだゼロ。E4/E5は評価機/少数実証。
   - したがって28日の航空支援は「ジェット化」せず、史実航空隊のserviceability/maintenance marginの差として扱う。

4. **通信/電源**
   - 浅井は電源、切替、印字、記録、保守を改善するが、1937年にportable-radio revolutionはない。
   - 中国側内部の命令未達、semantic mismatch、物理的電線sabotageを魔法の通信網で消さない。

5. **特殊鋼/工具/材料**
   - 「浅井鋼で全部強化」は禁止。
   - W-HSS/carbideは主に加工能力、耐熱鋼は排気弁/ターボhot side、Ni-Cr-W/Ni-Cr-Mo等は軸/歯車/疲労信頼性。
   - 実戦では製造安定、故障率、部品寿命、ready fractionに効く。史実にないpeak性能を無条件に足さない。

6. **U/W dense-core ammo**
   - 1937は少数の特殊徹甲弾。装甲目標がない局面には出さない。
   - modern DU U-Ti self-sharpeningを自然Uへ自動付与しない。
   - 37mm等の具体貫徹mmはQ-016 OPENのまま。

## historical-simulation rule

**条件が同じなら偶発的な出来事も起こるが、違えば起きない。**

史実eventを「史実だから」自動再生しない。各事件で、そのeventを生んだ局地条件がcurrent branchで同じかを確認する。浅井本人はエスカレーションを政治的に止めに行かないため、本人の介入で盧溝橋以後を分岐させない。

## 1937夏の浅井生産・軍需の重要anchor

- GT core actual ~125/年、hidden reserve ~280–320、1936–38 intentional overbuild完成 ~500–600、mobilization ~800–950。
- exhaust turbo actual ~1300 cores/年、hidden ~2000–2200、overbuild ~2800–3200、mobilization ~4000–4500。
- military exhaust turbo ~325–465/年、中央値~400。
- Army heavy-vehicle turbo new ~250–330/年 + spare 40–70。
- military GT ~30–60 cores/年。fixed E4 emergency GT ~15–25 new + spare 5–10。small GT mobile power vehicle ~5–12/年。
- aviation mass-production GT = 0。後のE5純jet/後置fan pitch用にcore factory overbuildが存在。

## 1937-07-07→27の因果上の重要な閉鎖

- 盧溝橋事件発生自体は同じ。
- 7/8–10の初期衝突・撤退交渉・竜王廟再戦も同じ。浅井通信で中国側内部の命令未達を直せない。
- 7/10竜王廟では撤収命令は届いており、牟田口が独断攻撃。通信改善で止まらない。
- 7/11現地和平と中央派兵準備が並走。浅井兵站は派兵decisionを変えず、実行readyを少し上げる。
- 7/14以降、浅井車両差は増援部隊のready fractionとして実盤面に乗るが、到着時刻を証拠なく前倒ししない。
- 7/20砲戦は浅井砲兵計算能力が既に成長しているが、威嚇/懲罰性の強い限定砲戦なので大戦果化しない。
- 7/21–24は第37師撤退、鉄道移送、協定実施細目のsemantic mismatch。浅井通信で解けない。
- 7/25廊坊事件は意図的な電線切断、access/security frictionが律速。浅井電機でも修理隊派遣と夜間衝突を消さない。
- 7/26広安門事件は車列の「豊台出発遅延」が律速。車両性能差で自動分岐させない。

## 作業規則

- 一つのevent/claimを閉じたら `03-CURRENT-BRANCH-INDEX.tsv`, relevant history/ledger, `06-CONFLICT-AND-REVIEW-QUEUE.tsv`, `07-SESSION-DELTA`, gate fileを更新。
- TSV width、duplicate IDs、local refs、manifest SHA256、ZIP CRCを機械監査する。
- 同名でも意味が変われば別claim record。old canonを黙って上書きしない。
- フルZIPの再構築は毎gate必須ではない。ユーザーが要求した時、またはhandoff時に行う。
