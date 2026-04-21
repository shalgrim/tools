#!/usr/bin/env python3
"""Clean up pasted Claude Code terminal output.

Local port of https://github.com/simonw/tools/blob/main/cleanup-claude-code-paste.html
"""
import argparse
import re
import subprocess
import sys


def cleanup(text: str) -> str:
    text = re.sub(r'^❯\s*', '', text, flags=re.MULTILINE)

    paragraphs: list[list[str]] = []
    current: list[str] = []
    for line in text.split('\n'):
        if line.strip() == '':
            if current:
                paragraphs.append(current)
                current = []
        else:
            current.append(line.strip())
    if current:
        paragraphs.append(current)

    return '\n\n'.join(
        re.sub(r'\s{2,}', ' ', ' '.join(p)) for p in paragraphs
    )


def _read_clipboard() -> str:
    return subprocess.run(
        ['pbpaste'], check=True, capture_output=True, text=True
    ).stdout


def _write_clipboard(text: str) -> None:
    subprocess.run(['pbcopy'], check=True, input=text, text=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        '-c', '--clipboard',
        action='store_true',
        help='Read from clipboard (pbpaste) and write to clipboard (pbcopy). macOS only.',
    )
    args = parser.parse_args()

    if args.clipboard:
        cleaned = cleanup(_read_clipboard())
        _write_clipboard(cleaned)
    else:
        sys.stdout.write(cleanup(sys.stdin.read()))


if __name__ == '__main__':
    main()
