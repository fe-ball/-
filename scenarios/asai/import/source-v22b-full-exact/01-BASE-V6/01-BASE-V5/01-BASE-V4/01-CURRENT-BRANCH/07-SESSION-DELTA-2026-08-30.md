# Session delta — 2026-08-30

Status: current conversational overlay. semantic v49ではないが、次の再構築ではlate-8/29 overlayより新しい。

## 1. 海軍GT実験船

CLOSED寄り：
- 横須賀海軍工廠所属の**雑役船（雑種船）**。
- 用途呼称：機関実験船。
- 固有船名なし。公称番号船。
- working designation：**公称第4017号**。ただし史実台帳との完全crosswalkまでは番号そのものを最終確定しない。
- schedule：1938要求、1939設計/発注、1940進水/艤装、1941本格試験。
- 700–900t基準、2軸、初期2×E6-M合計約4,000–4,400hp、safe-return diesel。

## 2. 回転翼研究 — 1937夏で第一幕CLOSE

- 1932後半：予備検討。
- **1933：浅井が自社で正式研究着手。** 萱場を成立条件にしない。
- 初期飛行用baseline：Siemens-Halske Sh 14A 160hpを少数購入。ライセンス量産はしない。
- 1934：縮尺/実寸rotor・hub・transmission試験。
- 1935：拘束浮揚・短いhop。
- 1936：自由飛行到達。
- 1935頃からガソリンターボ研究軸を母体に浅井製180–200hp級航空ガソリン機関を並行開発。
- 1937前半～夏：浅井機関搭載試作機で操縦、autorotation、rotor head、main reducer、振動、耐久を反復。
- 萱場：史実寄り独自回転翼研究を維持し、浅井成果を知って接触し得る。固定分業は解除。
- **1937夏以後のE5/E6大型ヘリ、軍用採用、輸送ヘリは見込み扱い。**

## 3. 1937夏までの史実航空への波及

- 既存史実機を一律性能向上させない。
- 主差は三菱・中島の発動機計算/試験文化、過給・冷却・振動・propeller matching、failure-loop短縮。
- A5M/G3M/Ki-15/Ki-27等は基本史実諸元を維持しやすい。
- 1937以後に要求される機体から、更新されたレシプロガソリン能力を設計入力として使う。

## 4. 植物FRP / 小型TP汎用機

資料系譜：
- pre-v48にはSTOL汎用機と材一号A/B構体試験が別機として存在。
- pre-naval 8/29 overlayには「**材一号系は少量販売域**」が残る。
- v48材料authorityは1937夏までの植物繊維FRP部分構造の成立を許すが、旧航空採用史はarchive化。

現在の扱い：
- **植物FRPを部分使用した実用寄り小型TP機系列が1937夏までに外部評価／少量販売域へ来ている、という歴史枝を救済する方向。**
- ただし「旧STOL汎用連絡機2.8t/E5 1000hp完成形」や「材一号という正式な同一機」を1937夏へ自動前倒ししない。
- exact機体構成、販売数、名称、STOL系列との同一性は再監査対象。

## 5. 1937夏のタービン生産 — WORKING数量

現時点の実需積み上げ第一案：
- GT core実生産：約125 cores/year。
- 排気ターボ完成core：約1,300 cores/year。

設備余力第一案：
- 通常一交代能力：GT E4/E5級約270–320 cores/year、turbo約2,000–2,200/year。
- 二交代混成：GT約350–400/yearを出しつつturbo約1,700–1,900/year。
- 航空最優先への転換上限：E5級GT約500–600/year級。
- 1938第二工場完成時のGT受入設備：700–900/year級。

これらは**まだWORKING**であり、設備表・人員・工作機械・材料負荷の監査後にCLOSEする。

## 6. 工場共通性 — WORKING

- ターボ↔GTは部品共通率より**設備・技能共通率**が高い。
- 高速回転体、熱処理、研削、動釣合、探傷、測定、品質管理、軸受等を共有。
- GT固有：多段compressor、combustor、多段hot turbine等。
- pure jetは航空用主減速機・大径propeller系を要求しないため、1937以後の航空発動機飢餓に対し「既存pistonラインと競合しにくい追加生産能力」として売り込める。
- 「jetはgearが全くない」ではなく、**propeller用main reduction gearが不要**という意味。

