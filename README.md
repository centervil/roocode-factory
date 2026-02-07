# Roocode Factory

本リポジトリは、AIエージェント（Gemini CLI および Roo Code）の能力を最大限に引き出すための「共通基盤（成果物）」の開発と、それを用いた高度な「プロジェクト運用」を両立するファクトリーリポジトリです。

## 1. 三層構造のアーキテクチャ

本リポジトリは、以下の三つの独立した役割を持つ層で構成されています。

### A. `.gemini/` (Common Infrastructure for Gemini CLI)
- **役割**: Gemini CLIという道具を使いこなすための共通基盤。
- **性質**: サブモジュールとして管理される**最終成果物**の一つ。他プロジェクトにポータブルに展開可能。
- **内容**: コアスキル、共通自動化スクリプト、共通監査定義。

### B. `.roo/` (Common Infrastructure for Roo Code)
- **役割**: Roo Code (Cline) という道具を使いこなすための共通基盤。
- **性質**: このリポジトリの**最終成果物**であり、将来的に他プロジェクトの `.roo/` に移植・展開されるテンプレート。
- **内容**: カスタムモード定義、共通指示書、ポータブルなスキル。

### C. `.ops/` (Project-Specific Operations)
- **役割**: 上記の共通基盤を用いて、**このプロジェクトそのもの**を自律的に運用するためのデータ・設定。
- **性質**: プロジェクト固有。他プロジェクトには持ち出さない、この場所だけの運用ログや計測結果。
- **内容**: 運用スクリプト、メトリクス履歴、ロードマップ、課題管理テンプレート。

## 2. 開発プロトコル: IDD (Issue Driven Development)

すべての変更は GitHub Issue から始まります。
- **Start**: `gh issue view` で要件を確認し、`docs/issues/[ID]/` に要件・設計・タスクを定義。
- **Task**: `tasks.md` に基づき実装。
- **Review/End**: 成果物をレビューし、PRを作成・マージ。

## 3. メトリクス管理
共通基盤（`.gemini` / `.roo`）が提供する収集機能を用い、プロジェクト固有のデータ（自律性・規約遵守率）を `.ops/audit_logs/` に蓄積します。
詳細は `skill-metrics-manager` および `.ops/metrics/METRICS.md` を参照してください。

## 4. Operational Protocols

エージェントの普遍的な行動規範を定義した `agents.md`（憲法）に対し、本 `README.md` はこのプロジェクト固有の具体的な運用定義（地図）を提供します。

### 4.1. Source of Truth (真実のソース)
本プロジェクトにおける課題管理とタスクの正解（Source of Truth）は **GitHub Issues** です。エージェントはセッション開始時、または新しいタスクに着手する際、必ず `skill-issue-manager` を有効化し、GitHub の最新状態と同期しなければなりません。

### 4.2. Concrete Mapping (抽象概念の実体定義)
`agents.md` で使用される抽象的な概念と、本プロジェクトにおける具体的なパスの対応表です。

| 抽象概念 (from agents.md) | 具体的なパス / 実体 |
| :--- | :--- |
| **Common Infrastructure** | `.gemini/` (Gemini CLI), `.roo/` (Roo Code) |
| **Project Operations** | `.ops/` |
| **Issue Workspace** | `docs/issues/[ID]/` |
| **Development Log** | `development_logs/` |
| **Common Skills** | `.gemini/skills/`, `.roo/skills/` |

### 4.3. Authorized Tooling (認定ツール)
- **Issue/Tasking**: `gh` (GitHub CLI)
- **State Tracking**: `skill-state-manager`
- **Audit/Metrics**: `skill-metrics-manager`
- **Architecture/Skill Management**: `project-and-skill-architect`
