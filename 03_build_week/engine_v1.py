"""
Day 15-16: Project Setup and Run Loop (no pauses yet)

Spec (see ../../fundamentals/03_build_week/README.md for full details):

- Load config/schema.json and config/system_prompt.txt.
- Read raw meeting notes from workspace/input.txt (write one manually if needed).
- Run the prompt-validate-retry loop from Week 2 (up to 2 retries).

If validation passes:
- Save output as workspace/final_summary.json.
- Append a line to workspace/AUDIT_LOG.md:
    [2026-06-13T10:00:00] node=prompt status=success

If validation fails after retries:
- Write workspace/PENDING_meeting_summary.md containing:
    - The last model output (raw JSON or raw text if it didn't parse).
    - Which fields failed validation and why.
    - Instructions: "Edit the JSON below, then run with --resume."
- Append [timestamp] node=prompt status=escalated to the audit log.

Print a clear, one-line status message at the end either way.

Test:
- Run with clear, well-structured notes -> expect final_summary.json.
- Run with vague/contradictory notes -> expect PENDING_meeting_summary.md.
"""

import json
import os
from datetime import datetime

import requests

CONFIG_DIR = "config"
WORKSPACE_DIR = "workspace"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


def load_config():
    # TODO: load config/schema.json and config/system_prompt.txt
    pass


def validate_against_schema(output, schema):
    # TODO: copy forward from Week 2's schema_checker.py
    return False, ["not implemented"]


def call_model(prompt_text):
    # TODO: copy forward from Week 2's model_caller.py
    pass


def append_audit_log(line):
    # TODO: append a timestamped line to workspace/AUDIT_LOG.md
    pass


def write_pending_file(last_output, errors):
    # TODO: write workspace/PENDING_meeting_summary.md with last_output,
    # errors, and resume instructions
    pass


def main():
    os.makedirs(WORKSPACE_DIR, exist_ok=True)
    schema, system_prompt = load_config()

    # TODO: read workspace/input.txt
    # TODO: prompt-validate-retry loop (up to 2 retries)
    # TODO: on success -> write final_summary.json + audit log line, print status
    # TODO: on failure -> write_pending_file + audit log line, print status


if __name__ == "__main__":
    main()
