# Slash Command Policy: Roocode/Gemini (スラッシュコマンド運用方針)

## 1. 概要 (Overview)
スラッシュコマンドは、Roocode/Gemini における AI エージェント（Mode）のワークフローを起動するための「エントリーポイント」です。コマンドの定義、配置、および運用に関する標準ルールを策定し、ユーザーインターフェースの一貫性を維持します。

## 2. 命名規則 (Naming Convention)
- **コマンド名**: `kebab-case` を使用します。
    - ✅ `setup-project`, `next-issue`
    - ❌ `setupProject`, `next_issue`
- **動詞 + 名詞**: 「何をどうするか」が伝わる形式を基本とします。
    - `audit-project`, `create-skill` など。

## 3. ディレクトリ構造と役割 (Directory Structure)
- **`.gemini/commands/`**: Gemini CLI 用のコマンド定義。
    - フォーマット: `TOML`
- **`.roo/commands/`**: Roo Code (VS Code Extension) 用のカスタムモード設定。
    - フォーマット: `Markdown`
- **SSOT (Source of Truth)**: 共通のロジックは必ず `Skill (SKILL.md)` または `scripts/` に記述してください。コマンドはそれらを呼び出す指示に徹します。

## 4. コマンドスキーマ (Command Schema)
### 4.1 .gemini (TOML)
```toml
name = "command-name"
description = "ユーザー向けの簡潔な説明"
prompt = """
あなたは、[役割] を担うエージェントです。
`activate_skill` を使用して [スキル名] を有効化し、以下の引数に基づきプロセスを開始してください。

引数: `{{arg-name}}`
- [引数がある場合の説明]
- [引数がない場合の説明]

[具体的なフローや完了定義]
"""

[[argument]]
name = "arg-name"
description = "引数の説明"
required = true/false
default = "default-value" (optional)
```

### 4.2 .roo (Markdown)
- 各カスタムモードの `Custom Instructions` として定義します。

## 5. プロンプトエンジニアリング基準 (Prompting Standards)
- **役割の明示**: 「あなたは〇〇エージェントです」という役割定義を冒頭に含めます。
- **スキルの有効化**: `activate_skill` によるスキル呼び出しを明示します。
- **引数の処理**: `{{args}}` または個別の `{{arg-name}}` をどのように解釈するかを定義します。
- **フローの明示**: ステップバイステップの指示を含めます。

## 6. 管理と更新
- 新しいコマンドを追加する際は、このポリシーに準拠しているか確認してください。
- コマンドは、プロジェクトの `Operational Protocols` (README.md) に列挙することを推奨します。
