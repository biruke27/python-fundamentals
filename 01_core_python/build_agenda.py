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
        print("\n--- Agenda Dashboard ---")
        print("1. Add item")
        print("2. Remove item by number")
        print("3. Show numbered list")
        print("4. Exit")

        choice = input("Select an option (1-4): ")
        if choice == "1":
            new_item = input("Enter agenda message: ")
            agenda_items.append(new_item)
            print(f"Added: '{new_item}'")
        elif choice == "2":
            try:
                target = input("Enter item number to remove: ")
                target_index = int(target) - 1
                removed_item = agenda_items.pop(target_index)
                print(f"Removed: '{removed_item}'")
            except (ValueError, IndexError):
                print(" Invalid number. Please try again!")
        elif choice == "3":
            print("\n--- Show numbered list ---")
            for index, item in enumerate(agenda_items, start=1):
                print(f"{index}. {item}")
        elif choice =="4":
            print("Exit")
            break  # remove once the loop is implemented
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

    # TODO: print final agenda as "- Item 1\n- Item 2\n..."
    # TODO: bonus - build the same string with a list comprehension
    print("\n=== Final Agenda ===")
    final_agenda_string = "\n".join([f"- {item}" for item in agenda_items])
    print(final_agenda_string if final_agenda_string else "- No items scheduled.")

if __name__ == "__main__":
    main()
