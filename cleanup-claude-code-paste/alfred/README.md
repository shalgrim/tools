# Alfred workflow setup

One-time setup in the Alfred preferences UI:

1. Open **Alfred Preferences → Workflows**, click the **+** button, choose **Blank Workflow**. Name it "Cleanup Claude Code Paste" (or whatever).
2. Right-click the canvas → **Inputs → Keyword**. Configure:
   - **Keyword:** `cleanup` (or your preference)
   - **Argument:** No Argument
   - **Title:** `Cleanup Claude Code Paste`
3. Right-click the canvas → **Actions → Run Script**. Configure:
   - **Language:** `/bin/bash`
   - **Script:**
     ```sh
     /Users/scotthalgrim/repos/tools/cleanup-claude-code-paste/alfred/run.sh
     ```
4. Drag a wire from the Keyword block to the Run Script block.
5. (Optional) Add an **Outputs → Post Notification** action wired off the Run Script so you get a "Copied" confirmation.

## How it works

The `run.sh` script invokes the Python tool with `-c`, which reads from `pbpaste` and writes the cleaned result back via `pbcopy`. Nothing else to configure — your clipboard content is replaced in place.

## Usage

1. Copy messy Claude Code terminal text to the clipboard
2. Trigger Alfred (`⌥Space` or whatever you use), type `cleanup`, press Enter
3. Paste — clipboard now holds the cleaned version
