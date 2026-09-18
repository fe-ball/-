# Scenario Status Convention

シナリオ内の情報は、少なくとも以下を混同しない。

- **CANON / APPROVED**: 現在の世界線で確定している
- **WORKING**: 作業上使用しているが、再検討可能
- **PROPOSED**: 提案段階
- **OPEN**: 未解決
- **SUPERSEDED**: 現在は上位判断に置換済み
- **ARCHIVE**: 再現・参照用の過去資料

Git の branch / main への存在自体は CANON を意味しない。
正史性・確定性はシナリオ文書内の precedence / decision / guard を優先する。

## Registry fields

中央registryでは最低限、以下を別々に持つ。

- **scenario id**: シナリオの不変識別子
- **authority_version**: どのauthority overlay / versionを現行として読むか
- **canonical_clock**: 現行世界線の歴史時刻
- **clock_state**: frozen / open / gate 等
- **frontier**: 次に処理すべき論点
- **repository + path**: 現在のGitHub上の物理配置
- **entrypoint**: 人間が最初に読む入口
- **source_import**: 元資料がGitHubへどこまで取り込まれているか

## Important guard

「最も未来の日付が書かれたファイル」「最大のversion番号」「最後に作成されたファイル」を自動的にcurrent authorityとしない。

authority_version と canonical_clock は独立した値である。
シナリオが再監査のため過去時点へ時計を戻す場合、後の時刻まで進んだ旧枝が存在しても current へ自動復帰させない。

シナリオ本体を別repositoryへ移動しても、scenario idは変えない。中央registryのrepository/pathだけを変更する。
