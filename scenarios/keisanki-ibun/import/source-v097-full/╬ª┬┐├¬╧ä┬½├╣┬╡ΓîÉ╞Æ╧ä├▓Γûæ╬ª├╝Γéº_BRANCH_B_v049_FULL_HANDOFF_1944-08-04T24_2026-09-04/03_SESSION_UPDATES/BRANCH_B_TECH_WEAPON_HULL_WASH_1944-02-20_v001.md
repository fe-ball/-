# Branch B 技術・兵器・艦艇残存 再洗浄台帳 v001

基準時点: **1944-02-20T24**（現行再監査frontier）  
意味論ベース: Branch B v048 / 2026-08-31 re-audit master

## 0. 読み方

本台帳は、兵器名が存在することと、戦場で使えることを分離する。

- **A / ACTIVE-HARD**: 20 Feb 1944までに現行Branchで成立し、該当部隊・装備なら必ず考慮する。
- **B / ACTIVE-WORKING**: 成立は強いが数量・性能・ready率は作業帯。イベントごとに再確認する。
- **C / TRACE-REQUIRED**: 装備/船体は存在・生残しているが、所在地・部隊転換・整備・乗員・弾薬等を追跡しないと戦力化しない。
- **D / FUTURE-GATED**: 研究・建造・試作は存在しても20 Feb 1944の戦闘力へ入れてはいけない。

常に `physical -> serviceable -> mission-ready -> committed` と、`existence -> production -> delivery -> unit conversion -> frontline-ready -> local allocation` を分離する。

---

# 1. 航空機・発動機

## 1.1 海軍戦闘機

### 瑞星零戦系 — A
開戦時から史実栄零戦ではなくBranch固有の瑞星零戦系が主力。後期瑞星零戦も1943年までに成熟している。性能差は最高速だけでなく、生産中央値、冷却・振動・公差、整備性、兵装較正に現れる。

### 金星零戦改 — A/B
1942H1に瑞星の成長限界を認識、1942中盤設計、1943H1試験、1943年9月先行量産。11月GALVANICでは18–24機程度がevent-ready、中心20。1944-02-02 FLINTLOCKでは第一撃55戦闘機のうち**28機が金星零戦**として実戦投入されているため、20 Feb時点では「存在するか」ではなく配備数量を問う段階。

性能作業帯: 586–593 km/h、6000m 6:35–6:55、安全長距離護衛550–620 km、兵装20mm×2 + 13.2mm×2、頭背面防弾・部分的燃料/火災防護。

### 雷電 J2M — A/B
1942末～43初に戦闘可能部隊化し、1943年には重要基地へ集中配備された実用邀撃システム。Jan-1944作業値は全国frontline assigned 255–300、通常serviceable 195–235だが、この全国値はevent OOBではない。

標準機は3–6 km邀撃が主用途。高高度機械過給subsetは少数。排気turbo型は20 Feb時点で**試験のみ、combat-ready 0**。

### 強風 N1K1 — A/C
1943春から実用水上戦闘機。滑走路非依存の局地防空/偵察阻止レイヤー。1943-10時点frontline中心50–65級。現地配備は要trace。

### 紫電改 — C/D
1944-01-28時点で試験/初期運用直前。20 Febの一般戦力として自動投入しない。具体的部隊・受領・訓練traceがあれば限定的に開く。

### 烈風 A7M — D
試作・艦上試験時計。1944-02の量的戦力ではない。存在を理由に空母戦力へ加算禁止。

## 1.2 艦攻・艦爆・偵察

### B5N 瑞星・防護強化型 — A
開戦時から瑞星15共通化と1941年後期の防護/火災安全 packageを持つBranch variant。B6N登場後も即時全廃されない。

### D3A 改良量産型 — A
開戦までに急降下包絡・量産再現性を改善。最高性能より同一条件での投弾再現性を評価。

### D4Y — A
高速偵察が1942H1から先行、爆撃型は1942後半～43に段階導入。1944-02-02の四空母第一撃では**60機**が中心値として使用されている。偵察・recontactにも重要。

### B6N — A
1942夏先行生産、1942末～43初初期部隊。1943の発動機耐久・spares/tools/training gateを通して拡大。1944-02-02四空母第一撃で**45機**中心。

