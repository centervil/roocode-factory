# Design: Issue #5 - Protocol Hardening

## Proposed Changes

### 1. Update Orchestrator Rules (`.roo/rules-orchestrator/00-contract.md`)
- Add a section on "Error Handling & Protocol Validation".
- Define how to handle `NG` or `BLOCK` status (Retry logic).
- Specify that the Orchestrator must validate incoming `DispatchObject` and outgoing `ResultObject` (manually or via tool).

### 2. Update Interaction Schema (`.roo/docs/protocols/interaction_schema.yaml`)
- Add specific error types and codes for protocol violations.
- Define a "Retry Policy" field if necessary, or specify it in the Orchestrator's internal logic.

### 3. Implementation of Validation Logic (Skill/Script)
- Create a simple validation script (e.g., `scripts/validate_protocol.py` or a skill) that can be used by any mode to verify if a YAML object conforms to the `interaction_schema.yaml`.
- This script should be callable via `run_shell_command`.

## Implementation Strategy
- **Phase 1**: Update documentation and rules to reflect the hardened protocols.
- **Phase 2**: Implement a validation script using a library like `jsonschema` (converting YAML to JSON or using a YAML schema validator).
- **Phase 3**: Update the Orchestrator and PM instructions to utilize this validation script.

## Alternatives Considered
- **Strict Prompting Only**: Relying solely on prompt instructions. (Lower robustness).
- **Hard-coded JSON only**: Switching from YAML to JSON. (YAML is more human-readable and token-efficient for some models, so we stay with YAML but harden it).
