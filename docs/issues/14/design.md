# Design: Extending Skill-Architect for Project Structuring

## Concept: Three-Tier Project Architecture
The skill will support the creation and maintenance of:
1.  **Constitution (`agents.md`)**: The behavioral rules for AI agents. Must be project-agnostic.
2.  **Map (`README.md`)**: The project-specific mapping of infrastructure, tools, and goals.
3.  **Implementation (Skills)**: The concrete tools and scripts.

## Functional Extensions
The `skill-architect` will be enhanced with scripts to automate the management of this architecture.

### 1. Project Scaffolding (`scripts/scaffold_project.sh`)
- Generates a generic `agents.md` that refers to the "Map" for details.
- Generates a structured `README.md` with sections for "Architecture" and "Operational Protocols" (Source of Truth, Path Mappings, Tooling).

### 2. Architecture Validation (`scripts/validate_architecture.sh`)
- Scans `agents.md` for abstract terms (e.g., "Common Infrastructure").
- Verifies that these terms are defined in the "Concrete Mapping" table in `README.md`.
- Checks if the mapped paths actually exist in the repository.

### 3. Template Management
- Store standard templates for `agents.md` and `README.md` in `.gemini/skills/skill-architect/templates/`.

## Updated SKILL.md Structure
Add a new section for "Project Architecture Management" to the existing `SKILL.md`, describing how to invoke these new scripts.

## Technical Stack
- **Shell Scripts / Node.js**: For file manipulation and template injection.
- **Markdown Parsing**: Simple grep/awk or a small script to extract tables from README.md.
