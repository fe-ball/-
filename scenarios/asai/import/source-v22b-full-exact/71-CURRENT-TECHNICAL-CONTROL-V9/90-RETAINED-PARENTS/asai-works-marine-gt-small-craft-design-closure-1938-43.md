# 舶用GT小型高速艇 design closure 1938–43 — 船型・軸系・prop・marine qualification

> **v29 current parent. 状態：TECHNICAL DESIGN REBASED / E5 MARINE-QUALIFICATION ARCHITECTURE CLOSED / PURE-GT PRODUCTION NOT CENTRAL / E6 50t PROCUREMENT CONDITIONAL。**
>

> **v41 E5 product-size warning.** 本v29本文の `E5-S 1,300hp` は、v41 standard E5-S=7.6kg/sでは成立しない（Ni installed centralでも必要flow≈9.29kg/s）。**1,300hp出力・それに依存する船速/燃料行はdownstream H→AまでCONDITIONAL**。one-GT boost architecture、salt/intake、shaft/prop、qualification methodologyは保持する。

> 旧current=`asai-works-marine-gt-small-craft-rebaseline-1934-43.md` は史実較正と一次Crouch計算の provenance として保持する。本稿はその未閉鎖だった水槽抵抗/trim、prop/cavitation、installed mass、salt MTBO、純GT量産、50t大型艇要求を再監査する。

## 0. 結論

1. **E5の中央を「2×1,300hp GT＋350hp diesel・3独立軸」から外す。** 独立三軸は合流歯車を消すが、巡航時の停止GT prop dragと、巡航専用diesel propの全速点matchingを消さない。
2. 1938–41の低リスク中央は、**既存高速艇の二本のpiston shaftを巡航/後進にも使い、中央一軸だけE5 GT boostを足すmarine-qualification艇**。これは後世MGB 2009の構成と同じ問題分解で、浅井世界線ではGTそのものが早いので試験時期だけ前へ出る。
3. 二基GTの27t高性能枝は成立するが、停止GT propを低抵抗化する**可変pitch/featheringまたは同等のshaft/prop措置**が追加gate。これを払わず「350hp diesel一本で15kt巡航」とはしない。
4. 43–45ktは**平水・clean hull・full-load trialの帯**として扱う。operating/service speedと同義にしない。戦時PT実績ではtrialとoperatingに8–10kt差を見込む証言があり、40kt実用を要求するならtrial 48–50kt級を設計要求に置く必要がある。
5. 50t E6案は4×45cm・長脚の**technical shadow**として成立するが、5,200hpで「40kt service保証」はしない。満載50–55tでtrial 42–44kt級が中央。40kt serviceを硬要求するなら出力約6,000–7,000hp級または軽量化が必要。
6. 純GTは技術実証/短距離sprintには残すが、**E5/E6期の通常魚雷艇量産中央には採用しない**。部分負荷燃費、後進、停止prop drag/CPPの追加費用がhybridに負ける。
7. E5/E6の完全舶用据付重量は旧1.5–2.5 kg/kWを撤回。1947 Gatric較正を踏まえ、**E5中央3.1 kg/kW級、E6中央2.5 kg/kW級**（GT path一式、fuel/shaft/prop除外）の設計帯へ戻す。

## 1. H — 史実較正

### 日本

- 第一号型：満載約20.5t、18.3×4.3m、約1,800hp、38–38.5kt、45cm魚雷2本。V底木造で、小型高速艇そのものは成立している。
- T-51大型枝：32.4m級、75–85t級、約3,680hpで29–30kt級。大型化・重量・機関/軸系統合の失敗側較正に置く。

### 米PT / 英marine GT

- Elco/Higginsの78–80ft級は50t前後のfull military loadで約4,000–4,500hp、40–45kt級。1945比較試験ではElco 28×29in級、Higgins 29×26in級prop、約2,270–2,680rpmで40–45ktを記録している。
- 同試験の戦歴保有者は、trialと実運用speedに**8–10kt**差を見込むべきと述べ、40kt serviceなら50kt trial付近を望んだ。よって「試運転43kt=実戦43kt」を禁止する。
- Metrovick Gatric 2,500shpは、engine+gearbox約2.77 lb/shp、艇内installation一式約5.40 lb/shp。後者は約**3.28 kg/kW**で、旧small-craft 1.5–2.5 kg/kW完全据付値は軽すぎる。
- MGB 2009はpiston enginesをcruise/asternに残し、独立GT shaftをboostに使った。small-craft GT初期試験の低リスク構成として強い比較対象。

