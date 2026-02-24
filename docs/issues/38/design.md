# Design: Final Full Repository Audit & Cleanup (Issue 38)

## 1. Overview
Phase 4 (Release Candidate) における最終監査。プロジェクトの成果物である `.roo` が設計思想通りに完成していることを保証し、リリース可能な状態にクリーンアップする。

## 2. Audit Focus Areas

### 2.1 System Definition Alignment
- **Source of Truth**: `.roo/docs/system-definition.md`
- **Audit Method**: 全ての機能、エージェント、プロトコルが物理的なファイル（スクリプト、Skill）として実装されているかを確認。不足があれば Issue を立てるか、今回のクリーンアップ範囲内で修正する。

### 2.2 Strategic Doc Separation (README vs AGENTS)
- **README.md**: 
    - 役割: プロジェクト概要、アーキテクチャ図、物理ディレクトリ構造、インストール・使用方法。
    - 修正方針: 技術的な「振る舞い」に関する記述を AGENTS.md へ移行。
- **AGENTS.md**: 
    - 役割: AI エージェントの憲章、行動指針、運用プロトコル（IDD ワークフロー等）、禁止事項。
    - 修正方針: プロジェクト構造の「説明」を README.md へ移行。重複を排除。

### 2.3 Skill Responsibility Optimization
- **Goal**: 1 Skill = 1 Responsibility.
- **Audit Method**: 各 Skill の `SKILL.md` を読み込み、機能の重複（例: `skill-research` と `skill-investigator` の境界線）を排除。必要に応じて Skill の統合や分離を行う。

### 2.4 Template Compliance & Cleanup
- **Template**: `.ops/templates/` 配下を正とする。
- **Cleanup**: 
    - ドキュメント内のリンク切れ、古いパス（`.gemini/` と `.roo/` の混同等）を修正。
    - `TODO` コメントの解消。
    - 一時的な検証用ファイル（`test-project/` 下の古いもの等）を削除。

## 3. Architecture Consistency
- **Common Infrastructure**: `.gemini/skills/` はサブモジュールとして独立性を保つ。
- **Product Isolation**: `.roo/` が外部依存なしに動作可能な構成であることを確認。
