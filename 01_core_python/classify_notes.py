"""
Day 1-2: Variables, Conditionals, Loops

Spec (see ../../fundamentals/01_core_python/README.md for full details):

- Start with this list of meeting note strings:
    notes = [
        "need to follow up on Q3 budget",
        "decided: launch date is June 15",
        "parking lot: office plants"
    ]

- For each note, classify it as:
    - "action item"  -> contains "need", "follow up", or "action"
    - "decision"     -> contains "decided", "agreed", or "final"
    - "other"        -> none of the above

- Print each note with its classification.
- Count and print totals of each category at the end.

Manual task (do this on paper first):
    Draw a table: "Loop iteration | current value | condition check"
    Trace 3 iterations before writing any code.
"""


def classify_note(note):
    """Return "action item", "decision", or "other" for a single note."""
    # TODO: implement classification logic
    pass


def main():
    notes = [
        "need to follow up on Q3 budget",
        "decided: launch date is June 15",
        "parking lot: office plants",
    ]

    # TODO: loop over notes, classify each, print note + classification
    # TODO: count totals per category and print them


if __name__ == "__main__":
    main()