史料アンカー：Office of Naval History, *An Administrative History of PTs in World War II* (1946), 1945 comparative trials；*Gas-Turbine Propulsion in a Naval Vessel*, Nature 160 (1947)；Institution of Marine Engineers, Gatric installation paper；日本造船学会系戦時モーターボート要目。

## 2. 速度の帳簿 — trial / operatingを分離

一次比較は従来どおり `V = C sqrt(P/Δ)` を使うが、用途を限定する。

- **Crouch**：clean-water full-load trialの一次比較。
- **水槽/実艇**：LCG、deadrise、trim、spray、turn、sea-state、prop ventilationを閉じる。
- **operating speed**：汚損、兵装増、海象、機関劣化、戦術運転を含む別値。

### E5 27tでの感度

- 2,700hpなら C=4.1/4.2/4.3 → 約41.0/42.0/43.0kt。
- 3,100hpなら C=4.1/4.2/4.3 → 約43.9/45.0/46.1kt。
- 旧2,950hpは約42.9/43.9/44.9ktだが、軸/prop matching問題を解かず総出力だけ足した値なのでcentralから外す。

### E6 50–55tでの感度

5,200hp、C=4.2–4.4なら、おおむね**42–45kt trial**。中央はfull-load 50–55t、C≈4.25–4.35として**42–44kt**を置く。

40kt operatingを要求してtrial 48–50ktを置くなら、50tで必要出力はC=4.2–4.4に対し概ね**6,000–7,100hp**。したがって5,200hp案は「4本・長脚・40kt service全部取り」ではない。

## 3. E5 — marine qualification中央

### 3.1 低リスク中央：1GT boost test boat

目的は量産魚雷艇の完成ではなく、**salt/intake、gear、shaft、prop、start/stop、hot-section inspectionを海上で閉じること**。

- full-load：**25–27t級**。
- hull：第一号型から一段拡大した木造V底。L≈19–20m、B≈4.5–4.8mを探索帯。
- outer shafts：既存の高速piston plantを二軸に残し、cruise/astern/harborを担当。marine qualification段階では史実型のgasoline plantを残してよい。
- center shaft：**E5-S marine GT 約1,300hp short/sprint rating**＋free power turbine＋single reduction＋freewheel。
- full-power総出力：base plant次第で約2,700–3,100hp級。
- trial：**42–46kt候補**。合否は最高値でなく、salt・gear・prop・restartを再現できること。

この構成ならcruise時にidleになる大径GT propは一枚だけで、二枚を引きずる旧中央より検証しやすい。

### 3.2 高性能branch：2GT + cruise engine

旧2×1,300hp GT案を完全廃棄はしない。ただし条件を追加する。

- outer：E5 GT 2×1,300hp。
- center：cruise engine 500–700hp級を設計比較。旧350hp固定は撤回。
- **必須gate**：GT propsの低速dragを抑える可変pitch/feathering、または同等のprop/shaft architecture。
- full speed時もcenter propのadvance ratioを外さないpitch schedule/gear scheduleが必要。

1930年代末には舶用hydraulic CPPは国外で実用入口にあるため概念は時代外れではない。ただし日本高速艇用のhub強度、oil passage、seal、blade-root fatigue、salt maintenanceは**浅井/艇屋側の新規受領項目**で、量産済みとみなさない。

## 4. hull / tank / trim gate

### 4.1 E5 25–27t探索帯

- L/B：**4.1–4.5**。
- transom deadrise：**12–16°**を中央探索帯。
- LCG：transomから前方へ**0.35–0.42 L**を振る。
- design-speed running trim：**3–5°**を目標帯。
- clean calm-water trial：40/43/46kt点で抵抗、trim、spray、porpoising onsetを採る。

### 4.2 E6 50–55t探索帯

- wooden double-diagonal / laminated structureを初期中央。all-metal T-51をそのまま写さない。
- L≈**24–25m**、B≈**5.5–6.0m**、L/B≈4.1–4.5。
- deadrise 12–16°、LCG 0.35–0.42Lを同じ実験計画で振る。

### 4.3 合格条件

最高速一点ではなく、次を同時に満たす。

