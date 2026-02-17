# Design: Issue #26 - Issue Prioritization Automation

## Architecture Overview
Gemini CLIのカスタムコマンド機能（`.gemini/commands/`）を利用して、プロジェクトの現状を分析し次の一手を提案するプロンプトを構築する。

## Components

### 1. Command Definition (`.gemini/commands/next-issue.toml`)
- **prompt**: プロジェクトの文脈（`project_state.md`, `gh issue list`）を動的に注入し、エージェントに分析を依頼する。
- **argument**: 必要に応じて、追加のコンテキストや優先度の重み付けを指定するための引数を定義する（今回は引数なしから開始）。

### 2. Analysis Prompt
エージェントに対して以下のステップで思考を促す。
1. **Status Review**: `project_state.md` から現在のフェーズとマイルストーンを理解する。
2. **Issue Scan**: `gh issue list` から未完了のIssueをリストアップする。
3. **Reasoning**: 各Issueが現在のフェーズの目標に対してどれだけ貢献するか、またはブロックされているかを推論する。
4. **Recommendation**: 最適なIssueを1つ選択し、その理由を構造化して提示する。

## Processing Flow
1. ユーザーが `/next-issue` を実行。
2. CLIが `!{cat .ops/project_state.md}` と `!{gh issue list --limit 30}` を実行し、結果をプロンプトに埋め込む。
3. エージェントが注入された情報を元に分析を実行。
4. 分析結果と推奨事項をマークダウン形式で回答。

## Safety & Security
- `gh issue list` は参照のみ。
- 特記すべき秘密情報の読み込みは発生しない。
