# E4/E5 product mass-flow / size rebaseline 1931–37 — v41

> **v43 downstream compressor update.** The P1-3 map gate left open by v41 is now closed in `asai-works-e5-e6-compressor-operability-rebaseline-1934-41.md`. E5 standard remains 7.6 kg/s / 1,000 hp; E5-S-HF ~8.08 kg/s is compressor-feasible; 9.29 kg/s marine 1,300 hp remains outside S.

> **v41 current authority. 状態：PRODUCT MASS-FLOW / SIZE REBASED / OUTPUT TARGETS ACCEPTED / COMPRESSOR MAP STILL OPEN / NO DOWNSTREAM H→A.**
>
> v40で冷却抽気・圧損・mechanical/accessory debitを払った `w_inst` を確定した。本稿はその値を固定入力として、E4 500 kWとE5 1,000 hpを、質量流量、圧縮機寸法・回転数、乾燥重量、free-power-turbine/reducer、燃料、cost、lifeの側から再受領する。航空機・艦船の性能・採用はまだ変更しない。

## 0. 結論

1. **E4 500 kWはACCEPT。** 数学的minimumは約6.60 kg/sだが、製品design flowは **6.7 kg/s** とする。v40 central `w_inst=75.73 kJ/kg` で約507 kWとなり、約1.5%のcentral marginを持つ。
2. **E5 1,000 hpはACCEPT。** Ni-only minimum 7.15–7.25 kg/sを標準製品流量にはせず、**E5-S standard gas path = 7.6 kg/s** とする。これでNi@800は約1,063 hp、non-Ni@800 fullは約1,014 hp、non-Ni@765 quantityは約952 hp。
3. E5の標準headline ratingは **1,000 hp**。Ni余剰は原則、headline出力増ではなくhot/high margin・寿命・劣化余裕へ配る。非Ni量産線@760–770℃は **約950 hp** を自然な連続格付けとする。
4. E4/E5とも既存の **S級（約5–8 kg/s）内**に残る。したがって新Mコアへの移行ではなく、同一寸法級内のannulus/impeller/shaft re-sizingで閉じる。
5. 一次外形はE4 **0.66–0.74 m径 / 2.0–2.4 m長**、E5 **0.68–0.76 m径 / 2.0–2.3 m長**をworking envelopeとする。これはproduct packaging coordinateであり、compressor map合格値ではない。
6. E4初期industrial productの乾燥重量は旧0.75 tから **0.80–0.90 t、中央0.85 t**へ再基線化。E5-S-Tの `core + power turbine + reduction + accessories` は **390–460 kg、中央425 kg**、prop/mount/duct込みinstalled powerplantは **510–640 kg、中央575 kg**へ置く。
7. 既存のE5-S **1,300 hp marine**はこの標準S gas pathでは成立しない。Ni installed centralでも約9.29 kg/sを要しS級上端を越えるため、後続H→Aで **約1,000–1,060 hpへ再格付け**するか、**別の高流量/M寄りcore**へ分離する。v41では艦艇性能をまだ再計算しない。
8. exact axial-stage count、stage loading、surge margin、start/acceleration、bleed/VSV、clearanceは **P1-3 compressor operability**に残す。v41で固定する段数・rpm・tip speedは一次size coordinateである。

## 1. 固定入力 — v40 installed cycle

| case | gross comparison | current installed shaft coordinate | fuel-based shaft η |
|---|---:|---:|---:|
| E4 710℃ | 93.5 kJ/kg / 18.37% | **75.73 kJ/kg** | **15.03%** |
| E5 Ni 800℃ | 125.5 / 22.58% | **104.32** | **19.25%** |
| E5 non-Ni 800℃ full | 125.5 / 22.58% | **99.47** | **18.75%** |
| E5 non-Ni 765℃ quantity | 113.8 / 21.86% | **93.45** | **18.41%** |

旧 `93×5.4≈500 kW`、`126×6≈756 kW` はgross-derived provenanceであり、製品shaft proofには使わない。

## 2. E4 — 500 kW product closure

### 2.1 mass-flow

- target power: 500 kW.
- central minimum: `500 / 75.7326 ≈ 6.602 kg/s`。
- product design flow: **6.7 kg/s**。
- central shaft capability: **507.4 kW ≈680 hp**。
- 旧5.4 kg/sからのflow増加は約24%。S級内部のresizeであり、新core familyにはしない。

500 kWをちょうど割る6.60ではなく6.7を置くのは、製造公差・ambient・汚れを何も払わない一点設計を避けるため。これはflat-rating保証ではなくsea-level design-point marginである。

### 2.2 inlet / compressor working geometry

一次annulus計算は `rho=1.225 kg/m3`, `Vx=110 m/s`, hub/tip=0.50 を共通仮定とする。

- annulus area ≈ **0.0497 m²**。
- inlet tip diameter ≈ **0.291 m**。
- hub diameter ≈ **0.145 m**。
- inlet blade height ≈ **72.6 mm**。

E4の既存architectureはaxial + centrifugal。PR4.5を一次的に、

