"""
Day 8-9: Reading and Writing Files

Spec (see ../../fundamentals/02_file_json_http/README.md for full details):

- Create a folder `workspace/` (os.makedirs("workspace", exist_ok=True)).
- Accept a meeting title from the user, then accept multi-line input for
  raw meeting notes -- keep reading lines until the user types "END" on
  its own line. Write all of it to workspace/input.txt.
- Append a line to workspace/run_log.txt with the current timestamp
  (from datetime import datetime) and the filename you just wrote.
- Read back all files in workspace/ (os.listdir) and print a summary:
  filename, size in bytes (os.path.getsize), and the first 50 characters
  of each file's content.
- Wrap file-reading operations in try/except FileNotFoundError so a
  missing workspace/ prints "No workspace yet" instead of crashing.
"""

import os
from datetime import datetime

WORKSPACE_DIR = "workspace"


def ensure_workspace():
    # TODO: os.makedirs(WORKSPACE_DIR, exist_ok=True)
    pass


def read_meeting_notes():
    """Prompt for a title, then read lines until 'END'. Return (title, notes_text)."""
    # TODO: implement
    pass


def write_input_file(title, notes_text):
    # TODO: write to workspace/input.txt
    pass


def append_run_log(filename):
    # TODO: append "<timestamp> wrote <filename>" to workspace/run_log.txt
    pass


def summarize_workspace():
    """Print filename, size in bytes, and first 50 chars for each file in workspace/."""
    # TODO: implement, wrap in try/except FileNotFoundError
    pass


def main():
    ensure_workspace()
    # TODO: tie the pieces above together
    summarize_workspace()


if __name__ == "__main__":
    main()
