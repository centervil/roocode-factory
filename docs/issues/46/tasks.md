# Tasks: /run-roo command implementation (Issue 46)

- [x] Issue ブランチの作成 `issue/46/run-roo-command`
- [x] `.gemini/commands/run-roo.toml` の新規作成
    - [x] `name = "run-roo"`
    - [x] モード指定 (`--mode`) とタスク内容の引数処理
    - [x] `skill-roo-driver` を起動・操作するプロンプトの記述
- [x] `skill-roo-driver` の動作確認
    - [x] `fetch-status` 等の既存アクションが正常に動作するか確認
- [x] テスト用スクリプトの作成（動作検証用）
- [x] `/run-roo` コマンドの動作検証
    - [x] モード指定が正しく機能するか
    - [x] プロンプトが送信されるか
    - [x] 監視ループが完了を検知できるか
- [ ] PR (Pull Request) の作成
