# Design Document: Issue #55 - RAW ログと信頼性スコアに基づく /self-optimize の刷新

## 1. 概要
従来の自己申告ベースの `/self-optimize` を、`.ops/audit_logs/raw/` の実行データと `integrity_audit.py` によるスコアリングに基づく客観的な改善サイクルへ刷新する。

## 2. アーキテクチャ構成
### 2.1 コンポーネント
- **CLI Command (`.gemini/commands/self-optimize.md`)**: エントリポイント。
- **Skill (`.gemini/skills/skill-self-optimizer/SKILL.md`)**: ロジックの実装。
- **Auditor (`.ops/scripts/integrity_audit.py`)**: 外部監査ツール。

### 2.2 データフロー
1. `self-optimize` 実行
2. `skill-self-optimizer` が起動
3. `integrity_audit.py` を呼び出し、最新の RAW ログからスコアを取得
4. スコアとエラー内容、過去のメトリクス (`.ops/audit_logs/metrics.json`) を分析
5. 改善提案 (Diff) を生成しユーザーに提示

## 3. 詳細設計
### 3.1 RAW ログの特定ロジック
- `.ops/audit_logs/raw/` から最新の `.log` ファイルを特定する。
- タイムスタンプが最も新しいものをデフォルトとする。

### 3.2 改善提案ロジックの強化
- **幻覚の検知**: 開発ログで「成功」と書いているが、RAW ログで `error` が出ている場合。
- **ツールの誤用**: 存在しないツールの呼び出しや、引数の不足。
- **調査不足**: `grep_search` や `read_file` の回数が極端に少なく、推測でコードを書いている場合。

これらのパターンに対し、`.roo/rules-*` に「具体的な制約」を追加する提案を行う。

## 4. 影響範囲
- `.gemini/commands/self-optimize.md`
- `.gemini/commands/self-optimize.toml` (引数の追加等が必要な場合)
- `.gemini/skills/skill-self-optimizer/SKILL.md`
- `.ops/audit_logs/` (読み取りのみ)
