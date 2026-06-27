# What I Learned — Week 2: File I/O, JSON, and HTTP

> Add an entry for each day. 15 minutes max — bullet points are fine.

## Day 8-9 — Reading and Writing Files
 ## 1. What I Learned
*   **Core Built-in / Concept:** Mastered the `open()` function and its critical access modes: **'r'** (read-only), **'w'** (destructive write/create), and ****'a'** (safe append). I also integrated the `os` module to manage infrastructure, utilizing `os.makedirs(exist_ok=True)` for directory creation and `os.listdir()` combined with `os.path.getsize()` for automated storage auditing [Milestone 1, 4, Assignment Clone].
*   **Error Handling / Control Flow:** Successfully implemented the **Context Manager** (`with` statement) to automate resource cleanup and prevent memory leaks or file locking. I mastered defensive programming using `try-except` blocks to handle `FileNotFoundError`, ensuring the program provides analytical feedback instead of crashing when external resources are missing [Milestone 3, 4, 646].

 2. What I Built
**The Security Archive Script (Cyber-Security Incident Logger)**
A robust system designed to automate the capture and auditing of security breach data.

*   **The Logic:** The script uses a sentinel `while True` loop to aggregate multi-line user descriptions into a single string payload until the "STOP" command is detected [Milestone 2]. It then applies specific storage strategies: overwriting the `latest_report.txt` while cumulatively appending to the `audit_history.txt` to maintain a chronological record [Milestone 3].
*   **The Automation:** The application dynamically scans the `security_logs` directory, calculates the exact size of every stored file in bytes, and generates a 50-character content preview for rapid auditing [Assignment Clone].

### Key Snippet:
```python
# The foundational block for defensive file auditing
try:
    with open(full_path, "r") as f:
        preview = f.read(50).replace("\n", " ") # Capture preview & sanitize newlines
    print(f"File: {filename} | Size: {size} bytes | Preview: {preview}...")
except FileNotFoundError:
    print("CRITICAL: No security archive detected.")
```

##  3. What Tripped Me Up (But Finally Clicked)

*   **Blocker:** Misinterpreting the final state of a file after consecutive write and append operations.
*   **Solution:** I realized that the **'w' mode** is a "Room Renovator" that clears the space the moment the bridge is opened, whereas the **'a' mode** is a "Librarian" that preserves every existing character and only adds to the end. Precision in choosing the mode is the difference between data persistence and data loss.

##  4. Note for Future

*   **The Golden Rule of Cleanup:** Never rely on manual `.close()` calls. Always utilize the `with` statement. It acts as a high-tech smart room that implicitly kills the file stream and flushes memory buffers the millisecond the code leaves the block, even if a crash occurs midway through execution.

## Day 10-11 — Working with JSON
-

## Day 12 — Ollama / Local LLM Setup
- How long did setup actually take?
-

## Day 13-14 — model_caller.py
-
