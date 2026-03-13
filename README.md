# Roocode Factory

> **📊 [プロジェクト・ダッシュボード (可視化メトリクス)](./docs/dashboard.md)**

---

本リポジトリは、
AIエージェント（Gemini CLI および Roo Code）の能力を最大限に引き出すための「共通基盤（成果物）」の開発と、それを用いた高度な「プロジェクト運用」を両立するファクトリーリポジトリです。

## 1. 三層構造のアーキテクチャ

本リポジトリは、以下の三つの独立した役割を持つ層で構成されています。

### A. `.gemini/` (Common Infrastructure for Gemini CLI)
- **役割**: Gemini CLIという道具を使いこなすための共通基盤。
- **性質**: サブモジュールとして管理される**最終成果物**の一つ。他プロジェクトにポータブルに展開可能。
- **内容**: コアスキル（`.gemini/skills/` に集約）、共通自動化スクリプト、共通監査定義。

### B. `.roo/` (Common Infrastructure for Roo Code)
- **役割**: Roo Code (Cline) という道具を使いこなすための共通基盤。
- **性質**: このリポジトリの**最終成果物**であり、将来的に他プロジェクトの `.roo/` に移植・展開されるテンプレート。
- **内容**: カスタムモード定義、共通指示書、ポータブルなスキル（`.gemini/skills/` と内容を同期したコピーとして管理）。

### C. `.ops/` (Project-Specific Operations)
- **役割**: 上記の共通基盤を用いて、**このプロジェクトそのもの**を自律的に運用するためのデータ・設定。
- **性質**: プロジェクト固有。他プロジェクトには持ち出さない、この場所だけの運用ログや計測結果。
- **内容**: 運用スクリプト、メトリクス履歴、ロードマップ、課題管理テンプレート。

## 2. 開発プロトコル: IDD (Issue Driven Development)

すべての変更は GitHub Issue から始まります。
- **Start**: `gh issue view` で要件を確認し、`docs/issues/[ID]/` に要件・設計・タスクを定義。
- **Task**: `tasks.md` に基づき実装。
- **Review/End**: 成果物をレビューし、PRを作成・マージ。

詳細は **[AGENTS.md](./AGENTS.md)** を参照してください。

## 3. 物理ディレクトリ構成 (Map)

| ディレクトリ | 内容 |
| :--- | :--- |
| `docs/issues/` | 各 Issue の仕様書、設計、タスクリスト。 |
| `development_logs/` | 各セッションの作業記録（トレーサビリティ）。 |
| `.ops/metrics/` | プロジェクトの自律性・規約遵守率の計測定義。 |
| `.ops/templates/` | 成果物の最新テンプレート（SSOT）。 |
| `.gemini/skills/` | Gemini CLI 向けの機能モジュール（共通 Skill）。 |
| `.roo/rules-*/` | Roo Code 向けの各 Mode 定義（00-contract, 10-operational-guidelines）。 |

## 4. 運用・監査
共通基盤（`.gemini` / `.roo`）が提供する収集機能を用い、プロジェクト固有のデータ（自律性・規約遵守率）を `.ops/audit_logs/` に蓄積します。
詳細は `skill-metrics-manager` および `.ops/metrics/METRICS.md` を参照してください。

## 5. 成果物テンプレート (Artifact Templates)

プロジェクトにおけるすべての定型成果物は、`.ops/templates/` 配下のテンプレートを「正解」として参照しなければなりません。
Skill およびエージェントは、新規ファイル作成時やレビュー時に必ずこれらのテンプレートを読み込み、構造の整合性を担保してください。
