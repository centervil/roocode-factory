# Design for Issue 45: Roo-Orchestrator 自動操作ロジックの実装 (Playwright Driver)

## アーキテクチャ概要
AIエージェントがブラウザ上の VS Code Server (Roo Code) を操作するための TypeScript スクリプト群を Skill として実装する。

## コンポーネント構成
- **Runtime**: Node.js (TypeScript) + Playwright
- **Configuration**: `.env` (URL, Password)
- **Logging**: `.ops/roo_driver_logs/`
- **Skill Interface**: `skill-roo-driver` (Gemini CLI から呼び出し可能)

## 実装戦略
1.  **環境整備**: Dockerfile に Playwright 実行環境（ブラウザ、システム依存関係）を追加。
2.  **ドライバ実装**: 機能ごとに単一責務のスクリプトを作成。
    - `connect.ts`: 認証とセッション維持。
    - `change-mode.ts`: モード切り替え。
    - `send-prompt.ts`: プロンプト入力と実行。
    - `fetch-status.ts`: パネル内容の取得。
3.  **Skill 統合**: 上記スクリプトをラップする `SKILL.md` を作成し、Gemini CLI が「状況判断 -> 操作」のループを回せるようにする。

## 監視ロジック (Gemini CLI 連携)
1. `fetch-status` で現在のチャット履歴とスクリーンショットを取得。
2. Gemini CLI がその情報を読み、"Working" か "Completed" か、あるいはエラーかを判断。
3. 次のアクション（待機、リトライ、または完了報告）を決定。
