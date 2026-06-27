"""
Day 8-9: Reading and Writing Files

Spec (see ../../fundamentals/02_file_json_http/README.md for full details):

- Create a folder `workspace/` (os.makedirs("workspace", exist_ok=True)).
- Accept a meeting title from the user, then accept multi-line input for
  raw meeting notes -- keep reading lines until the user types "END" on
  its own line. Write all of it to workspace/input.txt.
- Append a line to workspace/run_log.txt with the current timestamp
  (from datetime import datetime) and the filename you just wrote.
- Read back all files in workspace/ (os.listdir) and print a summary:
  filename, size in bytes (os.path.getsize), and the first 50 characters
  of each file's content.
- Wrap file-reading operations in try/except FileNotFoundError so a
  missing workspace/ prints "No workspace yet" instead of crashing.
"""
import os
from datetime import datetime

WORKSPACE_DIR = "workspace"


def ensure_workspace():
    """Ensure the target directory infrastructure exists safely."""
    os.makedirs(WORKSPACE_DIR, exist_ok=True)


def read_meeting_notes():
    """Prompt for a title, then read lines until 'END'. Return (title, notes_text)."""
    title = input("Enter the title: ")
    print("Enter the meeting notes. Type 'END' on a new line to finish: ")

    lines = []
    while True:
        line = input("> ")
        if line.upper() == "END":
            break
        lines.append(line)
        
    # FIX: Join the list of lines into a single string and return the payload
    notes_text = "\n".join(lines)
    return title, notes_text


def write_input_file(title, notes_text):
    """Write the structured note contents cleanly out to workspace/input.txt."""
    # FIX: Converted input.txt to a proper string literal "input.txt"
    filepath = os.path.join(WORKSPACE_DIR, "input.txt")
    with open(filepath, "w") as f:
        f.write(f"Title: {title}\n")
        f.write("-" * 20 + "\n")
        f.write(notes_text)


def append_run_log(filename):
    """Append a traceable change entry tracking timestamp and action target."""
    filepath = os.path.join(WORKSPACE_DIR, "run_log.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a") as f:
        f.write(f"[{timestamp}] Saved changes to {filename}\n")


def summarize_workspace():
    """Print filename, size in bytes, and first 50 chars for each file in workspace/."""
    try:
        # FIX: Changed RECORDS_DIR to the matching variable WORKSPACE_DIR
        files = os.listdir(WORKSPACE_DIR)
        
        if not files:
            print("The workspace folder is empty.")
            return

        for filename in files:
            filepath = os.path.join(WORKSPACE_DIR, filename)
            
            if os.path.isdir(filepath):
                continue
                
            file_size = os.path.getsize(filepath)
            
            with open(filepath, "r") as f:
                snippet = f.read(50).replace("\n", " ")  
            
            print(f"File: {filename} | Size: {file_size} bytes | Snippet: {snippet}...")
            
    except FileNotFoundError:
        print("No workspace yet")


def main():
    # 1. Establish directory environment
    ensure_workspace()
    
    # 2. Collect information streams from operator
    title, notes = read_meeting_notes()
    
    # 3. Save details out permanently to disk
    write_input_file(title, notes)
    
    # 4. Create an audit footprint entry
    append_run_log("input.txt")
    
    # 5. Display programmatic filesystem summary
    print("\n--- Workspace Summary ---")
    summarize_workspace()


if __name__ == "__main__":
    main() 