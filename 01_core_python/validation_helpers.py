"""
Day 7: Functions, Return Values, and try/except

Spec (see ../../fundamentals/01_core_python/README.md for full details):

- check_required_fields(data, required_fields)
    -> True if all required_fields exist as keys in dict `data`, else False.

- safe_divide(a, b)
    -> a / b, or the string "Cannot divide by zero" on ZeroDivisionError.

- parse_note_severity(note_text)
    -> extract the number from a string like "priority:3"
       (split on ":", int() the second part inside try/except ValueError)
       returns the number, or 0 if none found.

- main()
    -> calls each function above with a couple of test inputs and prints
       the results.
"""


def check_required_fields(data, required_fields):
    # TODO: implement
    pass


def safe_divide(a, b):
    # TODO: implement
    pass


def parse_note_severity(note_text):
    # TODO: implement
    pass


def main():
    # TODO: call check_required_fields with a couple of test dicts
    # TODO: call safe_divide with normal and zero-division inputs
    # TODO: call parse_note_severity with valid and invalid strings
    pass


if __name__ == "__main__":
    main()
