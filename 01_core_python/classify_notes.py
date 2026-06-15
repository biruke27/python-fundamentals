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
    if "need" in note or "follow up" in note or "action" in note:
        return "action item"
    elif "decided" in note or  "agreed" in note  or "final" in note:
        return "decision"
    else:
        return "other"

def main():
    notes = [
        "need to follow up on Q3 budget",
        "decided: launch date is June 15",
        "parking lot: office plants",
    ]

    # TODO: loop over notes, classify each, print note + classification
    # TODO: count totals per category and print them
    actions, decisions, others = 0, 0, 0
    
    for note in notes:
        category = classify_note(note)
        if category == "action item":
            actions += 1
        elif category == "decision":
            decisions += 1
        else:
            others += 1
        print(f"Note: '{note}' | Classification: {category}")

    print(f"\nTotals - Actions: {actions}, Decisions: {decisions}, Others: {others}")

if __name__ == "__main__":
    main()


