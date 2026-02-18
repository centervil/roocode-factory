# Design: Project Initialization Workflow as Slash Command (Issue #23)

## Overall Architecture
この機能は、Gemini CLIのSlash command（`/init`）として実装される。
コマンドは `skill-project-and-skill-architect` などの既存スキルを呼び出し、特定の初期化スクリプトを実行する。

## Components

### 1. Slash Command Definition (`.gemini/commands/init.toml`)
- **Name**: `init`
- **Description**: "プロジェクトをRoocode向けに初期化し、標準的なディレクトリ構造と設定ファイルを生成します。"
- **Prompt**:
  - `activate_skill` ツールを使って `skill-project-and-skill-architect` を有効化する。
  - プロジェクト名と概要をユーザーからヒアリングする。
  - 初期化スクリプト（`init-project.sh`）を実行し、ヒアリングした情報を渡す。

### 2. Initialization Script (`.gemini/skills/skill-project-and-skill-architect/scripts/init-project.sh`)
- **Responsibility**:
  - `README.md`, `AGENTS.md`, `.ops/`, `.gemini/`, `.roo/` の雛形をコピーする。
  - `.ops/templates/system/` にある最新のテンプレート（`00-contract.md`, `10-operational-guidelines.md` 等）を元に、適切な場所に配置する。
  - プレースホルダー（`{{PROJECT_NAME}}`, `{{PROJECT_DESCRIPTION}}` 等）を、ヒアリングした情報で置換する。

### 3. Skill Update (`skill-project-and-skill-architect`)
- `SKILL.md` にプロジェクト初期化の役割を追記する。
- スクリプト `init-project.sh` を `scripts/` に追加する。

## Implementation Details
- **Backup Strategy**: `mv` コマンドを使用して既存の `README.md` を `README.old.md` へ、`AGENTS.md` を `AGENTS.old.md` へリネームする。
- **Directory Structure**:
  - `README.md` (Generated)
  - `AGENTS.md` (Generated)
  - `.ops/`
    - `project_state.md` (Generated)
    - `templates/` (Copy of current project's work-artifacts templates)
    - `policies/`
- **Exclusion**: `.gemini/` および `.roo/` は本コマンドでは作成しない。ユーザーが手動で配置することを前提とする。

## Verification
1.  `/init` コマンドを実行する。
2.  対話的にプロジェクト名と概要を入力する。
3.  期待されるディレクトリ構造とファイルが生成されていることを確認する。
4.  生成された `AGENTS.md` と `README.md` の内容を確認する。
