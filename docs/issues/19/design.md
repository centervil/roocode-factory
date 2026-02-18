# Design: Issue #19 Refactor External Dependencies

## 1. Core Concept: Dynamic Resource Discovery
Currently, skills are coupled to specific file paths like `AGENTS.md`. We will implement a strategy where skills attempt to locate these resources relative to the current working directory (CWD) or through environment variables.

## 2. Architecture Changes

### 2.1. Project Root Discovery
Skills that need to access project-wide files (`AGENTS.md`, `.ops/`, etc.) will use the following lookup order:
1.  **Environment Variable**: `ROOCODE_PROJECT_ROOT` (if set).
2.  **Upward Search**: Look for a marker file (`.git`, `AGENTS.md`, or `.roo/`) starting from the CWD and traversing upwards.
3.  **Fallback**: If not found, default to CWD but handle missing files gracefully with informative error messages.

### 2.2. Abstraction of Path References
-   **Skill Instructions**: Replace literal strings like "Refer to AGENTS.md in the root" with generic descriptions or variable placeholders if the execution engine supports them.
-   **Scripts**: Shell scripts should not use absolute paths like `/home/centervil/...`. Use `$(dirname "$0")` for relative asset loading or the discovery mechanism described in 2.1.

## 3. Implementation Details

### 3.1. Identifying the "Core Identity File"
The project's "Source of Truth" (currently `AGENTS.md`) should be identified by its role rather than just its name. However, for compatibility, we will continue to look for `AGENTS.md` but through the dynamic discovery utility.

### 3.2. Error Handling
If a required file is missing after discovery, the skill must:
1.  Log a clear error message: "Required project metadata file (AGENTS.md) not found in [path] or its parents."
2.  Suggest the user to run the initialization skill (Issue #23).

## 4. Portability Strategy
The `my-skills` folder should be entirely self-contained logic-wise. Any interaction with the host project must be via standard interfaces or discovered paths.
