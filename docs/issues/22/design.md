# Design: Issue #22 - スラッシュコマンドの運用方針

## 1. 概要
本設計では、Roocode/Gemini におけるスラッシュコマンドの定義、配置、および運用に関する標準ルールを策定します。これにより、コマンドの乱立を防ぎ、ユーザーインターフェースの一貫性を維持します。

## 2. 方針と設計

### 2.1 命名規則 (Naming Convention)
- **コマンド名**: `kebab-case` を使用します（例: `setup-project`, `next-issue`）。
- **サブコマンド**: 主要なコマンド内で引数として処理することを推奨します（例: `dev start 123`）。
- **一貫性**: 動詞 + 名詞の形式を基本とします。

### 2.2 ディレクトリ構造と役割
- `.gemini/commands/`: Gemini CLI (Node.js/TypeScript) 向けのコマンド定義。
    - フォーマット: `TOML`
- `.roo/commands/`: Roo Code (VS Code Extension) 向けのコマンド定義。
    - フォーマット: `Markdown` (Custom Instruction)
- **SSOT (Source of Truth)**: 共通のロジックは `Skill (SKILL.md)` に記述し、コマンドはそれらを呼び出す「エントリーポイント」としての役割に徹します。

### 2.3 コマンドスキーマ (Standard Schema)
#### .gemini (TOML)
```toml
name = "command-name"
description = "ユーザー向けの簡潔な説明"
prompt = """
AIエージェントへの詳細な指示。
`activate_skill` を使用して特定のスキルを有効化し、処理を委譲する手順を含む。
"""

[[argument]]
name = "arg-name"
description = "引数の説明"
required = true/false
default = "default-value" (optional)
```

#### .roo (Markdown)
- Roo Code の Custom Mode 設定に基づき、各モードの `Custom Instructions` として定義。

### 2.4 プロンプトエンジニアリング基準
- **役割の明示**: 「あなたは〇〇エージェントです」という役割定義を冒頭に含める。
- **スキルの有効化**: `activate_skill` によるスキル呼び出しを明示する。
- **入出力の定義**: 期待される入力引数と、最終的な出力形式を明確にする。

## 3. 実装計画
1. `docs/policies/slash-commands.md` の作成。
2. 既存コマンド（`setup-project`, `next-issue`, `requirements`, `audit`, `dev`）の監査とリファクタリング（必要に応じて）。
3. `skill-project-and-skill-architect` の `setup-project.sh` テンプレートを新基準に合わせる。