- 2–3 stage axial booster: PR≈**1.6**,
- centrifugal HP stage: PR≈**2.81**,
- centrifugal tip speed working coordinate: **~420 m/s**,
- gas-generator speed: **~16,000 rpm**,
- corresponding impeller diameter: **~0.50 m**

へ分ける。ここからcasing/collector/combustor/accessory allowanceを払い、**overall diameter 0.66–0.74 m**をworking bandとする。

このsplitは「P1-1でサイズが破綻しないこと」を見るための座標であり、2段か3段か、diffuser/IGV incidence、surge line、start mapはP1-3で閉じる。

### 2.3 mass / fuel / product meaning

E4初期商品は航空裸機ではなく、定置・ポンプ・舶用も含むrobust industrial productで、独立動力タービン・燃焼器・補機を持つ。旧0.75 tはflow resize後には軽すぎるため、

- dry product engine: **0.80–0.90 t**, central **0.85 t**。
- specific dry mass at 500 kW: **1.6–1.8 kg/kW**。

へ更新する。

LHV=43 MJ/kgとv40 ηを使うと、simple-cycle central SFCは **0.557 kg/kWh**、500 kW時の燃料は **約279 kg/h**。旧230 kg/h級はgross efficiency由来としてsuperseded。regenerator版はP1-2で別監査する。

## 3. E5 — standard S gas path closure

### 3.1 why 7.6 kg/s, not 7.25

v40の7.25 kg/sはNi@800で1,000 hpを満たすminimum近傍のresize coordinateだった。製品gas pathをそこに固定すると、non-Ni full/quantity lineが毎回別flow設計になる。

そこで標準Sコアは **7.6 kg/s**へ置く。同一gas path上で材料・TIT格付けを変える。

| E5 rating line | `w_inst` | 7.6 kg/s shaft | product interpretation |
|---|---:|---:|---|
| Ni @800℃ | 104.32 kJ/kg | **792.9 kW = 1,063 hp** | standard headline 1,000 hp; marginをlife/hot-highへ |
| non-Ni @800℃ full | 99.47 | **756.0 kW = 1,014 hp** | 1,000 hp full ratingは成立。ただしv39 `L_core=150–300 h` |
| non-Ni @765℃ quantity | 93.45 | **710.2 kW = 952 hp** | quantity/continuous central **~950 hp** |

1,000 hpを成立させる必要flowはNi約**7.15**、non-Ni800約**7.50**、non-Ni765約**7.98 kg/s**。量産非Niを常時1,000 hpに押すとS級上端へ張り付くため、標準量産格付けにはしない。

### 3.2 inlet / compressor working geometry

同じ一次annulus仮定で7.6 kg/sは、

- annulus area ≈ **0.0564 m²**。
- inlet tip diameter ≈ **0.309 m**。
- hub diameter ≈ **0.155 m**。
- blade height ≈ **77.4 mm**。

となり、極端に薄いfront bladeへは落ちない。

E5 PR6のworking split：

- 3–4 stage axial booster: PR≈**1.8**,
- centrifugal HP stage: PR≈**3.33**,
- centrifugal tip speed coordinate: **~455 m/s**,
- gas-generator speed coordinate: **~17,500 rpm**,
- impeller diameter: **~0.50 m**。

overall product envelopeは **0.68–0.76 m径 / 2.0–2.3 m長**。centrifugal-stage PR3.33はP1-1のdesign coordinateであり、単段mapの実証済み値と同一視しない。P1-3では必要ならbooster PRを増やしcentrifugal burdenを下げる。

### 3.3 mass / reducer / prop installation

既存v5のE5-S-T `core+power turbine+reducer+accessories = 360–440 kg` は、6 kg/s/gross-derived productを含むため上方修正する。

- engine assembly: **390–460 kg**, central **425 kg**。
- propeller: **90–130 kg**。
- mount / duct / local installation: **30–50 kg**。
- installed powerplant: **510–640 kg**, central **575 kg**。

1,000 hpの出力軸トルクは1,200 rpmなら約 **5.93 kN m**。flowが6→7.6 kg/sへ増えても、headline shaft powerを1,000 hpに据える限りreducer transmitted torqueが26.7%増えるわけではない。主なtaxはgas generator/free-turbine flow areaとcasing。高速prop用1,100–1,300 rpmに対し、free power turbineのworking speedを15–18 krpm級に置くなら総減速比は概ね **12–16:1**。exact gear architectureはinstallation別に閉じる。

### 3.4 fuel

- Ni@800, 1,000 hp: SFC **0.435 kg/kWh**, fuel **~324 kg/h**。
- non-Ni@800 full, 1,000 hp: **0.447 kg/kWh**, **~333 kg/h**。
- non-Ni@765 quantity, 7.6 kg/s / ~952 hp: 約**323 kg/h**（同じηで出力が下がるため）。

Niを常に1,063 hpで売るより、1,000 hp common gearbox/ratingを保ち、Niの熱余裕を寿命・高温高地・劣化へ使う方が製品系列を単純化できる。

## 4. cost / life gate

