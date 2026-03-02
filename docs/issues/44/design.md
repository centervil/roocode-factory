# Design: 【MVP】Roo-Orchestrator インフラ基盤の構築 (Docker + Tailscale + Playwright)

## 概要
Gemini CLI から Roo Code を遠隔操作するための実行基盤（Dockerコンテナ）を構築する。

## 目標 (Goals)
- シングルコンテナ構成による管理の簡素化。
- Tailscale によるセキュアな VPN 接続。
- コンテナ再起動・再ビルド後も設定や認証が維持される「持続可能な開発環境」。
- Playwright を用いた Roo Code UI の自動操作基盤。

## 構成案 (Architecture)

### 1. 配置構成
- `.infra/`: Docker 関連ファイルを配置。
    - `Dockerfile`: `code-server` をベースに Playwright と Tailscale をインストール。
    - `docker-compose.yml`: ボリューム、ネットワーク、デバイスの設定。
    - `scripts/entrypoint.sh`: Tailscale と code-server の起動プロセス管理。

### 2. コンテナ詳細
- **ベースイメージ**: `codercom/code-server` (Ubuntuベース)
- **追加コンポーネント**:
    - `Tailscale`: VPN 接続。
    - `Playwright`: ブラウザ自動操作用。
    - `Node.js / npm`: 開発ツール。

### 3. 永続化戦略
- **Tailscale**: `/var/lib/tailscale` を `tailscale-data` ボリュームに保存。
- **code-server / Roo Code**: `/home/node/.local/share/code-server` を `code-server-data` ボリュームに保存。
- **ワークスペース**: ホストのプロジェクトルートを `/home/node/project` にマウント。

### 4. セキュリティ
- Tailscale 経由のアクセスのみを許可する（デフォルトのポート公開は最小限にする）。

## Success Criteria
- [ ] `.infra/` 内の `docker-compose up -d` でコンテナが正常に起動する。
- [ ] コンテナ再起動・再ビルド後も、Tailscale 経由で即座に VPN 接続ができる。
- [ ] コンテナ再起動・再ビルド後も、Roo Code の LLM 設定が保持されている。
- [ ] コンテナ内から Playwright を用いて、code-server の DOM を認識できる。
