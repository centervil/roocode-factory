# Design: Issue #20 - Requirement Definition Engine

## Architecture

### 1. Slash Command Layer
- **Interface**: `/requirements [issue_id]`
- **Implementation**: `.gemini/commands/requirements.toml`
- **Role**: `skill-requirement-expert` を起動し、Issue ID の有無に応じてインタビューを開始する。

### 2. Skill Layer (`skill-requirement-expert`)
- **Location**: `my-skills/skill-requirement-expert/`
- **Role**: 
    - 構造化された質問の提示。
    - ユーザー回答の要約と `requirements.md` への整形。
    - 新規Issue作成のサポート。

## Workflow Implementation
- **Deep Dive**: `gh issue view` を使用して既存情報を取得。
- **Template**: `requirements.md` の標準フォーマットを定義。

## Integration
- `.gemini` サブモジュールの更新と `my-skills` リポジトリへの反映。
