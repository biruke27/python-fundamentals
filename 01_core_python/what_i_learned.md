# What I Learned — Week 1: Core Python Fundamentals

> Add an entry for each day. 15 minutes max — bullet points are fine.
> What did you build, what tripped you up, what finally clicked?

## Day 1-2 — Variables, Conditionals, Loops, and Functions
#### **1. What I Learned**
*   **Variables & Types:** I learned basic data types (`str`, `int`, `float`, `bool`). I mastered assigning values using `snake_case`. I can work with numbers, Booleans (`True`/`False`), and strings. I learned how to use **f-strings** to inject variables and expressions directly into my output.
*   **Collections:** I learned that **lists** store ordered sequences and are zero-indexed. I can add items with `.append()` or check if an item exists using the `in` operator.
*   **Conditionals:** I learned to control program flow using `if`, `elif`, and `else`. I use comparison operators (`==`, `!=`, `<`, `>`) and boolean logic (`and`, `or`, `not`) to create complex rules.
*   **Loops:** I mastered **`for` loops** to iterate over sequences and **`while` loops** to repeat code as long as a condition remains true.
*   **Functions:** I learned to organize my code into reusable blocks with `def` and `return`.

#### **2. What I Built**
I built a **Project Status Classifier** that automates the sorting of meeting notes.
*   **The Logic:** I created a function `classify_note(note)` that uses keyword detection (`in`) to return a category.
*   **The Automation:** I used a `for` loop to process a list of notes, update multiple counters, and print a formatted summary.

**Key Snippet:**
```python
def classify_note(note):
    if "milestone" in note or "reached" in note:
        return "milestone"
    elif "need" in note or "todo" in note:
        return "action"
    # ... other categories
    else:
        return "other"
```

#### **3. What Tripped Me Up (But Finally Clicked)**
*   **Exclusive Ranges:** The `range(start, stop, step)` initially felt weird because the `stop` value is excluded. It clicked when I realized `start`: The number where you begin (this number is included) `stop`: The number where you want to end. Crucially, the loop stops just before it reaches this number `step`: How much you add to the number each time the loop runs.
*   **Truthiness:** I struggled with why some values behaved like Booleans. It clicked when I learned that `0`, `None`, and empty lists `[]` are inherently `False`, while everything else is `True`.
*   **Indentation:** Coming from other formats, remembering that Python uses **4 spaces** to define blocks of code was a shift, but now it feels natural.

#### **4. Note for Future**
*   **Indentation is critical:** Misaligned spaces will break the code.
*   **Zero-Indexing:** Always remember the first item in a list is at index `0`.
*   **The Guard:** Always use `if __name__ == "__main__":` at the bottom of scripts to keep the execution clean.


## Day 3-4 — Lists and List Operations
-

## Day 5-6 — Dictionaries and Sets
-

## Day 7 — Functions, Return Values, and try/except
-
