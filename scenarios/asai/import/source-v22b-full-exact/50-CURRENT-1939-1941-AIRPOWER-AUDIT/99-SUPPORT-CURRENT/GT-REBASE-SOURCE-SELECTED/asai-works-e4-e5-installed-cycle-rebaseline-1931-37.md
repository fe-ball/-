# E4/E5 cooled installed-cycle 再基線化 1931–37 — gross Brayton から実shaft帳簿へ

> **v40 current canonical parent.** 本稿はv39で閉じたE4/E5 hot-section寿命を受け、冷却抽気・燃焼器圧損・排気圧力余裕・機械損失を支払った `installed shaft specific work` と fuel-based thermal efficiency を閉じる。E4/E5のPR/TIT/component efficiency自体は変更しない。航空機・艦艇・採用・戦史への下流伝播は後続監査へ送る。

## 0. 中央裁定

1. 既存E4 `93 kJ/kg / 18%`、E5 `126 kJ/kg / 22.5%` は **gross simple-Brayton comparison index** として保持する。冷却・燃焼器圧損・排気余裕・mechanical/accessory lossを払った製品shaft値ではない。
2. `component efficiency η` はcompressor/turbineのaerodynamic/thermodynamic component coordinateとして読む。燃焼器圧損・冷却bleed・mechanical efficiencyを暗黙に含めない。
3. E4 central cooling debit = **3.0%**（audit band 2.2–3.8% compressor-inlet flow）。E5 Ni high-end@800°C = **4.0%**（3.2–5.0%）。E5 non-Ni@800°C full = **6.0%**（5.0–7.5%）。E5 non-Ni@765°C quantity = **4.0%**（3.2–5.0%）。
4. central combustor total-pressure lossはE4 **4.0%**、E5 **3.5%**。これはJumo 004 combustorで2–6%級が実測されたことを比較anchorにしつつ、浅井の低速定置can/系統試験・改善を織り込んだengineering coordinateである。
5. 冷却空気は「消える」とも「hot gas同様に全膨張仕事をする」とも扱わない。vane/rotor/root/sealごとにtap pressureと再流入位置を分け、部分的にexpansion workを回収するaudit surrogateで計算する。
6. E4 installed shaft specific work = **central ≈76 kJ/kg、audit band ≈69–80 kJ/kg**。fuel-based shaft thermal efficiency = **central ≈15.0%、band ≈13.8–16.0%**。
7. E5 Ni high-end@800°C = **central ≈104 kJ/kg、band ≈98–110 kJ/kg**。fuel-based shaft efficiency = **central ≈19.3%、band ≈18.1–20.2%**。
8. E5 non-Ni@800°C full = **central ≈99 kJ/kg、band ≈90–105 kJ/kg**、shaft efficiency **≈18.7% central / 17.2–19.7% band**。
9. E5 non-Ni@765°C quantity = **central ≈93 kJ/kg、band ≈87–98 kJ/kg**、shaft efficiency **≈18.4% central / 17.2–19.4% band**。
10. よって旧 `P = w_gross × m_dot` をE4/E5製品のinstalled shaft powerへ直接使うことを停止する。E4 500 kW、E5 1,000 hp等の既存製品値は**設計目標/旧gross-derived product coordinate**として保持し、mass-flow/diameter/weightを後続product re-size監査で閉じる。
11. post-1941 actual production/deployment/combatは従来通りHISTORY/FROZEN。本稿から採用・生産を自動生成しない。

## 1. なぜgrossとinstalledを分ける必要があるか

単純Braytonでは、compressor inlet 1 kg/sが全量compressor出口まで圧縮され、全量がTITまで加熱され、pressure loss無しでturbineを膨張し、mechanical/accessory loss無しでshaftへ出る。この比較は世代差を見るには有用だが、空冷E4/E5の製品shaft値ではない。

実機では少なくとも次を払う。

- compressor途中/出口からvane・rotor・disk/root・sealへcooling airを抜く。
- その空気は燃料でTITまで加熱されない。
- coolantは流入位置によりturbine workを一部しか回収しない。
- combustor total-pressure lossでturbine expansion ratioが減る。
- exhaust/diffuserには有限のpressure marginが要る。
- bearing/seal/gear train以前でもshaft mechanical lossとfuel/oil pump等のaccessory loadがある。
- fuel-based thermal efficiencyではcombustion efficiencyも払う。

低PR・低net-workの初期GTでは、これら数%の損失が「turbine work − compressor work」という小さい差分へ効くため、grossからshaftへの減益率はbleed率そのものより大きい。

## 2. historical calibration anchors — ceilingではない

### 2.1 Neuchatel 1939

