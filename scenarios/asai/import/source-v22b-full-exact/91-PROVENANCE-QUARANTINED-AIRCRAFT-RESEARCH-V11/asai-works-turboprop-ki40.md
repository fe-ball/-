> **v45 current authority:** E6-S-N-T standard is **1,500hp @7.8kg/s**. Dedicated H→A is now closed for the single-engine development: **625–650km/h @8km**, practical internal-fuel range **3,000–3,600km**. ~1,600hp high-flow short trim may reach **640–660km/h @8km** conditionally.

# 高高度戦略偵察機「Ki-40」発展型——機体側の詰め（E6-S-N-T）

> **v45 supersession note**：v5/v26の高度shadowをv44 product ratingへ再伝播済み。旧1,700hp・8km 730–990shp・standard 650–675km/hはsuperseded。現行値は本稿§4および `asai-works-e6-s-aircraft-h-to-a-rebaseline-1938-42.md`。


需要の高い一機（`turboprop-program` §8 が「本命の最初」とした司令部偵察）を、`jet-interceptor-airframe` と同じ深さで機体側まで詰める。発動機はカタログの **E6-S-N-T**（E-6・小型・Ni高温・プロペラ／**1,500馬力 standard**、~1,600馬力 high-flow short conditional、`turboprop-catalog`）。ターボプロップの長所（滑らか・灯油・高高度）が最も活きる機種。規則は `tensei-engineer-kufu-shu.md`、数値は要素モデルと物理計算から【確認済み】【物理】【設定】【要確認】。性能はその時期（1940–42）の Ki-46 で測る。

---

## 1. 位置づけと所管

- **陸軍 司令部偵察機**（Ki-15＝九七式司偵→Ki-46＝百式司偵の系統）。社内通称「遠耳（とおみみ）」【設定】。軍側は **Ki-40＋年式制式名称**で扱い、固有愛称は付けない。史実で未成に終わった三菱Ki-40司令部偵察計画枠が、浅井E系を得てこの単発TP司偵へ収束したものとして扱う。
- **役割**：無武装（または最小）で、速度・高度・航続で逃げる戦略偵察。撮影・索敵。ターボプロップの素性が一番効く用途——**高高度の出力保持・灯油の長航続・低振動の写真鮮鋭**。
- 八八式改造の試験機（`aviation-airframes` §1c）で示した「振動が減ると写真が鮮鋭」を、専用設計で活かす完成形。

---

## 2. 発動機——E6-S-N-T（高高度に振ったNi系）

カタログの **E6-S-N-T**（`turboprop-catalog` §4）。E-6小型核（**7.8 kg/s design**）＋**ニッケル系統で入口温度を上げ（約920℃）**＋独立動力タービン＋高比率減速ギヤ＋定速可変ピッチプロペラ。

- 軸出力：**1,500馬力 standard**【物理】（v44 installed shaft accounting）。~1,600馬力はhigh-flow short conditional。燃料基準shaft efficiencyは約**23.5%**、BSFC約**0.356 kg/kWh**。旧1,700馬力／26.5% product表記はsuperseded。
- **なぜNi高温か**：偵察は高度が欲しい。Ni系統で入口温度を上げると、**高度で出力を保ち**、上昇限度と高高度速度が伸びる（`core-elements` の材料系統×格付け＝高価値・全力・高温）。備蓄Niを最良機に充てる正当な使い道。
- 燃料は灯油（不揮発・高密度・戦略燃料）。難所は減速ギヤの捩り振動と重量（時計由来の精度が効くが消えない＝要確認）。

---

## 3. 機体構成

- **単発・与圧複座・引込脚・全金属応力外皮**。機首にターボプロップ（プロペラ牽引）、与圧キャビンに操縦者と偵察員。
- **高アスペクト比・薄翼**：高高度は空気が薄く揚抗比が要る→細長い翼。薄翼で高速の圧縮性に備える（約0.7マッハから、`aviation-forms` §8）。
- **低振動の活用**：往復部が無いので、垂直・斜めの写真機が鮮鋭（八八式試験の質的改善）。乗員疲労も減る。
- **双発の別変種**：生の速度を Ki-46級に振るなら 2×E6-S-T（非Ni中庸）の双発もある（`turboprop-catalog`）。本稿は**高高度・長航続の単発Ni型**＝戦略偵察の本命を詰める。

---

## 4. 性能（重量内訳・高度別・航続）

### 4a. 重量内訳（v45 current working band）【物理／設定】

旧「powerplant約600kg／全備3,700kg」の一点値は廃棄する。v45は同じ7.8kg/s gas pathを維持するので、rating低下だけを理由にエンジンを軽くしない。

| 区分 | v45 working band | 備考 |
|---|---:|---|
| E6-S-N-T installed powerplant | **640–830 kg** | core+power turbine+gear+prop+mount/duct |
| zero-fuel aircraft | **約2.5–2.7 t** | 与圧・写真・通信・乗員を含む |
| internal kerosene | **約1.3–1.4 t** | mission/reserveで使用率を分ける |
| normal clean recon | **約3.9–4.1 t** | v26 airframe anchorを維持 |

