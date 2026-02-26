# Design: Fix Roo Code command flow (Issue 42)

## 1. Objective
Roo Code と Gemini CLI のコマンド定義を物理的に分離し、それぞれのプラットフォームに最適化されたフォーマット（Markdown / TOML）を適用することで、コマンド認識の信頼性を向上させる。

## 2. Architecture & Patterns
### 2.1 File Separation
- **Gemini CLI**: `.gemini/commands/*.toml`
- **Roo Code**: `.roo/commands/*.md`

### 2.2 Formats
#### Roo Code (.md)
YAML Frontmatter を使用してメタデータを定義し、本文に Role と Instructions を記述する。
```markdown
---
name: command-name
description: ...
---
あなたは[Role]です。
`activate_skill` を使用して [Skill] を有効化し、以下の引数に基づきプロセスを開始してください。
...
```

#### Gemini CLI (.toml)
`docs/policies/slash-commands.md` に準拠し、Roo Code 用のフィールド（`"argument-hint"` 等）を除去する。

## 3. Impact Assessment
- **Gemini CLI**: 動作に変更はないが、設定ファイルがクリーンになる。
- **Roo Code**: カスタムモードの指示が正しく認識され、コマンド実行の確実性が向上する。
- **Documentation**: `docs/policies/slash-commands.md` を実態に合わせて更新する必要がある。

## 4. Risks & Mitigations
- **Risk**: Roo Code が Markdown 内の YAML Frontmatter をサポートしているか。
- **Mitigation**: 標準的な Markdown パーサーであれば無視されるかメタデータとして扱われる。不具合がある場合は、通常の Markdown 見出し形式にフォールバックする。
