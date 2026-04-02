# Tasks: Issue 56 - Metrics Dashboard (Mermaid.js)

- [x] **Task 1: [基礎] 0.0% 問題の修正と集計ロジックの改善**
    - [x] `.ops/scripts/extract_metrics.py` の修正。RAW ログ全体を適切にスキャンし、直近の平均値を算出できるようにする。
    - [x] `.ops/scripts/aggregate_metrics.py` を更新し、Integrity Score や Autonomy Rate の集計に対応。

- [x] **Task 2: [実装] Mermaid.js コード生成ロジックの追加**
    - [x] `.ops/scripts/generate_dashboard.py` を新規作成。Mermaid 形式（pie, xychart-beta, radar chart 等）を生成。

- [x] **Task 3: [成果物] 総合ダッシュボードの作成**
    - [x] `docs/dashboard.md` を作成。README 等からリンクを張る。
    - [x] `METRICS.md` ととの同期を確認。

- [x] **Task 4: [自動化] パイプラインへの組み込み**
    - [x] `.ops/scripts/update_state_metrics.sh` を更新し、ダッシュボードの生成も実行するようにする。

- [x] **Task 5: [検証] 表示確認と最終調整**
    - [x] 各 Markdown ファイルでグラフが正しくレンダリング（Mermaid 構文が正しいか）を確認。
    - [x] `project_state.md` に最新の非ゼロの数値が反映されることを確認。
