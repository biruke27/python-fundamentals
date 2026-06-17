# What I Learned — Week 1: Core Python Fundamentals

> Add an entry for each day. 15 minutes max — bullet points are fine.
> What did you build, what tripped you up, what finally clicked?

## Day 1-2 — Variables, Conditionals, Loops, and Functions
#### **1. What I Learned**
*   **Variables & Types:** I learned basic data types (`str`, `int`, `float`, `bool`). I mastered assigning values using `snake_case`. I can work with numbers, Booleans (`True`/`False`), and strings. I learned how to use **f-strings** to inject variables and expressions directly into my output.
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
- ## Day 3-4 — Lists and List Operations

#### **1. What I Learned**
* **List Storage & Indexing:** I learned that lists act as ordered collections. Python uses **zero-based indexing**, meaning the first position is `0`. I mastered extracting specific elements using index numbers.
* **Dynamic Alteration:** I learned how to grow a list dynamically using `.append()` to place new items at the end, and how to surgically remove items from any specific position using `.pop(index)`.
* **Index Shifting for UX:** I learned how to bridge the gap between human counting (starts at 1) and computer indexing (starts at 0). By using `enumerate(list, start=1)` for display and subtracting `1` from user input numbers, I can create an intuitive interface without breaking Python's internal logic.
* **List Comprehensions:** I discovered how to write elegant, inline `for` loops to transform lists instantly. I used this alongside `"\n".join()` to assemble clean multi-line display strings.

#### **2. What I Built**
I built an interactive, menu-driven **Agenda Dashboard** (`build_agenda.py`) to manage task lists.
* **The Logic:** I designed an infinite `while True` execution loop that hosts a clean command-line interface menu (Add, Remove, Show, Exit).
* **The Processing:** Option numbers route the user to specific logic gates. When removing, the program takes text input, safely scales it back by 1, and mutates the data list.
* **The Bonus:** Upon exiting, a single list comprehension maps over all raw text items, injects markdown bullet points (`- `), and presents a beautifully formatted agenda block.

    **Key Snippet:**
    ```python
    elif choice == "2":
        target = input("Enter item number to remove: ")
        target_index = int(target) - 1
        removed_item = agenda_items.pop(target_index)
        print(f"Removed: '{removed_item}'")

    # Bonus: Building the final formatted string cleanly with a list comprehension
    final_agenda_string = "\n".join([f"- {item}" for item in agenda_items])

#### **3. What Tripped Me Up (But Finally Clicked)**
* **The String-to-Integer Trap:** I initially forgot that `input()` brings data into the engine strictly as a string text data type (`str`). Passing a string into a list index method causes crashes. It clicked when I realized I must wrap user selections in `int()` to clear out text properties and transform them into real mathematical counters.
* **The Crash Boundary (IndexError):** I realized that looking for an item that isn't there (like popping index 5 from a 2-item list) forces Python to break. To code defensively, wrapping dangerous inputs inside structured validation blocks preserves system runtime.

#### **4. Note for Future**
* **Data Persistence:** Every time this CLI script finishes running, the list resets in memory. Later weeks will require file system saving so data survives script restarts.
* **Defensive Wrappers:** Always isolate index-dependent methods or numeric type casting within `try/except` configurations to intercept user typos seamlessly.

## Day 5-6 — Dictionaries and Sets
-

## Day 7 — Functions, Return Values, and try/except
-
