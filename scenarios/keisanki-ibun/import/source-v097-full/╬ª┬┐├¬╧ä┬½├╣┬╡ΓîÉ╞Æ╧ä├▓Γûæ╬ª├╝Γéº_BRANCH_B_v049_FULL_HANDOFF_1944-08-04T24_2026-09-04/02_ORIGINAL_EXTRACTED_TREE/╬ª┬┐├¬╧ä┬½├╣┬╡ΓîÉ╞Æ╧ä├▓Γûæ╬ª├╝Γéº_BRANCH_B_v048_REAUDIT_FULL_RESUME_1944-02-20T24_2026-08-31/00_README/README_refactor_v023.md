# 計算機異聞 refactor v023 — 1943再開点・runtime整合修復

Current synchronized time: **1943-10-01T00:00**.
Current formal restart: `CHECKPOINT_1943-09-30T24_v001`.

v023はv022の戦略裁定を進めず、再開機構と手戻り防止を修復するメンテナンス版。`current_version_families` の欠落familyを復旧し、旧1944 restartをcurrentから外し、1943-09-30T24の正式checkpointを追加した。

## Mandatory branch guard
`06_RUNTIME/BRANCH_INVARIANT_GUARD_1943-10-01_v001.json` を、歴史的既定値やdownstream provisionalより優先する。

固定する主な差分:
- Midway: current restartでは日本保有。旧Sep-1943米奪回はretained provisionalであり自動継承しない。
- New Caledonia: 日本軍が主要回廊・港湾・飛行場・対外交通を軍事支配、名目主権/民政枠組みはVichy。
- 米空母損失: Lexington/Yorktown/Enterprise/Hornet/Saratoga。Waspは生存。late Aug/Sepには新造Essex/Independence群が実戦要因化するが旧損失は戻らない。
- 英空母損失: Indomitable/Formidable。Eastern Fleetの史実空母余力を自動復元しない。
- 日本: Shokaku/Zuikaku/Hiryu/Soryuの四空母核心は生存。Hiei/Kirishima/Haruna/Yamamoto等も枝内後続状態を優先し、史実喪失日を自動適用しない。
- 技術/暗号: TECH v006の日本軍戦闘能力・COMSEC/COMINT差を必ず日付gate付きで読む。史実JN-25的高級暗号読解を戻さない。
- 中国: Five-Go Phase IIはHanzhongで閉じ、Sichuan Phase IIIはHOLD。Burmaへの工兵/輸送/航空移転は中国統合コストを払う。

## Runtime
- `95_AUDIT/current_version_families_v012.json`: full registry restored.
- `05_WARTIME/CHECKPOINT_INDEX_v011.json`: current restart repaired to 1943-09-30T24.
- `05_WARTIME/CHECKPOINT_GRAPH_v010.json`: 1944 v004 restart is retained provisional/non-execution-valid.
- `98_TOOLS/build_event_handout_v008.py`: current restart/invariant guardをhandoutへ注入。
- `98_TOOLS/build_combat_context_v003.py`: v008 generatorを使用。
- `98_TOOLS/validate_refactor_v011.py`: v023構造・枝不変条件・generator smoke testを再現可能に検証。

次の戦略裁定はv022同様、1943年10月の米carrier pressureから開始する。
