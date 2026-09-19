# E8/E9+ later-war propulsion 再基線化 1942–47 — 史実年代を天井にせず、支払済み能力と残存gateで判定する

> **v37 current canonical parent.** 史実の達成年は比較アンカーであって浅井世界線の上限ではない。E7までに支払った計算、圧縮機、冷却、材料、軸系、計測、試験、QC、service feedbackからE8/E9を積み上げる。post-1941 actual procurement/production/deployment/combatは従来どおりHISTORY/FROZEN。

## 0. 中央裁定

1. **E8 PR9–10 / TIT940℃ / component η≈0.86**は研究上端へ降格しない。浅井世界線では**high-end practical / qualifiable technical rating**としてcurrent。
2. 既存 **194 kJ/kg / 約31%** は冷却抽気前の**gross Brayton comparison index**と再定義する。4–5%級のcooling debitを簡易に払ったinstalled-core比較は約181–183 kJ/kg / 30.4–30.5%級を代表値とする。
3. E8は二軸必須ではない。**15–16-stage single-spool + VSV/bleed**を中央可能構成とし、two-spoolはoff-design/starting/surge marginを買う代替枝。
4. 旧「Ni系は1943–44で縁切れ」制約はhigh-end lineについてsuperseded。現行gateはcooling passage/yield、nozzle-vane/rotor/root/disk metal temperature、creep/oxidation/thermal fatigue、NDT、endurance/TBO、製造歩留まり。
5. **E9 PR11–12 / TIT≈1000℃ / η≈0.86–0.87**はcalendarでpostwar固定しない。design/component/rigは**current technical front**。flight-qualified/series ratingだけをCONDITIONALにする。
6. E9 series gateはtwo-spool rotordynamics/bearings/control、5–7%級staged cooling debit、full-core compressor/turbine map、start/accel/surge、endurance、manufacturing yield。
7. **generation ≠ thrust/core scale**。`E9 = 1,000 kgf/engine`を撤回。E6-L-Jにも1,000–1,150 kgf級research shadowがあり、fighter single-engine convergenceはinstalled thrust、mass flow、diameter/weight、inlet drag、TBOで判定する。
8. 旧 `1/2 Ve^2 = net Brayton w` をturbojet installed-cycle式として使わない。turbine workでcompressor/accessoriesを支払い、turbine-exit total state + nozzle + mass flowで推力を解く。既存E6 product thrustは保守的経験アンカーとして保持し、専用installed-engine H→Aまでは一括再計算しない。

## 1. 支払済み能力

E8時点で浅井側には、20年以上のGT研究、15年前後の商品/service feedback、多段軸流圧縮機、VSV/bleed、機械式燃料制御、Campbell図とrotordynamics、精密加工/隙間管理、Pt/Pt-Rh計測、NDT、管理図、燃焼器試験、中空空冷翼、精密鋳造/接合、拡散皮膜、Ni/非Ni二系統、専用試験場と計算室がある。よって「史実で後年だった」を単独の不成立理由にしない。

## 2. historical comparison anchors — ceilingではない

- NACA 19XB (1947) は10-stage axial compressorでdesign PR 4.17/30 lb/sを狙った。平均一段圧力比は約1.153。E8 PR9.5を16段で配分すると平均一段圧力比は約1.151で、異常な一段負荷ではない。難所は16段全体のmatching、tip clearance、stall/surge、rotor dynamics、VSV/bleed control。
- 同時代NACAはhollow-blade direct air coolingを体系的に研究しており、高いgas temperatureとblade lifeを冷却流量/geometry/stressの関数として扱っていた。浅井世界線ではその原理を早期から実装しているため、E7 900→E8 940℃の40℃差をcalendarで禁止しない。
- これらは**史実参照アンカー**であり、世界線の到達年を決めない。

## 3. temporal / qualification ledger

