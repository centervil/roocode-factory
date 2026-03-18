# Design Document: Issue #60 - Mode定義およびプロトコル遵守度の直接的評価システム

## 1. 目的
AIエージェント（Roo Code等）が設計された命令（Must/Must Not）やプロトコルに従っているかを、セッションの生ログから直接評価し、定量化・視覚化する。

## 2. アーキテクチャ概要
本システムは、以下のコンポーネントで構成される。

1. **Rule Extractor**: `.roo/rules-*/` や `.gemini/skills/` から制約（Must/Must Not）を抽出し、LLMが理解可能な監査ルールセットを生成する。
2. **Audit Engine**: `.ops/audit_logs/raw/*.log` を取得し、LLM（Gemini 2.0 Flash等）を使用してルールセットに基づいた行動監査を実行する。
3. **Metrics Aggregator**: 監査結果（JSON）を集計し、設計遵守スコアを算出する。
4. **Dashboard Updater**: スコアを `docs/dashboard.md` に反映し、視覚化する。

## 3. 監査プロンプトの設計
LLMに対して以下の情報を提供する：
- **Context**: 実行されたModeの定義、関連するSkillの制約。
- **Raw Log**: Roo Codeの実行時生出力。
- **Instruction**: 各発言やツール使用が制約に違反していないかを判定し、エビデンス（ログの引用）と共に結果を出力せよ。

## 4. データ構造 (Audit Result JSON)
```json
{
  "timestamp": "20260315_120000",
  "log_file": "20260315_115000_code.log",
  "mode": "code",
  "compliance_score": 95,
  "violations": [
    {
      "rule_id": "reviewer_no_edit",
      "severity": "high",
      "description": "Reviewer mode attempted to edit a file.",
      "evidence": "..."
    }
  ]
}
```

## 5. 可視化
- `docs/dashboard.md` に「Architectural Compliance」セクションを追加。
- 直近のセッションごとのスコア推移（Mermaid.js Line Chart）を表示。
- 主要な違反項目のランキングを表示。