## 軍需再走査：移動電源車をcurrent branchへ追加
- 旧 `asai-works-gt-apu.md` に存在した「基地移動電源」を、1937年夏までに少数実用化・軍評価/限定納入済みとしてcurrent branchへ昇格。
- 中央はAPU/小GT系の道路用移動電源車（数十～100数十kWe級）。E4 500kW級は固定式が本体で、大型可搬/牽引版は極少数特殊枝。
- 1937夏軍需を再走査し、`08-MILITARY-DELIVERY-LEDGER-1937-SUMMER.md` / `09-MILITARY-DELIVERY-LEDGER-1937-SUMMER.tsv` を追加。
- 軍需完成GTのworking年率は、固定式非常電源・移動電源・試験納入を合わせ約30–60コア/年。排気ターボ軍需は約325–465基/年を監査候補とする。いずれも旧資料の確定数量ではなくcurrent working estimate。


## 兵器影響台帳 — 1937夏
- `10-WEAPON-IMPACT-LEDGER-1937-SUMMER.md/.tsv` を追加。九四・九五・九六式の実配備層と、九七式の試作/前生産層を分離。
- 九七式チハはcurrent branch 180PS常用/200PS最大、1937夏は量産準備。旧200/220PSはSUPERSEDED。
- HIGH監査：九六式軽機関銃量産立上げ、九六式25mm撃針寿命、九六式24cm榴弾砲散布界、九七式迫撃砲年次、回収/工作/通信車、Ki-27/B5N日程、重車両ターボ装着累積。


## Machine-processing checkpoint

- User required that bookkeeping changes be mechanically processed, not merely discussed.
- Fixed `11-MATERIAL-TOOL-WEAPON-IMPACT-AUDIT-1937-SUMMER.tsv`: normalized comma-separated pseudo-TSV to true tab-separated 8-column TSV.
- Reflected session decisions into `03-CURRENT-BRANCH-INDEX.tsv` (B-0031–B-0035), `05-CURRENT-CLOSED-PRODUCT-WEAPON-LEDGER.tsv` (P-013), and `06-CONFLICT-AND-REVIEW-QUEUE.tsv` (Q-021–Q-022).
- Added automated schema/duplicate/reference/archive checks in `12-MACHINE-INTEGRITY-AUDIT.*`.


## ウラン枝の経済性再監査
- old `asai-works-uranium.md` / `uranium-ap.md` を再走査。
- bulk low-grade ore「捨て値備蓄」を廃し、vanadium/radium副産物のresidue/concentrate/oxideへのoff-takeを中央へ。
- 1937 natural-U specialty metalはsaleable可能性あり。working cost $8–15/lb、limited sale $12–20/lb。commodity ballastには不成立。
- U-0.75Ti級は1937 mass productから降格し、1937–39 research / 1940+再監査。
- 詳細：`14-URANIUM-ROUTE-ECONOMIC-AUDIT-1937.md/.tsv`。

## ウラン／タングステン高密度材 再監査
- U-0.75Tiを1937 uranium branchからREMOVE。Ti一般研究は別論点。
- UC/uranium carbideをWC/cemented carbideの切削・耐摩耗代替にする案はREJECTED-TECH。
- 1937 natural-U industrial dense metal priceを再監査：engineering metal cost $4.5–7/lb、controlled billet/simple alloy $6–10/lb、sale概ね$7–14/lb。
- 原料はCongo前提なし。Canada Port Hope/Eldorado radium byproductとColorado/Utah vanadium/radium processorのoxide/residue off-takeが中央。raw low-grade ore Pacific shipmentはしない。
- W heavy alloyは史実1935発明/1938商用化をanchorに、浅井の既存powder metallurgyから1935–37 small-commercial branchを追加。
- uranium dense-core / W-heavy-alloy coreは1937 evaluation可能、mass adoptionと具体弾道性能はOPEN。
- 詳細：`15-URANIUM-TUNGSTEN-DENSE-MATERIALS-AUDIT-1937.md/.tsv`。



