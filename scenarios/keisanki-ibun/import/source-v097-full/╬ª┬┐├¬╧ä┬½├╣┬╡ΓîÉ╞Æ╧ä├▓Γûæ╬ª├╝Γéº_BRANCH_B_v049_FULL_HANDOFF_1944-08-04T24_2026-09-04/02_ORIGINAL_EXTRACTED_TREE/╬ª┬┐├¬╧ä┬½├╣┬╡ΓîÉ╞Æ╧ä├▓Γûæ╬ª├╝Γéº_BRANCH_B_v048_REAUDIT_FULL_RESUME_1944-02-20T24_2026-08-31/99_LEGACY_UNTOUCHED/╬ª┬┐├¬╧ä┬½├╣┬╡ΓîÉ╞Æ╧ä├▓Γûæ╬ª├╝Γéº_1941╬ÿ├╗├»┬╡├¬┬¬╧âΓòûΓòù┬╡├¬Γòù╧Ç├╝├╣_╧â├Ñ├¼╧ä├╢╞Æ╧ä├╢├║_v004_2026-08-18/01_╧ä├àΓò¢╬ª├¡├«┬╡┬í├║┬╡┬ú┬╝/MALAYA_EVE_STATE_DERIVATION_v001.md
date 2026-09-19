# マレー 1941-12-07夜 状態導出規約 v0.01

## 0. 目的

「名目OOB」「集中中の損耗」「補充」「整備不良」を混ぜず、12月8日朝に実際に使用できる航空戦力を作る。

この文書は、数値が足りない部分を推定で埋めるためではない。**何が不明かを保持したまま戦史を前へ流すための会計規約**である。

## 1. 状態変数

各飛行戦隊・独立中隊について最低限次を持つ。

### 機体

- `table_strength`
- `arrived_forward_area`
- `serviceable_eve`
- `short_maintenance`
- `long_maintenance`
- `precombat_destroyed`
- `precombat_forced_landing_recoverable`
- `replacement_arrived_unassigned`
- `replacement_assigned_not_ready`

### 搭乗員

- `crew_present`
- `crew_experienced_core`
- `crew_formation_navigation_leader`
- `crew_fatigued`
- `crew_wounded_convalescent`
- `crew_kia_mia`
- `replacement_crew_low_skill`
- `replacement_crew_trained`

### 基地・支援

- `ground_crew_capacity`
- `airfield_battalion_capacity`
- `runway_capacity`
- `drainage_factor`
- `fuel_stock`
- `drop_tank_stock`
- `ammo_stock`
- `spares_tools`
- `weather_navigation_support`
- `transport_capacity`

## 2. 同じ時点の帳簿だけを足し引きする

原則式：

`SERVICEABLE_EVE(t)`
=
`PHYSICAL_PRESENT(t)`
- `SHORT_MAINTENANCE(t)`
- `LONG_MAINTENANCE(t)`
- `AIRFIELD_IMMOBILIZED(t)`

`PHYSICAL_PRESENT(t)`
=
`ARRIVED_FORWARD_AREA(t)`
+ `REPLACEMENT_ASSIGNED_AND_ARRIVED(t)`
- `AIRFRAME_LOSS_AFTER_THAT_SNAPSHOT(t)`

重要なのは、`TABLE_STRENGTH` がどの時点のsnapshotか不明なら上式へ直接代入しないこと。

## 3. 集中損失46機の扱い

Japanese Monograph No.55 の「集中中悪天候損失46機」は、開戦後331機とは別枠である。

しかし同じモノグラフは11月中旬から南方軍向け補充機148機の第一便も開始したと記す。

そのため、

- 46機の全てが第3飛行集団の12月8日OOBからさらに欠けている
- 148機の全てが12月8日までに第3飛行集団へ補充済み

のどちらも仮定しない。

### 会計

`PRECOMBAT_CONCENTRATION_LOSS_POOL_HIST = 46`

`PREWAR_REPLACEMENT_SHIPMENT_1_SOUTHERN_ARMY = 148`

ただし両者とも `UNALLOCATED` から開始する。

部隊・日時・機種が確認できた分だけ個別戦隊へ移す。

## 4. 12月7日に確認できるイベント

既知イベントは個別に状態へ入れる。

- 1戦隊の1個中隊：船団位置を見失い帰投。
  - 機体損失とはしない。
  - 燃料・整備時間・搭乗員疲労を消費。
  - `NAVIGATION/POSITIONING` 観測を1件追加。
- 98戦隊重爆3機：船団発見後、悪天候で帰投。
  - `WEATHER_ABORT`。
- 64戦隊側の船団掩護：低雲・スコールで帰投。
  - 2機未帰還。
  - 1機強制着陸。
- 同日、1戦隊側で午前・午後各1機が強制着陸で重損。
  - 修理可能性と搭乗員状態は未閉鎖。

これらは46機の一部に含まれる可能性があるため、**46機に加算しない**。46機の内数フラグを持つ。

## 5. 本世界差の適用順序

### 5.1 まず技術・練度が対応可能な原因へだけ作用

- 純粋な視界不良：ほぼ固定。
- 迷航・位置取り：航法、通信、気象支援、経験核で改善可能。
- 燃料余裕：機体航続、増槽在庫、燃料管理で改善可能。
- 機械故障：成熟度、工作公差、整備で改善可能。
- 強制着陸損傷：低速特性、脚、構造、飛行場支援で改善可能。
- 不明原因：中心線では改善しない。

### 5.2 その後に人員状態へ変換

機体1機の「救済」を、必ず熟練者1名生存へ直結させない。

結果は別々に、

- 機体救済・搭乗員救済
- 機体喪失・搭乗員生還
- 機体生還・搭乗員負傷
- 機体喪失・指揮官KIA

へ分ける。

この差が後続の自然還流・経験核撹拌へ入る。

## 6. 性能向上を戦域到着率へ使う

再走査で最初に比較するべき指標は撃墜交換比ではない。

### 集中区間

- `planned_aircraft`
- `arrived_forward_area / planned`
- `serviceable_eve / arrived`
- `experienced_leaders_arrived / planned`
- `noncombat_loss`
- `forced_landing_recoverable`
- `weather_abort`
- `navigation_miss`

### 開戦後反復区間

- `serviceable_D+1 / launched_D`
- `serviceable_D+2 / initial_serviceable`
- `crew_experienced_core_retained`
- `replacement_low_skill_share`
- `base_forwarding_delay`

これが「消耗が軽いのに後年の大きな進歩へつながらない」を検査する最初の状態列になる。

## 7. 当面の二つの枝

史料時点の不確実性を潰すまで、Dec 8 opening strengthは一値に固定しない。

### Branch H1: OOB表は集中後の現有名目に近い

46機の多くは既にOOB表へ反映済み。追加控除しない。

### Branch H2: OOB表は定数・編制表に近い

46機の一部がOOB表外の実可動減として残る。ただし補充到着分を相殺してから可動を求める。

Phase 1の既知出撃数を満たせない枝は棄却する。

これにより、出撃記録そのものを下限制約として利用できる。
