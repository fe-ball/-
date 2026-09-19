# 1941→再走査 Gate Matrix v0.04

## 0. 原則

各ゲートでは「戦果」だけでなく、次の三層を同時更新する。

1. **STATE**：機体、人員、艦艇、潜水艦、船腹、修理、配置。
2. **OBSERVATION**：日本・連合軍が何を観測したか。
3. **SWITCH/POLICY**：観測・需要・余力が制度/建造/教範変更の閾値を越えたか。

後続正本のカレンダー日付だけでSOFT/POLICYスイッチをONにしない。


## A0. 南方航空集中（1941-11-15～12-07）

### STATE

- 計画配当機数と実到着機数を分離。
- 集中中の事故、迷航、強制着陸、未帰還、指揮官級損失を開戦前状態として記録。
- 航空地区部隊・通信・気象・補給・輸送の先行展開をIJA既存能力として記録。

### OBSERVATION

- 悪天候下で何が原因になったか（純気象/航法/燃料/故障/着陸）。
- 経験者・指揮官喪失が開戦時部隊へ残す穴。

### SWITCH

- `IJA-AIR-BASE-MOBILITY` はOPERATIONAL_PARTIALのまま。
- 海軍空地分離、練度平準化、専任空輸等を前倒ししない。

## A. 1941-12-07夜

### CLOSED/HARD

- 現行機体・艦艇設計性能。
- 開戦時航空総量/空母航空枠。
- 九一式航空魚雷成熟。
- 水上魚雷再装填/第二攻撃教範。
- Type 2中央暗号計算所。
- 潜高第一/第二ロットの開戦前決定と建造負担。
- 1941末電探試験へ至る研究時計。

### OPEN/AMBER

- 参加航空隊の資格/経験コホート実数。
- 非空母水上艦の個艦Availability/OOB。
- 潜水艦1941-12-08個艦OOB。

## B. Pearl / Wake / Philippines初日（1941-12-07～10）

### STATE

- 空母航空：不可逆損失、損傷帰還、修理待ち、搭乗員KIA/MIA/負傷。
- Philippines/南方：同時刻の各基地航空隊は別状態で進行。Pearl生残者を瞬間移動させない。

### OBSERVATION

- 米側：零戦航続/性能、浅水深雷撃、攻撃統制。
- 日本側：米AA、迎撃、機体損傷/帰還の型。

### SWITCH

- 陸軍航空基地機動：OPERATIONAL_PARTIAL。基地転進の支援到着遅延を記録。
- 海軍航空空地分離：LATENT。基地転進摩擦の記録だけ開始。
- 熟練者還流：人員状態として常時追跡、制度効果なし。
- 艦政：変更なし。PearlだけでMI後政策を前倒ししない。

## C. Malaya / Philippines / DEI反復航空戦（1941-12～1942-03）

### STATE

日次で：

- start-of-day serviceable aircraft
- sorties flown / repeated sorties
- combat loss / noncombat loss
- damaged return / repair completion
- pilot KIA/MIA/wounded/fatigue/rest
- flight leader / navigation / radio qualified availability
- base move / direct-maintenance arrival / fuel-ammo-parts arrival
- transport/port/airfield construction clock

### OBSERVATION

- 基地転進時の地上支援摩擦。
- 同型機でも隊/基地により可動率が違うか。
- 経験者の有無が集合/航法/事故へ出るか。
- 連合軍側は日本機性能・雷撃・長距離侵攻の実観測を更新。

### SWITCH/POLICY

- IJA-AIR-BASE-MOBILITY: 既存の部分機能分離を実測し、物理的律速を記録。
- IJN-AIR-GROUND-SEPARATION: friction evidenceを蓄積。原則TRIAL以前。
- JOINT-BASE-STANDARDIZATION: 陸海軍間の受入/工具/補給摩擦が観測された場合のみOBSERVED候補。
- A-SKILL-LEVELING: まだLATENT。隊間差のデータを貯める。
- ASW-LOCAL-COMMAND: 船腹損失/接触が増えればOBSERVEDへ。
- TECH-RADAR: 技術時計に従い艦隊試験へ。配備優先は実需要で決める。

