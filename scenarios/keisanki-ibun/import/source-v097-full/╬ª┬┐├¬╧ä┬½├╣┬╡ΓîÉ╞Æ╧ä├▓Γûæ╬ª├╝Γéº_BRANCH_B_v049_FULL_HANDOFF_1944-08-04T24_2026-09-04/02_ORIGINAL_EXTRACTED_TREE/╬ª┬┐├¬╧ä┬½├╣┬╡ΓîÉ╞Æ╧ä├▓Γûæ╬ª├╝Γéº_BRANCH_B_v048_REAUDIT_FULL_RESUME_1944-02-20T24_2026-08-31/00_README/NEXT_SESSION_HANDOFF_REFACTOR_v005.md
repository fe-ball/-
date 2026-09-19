# NEXT SESSION HANDOFF — refactor v005

## 現在地

1942Q2再監査はMidway攻略決算まで完了。

正式restart：`05_WARTIME/CHECKPOINT_1942-06-15T24_v001.json`

次は1942年6月後半～9月を、旧81/82/86+から自動継承せず再走査する。

## 最初に読むもの

- `05_WARTIME/CHECKPOINT_1942-06-15T24_v001.json`
- `06_RUNTIME/1942Q2_OPERATION_C_MO_MI_REAUDIT_SETTLEMENT_v001.md`
- `06_RUNTIME/MIDWAY_1942-06-10_15_SETTLEMENT_v001.json`
- `02_TECH/TECH_INDEX_v003.json`
- `00_CONFIG/current_branch_overrides_v001.json`

## 現行戦略状態の要点

- 日本：Port Moresby、Tulagi、Midwayを保持。
- 日本空母：Akagi/Kaga喪失、Soryu/Hiryu大破生還、Shokaku修理中、Zuikaku健在。Ryujo/Junyo/Zuiho/Shoho健在、Hiyo完成接近。
- 米空母：Lexington/Yorktown/Enterprise/Hornet/Saratoga喪失。WaspはPacific転用途上。RangerはAtlantic維持が中心。
- 英国：Operation CでIndomitable/Formidable喪失。Indian Oceanの現代的艦隊航空が極端に薄い。
- 日本艦載航空：船体数より人員・部隊再編が律速。8-12週間の本格再編窓を優先する可能性が高い。
- Midway：巨大艦隊基地ではなく、前進検索・飛行艇・潜水艦支援・警戒節点として初期大量備蓄後に維持コストを下げる。

## 次に必ず再計算する論点

1. FSを次主作戦にするか、まず航空隊・船腹・護衛を再建するか。
2. 史実WATCHTOWER/Guadalcanalの代替。8月7日上陸を自動発生させない。
3. 米潜水艦によるMidway/南太平洋補給線妨害と日本の護衛/タンカー/標準船配分。
4. Shokaku/Hiryu/Soryuの修理時計と航空隊再編、人員自然還流。
5. 米Wasp/Ranger/Essex/Independenceの戦力化時計とHawaii/South Pacific守勢。
6. 英国空母危機がMalta/TORCH/Arctic/Indian Oceanへ与える配分効果。
7. Hornet/Midwayの鹵獲・実見機材が日本のradar/CIC/base/DC学習へ与える小さな時間短縮。
8. MI水上追撃の巡洋艦・駆逐艦個艦損害名寄せ。現時点ではクラス/隻数帯のみ固定。

## 禁止事項

- 旧81/82/85/86+の戦果を現在状態へコピペしない。
- Midway占領=Hawaii孤立、または日本の恒久的東太平洋制海とはしない。
- 空母喪失=航空搭乗員全滅とはしない。
- Toneの史実遅延や史実6月2-3日の霧を偶然条件として再固定しない。
- 水上艦改善を単純な一発命中率係数だけに縮約しない。接敵・実用速力・追尾・第二魚雷斉射・再突入までの連鎖で扱う。
