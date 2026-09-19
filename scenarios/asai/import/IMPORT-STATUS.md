# Import Status — 完全取り込み確認 2026-09-20

指定された原本ZIPと、その全ファイルをGit管理対象に取り込みました。

- 原本: [ZIP](archives/ASAI-WORLDLINE-HANDOFF-2026-09-19-FULL-V22B-CHINA-PEACE-GERMAN-JET-BRANCH-GATE(1).zip)（20,996,153 bytes）
- SHA-256: `4bea918064d011331dfe5e0ba3ceed3994e59cc4d2187e84495e59719bc63307`
- 展開保存先: [source-v22b-full-exact/](source-v22b-full-exact/)
- ファイル: **1,122 / 1,122**
- 展開後容量: 27,856,505 bytes
- ZIP CRC検査: 全件合格
- 原本ZIPコピーおよび展開ファイル: 全件SHA-256一致
- [ファイル別パス・サイズ・SHA-256一覧](FULL-IMPORT-MANIFEST-2026-09-20.tsv)
- [検証結果](FULL-IMPORT-AUDIT-2026-09-20.json)

## 保存範囲と現行正本

旧版、監査履歴、バイナリ、入れ子ZIPを含め、元ZIP直下の全ファイルを保存しています。
入れ子ZIPはファイルとして原寸保存し、再帰展開はしていません。空ディレクトリの記録も原本ZIPに残ります。
展開時はZIP内の名前をそのまま使用し、元から含まれる文字化け名を推測で修正していません。
元ZIPから保存先への対応はmanifestに記録しています。

現行authorityは **V23** のままです。`current/` の本文・時計・frontierは今回変更していません。
旧資料の収録はCANONへの昇格を意味しません。各資料のsupersession・WORKING・OPEN・ARCHIVE等の状態を維持します。
現行の読み始めは [シナリオREADME](../README.md) を参照してください。

## 既存の部分取り込みとの差分

従来の `source-v22b-full/` は43ファイルの部分取り込みで、ZIPと比較すると15ファイルは改行を除いて一致し、28ファイルには本文差があります。
今回の作業ではその43ファイルを上書きせず、履歴・既存の参照先を維持しました。
元ZIPの忠実な複製には **`source-v22b-full-exact/`** を使用してください。
差の原因や正史上の優先関係を、ファイル名や取り込み日だけでは断定しません。

- [既存取り込みとの比較一覧](PREVIOUS-IMPORT-COMPARISON-2026-09-20.tsv)
