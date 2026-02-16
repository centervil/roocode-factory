# Requirements: Issue #20 - Formalize Requirement Definition Process

## Goal
ユーザーの抽象的な要望を、エージェントが正確に実装可能な「明確な要件定義」へと昇華させるための標準的な対話プロセスとアウトプット形式を確立する。

## Background
- ユーザーの要求が抽象的（ぼんやりしている）な場合、エージェントが誤った解釈で実装を進めるリスクがある。
- 要件定義（Phase: Start）の質を安定させるための「型」が必要。
- これを Skill またはスラッシュコマンドとして実装し、IDDプロセスに強制的に組み込む。

## Functional Requirements
1. **Interactive Interview**: ユーザーに対して、以下の要素を引き出すための構造化された質問を行う。
   - **Context**: なぜこれが必要なのか？（背景）
   - **User Story**: 誰が、いつ、どのように使うのか？
   - **Success Criteria**: どのような状態になれば「完了」か？（具体的な期待値）
   - **Constraints**: 技術的、構造的、または運用上の制約。
2. **Output Generation**: 対話結果を `requirements.md` に自動的にまとめ、ユーザーの承認を得る。
3. **Integration**: IDDの `Phase: Start` において、このプロセスをデフォルトで実行する仕組み。

## Success Criteria
- ユーザーが「何をしたいか」を自分で詳細に書かなくても、エージェントとの数回のやり取りで `requirements.md` が完成すること。
- 完成した `requirements.md` に基づいて、エージェントが迷わずに `design.md` や `tasks.md` を作成できること。
