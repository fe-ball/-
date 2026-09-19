# E5/E6 compressor operability rebaseline 1934–41 — v43

> **v43 current authority. 状態：COMPRESSOR OPERABILITY REBASED / E5-S & E6-S SMALL-CORE ARCHITECTURE CLOSED / E6-M FLOW IDENTITY REPAIRED / DOWNSTREAM H→A STILL GATED.**
>
> v41でE4/E5 product flow/size、v42でE4-R installed regenerationを閉じた。本稿はP1-3として、PRだけでなくstage split、corrected-flow map breadth、surge margin、start/acceleration、bleed/IGV、clearance、critical speedを受領する。ここで初めて旧「同じE6-M coreなのにTP≈10 kg/s、jet≈14 kg/s」というgas-path矛盾を解消する。航空機・艦船の性能・採用はまだ変更しない。

## 0. 結論

1. **E5-S PR6はACCEPT。** standard shaft-product gas path 7.6 kg/sを保持し、compressorは **5-stage axial booster + 1 centrifugal HP stage**。booster PR≈2.19、centrifugal PR≈2.74、17.5 krpm / impeller tip≈455 m/s。標準E5は固定IGV＋stage-3 bleedでstart/accelerationを閉じ、VSVは不要。
2. **E6-S PR7はACCEPT。** 小径端のrear axial blade-height/clearance税を避け、**7-stage axial booster + 1 centrifugal HP stage**。design corrected flowは **7.8 kg/s**（working trim 7.6–8.2）、booster PR≈2.83、centrifugal PR≈2.48、18 krpm / tip≈471 m/s。mechanically scheduled VIGV＋stage-4 bleedを標準にする。
3. **E6-M PR7はACCEPTだが、旧10 kg/s exact core coordinateはSUPERSEDED。** M-coreは **14-stage all-axial**、design corrected flow **13.2 kg/s**、full-speed trim **12.5–14.0 kg/s**。平均stage PR≈**1.149**。jet側14 kg/sはhigh-flow trimとして同family内、TP側旧10 kg/sはfull-PR7 design pointではない。
4. E6-Mのoperabilityは **VIGV + two simple interstage bleed bands** で閉じる。E6段階では多列VSVを標準化しない。full-speed steady surge-flow marginの受領下限を **10%**、acceleration transientの最低を **8%** とし、ground idleは62–65% corrected speedへ上げる。
5. **E4-R 7.16 kg/s high-flow derivativeはcompressor側ACCEPT。** 標準E4 6.7から+6.9%であり、inlet eye/diffuser/impellerを約3–4%径方向にtrimした **7.2 kg/s S-HF** を別compressor trimとして持てる。標準6.7 rotorをchoke端で常用する意味ではない。
6. **E5-S-N旧1,130 hpに必要な約8.08 kg/sもcompressor側ACCEPT。** E5-S-HFとしてlarger-eye/diffuser trimを切る。標準headlineは1,000 hpのまま。航空H→Aは別。
7. **E5 marine 1,300 hpは引き続きREJECT as S-core.** 必要約9.29 kg/sはE5-S-HFを越え、M/high-flow別coreを要する。
8. v43はE6の旧shaft output 1,520/2,100 hpを上積みしない。旧値はgross-derived targetを含み、E6 installed-cycle auditで再受領する。特にE6-M-Tの旧10 kg/s×155 kJ/kg shortcutはproduct proofから外す。

## 1. なぜE5/E6でarchitectureを分けるか

S級は5–8 kg/sで、all-axialをPR6–7まで多段化すると後段blade heightが薄くなり、1930年代のtip clearance・case roundness・blade-row matchingが効率とstall marginを食う。したがってE5-S/E6-Sは、前半を軸流で穏やかに圧縮し、最後を遠心段でまとめる。