## Dense-core ammunition military impact audit
- W heavy alloy / WC / natural-U dense-core ammunitionを別物として整理。
- 1937の即戦力中央は20–37mm high-velocity anti-armor weaponsへのlimited special AP。
- Type 94 37mm AT gun: HIGH impact candidate.
- Type 97 20mm automatic cannon: production after adoption; dense-core ammo can materially extend usefulness once guns exist.
- Type 97 Chi-Ha 57mm: low velocity remains limiting; dense core alone does not convert it into a true AT gun.
- Natural U: no automatic import of later DU-alloy self-sharpening.
- After 1939 fission discovery, natural-U ammunition mass use is strategically disfavored because natural U becomes nuclear feedstock.
See `16-DENSE-CORE-AMMUNITION-MILITARY-IMPACT-1937.md`.


## Dense-material ammunition supply audit
- Port Hope historical production anchor: 1937 black oxide 9.1 t U3O8 (~7.7 t-U), 1938 23.8 t U3O8. Canada単独で1937数十t-U/yearを取る旧workingは下方修正。
- Uravan historical anchor: 1937–38 combined ~250,000 lb U3O8 (~113.4 t U3O8, ~96 t-U equivalent); annual split unknown.
- 1937 Asai current inflow 11–20 t-U/year、prior inventory込みusable feed 13–25 t-U。
- 1937 natural-U metal output 8–12 t/year、military dense-core allocation 1.5–3 t/year。1938 acceptance後は4–6 t/yearをworking。
- Uが実用化すればW special APを大幅に絞り、1938以後dense-core issueのU 75–90%、W系10–25%を中央方向。W節約は1937 2–4 t/year、1938 4–7 t/year order。
- exact round counts / core mass / penetration remain OPEN; logistics scale only.
See `17-DENSE-MATERIAL-AMMUNITION-SUPPLY-AUDIT-1937.md/.tsv`.

## 1937-07-07 event gate / dense-core ledger integration

- `10-WEAPON-IMPACT-LEDGER-1937-SUMMER`へ天然U/W系dense-core special APとW/U資源配分を統合。九四式37mm、九七式20mm、九七式57mm、九六式25mmへの影響を個別化した。
- 偶発事象ルールをCLOSE：実質条件が同じなら偶発事象も発生、関連条件が違えば史実結果を強制せず再シミュレーションする。
- 1937年7月7日夜の盧溝橋事件は、直接発火条件が実質同じため同日に発生する。最初の発砲者は固定しない。
- 7月8日以後の拡大はOPEN。車両、通信/電源、航空稼働率、補給、政治判断等のbranch差を各decision pointで適用する。
- `18-1937-07-07-EVENT-GATE.md/.tsv` を追加。

### 盧溝橋事件 初動gate
- 1937-07-07夕刻～1937-07-08 05:30前後を監査。
- 夜間演習→銃声→行方不明兵→交渉→再銃声→一木大隊前進/牟田口交戦許可→本格交戦開始はCLOSED-EVENT。
- 最初の発砲主体は固定しない。
- 浅井の過給重車両、移動電源、dense-core弾、GT航空はこの数時間の決心を変えない。九六式軽機の具体配備率だけminor OPEN。
- 次gateは7月8日05:30以後の初戦結果、増援、局地停戦、中央への報告。
### 盧溝橋 05:30–06:00 first-combat micro-gate
- 一次史料ベース再構成では05:30本格交戦、06:00に一時射撃停止。
- 浅井差（過給車両、移動電源、dense-core、GT）はこの30分に非関与。九六式軽機の少数早期配備余地はあるが戦術結果を分岐させない。
- 個別死傷数はこの30分だけへ分解できないためOPEN。
- 次gateは06:00–12:00の散発射撃・通信不調・撤退交渉・増援。
- `20-1937-07-08-FIRST-COMBAT-GATE-0530-0600.md/.tsv` を追加。



