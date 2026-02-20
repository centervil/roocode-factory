# Design: Restore `self-optimize` slash command to `my-commands` submodule

## Overview
Restore the `/self-optimize` slash command that was removed during the `my-commands` submodule integration. The command will be implemented as a `.toml` definition with a symbolic link `.md` for consistency with other commands.

## Architecture
- **Location**: `.roo/commands/` (which is the `my-commands` submodule).
- **Format**: `.toml` for the command definition and a `.md` as a symbolic link to the `.toml`.
- **Content**: Port the content from the old `self-optimize.md` to the `.toml` format.

## Implementation Details
1. **Definition (`self-optimize.toml`)**:
   - `name`: "self-optimize"
   - `description`: Analyze accumulated action logs and propose improvements to system definitions or Skills.
   - `argument-hint`: "log_file"
   - `prompt`: Ported and updated from the old `self-optimize.md`.
2. **Symbolic Link (`self-optimize.md`)**:
   - Link to `self-optimize.toml`.
3. **Submodule Integration**:
   - Update `my-commands` repo (within `.roo/commands/`).
   - Update `.roo` repo (root of the `.roo/` directory) to point to the new `my-commands` commit.
   - Update the root project to point to the new `.roo` commit.

## Considerations
- Ensure the prompt correctly activates `skill-self-optimizer`.
- Maintain the mission and procedure as defined in the original `self-optimize.md`.
