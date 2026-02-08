# Design: Relocate Policies to .ops

## Structural Changes
Policies define the "rules of the game" for this specific project. They are not inherent to Roo Code or Gemini CLI.

### Old Structure
- `.roo/policies/metrics.yaml`
- `.roo/policies/quality.yaml`

### New Structure
- `.ops/policies/metrics.yaml`
- `.ops/policies/quality.yaml`

## Reference Updates
I need to update the following known references:
1.  `.gemini/skills/skill-metrics-manager/scripts/check-gates.py`: Path to `metrics.yaml`.
2.  `.gemini/skills/skill-metrics-manager/SKILL.md`: Documentation mentions.
3.  `README.md`: Any mentions of the policy path.

## Verification Plan
1.  Run `run-audit.sh --check` and ensure it still finds the policy files and correctly validates the metrics.
