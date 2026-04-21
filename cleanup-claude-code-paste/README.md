# cleanup-claude-code-paste

Clean up pasted Claude Code terminal output: strip leading `❯` prompts, unwrap wrapped lines within a paragraph, and preserve paragraph breaks.

Local port of simonw's web tool: <https://github.com/simonw/tools/blob/main/cleanup-claude-code-paste.html>

## Usage

Stdin → stdout (composable):

```sh
pbpaste | uv run python cleanup_claude_code_paste.py | pbcopy
```

Clipboard round-trip (macOS):

```sh
uv run python cleanup_claude_code_paste.py -c
```

Stdlib only — no dependencies.

## Tests

```sh
uv run python -m unittest
```
