#!/bin/bash

# Define common flags
REPO_FLAG="" # Uses current directory context

# Create Labels if they don't exist (ignore errors if they do)
gh label create phase:core --color 0075ca -d "Phase 2: Core Implementation" 2>/dev/null
gh label create phase:validation --color d73a4a -d "Phase 3: Validation & Loop" 2>/dev/null
gh label create critical --color b60205 -d "Critical path items" 2>/dev/null

# Issue 1
gh issue create \
  --title "Implement Logging Skill (JSON/Markdown)" \
  --body "**Goal**: Enable standardized audit trails for all agents.\n\n**Tasks**:\n- Implement `skills/logging/SKILL.md`.\n- Support structured JSON output and human-readable Markdown.\n- Verify Orchestrator invocation." \
  --label "phase:core,critical,enhancement"

# Issue 2
gh issue create \
  --title "Implement State Management Skill" \
  --body "**Goal**: Automate the updates of `factory_state.md` and `project_state.md`.\n\n**Tasks**:\n- Create a skill to read current issue status.\n- Summarize progress and update the state markdown files.\n- Reduce PM cognitive load." \
  --label "phase:core,enhancement"

# Issue 3
gh issue create \
  --title "Implement Metrics Collection Base" \
  --body "**Goal**: Establish the foundation for quantitative quality assessment.\n\n**Tasks**:\n- Define temporary `policies/metrics.yaml`.\n- Create scripts to measure basic stats (e.g., test pass rate, code churn).\n- Output results to `audit_logs/`." \
  --label "phase:core,enhancement"

# Issue 4
gh issue create \
  --title "Dogfooding: Refactor a Skill" \
  --body "**Goal**: Validate the workflow by using Roocode to improve itself.\n\n**Tasks**:\n- Execute a full task cycle (PM -> Orchestrator -> Code -> Reviewer).\n- Target: Refactor one of the existing Skill definitions." \
  --label "phase:validation,test"

# Issue 5
gh issue create \
  --title "Integration of Quality Gates" \
  --body "**Goal**: Enable automated rejection based on metrics.\n\n**Tasks**:\n- Update Orchestrator protocol to check metrics.\n- Define failure paths (Rejection) when thresholds are not met." \
  --label "phase:validation,enhancement"

# Issue 6
gh issue create \
  --title "Protocol Hardening" \
  --body "**Goal**: Improve robustness of inter-agent communication.\n\n**Tasks**:\n- Add error handling for malformed YAML.\n- Implement retry logic for failed dispatches." \
  --label "phase:validation,enhancement"