### 瑞雲 E16A — A/C
1943年9月納入開始、最初のcombat-capable detachmentはOct-Nov。高速確認・接触維持・砲観・軽攻撃用の小規模water-air asset。大量爆撃機として扱わない。

## 1.3 陸軍航空

Ki-43は開戦前倒し主力、Ki-44は開戦時少数trialから早期邀撃機化。1944年春用のKi-61/Ki-84評価資料はあるが、**20 Feb現在の全国/戦域 fielding ledgerが海軍航空ほど硬化されていない**。Ki-84等を当前線へ自動配備しない。ここは独立監査対象。

## 1.4 航空兵器

同一戦術条件でのtechnical dispersion改善作業帯:

- 戦闘機固定銃: 命中確率 **+10–25% relative**
- 移動艦への急降下爆撃: **+10–25% relative**
- 航空魚雷攻撃: **+10–25% relative**

すべてpercentage-point加算ではない。敵CAP、AA、回避、天候、crew、attack geometryを通した後の同条件technical componentである。

---

# 2. 水上魚雷・砲戦

## 2.1 九三式/九五式魚雷 — A/B
名目速度・射程・炸薬量は史実級のまま。Branch差はstraight-run/depth dispersion、lot差、発射管/gyro較正、異常走・始動失敗・信管故障tailの削減。

- technical dispersion: -15–25%
- lot variation: -25–40%
- ship/tube calibration variation: -25–40%
- abnormal/start failures: -15–25%
- fuze technical failures: -15–25%
- routine oxygen accidents: -20–30%

1944年2月の航空九五式の標準弾頭は**約405 kg級**。大型弾頭を前倒ししない。

## 2.2 第二斉射システム — A
再装填機構・手順のfailure tailを削り、条件が合えば4本再装填6–9分演習、戦闘7–11分級、第一発射から第二有効斉射まで12–20分級。これは「搭載魚雷数を初撃で倍化」ではない。

## 2.3 艦砲射撃 — A/B
通常昼戦で命中確率+2–5% relative、初回有効解5–10%早期。長距離/非標準気象では初期systematic error -20–30%、first-straddle +8–15%、解収束10–20%高速化の作業帯。

機械式射撃盤を電子計算機へ置換したわけではない。

---

# 3. 水上艦艇の設計強化

## 3.1 朝潮/陽炎/夕雲系 — A/B
最高速の魔法的増加ではなく、航続・復原・機関信頼性・planned-speed realization・damage-state continuityを改善。

- 朝潮: trial 34.7–34.9 kt、4800–4900 nmi/18kt
- 陽炎: trial 35.4–35.7 kt、full-load practical 34.6–34.9 kt、約5300 nmi/18kt
- initial machinery faults -15–25%、unplanned yard days -10–20%級の技術系統

## 3.2 損傷制御/余裕 — A/C
計算で得た重量・強度余裕を局部補強、排水・消防、配電、換気、操舵、将来AA/radar I/Oへ再投資。装甲倍率ではなく、moderate damageからmission-killへ落ちる遷移確率に作用する。

## 3.3 金剛型 — A/B
**金剛・比叡・霧島・榛名の4隻がBranchでは1944へ残存。** 30kt級快速戦艦formationとして、機関信頼性・予定速力再現性・damage-state continuityを改善。装甲限界は史実級で、現代米戦艦との昼戦を万能化しない。

## 3.4 大和型 — A/B
大和・武蔵とも存在。46cm砲、27kt級、集中防御は維持。低価値重量145–230t（中心約190t）を局部支持、配電区画、消防、操舵、将来AA/radar I/O余裕へ再投資する設計線。武蔵は大和実測の反映で就役時6–10か月程度の技術成熟差を持つ作業線。

**30kt大和、46cm威力増、装甲倍率化は禁止。**

## 3.5 伊勢/日向 — A
航空戦艦化しない。通常戦艦として残る。千歳/千代田も空母化せず水上機母艦を維持。

## 3.6 最上型 — A/C
Branch MI divergenceにより4隻生存。中損傷後のavailabilityは個艦trace。教師艦（最上/三隈）と成熟群（鈴谷/熊野）の設計学習差を持つ。

---

# 4. 艦艇残存・建造財布

## 4.1 日本空母 — 20 Febの重要残存差

### 恒久喪失
- 赤城
- 加賀

### 第一線核心 — A/C
- 翔鶴
- 瑞鶴
- 飛龍
- 蒼龍