- full military loadでtarget trial speed。
- 40kt域までsteady porpoisingなし。
- ±燃料/魚雷消費によるCG移動でtrim破綻なし。
- turn中に外軸propが継続ventilationへ落ちない。
- rough-waterではspeedを落としても構造slam/操舵が受領帯内。

水槽は「Crouch Cを当てる儀式」ではなく、**LCG×deadrise×prop/shaft angleの組合せを落とす試験**とする。

## 5. shaft / prop / cavitation gate

1945 US PT試験の28–29in propと2,270–2,680rpmをscale anchorに使う。

### E5 outer GT shaft

- prop D：**0.74–0.80m**。
- shaft rpm：**2,050–2,300rpm**。
- pitch ratio：0.95–1.10級から水槽/実艇で詰める。
- 3-blade broad-areaを初期中央。expanded area ratioは**0.65–0.72級**を比較。
- 44kt、D=0.76m、2,200rpmで advance coefficient J≈0.77、tip tangential speed≈88m/s級。歴史的PTの運転帯と同程度。

### E6 outer GT shaft

- prop D：**0.86–0.94m**。
- shaft rpm：**1,750–1,950rpm**。
- 3 broad-bladeと4-bladeを比較。4-bladeはdiameter/pressure pulseを下げられるがhub/drag/製造を払う。
- 44kt、D=0.90m、1,850rpmで J≈0.77、tip tangential speed≈87m/s級。

### cavitation/ventilation

高速浅吃水艇では「完全無cavitation」を要求しない。合格基準は、

- thrust collapseを起こすsheet cavitationへ入らないこと、
- turn/波浪でair drawを継続しないこと、
- blade-root/shaft bearingの振動とerosionが受領時間を超えること。

prop diameterだけ大きくして解決せず、blade area、pitch、shaft angle、immersion、LCG/trimを同時に振る。

## 6. installed mass gate

旧 `艇は1.5–2.5 kg/kW` を**裸機/gear寄りの値と完全installationの混同**として撤回する。

### 定義

ここでの `marine installed GT path` は、gas generator、free power turbine、reduction gear、clutch/freewheel、mount、防振、oil/start/control、必要なshort intake/exhaustまで。**fuel、long shaft、prop/rudderは別**。

- E5：**2.8–3.4 kg/kW、中央3.1**。
- E6：**2.2–2.8 kg/kW、中央2.5**。

これはGatric complete installation約3.28 kg/kWをH anchorにし、purpose-designed short-duct craftとE6成熟で下げる設定値。

### E5 2GT branchの重量感度

2×1,300hp = 約1.94MWなのでGT pathsだけで中央**約6.0t**。cruise engine、shaft/prop、fuelを足すと推進系は軽々3–4tでは済まない。27t艇には入るが、**「GTが軽いから重量問題は消える」枝ではない**。

### E6 2GT branch

2×2,300hp = 約3.43MW。GT paths中央**約8.6t**。600hp級cruise engineとshaft/propを含めると推進系**10–12t級**を見込む。50–55t艇なら成立余地がある。

## 7. fuel / range

### E5

E5軸効率22.5%級ならfull-power theoretical SFCは約0.37kg/kWh級。GTを20min sprint、cruiseはpiston/diesel側とする構成なら、**1.4–1.6t fuel budgetは技術試験/短距離戦闘艇として成立余地**がある。ただしbase piston fuelとGT keroseneを別tankにする試験艇ではtank/配管重量が増える。

### E6 50–55t

600hp級cruise engineが15ktで約500–600hpを必要とする旧計算をそのまま使う場合、5–6t fuelはおおむね**35–45h級gross endurance**。15ktなら約525–675nm gross。dash・reserve・sea marginを引き、planning rangeは**450–600nm級**を中央とする。

旧「500–800nm級の行動半径/航続」は、radiusとrangeを混同し上端を盛っているため撤回。800nmは低速化、より大きなfuel fraction、または船型/巡航機関の追加改善が要る。

## 8. salt / intake / MTBO gate

GT艇はcruise主機ではなくboostなので、航空/陸上機と同じhour数を要求しない。重要なのは**salt exposureごとの再現性とhot-section damageの進行を測ること**。

### intake

- spray separator + inertial turn + washable mesh/demister + drainを基本。
- clean pressure loss：**≤1.5–2% total pressure**目標。
- wet/salt fouled：**≤3%**を受領上限候補。
- compressor washを通常整備へ組み込み、wash前後のcorrected flow/pressure ratioを記録する。

### E5 qualification