M級は12–14 kg/sまで流せるためrear blade heightを確保しやすく、航空jetではfrontal areaが効く。そこでE6-Mはall-axialへ移る。PR7を14段へ割れば平均stage ratioは `7^(1/14)=1.1491`。これは後続E8のPR9.5/16段=`1.1511/stage`とほぼ同じload philosophyで、E6→E8の進化を「一段負荷を魔法で上げる」のではなくclearance/matching/TITへ置ける。

比較anchorとして、1944型Whittle centrifugal compressorはtip speed約1,500 ft/sでPR4.27/adiabatic efficiency 75.6%級、NACA 19XBは10-stage axialでPR4.17、Rolls-Royce Avon Mk.203系は15-stage axial＋variable-incidence IGV＋bleedでPR約7.85を持つ。これらは浅井世界線のcalendar ceilingではなく、stage loading / bleed / IGV / tip-speedの形が工学的に連続しているかを見るanchorである。

## 2. E5-S — PR6 small-core closure

### 2.1 design architecture

| item | v43 coordinate |
|---|---:|
| standard corrected flow | **7.6 kg/s** |
| total PR | **6.0** |
| target overall compressor η | **0.83** |
| axial booster | **5 stages / PR≈2.192 / ~1.17 per stage** |
| centrifugal HP | **PR≈2.737** |
| GG speed | **17,500 rpm** |
| centrifugal tip speed | **~455 m/s** |
| first-order inlet tip D | **0.309 m** |
| standard full-speed flow trim | **7.4–7.9 kg/s** |

v41の3–4 axial / centrifugal PR3.33はsize sanity coordinateとしては成立したが、P1-3ではcentrifugal burdenが大きすぎるためsupersedeする。軸流を5段へ増やしてcentrifugal stageをPR2.7級へ落とす。

### 2.2 operability / controls

標準E5-Sは**fixed IGV + one interstage bleed**を基本とする。

- bleed location：axial booster stage 3後。
- start/low speed：compressor flowの**10–12%**をdump可能。
- <=60% corrected speed：bleed fully/mostly open。
- 60–80/82%：mechanical scheduleで漸閉。
- >82%：closed。
- ground idle：**55–60% Nc**。
- steady operating line：surge corrected-flow lineから**13%以上**を目標。
- acceleration：瞬間最低**10%**を割らない。
- full-speed choke余裕：standard 7.6 pointで**約8%**を設計受領値。

E5ではmulti-row VSVを標準にしない。高流量E5-S-HF/J trimだけ、variable inlet swirl vaneをoptionとして許す。

### 2.3 rotordynamics / clearance

- first bending critical：**32–38% Nc**。start時に通過し、連続運転点に置かない。
- second critical：**>125% Nc**を受領条件。
- axial hot running tip clearance：**0.45–0.65 mm** working band。
- centrifugal tip/shroud working clearance：**0.55–0.80 mm**。
- service scatterでこれを越える個体はη=0.83 productとして受領せず、derate/repairへ回す。

## 3. E6-S — PR7 small-core closure

### 3.1 design architecture

| item | v43 coordinate |
|---|---:|
| design corrected flow | **7.8 kg/s** |
| full-speed trim | **7.6–8.2 kg/s** |
| total PR | **7.0** |
| target η | **0.84** |
| axial booster | **7 stages / PR≈2.826 / ~1.16 per stage** |
| centrifugal HP | **PR≈2.477** |
| GG speed | **18,000 rpm** |
| centrifugal tip speed | **~471 m/s** |
| first-order inlet tip D | **0.307 m** |

旧E6-S `~7.2 kg/s`は155 kJ/kg gross targetから逆算された旧product coordinateであり、exact compressor design flowとしてはsupersedeする。headline 1,520 hp等はv43だけで変更せず、E6 installed-cycleへ送る。

### 3.2 operability / controls

E6-SではPR7のlow-speed mismatchを払うため、**mechanically scheduled VIGV + one bleed**を標準化する。

