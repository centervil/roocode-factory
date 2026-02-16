# Design: Issue #21 - Roocode Self-Optimization Cycle

## Architecture

### 1. New Skill: `skill-self-optimizer`
- **Logging logic**: `.ops/audit_logs/self_optimization.json` に追記。
- **Analysis logic**: ログを要約し、現在の定義ファイルとの差分を抽出。
- **Output**: JSON/Markdown 形式のテンプレートに従った高密度ログ。

### 2. Mode Definition Updates (.roo/rules-*.md)
各Modeの指示の末尾に、以下のようなフックを追加する。
> "作業中に重要な判断を行った場合、またはツール実行後に想定外の結果を得た場合、`skill-self-optimizer` を使用してその文脈を記録せよ。"

### 3. Slash Command: `/self-optimize`
- **Location**: `.roo/custom_modes.json` (※今回は.roo専用とする)
- **Logic**: 
    - ログファイルを読み込む。
    - `skill-self-optimizer` を起動。
    - 改善提案を表示。

## Data Format (Log Template)
```json
{
  "timestamp": "ISO8601",
  "mode": "Mode Name",
  "context": "Short description of the task",
  "decision": "What you decided and why",
  "outcome": "Success/Failure/Unexpected",
  "key_metric": { "token_usage": "...", "turn_count": "..." }
}
```