### 盧溝橋 06:00–12:00 morning gate
- 06:00停戦報告後も停止命令が完全徹底せず、07時過ぎまで散発射撃。CLOSED-SAME。
- 宛平側は概ね停止、長辛店方面との射撃継続。浅井装備差は非分岐。
- 豊台―天津/北平軍用電話障害をCLOSE。線路漏電/障害であり、GT移動電源車では解決しない。浅井が当該線路を直接供給した設定も置かない。
- 10–12時の撤退交渉、長辛店中国軍増強は史実同様。
- 通州方面部隊は11:40出発をCLOSE。厳密編成・輸送手段・到着時刻はOPENで次gateへ。
- 浅井本人は事件収拾への政治介入をせず、開戦なら敗北を避けたい方向へ心情が強まるというcharacter canonを記録。
- `21-1937-07-08-MORNING-GATE-0600-1200.md/.tsv` を追加。


## 1937-07-08 afternoon gate 12:00–18:30

- 12:00–18:30はCLOSED-SAME。北平交渉難航、日本側/中国側増援接近を含めても浅井差は決心を分岐させない。
- 通州/天津方面の混成増援では浅井過給重車両が故障脱落・牽引余裕を改善し得るが、戦車/砲/歩兵/道路律速があるため大幅な早着は置かない。exact transport/arrivalはOPEN。
- 日本側は18:30を期して永定河東岸へ自発撤収する決定を史実同様に行う。交渉決裂時には天津増援到着後の攻撃という腹案を保持。
- 次gateは18:30→7/9 05:00。中央不拡大指示、19時頃の増援到着、中国側増強、夜間交渉、第219団側夜襲を個別判定。


## 1937-07-08 18:30–07-09 02:10 evening/overnight gate
- 18:42参謀本部臨命400号の不拡大指示をCLOSED-SAME。18:30現地撤収決定後なので即時branch driverではない。
- 天津増援は19時頃到着を維持。編成に歩1第2大隊、戦車、砲兵第2大隊、工兵。砲兵第2大隊は機械化15cm榴弾砲側で、浅井turbo牽引/重貨物車が入る余地はあるがexact crosswalkはOPEN。差は早着ではなく落伍減/到着時稼働率。
- 第37師/第219団の夜襲eventは保存。ただし具体時刻・人数・戦果はOPEN。
- 19:00–02:10の北平/天津並行交渉は史実同様に進み、05:00撤兵案へ到達。次gateは02:10–07:10の命令伝達failureと05:00再射撃。
- `23-1937-07-08-09-EVENING-OVERNIGHT-GATE-1830-0210.md/.tsv` を追加。


## 1937-07-09 02:10–07:10 event gate
- 05:00撤兵合意は中国側前線へ伝達されず、05:00前後に再射撃が発生する枝をCLOSE-SAME。
- 「日本軍が電話線を切った/中国側伝令を阻止した」は中国側説明として保持し、原因の独立確定はしない。
- 05:10再連絡措置、06:40頃現地到着、07:10頃宛平入城・直接命令伝達を史実同様にCLOSE。
- 浅井系通信/電源は中国側内部命令網を置換しない。浅井車両も混成連絡団の調整・警戒線通過を律速解除しないため時刻前倒しなし。
- 次gate Q-024：07:10以後の撤退監視、2個中隊残置、保安隊引継ぎと五里店附近の誤認衝突。


## 盧溝橋進行：1937-07-09 07:10–16:00

- 07:10直接命令伝達後の撤退監視、監視用日本軍2個中隊残置を史実同様にCLOSE。
- 「保安隊」誤認衝突を再監査。単純な雨天制服誤認ではなく、実際に馮治安直属正規軍部隊を変装させて派遣していたことを重視。到着連絡伝令阻止＋同型外套＋実体が正規軍という条件が保存されるため五里店附近衝突も保存。
- 1937浅井radio差はreliability/電源/受領試験支援であり、歩兵小部隊へportable tactical radio/IFFが高密度配備されたCLOSED設定はない。通信差で誤認を消さない。
- 12:20頃再協議、16:00頃までの中国軍西岸撤退・警備引継ぎをCLOSE。警備部隊50/150名の記録差は段階差としてOPEN-detail。
- 次gate：7/9 16:00→7/10 16:00。