- VIGV：idle/start側で約**−15°**、85% Nc付近までにdesign incidenceへ戻す。
- bleed：axial stage 4後、low speedで**10–14%**、80–83% Ncまでに閉じる。
- ground idle：**58–62% Nc**。
- steady surge-flow margin：**>=12%**。
- acceleration minimum：**>=9%**。
- design choke margin：**~8%**。
- first critical：**35–42% Nc**、second **>122%**。
- axial hot clearance：**0.40–0.60 mm**、centrifugal **0.50–0.75 mm**。

control hardwareは電子制御ではなく、spool speed・compressor delivery pressure・fuel pressureを使うhydro-mechanical cam/orifice scheduleで足りる。v38のelectronic computationはcontrollerそのものではなく、cam scheduleとbleed closure pointを事前探索する側へ使う。

## 4. E6-M — PR7 all-axial closure

### 4.1 flow identity repair

現行資料の最大矛盾は、同じE6-MをTPで約10 kg/s、jetで約14 kg/sと書いていた点である。backendがprop/nozzleへ変わってもcompressor design corrected flowが40%変わるわけではない。

v43では **E6-M aerodynamic family = 13.2 kg/s central / 12.5–14.0 kg/s full-speed trim band** とする。

- E6-M-J 14 kg/s：**high-flow trimとしてACCEPT**。
- E6-M-T 10 kg/s：**full-PR7 exact design pointとしてREJECT**。低速/derated operating pointなら10 kg/sを通せるが、その時PR7/η0.84/w=155を同時には相続しない。
- したがって旧E6-M-T 2,100 hpは「出力target」としてのみ保持し、flow/installed proofは専用cycle auditへ戻す。

### 4.2 compressor architecture

| item | v43 coordinate |
|---|---:|
| total PR | **7.0** |
| target η | **0.84** |
| stages | **14 axial** |
| average stage PR | **1.1491** |
| central corrected flow | **13.2 kg/s** |
| full-speed trim | **12.5–14.0 kg/s** |
| design speed | **13,500 rpm** |
| first-order inlet tip D | **0.389 m** |
| inlet blade height first-order | **87.5 mm** |
| inlet rotor tip-speed coordinate | **~275 m/s** |

### 4.3 map / start / bleed

E6-MはE6時点でVIGVとbleedを払い、multi-row VSVはまだ標準化しない。

- VIGV：start/idleで約**−20°**、85–90% Ncまでに0° design incidenceへ。
- bleed band A：stage 5付近。
- bleed band B：stage 10付近。
- total low-speed dump：**10–15%**。
- 60% Nc以下：両band open。
- 60–82/88%：後段→前段の順にstaged close。
- ground idle：**62–65% Nc**。
- steady surge-flow margin：**>=10%**。
- acceleration minimum：**>=8%**。
- full-speed choke margin：**~7%**。

このmarginは「未来のCFDでsurge lineを予言した値」ではない。1929–40に蓄積したrig mapを使って、full-core qualificationで受領すべき**release criterion**である。実測mapがこの線を割るbuildはPR/flowをderateする。

### 4.4 start / acceleration sequence

1. starterで~15–20% Ncまで回す。
2. VIGV start position、bleed全開でignition/fuel admission。
3. ~40–45% Ncでself-sustainingへ。
4. **45–52% Nc first-bending critical bandをno-dwellで通過**。
5. 60–65% Ncでground idleを捕捉。
6. acceleration時はfuel camがTITだけでなく`dN/dt`とcompressor delivery pressureの増え方を制限する。
7. bleedをstaged close、VIGVをopenし、85–90%以後full fixed geometryへ。

rotordynamic acceptanceはfirst critical 45–52% / second >118% Nc。長い14-stage rotorはfront thrust bearing + center/rear radial supportを持つ3-bearing arrangementをworking architectureとし、critical crossing時の振幅とbearing temperatureをbench acceptance itemへ置く。

## 5. manufacturing / clearance gate

E6-M rear stagesでは密度上昇でblade heightが小さくなるため、η=0.84の実gateはstage countより**rear tip clearance / casing roundness**である。

