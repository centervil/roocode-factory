# Requirements: Design and Implement Project-Agnostic Metrics Architecture

## User Stories
- As a **Platform Maintainer**, I want a **project-agnostic metrics architecture** so that I can collect AI-centric metrics (like Autonomy and Compliance) without hardcoding project-specific logic into shared infrastructure.
- As a **Project Lead**, I want to define **project-specific collectors** outside of the shared `.gemini` folder so that I can customize metrics for my specific project needs without forking the core tools.
- As a **Compliance Officer**, I want to see a **Compliance Score** based on protocol adherence so that I can verify if the AI agents are following the rules.

## Acceptance Criteria
- [ ] **Architecture**: The metrics collection system is refactored to support a plugin-like architecture.
- [ ] **Separation of Concerns**: `.gemini` scripts act only as orchestrators; specific collectors are defined in project-level configuration (e.g., `.ops/` or similar).
- [ ] **Metric Definitions**: Definitions for "AI Autonomy" and "Protocol Compliance" are documented and implemented.
- [ ] **Proof of Concept**: A working PoC calculates and reports a "Compliance Score".
- [ ] **Backward Compatibility**: Existing metrics (if any) continue to function or are migrated.
