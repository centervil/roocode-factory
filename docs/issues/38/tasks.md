# Tasks: Final Full Repository Audit & Cleanup (Issue 38)

## 1. Phase 1: Audit & Discovery
- [ ] **1.1 Master Definition Audit**:
    - `.roo/docs/system-definition.md` を読み込み、現在の物理ファイル（スクリプト、Skill）との乖離をリストアップ。
- [ ] **1.2 Strategic Doc Role Audit**:
    - `README.md` と `AGENTS.md` の記述を精査し、重複や本来あるべき場所以外の記述を抽出。
- [ ] **1.3 Skill Responsibility Audit**:
    - 全ての `SKILL.md` を読み込み、機能の重複、曖昧さ、テンプレート非準拠をリストアップ。

## 2. Phase 2: Refactoring & Optimization
- [ ] **2.1 Document Separation Execution**:
    - `README.md` と `AGENTS.md` の役割分担を物理的に修正。
- [ ] **2.2 Skill Template Compliance & Optimization**:
    - `SKILL.md` を `.ops/templates/` 配下の最新テンプレートに全件適用。
    - 重複する Skill 責務の整理（統合または分離）。
- [ ] **2.3 System Consistency Fixes**:
    - 監査で見つかった設計との乖離（不足機能や過剰な実装）を修正。

## 3. Phase 3: Final Cleanup & Validation
- [ ] **3.1 Dead Assets & Links Cleanup**:
    - 全ドキュメントのデッドリンク修正。
    - TODO コメントの全廃。
    - 一時的なスクリプトや古い構成ファイルの削除。
- [ ] **3.2 Full Repository Validation**:
    - `.roo/` が独立した成果物として完結しているかを再確認。
    - 全体の整合性を確認する最終レビュー。
