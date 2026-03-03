# Design: Gemini CLI integration with Roo Code CLI (/run-roo)

## Overview
Implement the `/run-roo` command for Gemini CLI to interact with Roo Code through the official `roo` CLI instead of Playwright. This approach improves stability and bypasses authentication challenges of web-based interfaces.

## Backend: Roo Code CLI
- **Source**: `https://github.com/RooCodeInc/Roo-Code/tree/main/apps/cli`
- **Installation**: Official install script.
- **Capabilities**: Support for various modes (architect, code, ask, etc.) and non-interactive execution.

## Components

### 1. CLI Setup
- Automate the installation of `roo` CLI using the `.infra/scripts/setup_roo.sh` script.
- Ensure `roo` is in the PATH by updating shell profiles.
- Verify installation with `roo --version`.

### 2. Command Definition (`.gemini/commands/run-roo.toml`)
- Define the `/run-roo` slash command.
- Map arguments to `roo` CLI flags.
  - `--mode <mode>` -> Passed to `roo`.
  - `<prompt>` -> Passed to `roo`.

### 3. Environment Variable Management
- `roo` CLI requires API keys (e.g., `OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY`).
- These should be managed via `.env` or system environment variables.

### 4. Integration Logic
- The Gemini CLI will execute the `roo` command via shell.
- Monitor output and handle task completion.

## Security
- API keys must not be logged or exposed.
- Use standard environment variable practices.
