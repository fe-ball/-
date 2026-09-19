# GALVANIC 1943-11 航空基地掩体・防護強度モデル — WORKING v001

status: WORKING / NOT CURRENT AUTHORITY

## 1. 「掩体が充実」の意味

本再監査では aircraft revetment を「航空機用防空壕」と同義にしない。1943年の Marshall/Gilbert で主力になるのは、土・珊瑚・椰子材またはコンクリート側壁を持つ**開放式 dispersal/revetment**である。

効果の中心は:
- 隣接機への爆風・破片・炎上連鎖を切る。
- 横方向からの破片・小火器・一部爆風を減らす。
- 機体、燃料、弾薬を一群で失う cluster kill を減らす。

限界:
- 上面は開いており、直撃爆弾には弱い。
- 低空銃撃を完全には防げない。
- 空撮で位置が割れた固定revetmentは反復攻撃の標的になる。
- runway crateringそのものは防がない。

したがって Branch B の要塞化利益は「一回の空襲を無効化」ではなく、**同じ空襲で基地機能を同時に全部失う確率を下げ、二撃目・三撃目を要求する**ことに置く。

## 2. 防護クラス

- P1: 分散駐機のみ。銃撃・破片とも弱い。
- P2: earth/coral/log open-top revetment。横方向破片・爆風分離は中、銃撃・直撃には弱い。
- P3: concrete/coral heavy open-top revetment。横方向の破片・近接爆風にはより強いが、直撃への航空機保護は限定。
- S1: earth/log personnel/store shelter。破片・小型弾近接に有効。
- S2: reinforced concrete + sand/coconut-log bombproof shelter/magazine。人員・小型物資は大きく生残する。艦砲/大型爆弾直撃を保証しない。
- N1: natural excavation/raised-island shelter。Nauru型。人員・小型store/C2には有利だが航空機を洞窟化したことにはしない。

## 3. 島ごとの意味

### Tarawa
史実時点でも強力な地上bombproof shelterと航空機revetmentが存在する。Branch差は新しい地下飛行機壕ではなく、revetment・弾薬庫・電話線・障害・戦車待機位置の完成率。Betioが極小で全域を艦砲・航空で反復できるため、航空基地hardeningの上限は低い。一方、S2級の人員/弾薬/C2生残はD-Day fire systemへ効く。

### Taroa / Wotje / Mili
Marshallで最も「revetmentの追加が仕事をする」群。既に大規模airbase、dispersal、workshop、fuel、AA、road networkを持ち、コンクリートrevetmentも存在する。Branch Bでは工程完成率と分散が上がる。しかし平坦なatollなので、位置が判明した後の反復carrier strikeに対しては時間を買うだけで、永続防護ではない。

### Jaluit
水上航空はrunwayと独立できる反面、機体自体は水上で脆い。価値はramp/fuel/radio/workshop/support craftを分散させ、「滑走路を潰したから索敵も終わり」を成立させないこと。

### Nauru
最も質的差が出やすい。raised islandと既存掘削地形が人員、repair、fuel小分散、通信の shelter として働く。航空機自身は開放式revetmentなので直撃には弱い。したがって「航空機が強固」ではなく**基地の再生系が強固**になる。

## 4. GALVANICへの適用

D-1再計算では、各US攻撃について以下を別々に引く:
1. aircraft on dispersal/revetment
2. runway/taxiway
3. fuel/ordnance
4. workshop/repair plant
5. C2/radio/radar
6. AA
7. water-air ramp/crane/support craft

一つの爆撃結果から全7層を同時に落とさない。

同時に、Branch改善を protection percentage 一枚にしない。P2/P3が効くのは主に near-miss/fragment/chain-loss、S2/N1が効くのは人員/store/C2、plant uptimeが効くのは復旧時計である。
