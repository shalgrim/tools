#!/bin/bash
# Alfred runner: take current clipboard → cleanup script → clipboard.
# Hook this up in Alfred as a Keyword → Run Script action (language: /bin/bash).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

uv run python "$SCRIPT_DIR/cleanup_claude_code_paste.py" -c
