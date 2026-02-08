# Requirements: Relocate Policies to .ops for Tool Independence

## Context
Currently, project policies are located in `.roo/policies/`, which creates an asymmetric dependency and places tool-agnostic rules inside a tool-specific folder.

## Goal
Relocate policies to `.ops/policies/` to ensure that `.gemini` and `.roo` remain independent, flat, and interchangeable infrastructure folders.

## Acceptance Criteria
- [ ] **Data Migration**: All files in `.roo/policies/` are moved to `.ops/policies/`.
- [ ] **Broken Reference Fixes**: All scripts and documentation referencing `.roo/policies/` are updated to point to `.ops/policies/`.
- [ ] **Independence Verified**: `.gemini` and `.roo` no longer contain shared project policies, establishing them as pure tool-specific infrastructure.