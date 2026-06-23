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
    for field in required_fields:
        if field not in data:
            return False
    return True


def safe_divide(a, b):
    # TODO: implement
    try:
        ration = a / b
        return ration
    except ZeroDivisionError:
        return "Cannot divide by zero"


def parse_note_severity(note_text):
    # TODO: implement
    try: 
        parts = note_text.split(":")
        numerical_value = int(parts[1])
        return numerical_value
    except ValueError:
        return 0



def main():
    # TODO: call check_required_fields with a couple of test dicts
    # TODO: call safe_divide with normal and zero-division inputs
    # TODO: call parse_note_severity with valid and invalid strings
# 1. Testing check_required_fields
    required = ["id", "title", "severity"]
    test_dict_valid = {"id": 101, "title": "System Reboot Required", "severity": 3, "user": "admin"}
    test_dict_invalid = {"id": 102, "title": "Minor Warning"} # Missing 'severity'
    
    print("1A. check_required_fields (Valid Match):", check_required_fields(test_dict_valid, required))
    print("1B. check_required_fields (Missing Key):", check_required_fields(test_dict_invalid, required))
    print("-" * 50)

    # 2. Testing safe_divide
    print("2A. safe_divide (Standard Division):", safe_divide(25, 5))
    print("2B. safe_divide (Zero Division Safety):", safe_divide(25, 0))
    print("-" * 50)

    # 3. Testing parse_note_severity
    print("3A. parse_note_severity (Valid Text):", parse_note_severity("priority:3"))
    print("3B. parse_note_severity (Invalid Text Data):", parse_note_severity("priority:HIGH"))
    
    print("\n--- ALL TESTS EXECUTED SUCCESSFULLY ---")


if __name__ == "__main__":
    main()
