#!/bin/bash
# Alfred runner: take current clipboard → cleanup script → clipboard.
# Hook this up in Alfred as a Keyword → Run Script action (language: /bin/bash).
#
# Alfred's Run Script PATH is minimal (no ~/.local/bin, no /opt/homebrew/bin),
# so we use absolute paths to uv and prepend common install locations to PATH
# in case uv shells out to anything else.

set -euo pipefail

export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"
UV="$HOME/.local/bin/uv"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"$UV" run python "$SCRIPT_DIR/cleanup_claude_code_paste.py" -c

echo "Cleaned Claude Code paste copied to clipboard"