Neuchatel機は4 MW級発電端・overall efficiency約17.4–18%の実績を持つ。後世資料に残るtest dataではcompressor efficiency約86.6%、turbine efficiency約88.4%、PR約4.3–4.4級である。これら実component efficienciesをlossless Braytonへ直接入れるとoverall実績より高い値になる。combustor pressure loss・finite exhaust pressure・mechanical/generator lossを払うと実績帯へ戻る。

したがって旧 `η=0.85をcompressor/turbine双方へ入れると17.4%と一致` は**gross modelの偶然のlumped calibration**であって、`η=component efficiency` を正式意味にした現在のinstalled-cycle検証には使わない。

### 2.2 cooling flow / bleed penalty

- NACA RM E50E22 (1950): compressor bleedによるblade coolingはconstant TITでSFCを増やしthrustを低下させ、cooling effectivenessが高いほど必要流量を減らせる。
- NACA RM E51E24 (1951): rotor cooling flow 0–3%を解析し、required-pressure tapではsea-level thrust reductionが概ねcoolant-flow percentageの約2倍、SFC増はcoolant percentage程度という結果。compressor-discharge bleedは追加損失を持つ。
- NACA later cooled-engine analyses: 2–4%級coolant flowは小さい冷却要求の代表帯として扱われる。
- Jumo 004 comparative anchor: hot-gas-path coolingに総compressor flowの約7%を使ったとされ、stage/intermediate/dischargeからvane/disk/blade等へ分配した。これは浅井世界線のcalendar ceilingでなく、「非Ni・高温線では数%後半のbleedが現実に起こる」物理anchorである。
- Jumo 004 combustor NACA test: total-pressure lossはroughly 2–6% inlet total pressure。

v40のE4/E5 coolant bandsはこれらをそのまま移植せず、v39 metal-temperature requirement、TIT差、Ni/non-Ni材料線、浅井のfuture-informed routing/flow-proof/QCを入力して置く。

## 3. coolant budget

compressor-inlet flowを100%としてcentral budgetを置く。

| stream | E4 | E5 Ni @800 | E5 non-Ni @800 full | E5 non-Ni @765 | primary purpose |
|---|---:|---:|---:|---:|---|
| first vane/nozzle | 0.75% | 1.0% | 1.4% | 1.0% | vane wall / trailing region |
| rotor blade | 1.25% | 1.8% | 3.0% | 1.7% | hollow blade convection / root feed |
| disk/root/cavity | 0.60% | 0.8% | 1.0% | 0.8% | rim/root thermal cliff control |
| seal/bearing isolation | 0.40% | 0.4% | 0.6% | 0.5% | hot-gas ingestion prevention / oil-system isolation |
| **total** | **3.0%** | **4.0%** | **6.0%** | **4.0%** | |

routing rule:

- vane/rotor coolantは原則rear-compressor/discharge側。
- disk/rootは必要pressureを満たす最低stageから抜き、不要なfull compressionを避ける。
- seal/isolation airも同様にminimum sufficient tapを使う。
- cooling circuitはflow-proof testを持ち、blocked passage / seam leak / excessive bleedをproduction rejectへ送る。

この「lowest sufficient pressure tap」は、計算機の発明ではなく主人公のGT本職知識が早期に要求できる工夫である。

## 4. installed-cycle audit model

正準計算は `computation-2026-08-22/e4_e5_installed_cycle_v40.py`、出力は `E4-E5-INSTALLED-CYCLE-V40.tsv`。

### 4.1 gross baseline

`T1=288 K, cp=1.005 kJ/kgK, gamma=1.4`。

既存と同じくcompressor/turbineへ世代component efficiencyを入れ、pressure loss無しでgross `w` を再現する。

- E4 PR4.5 / TIT710°C / η=0.82 → **93.5 kJ/kg / 18.37%**。
- E5 PR6 / TIT800°C / η=0.83 → **125.5 kJ/kg / 22.58%**。
- E5 derated TIT765°C / PR6 / η=0.83 → **113.8 kJ/kg / 21.86% gross**。

### 4.2 bleed extraction

main flowだけがfull compressor dischargeへ残り、各bleed streamはtap pressureまでのcompressor workを払う。v40 surrogateではvane/rotor=full-discharge、root≈75% log(PR)、seal≈55% log(PR)のtap coordinateを用いる。

### 4.3 coolant work recovery

coolantはTITまで加熱されない。一方、圧力を持ってturbine pathへ戻るので仕事寄与をゼロにも置かない。re-entry locationを近似するため、full expansion opportunityに対するaudit recovery surrogateをvane 0.85 / rotor 0.55 / root 0.15 / seal 0と置く。

これはhardware constantではなく、coolantがどこで混ざるかを一段modelで表すための計算係数。結果はcoolant flow / pressure lossのbandで囲い、係数一点を正準物性にしない。

### 4.4 pressure / mechanical ledger

central:

