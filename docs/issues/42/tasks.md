# Tasks: Fix Roo Code command flow (Issue 42)

- [ ] **Phase 1: Implementation**
    - [ ] `.roo/commands/*.md` を独立したファイルとして作成 (TOML 混在を排除)
    - [ ] `.gemini/commands/*.toml` から Roo Code 専用フィールドを削除
    - [ ] `.roo/commands/*.toml` および `.gemini/commands/*.md` などの重複・不要ファイルを削除
    - [ ] `docs/policies/slash-commands.md` の更新
- [ ] **Phase 2: Validation**
    - [ ] Gemini CLI で各コマンドが正常にパース・実行できることを確認
    - [ ] Roo Code 用の Markdown フォーマットが正しいか自己レビュー
- [ ] **Phase 3: Completion**
    - [ ] PR 作成
