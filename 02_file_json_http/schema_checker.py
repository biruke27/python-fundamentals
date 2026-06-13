"""
Day 10-11: Working with JSON

Spec (see ../../fundamentals/02_file_json_http/README.md for full details):

- Load schema.json (already provided in this folder) with json.load.
- Write validate_against_schema(output, schema) that checks:
    - All fields in schema["required"] are present as keys in `output`.
    - output["summary"] is a string with length >=
      schema["properties"]["summary"]["minLength"].
    - output["action_items"] is a list with length >=
      schema["properties"]["action_items"]["minItems"].
- Return (True, []) if valid, or (False, ["reason 1", "reason 2", ...])
  listing every failed check.
- Test against at least four dictionaries:
    1. fully valid
    2. missing a required field
    3. summary too short
    4. action_items empty list
  Print the result of each test clearly.
"""

import json

SCHEMA_PATH = "schema.json"


def load_schema(path=SCHEMA_PATH):
    # TODO: json.load the schema file
    pass


def validate_against_schema(output, schema):
    """Return (True, []) if valid, else (False, [reasons...])."""
    # TODO: implement all three checks described above
    return False, ["not implemented"]


def main():
    schema = load_schema()

    test_cases = {
        "fully valid": {
            "summary": "This is a sufficiently long summary.",
            "action_items": ["Follow up with finance"],
        },
        "missing required field": {
            "summary": "This is a sufficiently long summary.",
        },
        "summary too short": {
            "summary": "short",
            "action_items": ["Follow up with finance"],
        },
        "empty action_items": {
            "summary": "This is a sufficiently long summary.",
            "action_items": [],
        },
    }

    # TODO: loop over test_cases, call validate_against_schema, print results clearly


if __name__ == "__main__":
    main()
