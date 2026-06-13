"""
Day 17-18: Add Human Resume

Spec (see ../../fundamentals/03_build_week/README.md for full details):

Copy this file forward from engine_v1.py and extend it.

New concept -- sys.argv:
    When you run `python engine_v2.py --resume`, sys.argv is
    ["engine_v2.py", "--resume"]. Check "--resume" in sys.argv to detect
    the flag. `import sys` at the top.

- At the top of main(), check `if "--resume" in sys.argv:` and branch.

When resuming:
- Read workspace/PENDING_meeting_summary.md.
- Extract the edited JSON from a ```json ... ``` code block.
- Re-validate the edited JSON against the schema.
- If valid: save as final_summary.json, append
    [timestamp] node=prompt status=approved by=human
  to the audit log, print success, exit.
- If still invalid: overwrite PENDING_meeting_summary.md with updated
  errors, append [timestamp] node=prompt status=escalated again, print
  that it's still pending, exit.

The script should work correctly whether run fresh (python engine_v2.py)
or with --resume -- same file, same logic, different entry path.

Test:
1. Run fresh, force a failure (use confusing notes).
2. Open PENDING_meeting_summary.md, fix the JSON to match the schema, save.
3. Run `python engine_v2.py --resume`. Verify final_summary.json is
   created and the audit log shows "approved by=human".
4. Repeat, but edit the pending file *incorrectly* (e.g. empty
   action_items). Confirm it re-escalates with updated errors.
"""

import json
import os
import sys
from datetime import datetime

import requests

CONFIG_DIR = "config"
WORKSPACE_DIR = "workspace"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


def load_config():
    # TODO: copy forward from engine_v1.py
    pass


def validate_against_schema(output, schema):
    # TODO: copy forward from engine_v1.py
    return False, ["not implemented"]


def call_model(prompt_text):
    # TODO: copy forward from engine_v1.py
    pass


def append_audit_log(line):
    # TODO: copy forward from engine_v1.py
    pass


def write_pending_file(last_output, errors):
    # TODO: copy forward from engine_v1.py
    pass


def extract_json_from_pending():
    """Read workspace/PENDING_meeting_summary.md, return the edited dict from the ```json block."""
    # TODO: implement
    pass


def run_fresh(schema, system_prompt):
    # TODO: same prompt-validate-retry loop as engine_v1.py
    pass


def run_resume(schema):
    # TODO: extract_json_from_pending(), re-validate, write final_summary.json
    # or re-escalate, per spec above
    pass


def main():
    os.makedirs(WORKSPACE_DIR, exist_ok=True)
    schema, system_prompt = load_config()

    if "--resume" in sys.argv:
        run_resume(schema)
    else:
        run_fresh(schema, system_prompt)


if __name__ == "__main__":
    main()