## D. Indian Ocean / early submarine war / southern consolidation（1942春）

### STATE

- 生残航空員が原隊/後送/新機受領/再編へどう流れたか。
- 潜水艦：個艦哨戒日、接触、射点、再捕捉、修理。
- 護衛：船団損失、DD拘束、ASW接触後再捕捉。

### SWITCH/POLICY

- ASW局地幕僚強化の強度を実損失で更新。
- 東海量産優先度を潜水艦脅威から更新（初飛行時計自体は維持）。
- 潜高第三ロットはまだ自動発注しない。

## E. MOゲート

### STATE

- 空母/航空隊の損傷・生残・修理時計。
- 艦上資格者、編隊指揮、航法、甲板/整備核の生残。
- 米空母側も実損害/修理で更新。

### OBSERVATION

- CAP、索敵、予備攻撃、攻撃隊同期、母艦収容、損害制御。

### SWITCH

- 空母戦術研究がOBSERVED/TRIALへ進む可能性。
- 母艦航空隊可搬化は、損傷艦・他艦収容経験が出た場合のみ観測蓄積。

## F. MIゲート

MIは大きな政策ゲートだが、**旧85結果を前提にしない**。

### 必ず再決定

- P-C01 艦上航空教育拡大の規模。
- P-C02 雲龍/飛龍系の要求数・ロット。
- P-C03 緊急改装空母。
- P-C04 千歳/千代田。
- P-C05 伊勢/日向。
- P-C06 信濃。
- P-C07 雲龍への火災/燃料/消防戦訓。
- P-SF01/P-SF02 駆逐艦・戦時型需要。

### 人員/制度

- 自然還流は既に累積している。
- MIが大量の修理/再編/療養を生めば人員撹拌流量が跳ねる。
- ただし次作戦圧力が強ければ再編演習期間は短くなる。

## G. 1942 H2

カレンダーではなく、次を検査する。

- air-ground separation friction evidence
- weeks available for trials
- veteran nuclei available
- unit skill variance observed
- destroyer loss/escort pressure
- submarine/shipping pressure
- Sen-Taka first boat/electrical test results

これにより、空地分離TRIAL、局地護衛指揮所、潜高第三ロット、戦時型DD要求等を個別判定。

## H. 1943 H1/H2

旧正本の「1943だからON」を禁止し、状態機械を評価する。

- 空地分離：TRIAL→STANDARDへ進めるだけの実績があるか。
- 経験核：隊間技能分散と人員余力があるか。
- 練度平準化：大編隊/混成隊失敗のデータがあるか。
- 専任空輸：戦闘搭乗員拘束/事故が大きいか。
- 護衛常設化：船腹損失が十分深刻か。
- 松型/簡易護衛艦：駆逐艦・護衛需要が閾値を越えたか。
- 空母改装/信濃/伊吹：実空母損耗と造船所競合で再決定。

## I. 以後の戦史

旧Efate/第二次Midway/GALVANIC/Marshall/Truk/Palau/FORAGERは、日付・OOB・損害を固定しない。

一方、後続研究で得た以下は再利用する。

- 作戦候補。
- 敵味方が当時観測可能な戦訓候補。
- 技術のHARD-CLOCK。
- Hull→Availability等の評価法。
- 人員/組織の状態遷移法。



## J. サービス別スイッチの禁止事項（v0.03）

- 陸軍航空の1941年時点の航空地区部隊・飛行場大隊等を「未発明」としない。
- 逆に、その機能を海軍航空へ自動的に付与しない。
- 自然還流は開戦初日から状態遷移として追うが、意図的な経験核再配分や練度平準化制度を前倒ししない。
- 後続正本で固定された成熟日が旧MI/Guadalcanal枝に依存する場合、その日付は再走査で解除し、観測・必要性・実施余力から再判定する。