## 1937-07-09 16:00–07-10 16:00 event gate

- Backfill: 9日朝の東京は不拡大方針を再確認し、内地3個師団派遣案を一旦見送り。
- 第29軍は陣地構築・弾薬補充・移駐準備へ入り、第132師/騎兵第9師も行動準備。第37師は深夜に吉星文部隊を出撃。
- 10日正午の現地観察では日中両軍の局地離隔が成立。
- 浅井系turbo重車両は日本機械化/砲兵部隊の可動率を若干改善するが、10日16時までevent/timing差なし。
- 10日16時頃、竜王廟日本側斥候へ八宝山方面から迫撃砲射撃。次gateの再衝突triggerとしてCLOSE。


## 1937-07-10 16:00–21:15 Longwangmiao second-battle gate

- 17:00橋本参謀長の兵力進出抑制電話は史実同様に到達。
- 17:10頃、第220団/特殊兵中心の約100名が迫撃砲支援で前進、18:00頃竜王廟占領。初発の第219団第3営とは別。
- 18:00、馮治安は第675団1営+山砲1連+野砲1連+重迫撃砲4門を西苑→長辛店へ増援命令。21:15以前の全量現着は自動仮定しない。
- 18:20/18:55日本側撤収命令は到達するが、斥候小隊は交戦/負傷者/敵増加で離脱困難。通信failureではない。
- 19:00牟田口が第1大隊へ独断攻撃命令。19:25中国側迫撃砲斉射、20:20河邉現着・事実上追認、21:15竜王廟再占領をCLOSED-SAME。
- 浅井差は小火器reliability/readinessのminor域。dense-core AP、15cm turbo牽引、移動電源は非因果。河邉の装甲車両を浅井turbo仕様に自動同定しない。
- 次gate Q-027：21:15→7/11 05:00。
- `27-1937-07-10-LONGWANGMIAO-SECOND-BATTLE-GATE-1600-2115.md/.tsv` を追加。


### 1937-07-11 05:00–20:00 gate
- 11:30頃の今井相互撤兵案による現地実質妥結をCLOSED-SAME。
- 同日中央の関東軍/朝鮮軍/内地3個師団を含む増援準備承認もCLOSED-SAME。浅井車両/整備力はready fractionを改善するが動員decisionを反転させない。
- 14:00/16:00の現地認可・動員抑制上申、18:30政府派兵声明、20:00三カ条協定正式調印を保存。
- local-centralのねじれは通信failureではなくdecision synchronization問題。
- `28-1937-07-11-LOCAL-SETTLEMENT-CENTRAL-DISPATCH-GATE-0500-2000.md/.tsv` を追加。


### 2026-08-30 branch progress — 1937-07-11 20:00 to 07-13 20:00
- B-0093..B-0100追加。
- 11日夜の発砲報、12-13日鉄道増援/中国中央軍北上、第20師団応急動員、大紅門弾薬truck爆発、13日内地派兵保留を処理。
- 大紅門eventはCLOSED、cause/vehicle/exact casualtyはOPEN。
- 浅井社内 readiness check はWORKING-HIGH-CONFIDENCE、大量増産開始は未CLOSE。

### 2026-08-30 branch progress — 1937-07-13 20:00 to 07-17 evening
- B-0101..B-0109追加。
- 14日抑制方針、天津→北平方面3,500名+砲12門道路移動、第37師攻勢準備、永定門/団河/16日小衝突、17日期限方針と廬山声明をCLOSE。
- 14日道路移動は全員motorizedとせず、浅井差をheavy vehicle/tractor/support echelonのready fractionへ限定。
- Q-029をCLOSED、Q-030を次gateとして追加。
- `30-1937-07-13-17-REINFORCEMENT-LOCAL-CLASH-LUSHAN-GATE-2000-1800.md/.tsv` を追加。


