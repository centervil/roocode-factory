# Task List: Issue #55 - RAW ログと信頼性スコアに基づく /self-optimize の刷新

- [x] **Task 1: データ収集ロジックの実装 (Research & Collection)**
    - [x] `.ops/audit_logs/raw/` から最新の RAW ログを特定するロジックの定義。
    - [x] 最新の開発ログ (`development_logs/`) を特定する。
- [x] **Task 2: `integrity_audit.py` の統合 (Audit Integration)**
    - [x] `skill-self-optimizer/SKILL.md` 内で `integrity_audit.py` を実行し、結果をパースする機能を追加。
- [x] **Task 3: 分析ロジックの刷新 (Analysis Logic)**
    - [x] スコアとエラー内訳に基づいた改善要因の抽出。
    - [x] 過去のメトリクスとの比較機能。
- [x] **Task 4: コマンドとモード指示書の更新提案 (Proposal Generation)**
    - [x] `self-optimize.md` の命令文を新しいフローに合わせる。
    - [x] AI が自己改善案を提示する際のフォーマット調整。
- [x] **Task 5: 検証 (Validation)**
    - [x] サンプルのログを用いて `/self-optimize` をテスト実行。
    - [x] スコアに基づいた妥当な修正案が出ることを確認。
