# Requirements: Project Initialization Workflow as Slash Command (Issue #23)

## Goal
別のプロジェクトにRoocodeを移植する際の初期設定（README.md, AGENTS.md, 各種テンプレート等）を高品質に完了させるワークフローを、Gemini CLIのSlash commandとして定義する。

## Background
新しいプロジェクトにRoocodeを導入する際、適切なディレクトリ構造（`.ops/`, `.gemini/`, `.roo/`）と、プロジェクトの「憲法」（AGENTS.md）や「地図」（README.md）を整合性を持って作成する必要がある。これを手動で行うのは時間がかかり、品質のばらつきが生じる。

## Functional Requirements
- **Slash Command `/setup-project`**: ユーザーが実行可能なセットアップコマンドを提供する。
- **Automated Structure Generation**:
  - `README.md` (Project Map / Static Definition)
  - `AGENTS.md` (Project Constitution / Principles-only)
  - `.ops/` (Operational logs, metrics, templates)
- **AGENTS.md Philosophy**: 具体的なIDDのフェーズ手順などは含めず、「Identity（自己の定義）」「Behavioral Principles（Issue-Centricity, Architectural Separation）」などの抽象化された普遍的な原則のみを定義する。
- **Backup Logic**: `README.md` または `AGENTS.md` が既に存在する場合、それぞれ `README.old.md`, `AGENTS.old.md` としてリネームしバックアップを作成してから新規生成する。
- **Manual Infrastructure**: `.gemini/` および `.roo/` はユーザーが手動で配置することを前提とし、このコマンドの自動生成対象からは除外する。
- **Template-Based**: `.ops/templates/system/` にあるテンプレートを使用して各ファイルを生成する。
- **Project Specific Adaptation**: プロジェクト名や概要をユーザーからヒアリングし、生成されるファイルに反映させる。

## Non-Functional Requirements
- **High Quality**: 生成されたファイルは、Roocodeの標準（AGENTS.mdのポータビリティ、README.mdのOperational Protocolsセクション等）に準拠していること。
- **Idempotency**: 既にファイルが存在する場合、上書きするか、差分を適用するかを選択できるようにする（初期実装では確認の上上書きを推奨）。

## Success Criteria
- `/init` コマンドを実行することで、Roocodeの運用に必要な基本ディレクトリとファイルが正しく生成されること。
- 生成された `AGENTS.md` と `README.md` が、プロジェクトの実態（ディレクトリ構成等）と整合していること。