### 1937-07-17→20 event progression
- Q-030 closed SAME.
- 18 Jul Soong/Katsuki compliance visit and Peiping-Hankow troop-train air incident preserved; aircraft type not auto-assigned to Ki-15.
- 19 Jul detailed implementation agreement and free-action warning preserved.
- 20 Jul renewed withdrawal effort and subsequent Marco Polo/Wanping artillery clash preserved.
- Asai heavy-vehicle/artillery-production quality changes only operational margin; dense-core ammunition is irrelevant to this infantry/fortification fight.
- Next: Q-031, 21–22 Jul withdrawal / rail transport / home-division employment decision.

### 2026-08-30 correction — 20 July artillery-effect wording
- B-0116 / gate 31 revised. By July 1937, artillery computation/survey/firing-table/QC maturity is a **real branch advantage**, not merely a metallurgy/reliability footnote.
- For the 20 July Wanping/Marco Polo artillery exchange, however, the mission is strongly warning/punitive and limited in scope. Better calculations improve consistency/correction but do not justify dramatically greater destruction or casualty totals.
- Dense-core U/W ammunition remains irrelevant because the targets are not armored.


### 1937-07-21–22 gate
- B-0119..B-0124 added.
- Q-031 CLOSED-SAME; Q-032 opened for 23–24 Jul.
- Chinese railway repair / 37th Division rail withdrawal is not accelerated by Asai because no Asai role is established in the Peiping-Hankow railway.
- Tientsin Army historical judgment that current forces were sufficient is preserved; Asai-worldline readiness only slightly reinforces that judgment.


### 1937-07-23–24 gate
- B-0125..B-0131 added.
- Q-032 CLOSED-SAME; Q-033 opened for Langfang incident.
- 23 Jul 37th Division withdrawal slowdown, 132nd Division entry discrepancy, Hsiung Pin arrival, and 24 Jul Soong implementation-detail semantic mismatch preserved.
- Asai communications do not solve an authority/meaning mismatch. Asai heavy-vehicle readiness only marginally reinforces Soong's historical time-buying judgment.
- Added `33-1937-07-23-24-COMPLIANCE-SEMANTIC-BREAKDOWN-GATE.md/.tsv`. Full ZIP not rebuilt per user request.

### 1937-07-25–26 Langfang communications-line gate
- B-0132..B-0139 added.
- Q-033 CLOSED-SAME; Q-034 opened for the 26 Jul Kuanganmen truck-convoy timing audit.
- Langfang wire cuts are deliberate single-point communications sabotage, not a terminal-equipment reliability problem; Asai equipment does not prevent them.
- No closed 1937 Asai radio-relay / dense portable-radio topology makes the Peiping–Tientsin fixed line disposable. Repair and line-security deployment therefore remains necessary.
- 23 Jul blocked attempt, 24 Jul prior permission, 25 Jul ~16:30 repair start, night presence/friction, ~23:10 clash, ~03:30 Tientsin Army policy shift, ~06:00 air intervention, and morning Japanese control are preserved.
- Exact repair-completion time, exact battle-end hour, and absolute first-shot attribution remain OPEN-detail; Japanese-first/Chinese-first accounts are recorded separately, with the Iwatani synthesis favoring the Japanese sequence on internal consistency.
- Full ZIP not rebuilt per user request.



### 1937-07-26–27 Guang'anmen convoy-delay gate
- B-0140..B-0149 added.
- Q-034 CLOSED-SAME through 27 Jul ~04:30; Q-035 opened for the final 27–28 Jul attack-decision/execution gate.
- Historical >1 h convoy delay is localized to **late departure from Fengtai**, not demonstrated road-speed/overheating/breakdown. No Asai-caused early departure is granted.
- A punctual ~16:00 arrival could plausibly have altered the gate incident, but remains counterfactual-only because the branch does not change the departure-delay cause.
- ~15:20 pre-arrival Chinese closure/arming, ~16:00 first negotiated opening, ~17:40 second open order, ~18:20 split-column firefight, ~22:20 Japanese attack order and ~04:30 temporary postponement are preserved.
- Exact convoy truck types, first-shot attribution, first-fire vehicle ordinal and exact casualties remain OPEN-detail.
- Full ZIP not rebuilt per user request.