| 時期 | 項目 | v37 current判定 |
|---|---|---|
| 1942–44 | E7 paid foundation | PR≈8 / TIT≈900℃ / η≈0.85をfrontline floorとし、multi-stage aero、cooling、materials、instrumentation、QC/service dataをE8へ継承 |
| 1945–46 | E8 practical high-end rating | **PR9–10 / TIT940℃ / component η≈0.86**。high-end practical/qualifiable technical rating |
| 1945–46 | E8 gross cycle index | cooling debit前のsimple Brayton比較として **w≈194 kJ/kg / ηth≈31%** |
| 1945–46 | E8 cooled installed-core comparison | 4–5% cooling debitの代表比較で **w≈181–183 kJ/kg / ηth≈30.4–30.5%**。製品推力そのものではない |
| 1945–46 | E8 compressor architecture | 15–16-stage single-spool + VSV/bleedが中央可能。two-spoolはoperabilityを買うalternative |
| 1945–46 | E8 material/endurance gate | old Ni 1943–44 cutoffはsuperseded。cooling passage/yield、vane/rotor/root/disk temp、creep/oxidation/thermal fatigue、NDT/TBOがhard gate |
| 1945–47 | E9 technical front | **PR11–12 / TIT≈1000℃ / η≈0.86–0.87** design/component/rig workはcurrent technical front |
| 1945–47 | E9 flight/series rating | CONDITIONAL。two-spool/bearing/control、5–7% staged cooling、full-core map、start/accel/surge、endurance/yieldを全て通す |
| 1942–47 | generation/core-scale separation | generation numberからthrustを自動導出しない。E6-L-J 1,000–1,150 kgf research shadowはcore scaleの別軸 |
| 1942–47 | turbojet installed accounting | gross Brayton wとnozzle kinetic energyを分離。compressor/turbine/nozzle/mass-flow/inlet accountingでinstalled thrustを求める |
| 1945+ | single-engine fighter convergence | CONDITIONAL。required installed thrust、core diameter/weight、inlet drag、fuel/TBO、airframe CG/structureを満たした場合のみ再OPEN |
| 1941-12-08+ | actual procurement / production / deployment | HISTORY/FROZEN。E8/E9 research capabilityを実生産・配備・戦果へ自動変換しない |

## 4. E8 compressor gate

PR9.5を16段へ均等配分した平均stage ratioは約1.151。したがってE8の難所を「一段当たり圧力比が未来的」と置かない。実gateはfront/rear stage loadingの不均一、Re/Mach、tip clearance、interstage matching、stall/surge line、VSV/bleed schedule、shaft critical speed、bearing/seal、start/acceleration transientである。

単軸でこれを閉じられる範囲ではsingle-spoolを中央に残す。two-spoolは必須資格ではなく、off-design matchingとstarting/accelerationを買う代わりにconcentric shaft、追加bearing、control、assembly/inspection税を払うtradeである。

## 5. E8 hot-section / cooling gate

TITはgas temperatureであってblade metal temperatureではない。受領帳簿はcooling air fraction、coolant distribution、vane/rotor metal-temperature map、root/platform/disk rim、thermal gradient、creep life、oxidation/coating loss、thermal-cycle count、casting/drilling/joining yield、NDT reject rateを持つ。

Niは性能上の選択肢であり、現行high-end需要量では旧1943–44自動cutoffを置かない。ただしNi lineを量産万能にせず、非Ni cooled lineとの二系統によるspares/TBO/maintenance二重化は引き続き税として払う。

## 6. E9 — current technical front, series conditional

E9で実質的な段差になるのはPR/TITというラベルより、二軸を採用した場合のrotordynamics/bearing/control、冷却抽気5–7%級での圧縮機/turbine matching、start/accel/surge、hot-section endurance、歩留まりである。component/rigはE8から連続的に開く。flight/seriesはこれらを同時に閉じた時だけcurrentへ昇格する。

## 7. turbojet thrust rule

Braytonのnet specific workはshaft-cycle比較に有用だが、そのまま `1/2 Ve^2` へ置くとturbojetのcompressor work、turbine pressure ratio、turbine-exit total stateを二重/誤勘定する。今後のinstalled thrustは少なくともinlet recovery → compressor map/work → combustor loss/TIT → turbine work/cooling → nozzle expansion → mass flowの順で閉じる。

既存E6の約500 kgf/基等は実機比推力より低い保守的empirical anchorとして保持し、専用installed-engine H→Aで再較正するまでv37だけで一括変更しない。