4 hullとも20 Febまで生存。2 Feb FLINTLOCK後は翔鶴・瑞鶴・蒼龍が作戦可能、飛龍がdeck damage。飛龍はTrukで緊急修理後、HAILSTONE前に西方退避。4隻ともTruk防衛へ反転しない。

### 二線/補助deck — A/C
- 隼鷹
- 飛鷹
- 龍驤
- 瑞鳳

1944-01-15時点でcombat-useful aircraft 100–120級、2 Feb後も88–104 mission-ready級のrear-deck depth。ただしCAP relay、cross-deck recovery、ferry/reorganization、bounded searchが主で、第一線4空母と同格strike deckではない。

### その他carrier hull — C
- 龍鳳、祥鳳はBranch生残/建造系統上の候補。現行frontierでの所在地・air group・deck readinessをハードに閉じていないため、戦闘財布へ自動投入禁止。
- 大鳳: 1944年2月完成時計だがwork-up段階。**20 Febの同期打撃空母ではない**。正確な引渡日/訓練状態は要close。
- 雲龍: まだ不可。
- 信濃: 現行1943政策では自動空母化しない。

## 4.2 日本駆逐艦 — B/C
1944-01-01 current reconciliation anchor:

- modern fleet-type physical hulls center **81**
- mechanically/crew-ready **70–75、center 72**
- short maintenance/work-up **6–11**

史実ソロモン方面の損失鎖が多数存在しないため、村雨、川風、夕雲、巻雲、巻波、高波、大波、清波、涼波、照月、新月など多数がBranchでは残存側へ戻る。

Branchで確定している主要永久損失には夕立、夏雲、吹雪などがある。ready 72を一箇所へ集められるわけではなく、空母screen、Central Pacific、南方基地、タンカー/船団護衛等へ配分済み。

## 4.3 日本軽巡 — B/C
1944-01-01 current reconciliation anchor:

- physical combat hulls center **21**
- fully/near-ready **18–20**

史実Guadalcanal/New Georgia系損失を自動継承しないため、天龍、由良、神通、川内などがBranchでは残る。矢矧は1943-12-29完成でJan初めwork-up。個艦所在地はevent trace必須。

## 4.4 その他重要生残/喪失

- 陸奥: 1943-06-08沈没は維持。
- 比叡/霧島: 史実Guadalcanal喪失なし。
- 榛名: 1942 New Caledoniaで16in×2中大破したが1943-01復帰。
- 鳥海: 1942 MI pursuitで大破、1942-08末復帰。
- 日進: New Georgia史実損失鎖がなく生残。

---

# 5. 潜水艦

## 5.1 通常潜水艦 — A/B
成熟classでは代表値としてsurface speed +0.3–0.4kt、submerged +0.15–0.2kt、surface range +8–9%、submerged endurance +7–10%、dive time -10–15%。主効果はpatrol-day、故障、到着、再出撃率。

## 5.2 潜高第一世代 Ko-1..6 — A/C
**6隻が1943年中にcombat-readyとなるBranch独自の大きな前倒し。**

- submerged max 18.5–19.0 kt
- full-speed budget 55–65 min
- dive 42–47 s
- 6200–6500 nmi/14kt
- submerged 145–155 nmi/3kt

高速は射点修正/reposition用で、連続19kt追跡や高速聴音を意味しない。Ko-4はEfateで中破後1943-07までに復帰し、年末には6 hull物理available subject to maintenance。

## 5.3 独技術上乗せ — A/C
I-30生還・帰国によりMetox級metric RWR、Bold級音響欺瞞、Würzburg級追尾/servo等が1943に段階実用化。U-511/RO-500は溶接、machinery mounting、振動、maintenance access、acoustic reference。I-8帰還者のtacit knowledgeは1944Q1から一部手順へ入る。

**Ko-1..6をType IX風に遡及再設計しない。** Ko-7/8以降の艤装/試験へ反映しうる。

---

# 6. レーダー・ESM・EW・C2

## 6.1 レーダー — A/B/C
1942はhuman-loop early warning。1943Q2-Q3にA級固定基地で、radar range + optical bearing + plot prediction + fighter/AA directionを組み合わせた限定closed-loopが成立。selected major shipsはQ3-Q4以降の段階導入。