- 1,300hpは**20–30min sprint rating**。
- marine cumulative test：**150h級**をlimited-service gate。
- hot-section visual/dimensional inspection：50h級。
- salt exposure 10–20h相当ごと、または濃いspray sortie後にcompressor wash/inspection。
- 150h到達は「fleet MTBO 150h保証」ではなく、test/high-end craftでcatastrophic salt failureがない最低線。

### E6 qualification

- 2,300hp short/sprint、continuousは**2,000–2,100hp級へderate**。
- cumulative marine qualification：**300h級**。
- hot-section inspection：100h級。
- design TBO target：**500h級**。実艦fleet平均として自動昇格させない。

Marine qualificationはsaltだけでなく、gear tooth pitting、bearing temperature、seal leakage、freewheel/clutch transient、intake water ingestionを同じlogで取る。

## 9. 純GT 27t — technical yes / production no

旧3×900hp pure-GTはpower/weightだけなら成立する。しかし通常魚雷艇では、

- low-load SFC、
- astern/harbor、
- idle shaft prop drag、
- CPP/reversing gear追加、
- three-GT maintenance burden

を同時に払う。

したがって**E5/E6期の通常量産中央には採用しない**。short-range interceptor / engine demonstrator / record craftとしてconditional shadowに残す。後にCPPとpart-loadが別論点で大幅改善した場合のみ再OPEN。

## 10. E6 50–55t large MTB technical shadow

### 10.1 requirement

T-51の問題を「日本は大型艇を作れない」と読まない。要求を分ける。

- 45cm torpedo **4本**。
- 15kt級long cruise。
- heavy gunboat化しすぎない。
- clean full-load trial 42–44kt級。
- 40kt serviceは**別の高出力requirement**。

### 10.2 hull / mass

- full-load：**50–55t、中央52t**。
- L 24–25m、B 5.5–6.0m。
- wood double-diagonal/laminated first; GFRPは次論点。
- 45cm魚雷は1本約0.75–1.0t級なので4本＋rackで概ね4t級を見込む。53cm×4をbaselineにしない。

### 10.3 propulsion branch

High-power branchは2×E6 GT＋600hp級cruise engineを維持してよいが、**CPP/featheringまたは同等のlow-speed prop drag対策をmandatory**とする。対策なしならone-GT boost + two conventional propulsion shaftsへ戻す。

- 2GT branch：2×2,300hp short + center 600hp級 = nominal 5,200hp。
- calm full-load trial：42–44kt中央。
- continuous/service high-speedはderateとsea-stateを別帳簿。

### 10.4 armament central shadow

技術比較の標準loadは、

- 4×45cm torpedo、
- 25mm single 1基、
- light MG 1–2基、

まで。25mm増設、爆雷、大型無線/radarを足す場合はfuel/speed/CGから同重量を戻す。**4 torpedo + heavy gunboat + long range + 40kt serviceを同時に無料で取らない。**

### 10.5 procurement status

technical designは成立。しかしactual requirement、制式採用、量産数、1941-12-08以後の配備/戦果はFROZEN。したがって**E6 50–55tはPROCUREMENT CONDITIONAL**のまま。

## 11. CLOSED / CONDITIONAL / NEXT

### CLOSED / REBASED

- trial speedとoperating speedを分離。
- old 2GT+350hp independent-3-shaft centralを撤回。
- E5 first marine qualificationはone-GT boost architectureをcentral化。
- shaft rpm/prop diameter/pitch-areaの初期設計帯を設定。
- old small-craft full-installation 1.5–2.5 kg/kWを撤回しE5/E6 mass bandを再設定。
- salt/intake/inspection/qualification hour gateを設定。
- pure-GT standard mass productionをE5/E6では**NO**に閉鎖。
- 50–55t E6 technical shadowのhull/armament/range/power tradeを閉鎖。
- 5,200hpで40kt service保証をしない。

### CONDITIONAL

- high-power 2GT craft用の高速marine CPP/featheringの国内実装。
- E6 50–55t actual procurement/series production。
- 1941-12-08以後のactual OOB/production/deployment/combat。

### NEXT

**GFRP艇体**：v30 `asai-works-gfrp-small-craft-hull-rebaseline-1940-46.md` で再基底化済み。1942–43はsection/8–12m demonstrator、20–30t full high-speed hullは1943–44+ conditional、50–55t full-GFRP E6は1946+ conditional。
