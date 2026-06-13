"""
Day 13-14: model_caller.py

Spec (see ../../fundamentals/02_file_json_http/README.md for full details):

- Read system_prompt.txt and test_input.txt.
- POST to http://localhost:11434/api/generate with JSON body:
    {"model": "llama3.2:3b", "prompt": system_prompt + "\n\n" + meeting_notes,
     "stream": false}
- Parse the response JSON; extract the "response" field (a string).
- json.loads() that string to get the model's {"summary": ..., "action_items": ...} dict.
- Call validate_against_schema() (from schema_checker.py) on this dict.
- If valid, write the dict to workspace/model_output.json (json.dump).

Error handling:
- requests.exceptions.ConnectionError ->
    print "Ollama not running; start with `ollama serve`"
- json.JSONDecodeError on the model's response string ->
    print "Model returned invalid JSON, raw response saved"
    and write the raw string to workspace/raw_response.txt

Retry loop:
- If validation fails, re-send the prompt with an added note describing
  what was wrong (e.g. append "\n\nYour previous response was missing
  'action_items'. Try again."), up to 2 retries.
- If still failing after that, print "Escalation needed — human review required."
"""

import json
import os

import requests

from schema_checker import load_schema, validate_against_schema

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"
WORKSPACE_DIR = "workspace"


def load_prompt_pieces():
    # TODO: read system_prompt.txt and test_input.txt, return both as strings
    pass


def call_model(prompt_text):
    """POST to Ollama, return the raw 'response' string. Handles ConnectionError."""
    # TODO: implement
    pass


def main():
    os.makedirs(WORKSPACE_DIR, exist_ok=True)
    schema = load_schema()

    # TODO: build initial prompt from system_prompt + meeting notes
    # TODO: loop up to 3 attempts total (1 initial + 2 retries):
    #   - call_model()
    #   - json.loads() the response, handle JSONDecodeError
    #   - validate_against_schema()
    #   - if valid: write workspace/model_output.json, break
    #   - if invalid: append failure note to prompt, retry
    # TODO: if still invalid after all attempts, print escalation message


if __name__ == "__main__":
    main()
