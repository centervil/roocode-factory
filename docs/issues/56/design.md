# Design: Issue 56 - Metrics Dashboard (Mermaid.js)

## 1. Goal
Markdown 内で Mermaid.js を活用し、プロジェクトの健全性（Integrity, Autonomy, Performance）を視覚化する。
また、現状のメトリクス収集の不備（0.0% 問題）を解消し、正確なデータを反映させる。

## 2. Components
- **Data Source**: `.ops/audit_logs/raw/*.log` (RAW logs)
- **Aggregation Logic**: `.ops/scripts/extract_metrics.py` (Improved to scan all recent logs)
- **Visualization**:
    - `docs/dashboard.md`: 新規作成。Mermaid.js によるグラフを含む総合ダッシュボード。
    - `.ops/metrics/METRICS.md`: 更新。サマリー表に加えてグラフを挿入。
- **Automation**: `.ops/scripts/update_metrics_markdown.py` を拡張し、Mermaid コードの生成ロジックを追加。

## 3. Visualization Plan (Mermaid.js)
- **Pie Chart**: Autonomy Rate (AI vs Human turns).
- **Line Chart**: TSR (Total Success Rate) over time.
- **Radar Chart**: System Integrity (Protocol Fidelity, Behavioral Alignment, etc.).

## 4. Addressing the 0.0% Issue
- `extract_metrics.py` が最新のセッションだけでなく、指定期間（直近10セッションなど）の平均を計算するように修正。
- ログのパース処理を強化し、未定義のフィールドがある場合でもデフォルト値を設定して計算不能に陥らないようにする。
