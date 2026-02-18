# Tasks: Project Initialization Workflow as Slash Command (Issue #23)

## Phase 1: Environment Preparation
- [x] 1.1 `docs/issues/23/requirements.md` および `docs/issues/23/design.md` の作成。 (完了)
- [x] 1.2 `docs/issues/23/tasks.md` の作成。 (完了)

## Phase 2: Implementation
- [x] 2.1 Slash command `/setup-project` の定義 (`.gemini/commands/setup-project.toml`)。 (名称変更反映済)
- [x] 2.2 `skill-project-and-skill-architect` スキルへの `setup-project.sh` スクリプトの追加。
- [x] 2.3 `skill-project-and-skill-architect/SKILL.md` にセットアップ機能についての説明を追記。
- [x] 2.4 `setup-project.sh` 内でのテンプレートコピーとプレースホルダー置換のロジック実装。
- [x] 2.5 `README.md` および `AGENTS.md` のバックアップ機能（`.old.md`）の実装。 (完了)
- [x] 2.6 `AGENTS.md` を原則（Constitution）に特化させた雛形への修正。 (完了)

## Phase 3: Verification
- [x] 3.1 ダミーのターゲットディレクトリを作成し、`/setup-project` コマンドを実行して初期化を確認。
- [x] 3.2 生成された `README.md`, `AGENTS.md` の品質と整合性の検証。
- [x] 3.3 バックアップ処理の動作確認。

## Phase 4: Finalize
- [x] 4.1 開発ログの記録 (`development_logs/`).
- [x] 4.2 コミットとブランチ移行 (`feat/issue-23`).
- [x] 4.3 Issueのクローズ。