Würzburg技術はprecision tracking、servo、error measurement、radar-to-director interfaceのmissing cardを埋めるが、SG/PPI/CIC同等ではない。

## 6.2 ESM/RWR — A/C
1943H2 priority ships/submarines/basesでmetric-band passive warningが実用。得られるのはemitter existenceとbearing historyで、range/ship identity/weapon-qualityではない。米SG等10cm級への万能警報はない。

## 6.3 RCM/EMCON — B/C
周波数適合chaff/reflectorはmetric radarにminutes-scale clutter/track-splittingを作り得る。EMCON、短時間active search、reserve set/power、分散、rapid repairがpriority baseで成熟。

## 6.4 Base C2 — A/C
TrukのようなA級基地では radar + visual + RI/DF + weather + plot + radio/telephone + staged readiness + AA fire direction + independent water aviation が一つのsystem。固定レーダーが壊れてもplot/power/comms/sparesの分散で部分復旧可能。

---

# 7. ASW

## 7.1 日本ASW system — A/B/C
1942-43から自己雑音速度帯、sonar calibration median、depth setting、2艦handoff、航空→局地化→艦艇攻撃を統合。late 1943–44H1ではdatum後MAD close localizationを導入。

priority coverage zoneの作業中心:
- detection opportunity ~1.8× historical-Japanese-equivalent
- datum/weapon-delivery opportunity ~2.5–3×

ただし撃沈率を同倍率にしない。最初に効くのは米潜攻撃の中止、re-attack阻止、護衛継続。

---

# 8. 陸戦兵器・車両・築城

## 8.1 原則 — A
Branchの主改善は口径/装甲の未来化ではなく、射表、弾薬lot、照準/測量、通信稼働、車両reliability/recovery、工兵機材uptime、弾薬/水/通信の分散。

- 47mm等がM4正面を魔法的に撃破できるようにはならない。
- 新型/追加戦車・重砲をtraceなしで生成しない。
- reliability改善はphysical countではなくdaily usable fractionとrepair returnへ入れる。

## 8.2 Eniwetok current hard trace — A
Type 95: **9両 physical / center 9 serviceable**、Engebi/Eniwetok/Parry各3。これ以上は生成しない。短期改善は隠蔽local reserve、registered fire、alternate positions、ammo/water/comms dispersionであり、Peleliu/Iwo級地下要塞の前倒しではない。

---

# 9. 工業・兵站・材料

## 9.1 計算サービス — A
1932 relay+drum系から計算を軍需/設計/輸送のserviceとして拡散。1939–41 sealed-reed/Type-2 era、1943 Type2P hybrid実験、1944 Type3 full-logic parametron。1942-43の成果を成熟parametronへ逆投影しない。

## 9.2 輸送/標準船 — A/B
既存船でeffective cargo/voyage +4–8%、port stay -8–15%、monthly turnaround +5–10%級。標準船工程ではlabor -10–18%、rework -20–35%、cargo +2–4%、fuel -3–6%の設計/工程帯。ただし造船量の全国flat multiplierは禁止。

1944初頭の大きな差は「大量の架空新造船」より、1942-43の低損失による既存商船残存とoff-hire削減。

## 9.3 材料 — A/B
New Caledonia Ni/Cr backhaulはpriority war-spec floorを支えるが、資源制約を消さない。Feb-1944作業状態はNi priority GREEN/economy YELLOW、Cr GREEN～GREEN-YELLOW、W YELLOW、Mo YELLOW-RED、Co RED、Cu YELLOW-RED。高温材は排気弁、過給器、turbine/blade/bearing実験へ選択投入。

---

# 10. 将来ゲート：20 Febに使わないもの

- **大鳳**: hull completionはFeb時計だが、同期打撃空母として未成熟。
- **雲龍/天城/葛城**: future construction/work-up。
- **烈風**: 量産戦力ではない。
- **紫電改**: 一般部隊へ自動投入しない。
- **排気turbo雷電**: combat-ready 0。
- **operational jet**: なし。国内bench研究のみ。
- **I-400/晴嵐 integrated combat system**: TECH gateは1944-03以降。20 Febには不可。
- **潜高改 Ko-7/8**: readiness checkpointが必要。Ko-9/10前借り禁止。
- **I-34/I-29 future German hardware effects**: 20 Feb以前へback-port禁止。
- **九五式大型弾頭/後期改良**: dated gate前に標準化しない。