### 4b. 高度別 最高速度【物理／設定】

| 高度 | Ki-40（E6-S-N-T standard） | 読み |
|---|---:|---|
| 海面 | **約490–520 km/h** | old 510–540をpower-scale |
| 6 km | **約555–595 km/h** | old 580–620をpower-scale |
| **8 km** | **625–650 km/h** | v45 standard canonical |

8km shaft-power shadowは**645–870shp**。旧730–990shpはsuperseded。1,600hp high-flow short trimを同じairframeへ当てると**640–660km/h @8km**のshadowだが、continuous standard値にはしない。

### 4c. 航続・上昇限度【物理／設定】

- **航続**：v44 BSFC 0.356kg/kWh、全備3.9–4.1t、内部灯油1.3–1.4t、mission-usable 80–85%、L/D 11.5–12.5、ηp 0.80–0.82のBreguet cross-checkから、**実用内部航続3,000–3,600km級**。旧5,000–6,000km routine値は使わない。増槽/ferryは別payload-reserve計算。
- **上昇限度**：10km power shadowは480–720shp。exact service ceilingはcompressor/prop/与圧map未計測のため一点lockしない。**~11km級 working**までは許容するが、旧11.5–12kmをv45 exact値として引用しない。

---

## 5. 戦い方——速度・高度・航続で逃げる

- **単独・長距離進出**：地上管制に頼らず、洋上・大陸奥地へ単機で進出。灯油で航空ガソリンの細る後期も飛べる（`asw-effect` §燃料置換）。
- **高度で振り切る**：偵察高度8〜10 kmは、同時期ピストン邀撃機（全開高度6 km級）の上。捕まえに上がってくる頃には離脱。
- **撮影**：低振動で垂直・斜め写真が鮮鋭。高高度から広域を一度に。
- **無武装の合理**：武装・防弾を積まず、その重量を燃料・高度・速度へ。被弾前提でなく被発見前に去る。

---

## 6. 同等品と位置

| 項目 | Ki-40（E6-S-N-T） | Ki-46-III（百式司偵三型）【確認済み】 |
|---|---|---|
| 発動機 | 単発ターボプロップ **1,500馬力 standard**・灯油 | 双発ピストン 2×1,500馬力・航空ガソリン |
| 最高速 | **625–650 km/h（8 km）** | 約630 km/h（6 km） |
| 上昇限度 | **~11 km級 working／exact未lock** | 約10,700 m |
| 航続 | **約3,000–3,600 km（内部・実用）** | 約4,000 km |
| 写真 | 低振動で鮮鋭 | 双発振動 |
| 燃料 | 灯油（戦略燃料） | 航空ガソリン（隘路） |
| 時期 | 1940–42（E-6） | 1942〜 |

速度は同等〜やや上だが跳躍ではない。差は**高度・航続・灯油・写真の鮮鋭**に出る。史実の実用ターボプロップ（1945〜）に対し**約8〜12年前倒し**で、しかも単発で Ki-46 双発の仕事をする。

---

## 7. 弱点・要確認

- **減速ギヤの重量・捩り振動**（出力重量比の実数を縛る最大の要確認）。
- **Ni系統の入口温度上限**（920℃が妥当か、備蓄Niの消費年数）。
- **プロペラの圧縮性**（高度8 kmで約0.62〜0.65マッハ頭打ち＝速度の天井）。
- **単発の被弾抗堪**（双発より冗長性が無い。ただし高高度・速度で被発見前に去る前提）。
- 与圧・高高度装備の重量、写真機の実装、各高度の実速度・実上昇率。

---

## 8. タグ・次の作業

- 【確認済み】：Ki-46-III（双発・約630 km/h・航続約4,000 km・上昇限度約10,700 m）、Ki-15、実用ターボプロップ史実1945〜、灯油の物性。
- 【物理】：v44 installed shaft power、高度shadow、cube-root speed propagation、Breguet range cross-check、重量内訳。
- 【設定】：固有名「Ki-40／遠耳」、Ni高温920℃、各機体配分。standard rating/性能帯はv44/v45物理監査を優先。
- 【要確認】：減速ギヤ重量、Ni入口温度上限、プロペラ圧縮性の実頭打ち、与圧・写真機の実重量、双発変種の比較。
- 次：**残るE6-S H→A**——凱風二一型などS-core fighter、および2×E6-S-T双発高速偵察。天山はv45で再計算済み。

---

## 9. 索引への接続

- 親：`asai-works-turboprop-catalog.md`（E6-S-N-T の素性）／`asai-works-core-elements.md`（材料系統×格付け）。
- 機体側：`asai-works-turboprop-program.md`（諸元総覧）／`asai-works-turboprop-first.md`（E-5初期の偵察）／`asai-works-aviation-airframes.md`（八八式改造の試験）。
- 対：`asai-works-jet-interceptor-airframe.md`（ジェット側の同深度の機体詰め）。
