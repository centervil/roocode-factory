# Design: Abstracting behavioral principles in AGENTS.md

## Abstraction Mapping
The following project-specific terms will be replaced with abstract concepts:

| Project-Specific Term | Abstract Replacement |
|-----------------------|----------------------|
| `.gemini/`            | Common Infrastructure (Tool-specific) |
| `.roo/`               | Common Infrastructure (Tool-specific) |
| `.ops/`               | Project-Specific Operations / Data |
| `docs/issues/[ID]/`   | Issue Workspace |
| `work/issue-xxx/`     | Temporary Work Area |

## Architectural Principles
Instead of hardcoding paths, the principles will refer to the **"Three-Tier Architecture"** (Infrastructure, Shared Config, Project Operations) or the definitions provided in the project's root `README.md`.

## Integration with README.md
`AGENTS.md` will explicitly state that the concrete folder structure and project goals are defined in `README.md`, which serves as the "Map" for the agent.
