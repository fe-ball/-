# Authority / Evidence Status

## 最新と現行正本を分ける

ファイルの作成日、歴史上の時刻、バージョン番号の大きさだけで current authority を決めない。

各シナリオは少なくとも次を明示する。

- authority_version
- canonical_clock
- clock_state
- entrypoint
- precedence / supersession rule
- current frontier

古いファイルにより未来の歴史時刻が書かれていても、上位authorityが時計を巻き戻して再監査している場合、その未来枝をcurrentへ自動昇格しない。

## 情報の状態

- CANON / APPROVED: 現在の世界線で確定
- WORKING: 現在の分析で使用するが再検討可能
- PROPOSED: 提案
- OPEN: 未解決
- SUPERSEDED: 上位判断で置換
- ARCHIVE: 再現・参照用

## 出所

可能な範囲で次を区別する。

- USER-DIRECT
- DERIVED
- ASSISTANT-PROPOSAL
- HISTORICAL-ANCHOR
- SOURCE-PACKAGE-INHERITED

GitHubに存在すること、mainに入っていること、文章が断定調であることはCANONの十分条件ではない。
