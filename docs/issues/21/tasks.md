# Tasks: Issue #21 - Roocode Self-Optimization Cycle

## Phase: Task (Implementation)
- [ ] `skill-self-optimizer` の基本実装 (SKILL.md)
- [ ] ロギング用テンプレートの定義とドキュメント化
- [ ] `.roo/rules-*.md` へのロギング指示の追加 (Orchestrator, Code, Reviewer 等)
- [ ] `.roo/custom_modes.json` への `/self-optimize` コマンド追加
- [ ] ログ収集ディレクトリ `.ops/audit_logs/` の準備

## Phase: Review
- [ ] ダミーの作業を行い、ログが正しく蓄積されるか確認
- [ ] `/self-optimize` を実行し、改善提案が生成されるか確認
- [ ] GLM-4.5-air のコンテキスト内で処理が完結するか確認

## Phase: End
- [ ] 開発ログの記録
- [ ] PR作成/マージ
- [ ] Issueのクローズ
