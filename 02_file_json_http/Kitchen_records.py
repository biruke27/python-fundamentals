import os
from datetime import datetime

RECORDS_DIR = "kitchen_records"

def ensure_records_directory():
    """Ensure the kitchen_records directory exists."""
    os.makedirs(RECORDS_DIR, exist_ok=True)

def capture_recipe_details():
    """Prompt for a recipe name, then read lines until 'DONE'. 
    Return (recipe_name, recipe_text).
    """
    recipe_name = input("Enter the recipe name: ")
    print("Enter the ingredients and instructions. Type 'DONE' on a new line to finish:")
    
    lines = []
    while True:
        line = input()
        if line.strip() == "DONE":
            break
        lines.append(line)
        
    # Join the lines together with newlines
    recipe_text = "\n".join(lines)
    return recipe_name, recipe_text

def save_recipe_file(recipe_name, recipe_text):
    """Write the recipe name and details into kitchen_records/recipe.txt."""
    filepath = os.path.join(RECORDS_DIR, "recipe.txt")
    with open(filepath, "w") as f:
        f.write(f"Recipe: {recipe_name}\n")
        f.write("-" * 20 + "\n")
        f.write(recipe_text)

def log_kitchen_activity(filename):
    """Append a timestamped entry to kitchen_records/activity_log.txt."""
    filepath = os.path.join(RECORDS_DIR, "activity_log.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filepath, "a") as f:
        f.write(f"[{timestamp}] Saved changes to {filename}\n")

def display_records_summary():
    """Print filename, size in bytes, and first 50 chars for each file in kitchen_records/.
    Wrap in a try/except FileNotFoundError block.
    """
    try:
        # List all items in the directory
        files = os.listdir(RECORDS_DIR)
        
        if not files:
            print("The kitchen records folder is empty.")
            return

        for filename in files:
            filepath = os.path.join(RECORDS_DIR, filename)
            
            # Skip directories if any exist inside
            if os.path.isdir(filepath):
                continue
                
            # Get file size
            file_size = os.path.getsize(filepath)
            
            # Read first 50 characters safely
            with open(filepath, "r") as f:
                snippet = f.read(50).replace("\n", " ")  # Clean up newlines for cleaner printing
            
            print(f"File: {filename} | Size: {file_size} bytes | Snippet: {snippet}...")
            
    except FileNotFoundError:
        print("No kitchen records found")

def main():
    # 1. Prepare the environment
    ensure_records_directory()
    
    # 2. Collect data from user
    recipe_name, recipe_text = capture_recipe_details()
    
    # 3. Write data to the primary file
    save_recipe_file(recipe_name, recipe_text)
    
    # 4. Append log tracking metadata
    log_kitchen_activity("recipe.txt")
    
    # 5. Read back and summarize everything in the directory
    print("\n--- Current Kitchen Records Summary ---")
    display_records_summary()

if __name__ == "__main__":
    main()