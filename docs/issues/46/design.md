# Design: /run-roo command implementation (Issue 46)

## 概要
Gemini CLI から Roo Code を自律操作するためのインターフェース `/run-roo` を実装する。
このコマンドは `skill-roo-driver` を利用して、ブラウザ上の Roo Code に指示を送り、完了まで自律的に監視を行う。

## アーキテクチャ
1.  **コマンド定義**: `.gemini/commands/run-roo.toml`
    - `/run-roo --mode "Code" "Task description"` の形式で受け取る。
2.  **スキル連携**: `skill-roo-driver`
    - `change-mode`, `send-prompt`, `fetch-status` の各アクションを実行する。
3.  **自律制御ロジック**:
    - Gemini CLI が `fetch-status` の結果（テキスト履歴、スクリーンショット）を解析。
    - タスクの完了（Success Criteria の達成）を判断するまで、必要に応じてプロンプトを再送または待機する。

## 実装詳細
- **run-roo.toml**:
    - 名前: `run-roo`
    - 引数: `--mode` (オプション, デフォルト: Code), `prompt` (位置引数)
    - プロンプト定義: `skill-roo-driver` を起動し、指定されたモードでタスクを実行・監視する指示を含む。
- **監視ループ**:
    - `fetch-status` を実行し、Roo Code の最新メッセージを確認。
    - 完了していない場合、一定時間待機（または Roo Code からの質問に回答）して再度確認。
    - 完了した場合、またはエラーが発生した場合に終了。

## Success Criteria
- [ ] `.gemini/commands/run-roo.toml` が作成されている。
- [ ] コマンド実行時に `/[ModeName] ` がプロンプトの先頭に付与される。
- [ ] `skill-roo-driver` を通じて Roo Code に指示が送信される。
- [ ] タスク完了まで自律的に監視が継続される。
- [ ] 完了報告がユーザーに返される。
