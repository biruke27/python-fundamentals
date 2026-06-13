"""
Day 3-4: Lists and List Operations

Spec (see ../../fundamentals/01_core_python/README.md for full details):

- Start with an empty list `agenda_items`.
- Menu loop (using `while True` and `input()`):
    1. Add item
    2. Remove item by number
    3. Show numbered list
    4. Exit
- After exiting, print the agenda as a formatted string:
    "- Item 1\n- Item 2\n..."
- Bonus: build that string using a list comprehension instead of a loop.
"""


def main():
    agenda_items = []

    while True:
        # TODO: print menu (1-4), get user choice with input()
        # TODO: handle "Add item" -> input() then append to agenda_items
        # TODO: handle "Remove item by number" -> input() index, pop()
        # TODO: handle "Show numbered list" -> enumerate + print
        # TODO: handle "Exit" -> break
        break  # remove once the loop is implemented

    # TODO: print final agenda as "- Item 1\n- Item 2\n..."
    # TODO: bonus - build the same string with a list comprehension


if __name__ == "__main__":
    main()
