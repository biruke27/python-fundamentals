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
- ## Day 5-6 — Dictionaries and Sets

#### **1. What I Learned**

* **Key-Value Pair Allocation:** I learned that dictionaries (`dict`) map unique keys directly to dynamic values, making them the ideal data structure for maintaining associative counters (like tracking exactly how many times a word appears).
* **Safe Increments via `.get()`:** I learned that looking up a missing key with normal brackets causes a severe `KeyError`. Using `.get(key, default)` acts as a defensive wrapper, handing over a `0` for brand-new items so they can be securely incremented without crashing the execution loop.
* **Sets for Fast Membership Checking:** I mastered sets as unordered collections containing strictly unique elements. Checking if an element exists inside a set (using `in` or `not in`) is optimized for ultra-fast, fixed-time lookups ($O(1)$ complexity), unlike lists which require checking every element sequentially.
* **Tuple Extraction with `.items()`:** I discovered that `.items()` extracts the key-value map from a dictionary and unwraps it into an iterable structure of separate tuple pairs, which is a prerequisite for custom formatting or sorting routines.
* **Text Sanitization:** I learned how to standardize unstructured string sequences using `.lower()` alongside chained `.replace()` functions to strip lingering structural punctuation before splitting.

#### **2. What I Built**

I built an automated transcript analyzer (`summary_stats.py`) to extract analytics and tracking items from meeting logs.

* **The Frequency Engine:** It parses a collection of raw text transcripts, sanitizes them, and filters out common connector words using a fixed `STOP_WORDS` set. It builds an aggregate tally mapping using `.get()` fallback initialization.
* **The Keyword Extractor:** It screens transcripts against an `ACTION_KEYWORDS` checklist, gathering every unique target phrase found across the script into an isolated set wrapper.
* **The Top-5 Ranker:** It feeds the unstructured tracking data into Python's native `sorted()` algorithm, combining list extraction slices (`[:5]`) with inline processing functions to display the final output cleanly.

**Key Snippet:**

    ```python
    # Extracting the word-count tracking pairs as coordinates and sorting by the tally count
    sorted_words = sorted(
        frequencies.items(), 
        key=lambda item: item[1], 
        reverse=True
    )
    top_5 = sorted_words[:5]

    ```

#### **3. What Tripped Me Up (But Finally Clicked)**

* **Why Use a Dict vs. a Set?:** I initially struggled to understand when to use which structure. It clicked when I realized that **dictionaries store an association** (a word connected to its changing count tally), whereas **sets store simple presence** (a checklist where an item either exists or doesn't, with zero duplicates allowed).
* **The Direct Accumulation Crash:** I tried to write `word_counts[word] += 1` directly on uninitialized elements. It clicked when I realized Python cannot increment a container slot that hasn't been instantiated yet; using `.get(word, 0) + 1` safely instantiates the key with a zero baseline when encountered for the first time.
* **The Mechanics of the `lambda` Sorter:** I struggled to understand why `key=lambda item: item[1]` was necessary. It clicked when I realized that `.items()` extracts dictionary elements as coordinate pairs—e.g., `("need", 6)`. The sorting engine needs an explicit instruction telling it what to sort by. The `lambda item: item[1]` extracts index `1` (the numerical count) as the sorting criterion rather than index `0` (the alphabetical word text). Setting `reverse=True` flips the default ascending behavior to descending order.

#### **4. Note for Future**

* **Case and Punctuation Mismatches:** Unfiltered characters like `"Action."` or `"Action!"` look completely different to Python than `"action"`. Always chain `.lower()` and character replacements prior to lookup operations.
* **Lookup Speeds Matter:** Never use large lists to filter out baseline terms. Use sets for checklists and blacklists to bypass scanning delays entirely.
* **The Lambda Coordinate Mapping:** When sorting dictionary item transformations, `item[0]` maps to the Key and `item[1]` maps to the Value. Missing this distinction will cause your algorithms to sort alphabetically rather than numerically.

## Day 7 — Functions, Return Values, and try/except
- ## Day 7 — Functions, Return Values, and try/except

#### **1. What I Learned**

* **Function Architecture & Scope:** I learned how to isolate repeatable logic blocks using `def`. Variables initialized inside a function exist strictly within that function's local "cleanroom" scope and vanish once execution finishes, protecting the global namespace.
* **The Return Value Contract:** I mastered the difference between *printing* a value (just displaying it to the user) and *returning* it (passing data back to the calling statement). A `return` statement immediately exits the function and passes a live data object back.
* **Defensive Error Handling (`try/except`):** I learned how to build emergency runaway ramps for code using structured exception handling. Instead of allowing bad data or edge cases to crash the program, I can target specific exceptions to keep the runtime alive.
* **Targeted Exception Types:** I learned to intercept mathematical breakdowns using `except ZeroDivisionError:` and type-casting failures using `except ValueError:`, ensuring data flows cleanly or fails safely with custom defaults.

#### **2. What I Built**

I built a robust input and calculations data validation toolset (`validation_helpers.py`) to parse notes and run calculations safely.

* **The Presence Verification Loop:** I created `check_required_fields(data, required_fields)` which matches a tracking list of mandatory keys against a data dictionary, using an early-exit loop strategy to immediately drop out with `False` if any field is missing.
* **The Defensive Calculator:** I implemented `safe_divide(a, b)` to safely evaluate numbers, cleanly trapping division-by-zero attempts and replacing a standard system crash with a helpful warning string.
* **The Substring Text Parser:** I wrote `parse_note_severity(note_text)` which uses `.split(":")` to slice up text properties (like `"priority:3"`) and attempts to cast the extracted string into an integer inside a defensive `ValueError` block, returning a baseline fallback metric of `0` if parsing fails.

**Key Snippet:**

```python
def parse_note_severity(note_text):
    try: 
        parts = note_text.split(":")
        numerical_value = int(parts[1])
        return numerical_value
    except ValueError:
        return 0  # Safe fallback if string casting fails

```

#### **3. What Tripped Me Up (But Finally Clicked)**

* **The Return vs. Print Disconnect:** I used to think `print()` inside a function sent data back to the rest of my program. It clicked when I realized `print()` is just a one-way mirror for human eyes; only `return` can hands live data packages over to other variables or functions.
* **The Try-Block Abandonment Rule:** I didn't initially understand why lines inside my `try` block were being skipped when an error happened. It clicked when I learned that the moment Python runs into an exception, it abandons the remaining lines inside the `try` block instantly and makes a hard pivot directly into the `except` safe room.

#### **4. Note for Future**

* **Don't Catch Everything Blindly:** Avoid using bare `except:` statements. Always specify the explicit error type (`ValueError`, `ZeroDivisionError`) so you don't inadvertently silence unexpected bugs or system keyboard interrupts.
* **Early Exit Efficiency:** When searching for invalid states in a loop, return `False` immediately upon discovering the first missing requirement to save compute cycles instead of waiting for the entire sequence to conclude.
