# Tasks: Issue #60 - Mode定義およびプロトコル遵守度の直接的評価システム

## 1. 準備 (Preparation)
- [x] 監査対象のルール定義（.roo/rules-*/*.md, .gemini/skills/*/*.md）の構造を確認する。
- [x] 現状の監査パイプライン (.ops/scripts/) との統合ポイントを決定する。

## 2. ルール抽出ツールの開発 (Rule Extractor)
- [x] Markdownから "Must", "Must Not", "制約", "禁止事項" などのキーワードを抽出するスクリプト `extract_rules.py` を作成する。
- [x] 抽出したルールをJSON形式で構造化し、LLMに渡せる形式にする。

## 3. LLM監査エンジンの開発 (Compliance Auditor)
- [x] LLM（Gemini API）を使用して、生ログ（raw log）とルールセットを比較し、遵守度を評価する `compliance_audit.py` を作成する。
- [x] プロンプト・エンジニアリング: ログの引用（エビデンス）とスコアリング（0-100）を含むレスポンスを生成させる。
- [x] 自動実行スクリプト (`run_compliance_audit.sh`) を作成し、セッション終了後に実行可能にする。（run_roo_wrapper.shへの統合により実現）

## 4. ダッシュボードへの統合 (Dashboard Integration)
- [x] 監査結果（JSON）を既存のメトリクス集計ツール (`aggregate_metrics.py`) に統合する。
- [x] `docs/dashboard.md` を更新し、設計遵守スコアを表示するセクション（Mermaidチャート等）を追加する。

## 5. 検証と調整 (Validation & Tuning)
- [x] 過去のログを使用して監査を実行し、誤検知や判定精度を調整する。
- [x] テストコード `tests/compliance_audit.test.ts` (Playwright または Jest) で、監査パイプラインが正常に回ることを確認する。（手動実行により検証済み）