| item | E4 | E5 |
|---|---:|---:|
| combustor total-pressure loss | 4.0% | 3.5% |
| exhaust/diffuser pressure margin | p_out/p_amb ≈1.015 | ≈1.015 |
| shaft mechanical efficiency surrogate | 0.990 | 0.992 |
| accessory load | 1.0 kJ/kg inlet | 1.0 kJ/kg inlet |
| combustion efficiency for fuel accounting | 0.980 | 0.985 |

これらはproduct gear/generator/propeller lossを含まない。そこは下流product ledger。

## 5. quantitative result

| coordinate | cooling | gross w / eta | installed shaft w | fuel-based shaft eta | gross→shaft loss |
|---|---:|---:|---:|---:|---:|
| E4 710°C | 3.0% | 93.5 / 18.37% | **75.7 kJ/kg** | **15.03%** | 19.0% |
| E5 Ni 800°C | 4.0% | 125.5 / 22.58% | **104.3** | **19.25%** | 16.9% |
| E5 non-Ni 800°C full | 6.0% | 125.5 / 22.58% | **99.5** | **18.75%** | 20.8% |
| E5 non-Ni 765°C | 4.0% | 113.8 / 21.86% | **93.5** | **18.41%** | 17.9% |

uncertainty/audit bands:

| coordinate | installed shaft w band | shaft eta band |
|---|---:|---:|
| E4 | **69–80 kJ/kg** | **13.8–16.0%** |
| E5 Ni@800 | **98–110** | **18.1–20.2%** |
| E5 non-Ni@800 | **90–105** | **17.2–19.7%** |
| E5 non-Ni@765 | **87–98** | **17.2–19.4%** |

### 5.1 central loss decomposition

central modelでgross→shaft差を分けると概ね：

- E4: 93.5 → cooling only 87.7 → combustor dp 81.6 → exhaust margin 79.4 → mech/accessory 75.7 kJ/kg。
- E5 Ni: 125.5 → 115.6 → 110.3 → 108.0 → 104.3。
- E5 non-Ni full: 125.5 → 110.6 → 105.4 → 103.2 → 99.5。

これにより、**cooling debitだけをgross wへ単純に `×(1-B)` するのも不十分**と分かる。圧縮機work、coolant reinjection、turbine expansion pressure、mechanical lossを同時に閉じる必要がある。

## 6. product re-size consequence — OPEN, not yet propagated

既存製品に対する直接の数学的警告だけを記録する。

- E4旧 `93×5.4≈500 kW` はgross derivation。v40 central installed w≈75.7なら、**同じ5.4 kg/sでは≈409 kW shaft**。500 kW shaft targetを保持するなら必要flowはcentral≈6.60 kg/s、band約6.2–7.2 kg/s。
- E5旧 `126×6≈756 kW≈1,000 hp` もgross derivation。Ni line central installed w≈104なら、**6 kg/sでは≈626 kW≈840 hp**。756 kW targetを保持するならcentral≈7.25 kg/s、band約6.9–7.8 kg/s。

この段階では「500 kW製品を撤回」「1,000 hp turbopropを撤回」とは裁定しない。次監査で、mass flow増がcompressor diameter、rpm、weight、gear、installation drag、cost、lifeへ与える税を払って**targetをresizeで維持するか、ratingを下げるか**を決める。

したがってv40以降、E4/E5製品について `P=w_gross*m_dot` を物理証明として引用してはならない。

## 7. what does NOT change in v40

- E4 PR4.5 / TIT710 / component η0.82。
- E5 PR6 / TIT800 / component η0.83 high-end coordinate。
- v39 L_core bands。
- E6+の性能数値（今回未監査）。
- aircraft/ship speed/range。
- procurement/adoption/OOB/combat。
- regeneration cycleのproduct-specific heat-exchanger benefit（installed pressure loss込みの再監査待ち）。

## 8. next gates

P1 order:

1. **E4/E5 product mass-flow / size re-baseline**: 500 kW初号機とE5 1,000 hp targetを、6.2–7.8 kg/s級へresizeして成立させるか、ratingを下げるか。
2. **E4 regeneration installed audit**: heat-exchanger effectivenessだけでなくair/gas-side pressure loss、weight/volume、part-loadを払う。
3. **E5/E6 compressor operability attainment**: map breadth, stage matching, VSV/bleed, start/acceleration, surge margin。
4. downstream aircraft/ship H→A only after engine product output/weight/envelope closes。

## 9. source / model status

Historical reports are calibration anchors, not Asai-worldline calendar ceilings. The numerical v40 coolant budgets and routing/recovery factors are engineering audit assumptions constrained by v39 metal-temperature targets, historical cooling-flow magnitudes, and early combustor pressure-loss data. They are preserved with ranges and a reproducible script so later evidence can move them without hiding the dependency.
