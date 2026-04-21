---
name: cleanup-claude-code-paste
description: Clean up the most recent assistant response (strip ❯ prompts, unwrap wrapped lines, preserve paragraphs) and copy the cleaned text to the macOS clipboard.
---

Take the text of your most recent assistant response in this conversation, pipe it through the `cleanup-claude-code-paste` script, and place the cleaned output on the user's clipboard.

## Steps

1. Locate your most recent completed assistant response in this conversation — the message immediately before the user's invocation of this skill. Use the full rendered text of that message (preserve markdown formatting, code fences, etc.).

2. Write that text to a temp file with the Write tool:
   - Path: `/tmp/cleanup-claude-code-paste-input.txt`
   - Content: the exact text of your prior response

3. Run this Bash command to clean the text and copy it to the clipboard:
   ```sh
   uv run python /Users/scotthalgrim/repos/tools/cleanup-claude-code-paste/cleanup_claude_code_paste.py < /tmp/cleanup-claude-code-paste-input.txt | pbcopy && rm /tmp/cleanup-claude-code-paste-input.txt
   ```

4. Confirm to the user in one short sentence that the cleaned response is on their clipboard.

## Notes

- If there is no prior assistant response (e.g., the skill is the first thing in the conversation), tell the user there's nothing to clean and stop.
- Do not modify or summarize the prior response — the script handles transformation. Your job is only to feed the original text through it.