---

# 11. 現時点で見つかった「要追加監査」

## 優先度S — シナリオへ直結

1. **1944-02-20日本艦隊個艦master roster**  
   Jan1のDD/CL reconciliationは強いが、20 Febの個艦 location/repair/fuel/ammo/radar fitまで一本化された台帳がない。特に増えた駆逐艦・軽巡が空母screen、船団護衛、Truk/Palau、南方へどう割かれているかを閉じる必要がある。

2. **日本空母全11 hull候補の20 Feb状態**  
   第一線4＋二線4はかなり硬いが、Ryuho/Shoho/Taihoのphysical completion、所在地、air group、deck readinessを同一表で閉じる必要がある。Taihoは「完成」と「戦闘空母」を厳格に分離。

3. **carrier air-group type/crew ledger at 20 Feb**  
   金星零戦/D4Y/B6Nの存在は硬いが、2 Febの86機irrecoverableとcadre debt後に、各deckへ何機・どのcrew qualityが残っているかを個艦別に閉じる。

4. **潜高Ko-1..6の20 Feb allocation**  
   6 hull existenceは硬いが、Truk/Marshall/Indian Ocean/repair/transportのどこにいるかがイベントごとに散在。潜高を通常I-boatと同じ匿名poolに入れない。

## 優先度A — 技術効果の誤用防止

5. **艦艇radar/ESM fit ledger**  
   「selected major ships」「priority formations」のままだと個艦戦で過大/過小評価が起きる。各CV/BB/CA/CL/DD/SSについて radar type、RWR、operator maturity、spares/field-serviceを明示する。

6. **damage-control/refit ledger by class/hull**  
   DC marginはclass/refit-specific。全艦へ一律付与せず、金剛型、大和型、最上型、新型DD、旧型艦を分ける。

7. **Army aviation Feb-1944 fielding ledger**  
   Ki-43/Ki-44までは系譜があるが、Ki-61/Ki-84等の1944-02 frontline quantity/readinessが海軍ほど硬くない。

8. **land weapon/platform inventory**  
   Eniwetok Type95のようなlocal traceはあるが、中国/ビルマ/島嶼の戦車・AT gun・砲・車両を一枚で管理するcurrent ledgerが弱い。

## 優先度B — downstreamの整合

9. **Taiho exact completion/work-up clock**  
   「Feb completion」はあるが、20 Febのphysical statusを明記したcurrent overlayが必要。

10. **Ryuho/Shoho/Nisshin/Chitose/Chiyoda current location/readiness**  
    生残/role policyは分かるが、20 Febのlocationとmission statusをhard-closeする。

11. **merchant/tanker surviving hull ledger**  
    艦隊燃料と修理能力を本当に決めるのはタンカー/修理船/給糧・輸送船。HAILSTONEでAkashi/major oilersを退避させているため、以後のfleet availabilityに直接効く。

---

# 12. 今後のシミュレーションでの強制チェック

イベント開始時に最低限以下を読み出す。

1. hull/airframe physical count
2. repair/serviceability
3. crew/aircrew quality and fatigue
4. weapons/ammunition/torpedo lot
5. sensors: radar/RWR/DF/visual
6. C2/plot/comms
7. mobility/fuel/range
8. damage-control/refit state
9. local allocation and mission
10. enemy observation/adaptation state

これを満たさない兵器・艦艇は、存在していても自動的に戦闘力へ加算しない。

---

# 13. 現時点の要約

Branch Bの1944年2月は、史実より「数年先の万能兵器群」ではない。差の中心は、

- 早い計算/統計/品質管理による量産中央値・ready率・故障tail改善
- D4Y/B6N/Raiden/Kyofu/Zuiun/Kinsei Zeroなどの前倒し・早期成熟
- 水雷・砲戦・carrier deck/search/CAPのprocess成熟
- radar/ESM/field serviceを持つ選択部隊/基地
- 潜高6隻という明確な新規能力
- 史実Guadalcanal等で失われた多数の日本水上艦が残っていること

の積である。

特に**残存駆逐艦・軽巡・空母補助deck・潜高**は、今後のシナリオで単に背景戦力にせず、護衛・索敵・ASW・補給・cross-deck recovery・夜戦へ財布として明示的に割り当てる必要がある。
