def main():
    notifications = []

    while True:
        print("\n--- Notification Dashboard ---")
        print("1. Add Alert")
        print("2. Clear Alert by Number")
        print("3. View Active Alerts")
        print("4. End Session")

        choice = input("Select an option (1-4): ")

        if choice =="1":
            new_alert = input("Enter alert message: ")
            notifications.append(new_alert)
            print(f"Added: '{new_alert}'")
        elif choice =="2":
            target = input("Enter alert number to clear: ")
            target_index = int(target)
            removed_alert = notifications.pop(target_index)
            print(f"Cleared: '{removed_alert}'")
        elif choice == "3":
            print("\n--- Current Alerts ---")
            for index, alert in enumerate(notifications):
                print(f"{index}. {alert}")
        elif choice =="4":
            print("Ending session...")
            break

    print("\n=== Final Archive ===")
    for alert in notifications:
        print(f"- {alert}")

if __name__ == "__main__":
    main()