### cost

E4 5.4→6.7、E5 6.0→7.6はflowで約24–27%増だが、外形・重量は同率では増えない。power targetが固定なのでreducer/出力軸は全流量比例で肥大しない。working procurement burdenは旧product basis比 **+10–20%級**をcost-ledger用の暫定帯とし、「別core familyを起こすほどのcost cliffではない」と判定する。具体単価は未固定。

### life

v41はPR/TIT/cooling fractionとv39 metal-temperature/life ladderを変更しない。流路面積とcooling passagesを新flowに合わせてscaleし、tip speed/stressをworking band内に置く限り、resizeそのものを理由に `L_core` を下げない。

保持：

- E4: **250–450 h**。
- E5 Ni@800: **400–700 h**。
- E5 non-Ni@800 full: **150–300 h**。
- E5 non-Ni@760–770 quantity: **350–600 h**。

ただしcompressor/turbine disk critical speed、bearing DN、blade vibrationはP1-3/rotordynamicsで再受領する。

## 5. downstream conflict ledger — v41では伝播しない

### 5.1 E5-S-N old 1,130 hp aviation product

Ni centralで1,130 hpには約 **8.08 kg/s**が必要。標準7.6 gas pathから外れるため、旧1,130 hpを標準E5-S-N headlineとして自動保持しない。選択肢は、

- common 7.6 coreで~1,000 hp rating＋Ni margin、
- 1,050–1,060 hp級のlimited high-end rating、
- 8.1 kg/s級high-flow S derivative

のいずれか。航空H→Aで機体要求から選ぶ。

### 5.2 E5-S old 1,300 hp marine sprint

Ni centralでも約 **9.29 kg/s**、non-Ni800で約9.75 kg/sを要する。これは現行S bandを明確に越える。従ってv29 small-craftの「1,300 hp E5-S」は**出力だけconditional**へ戻す。艇architecture、salt test、shaft/prop methodologyそのものは保持する。

v41時点で船速・総出力・艇重量を改変しない。後続H→Aで、

1. standard E5-S ~1,000–1,060 hpへ再格付けして艇側を再計算、または
2. E5-M/high-flow derivativeを別productとして受領

する。

## 6. historical/engineering calibration — 使用法

サイズのsanity checkには、戦後初期のMambaが30 inch未満のcowling内に10-stage axial compressor・two-stage turbineを収めたこと、NACA 1947が14 inch class impellerでtip speed 1480 ft/s（約451 m/s）・design PR4.5を研究していたこと、日本機械学会1952試験でsingle-stage centrifugal PR2.79 @435.3 m/sが得られたことを比較anchorに使う。

これらは浅井世界線の年代を決めるceilingではなく、「0.50 m impeller / 420–455 m/s / 0.7 m class casingが幾何学的に荒唐無稽ではない」ことの外部較正である。E4/E5の1930年代での実現性は世界線内の長期compressor rig、精密加工、計算・試験蓄積で別に支払う。

## 7. v41 canonical product coordinates

| item | E4 | E5-S standard |
|---|---:|---:|
| design flow | **6.7 kg/s** | **7.6 kg/s** |
| headline output | **500 kW** | **1,000 hp** |
| material/rating split | non-Ni central | Ni 1,000 common / non-Ni800 1,000 full / non-Ni765 ~950 quantity |
| inlet tip D first-order | 0.291 m | 0.309 m |
| centrifugal impeller D working | ~0.50 m | ~0.50 m |
| GG rpm working | ~16 krpm | ~17.5 krpm |
| overall diameter working | **0.66–0.74 m** | **0.68–0.76 m** |
| length working | **2.0–2.4 m** | **2.0–2.3 m** |
| dry/engine assembly mass | **0.80–0.90 t** industrial product | **390–460 kg** core+PT+reducer+acc |
| installed TP powerplant | separate aviation audit | **510–640 kg** incl prop/mount/duct |
| exact compressor map | OPEN P1-3 | OPEN P1-3 |

## 8. propagation rule / next gate

P1-1はここでCLOSED。

次は **P1-2 E4 regeneration installed audit**。heat-exchanger effectivenessだけでなく、air/gas-side Δp、weight/volume、ducting、part-load、start/transientを払って旧25% / 0.33 kg/kWh級を再受領する。

その後P1-3 **E5/E6 compressor operability**。ここでstage count、map breadth、surge margin、start/acceleration、bleed/VSV/control、rotordynamicsを閉じる。

**航空機・艦船の性能/採用H→Aはまだ開始しない。** v41でengine product targetとenvelopeは閉じたが、既存platform側の重量・drag・prop/shaft・mission performanceを個別に再計算して初めて伝播する。post-1941 actual production/deployment/combatはHISTORY/FROZENのまま。

## 9. reproducibility

計算正本：

- `computation-2026-08-22/e4_e5_product_resize_p1.py`
- `computation-2026-08-22/E4-E5-PRODUCT-RESIZE-P1.tsv`

一次annulusは密度・axial velocity・hub/tipを明示した簡易size model。compressor aerodynamic closureではない。