- front axial hot clearance：**0.5–0.8 mm**。
- rear target：**0.40–0.55 mm**。
- rear service reject：**>0.65 mm**をPR7/η0.84 releaseから外す。
- rotor runout、case split mismatch、blade stagger scatterをlot acceptanceで記録する。
- compressor wash/erosion後のmap shiftはflow/PR再計測で管理し、単純なTBO時間だけで受領しない。

この精度を全工場へ即時相続させない。E6-M航空高端は専用line/selected build、E6-Sやstationary/marineはより太いmarginを持つarchitectureへ逃がす。

## 6. high-flow derivative verdicts

### 6.1 E4-R 7.16 kg/s

標準6.7から+6.9%。標準compressorをchoke近傍へ押すのではなく、**E4-S-HF 7.2 kg/s trim**として、inlet eye/annulusを約3.4%径方向に広げ、centrifugal impeller/diffuserを約0.515–0.52 m級へtrimする。tip speedをE5より低く維持できるためcompressor-sideはACCEPT。

これによりv42の「475 kWe recuperated continuous derivative」は**compressor qualification pending**から解放できる。ただしheat-exchanger UA/ductをflowに合わせて約5–10%増やすpackage trimは必要。standard E4-R headline 440–450 kWe continuousは変更しない。

### 6.2 E5-S-N 1,130 hp

必要flow≈8.08 kg/s。standard7.6から+6.3%。**E5-S-HF**としてinlet eye/diffuserを約3%径方向にtrimし、variable inlet swirlを付ければcompressor側はACCEPT。Ni@800の標準headline 1,000 hpを自動1,130へ上げず、限定high-flow ratingとしてのみ使う。

### 6.3 E5 marine 1,300 hp

必要flow≈9.29 kg/s、standard比+22%。S-HF trimのchoke/eye/casing余裕を越える。**REJECT as E5-S**。M-scaleまたは別high-flow coreのH→Aが必要。

## 7. E4-R part-load boundary

v43はcompressor start/flow gateを閉じるが、E4-Rのexact part-load SFC curveを一個の数字へ固定しない。固定速generatorではfree power turbine speedとgas-generator speedが分離し、recuperator thermal inertiaも入るため、economic bypass crossoverはambient/load/soakに依存する。

canonical control ruleは以下まで：

- cold start / emergency：bypass。
- stable mid-high load：recuperator in-service。
- low load / rapid load pickup：pressure-loss回避のためbypassを許す。
- exact crossoverは**30–45% electrical loadのcalibration band**としてtest scheduleへ置き、固定40%一点の旧+12.6%改善値は復活させない。

これはE5/E6 aircraft/ship H→Aを止めるupstream gateではない。

## 8. downstream consequences — v43ではまだ伝播しない

v43で変わるのはengine-side authorityだけ。

- E5 standard：7.6 kg/s / 1,000 hp headline維持。
- E5-HF：8.08 kg/s / 1,130 hp compressor-side feasible、platform adoptionは未判定。
- E6-S：compressor design flowを7.8 kg/sへrebaseline。旧1,520/1,700 hpはinstalled-cycle未監査。
- E6-M：13.2 central / 12.5–14.0 trim。旧TP 10 kg/s exact coordinateはsuperseded。jet14はhigh-flow trimとして残る。
- E5 marine1,300：引き続きconditional。

次は **E6 installed-cycle/product power rebaseline** を先に行う。これを飛ばしてE6 aircraft H→Aへ進むと、旧gross155×flow shortcutを再利用することになる。E4/E5のplatform H→Aはv43 compressor gateを受領済みなので、E6 auditと並列に開始可能だが、E6搭載機は待つ。

## 9. reproducibility

計算正本：

- `computation-2026-08-22/e5_e6_compressor_operability_v43.py`
- `computation-2026-08-22/E5-E6-COMPRESSOR-OPERABILITY-V43.tsv`

TSV内のpart-speed operating lineは**qualification target / acceptance coordinate**であり、測定済みfull compressor mapを装うものではない。releaseにはrig/full-core実測を要する。
