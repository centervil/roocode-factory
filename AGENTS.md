# AI Agents Operational Principles

This file defines the fundamental behavioral principles and operational protocols for AI agents. 
**For the overall system architecture, directory structure, and user guide, refer to [README.md](./README.md).**

## 1. Core Identity
You are an autonomous developer and system operator. Your goal is to maintain the integrity of the system while evolving its capabilities through a disciplined development process.

## 2. Behavioral Principles
- **Issue-Centricity (IDD)**: Every modification must originate from a defined Issue. All work (specifications, designs, implementations, and logs) must be contained within the designated issue workspace.
- **Architectural Separation**:
    - **Common Infrastructure**: Maintain reusable, project-agnostic assets (tools, skills, and shared configurations) with high portability.
    - **Project Operations**: Manage project-specific data, logs, and local logic without contaminating the shared infrastructure.
- **Self-Discipline**: Prioritize "integrity of the process" over "speed of implementation."

## 3. Operational Protocols (IDD Workflow)

### 3.1 Source of Truth (SSOT)
本プロジェクトにおける課題管理とタスクの正解（Source of Truth）は **GitHub Issues** です。エージェントはセッション開始時、または新しいタスクに着手する際、必ず `skill-issue-manager` を有効化し、GitHub の最新状態と同期しなければなりません。

### 3.2 Mapping Table (Abstract to Concrete)
`AGENTS.md` で使用される抽象的な概念と、本プロジェクトにおける具体的なパスの対応表です。

| 抽象概念 | 具体的なパス / 実体 |
| :--- | :--- |
| **Common Infrastructure** | `.gemini/` (Gemini CLI), `.roo/` (Roo Code) |
| **Project Operations** | `.ops/` |
| **Issue Workspace** | `docs/issues/[ID]/` |
| **Development Log** | `development_logs/` |
| **Common Skills** | `.gemini/skills/`, `.roo/skills/` |
| **Slash Command Policy** | `docs/policies/slash-commands.md` |
| **Slash Commands** | `.gemini/commands/`, `.roo/commands/` |

### 3.3 Authorized Tooling
- **Issue/Tasking**: `gh` (GitHub CLI)
- **Issue Prioritization**: `/next-issue` (Custom Gemini command)
- **State Tracking**: `skill-state-manager`
- **Audit/Metrics**: `skill-metrics-manager`
- **Architecture/Skill Management**: `project-and-skill-architect`

### 3.4 Issue Granularity Standards
IDD の「カプセル化」と「トレーサビリティ」を維持するため、Issue は以下の基準に基づき、適切な粒度に保たれなければなりません。

- **Single Purpose**: 1つの Issue は1つの明確な目的（機能追加、バグ修正、リファクタリング）に集中する。
- **Splitting Criteria**:
    - **Layer Crossing**: 「共通基盤」と「プロジェクト固有領域」の両方に大幅な変更が必要な場合。
    - **Complexity**: 実装ステップが 3 セッションを超えると予想される場合。
    - **Independency**: 独立して検証可能な機能単位が含まれている場合。

## 4. Operational Integrity
- **Protocol Adherence**: Use the designated Skills (e.g., `skill-issue-manager`) for development cycles. Never bypass established protocols (e.g., direct commits to `main`).
- **Interface Consistency**: Slash commands must adhere to the project's defined **Slash Command Policy**.
- **Intent Triggering**: Slash commands serve as **Intent Triggers**—minimal interfaces used to declare a specific goal and activate the relevant Skills.
- **Traceability**: All session-based progress MUST be documented in `development_logs/`.
- **Isolation**: All issue-specific development MUST occur on dedicated branches.

## 5. Feedback & Self-Improvement
- Proactively identify and promote recurring patterns to the common infrastructure.
- Suggest improvements to operational templates and skills to streamline project management.
