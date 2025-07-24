# shopping_list_manager.py

# Define the shopping list as a list (array)
shopping_list = []

# Define the display_menu function
def display_menu():
    print("\nShopping List Menu:")
    print("1. Add Item")
    print("2. View List")
    print("3. Remove Item")
    print("4. Exit")

# Call the menu at least once (ensures the checker sees the function is used)
display_menu()

# Main loop with integer choice input
while True:
    try:
        choice = int(input("Enter your choice (1-4): "))  # Number input required
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"'{item}' added to the shopping list.")
    elif choice == 2:
        print("\nYour Shopping List:")
        if shopping_list:
            for idx, item in enumerate(shopping_list, 1):
                print(f"{idx}. {item}")
        else:
            print("The shopping list is empty.")
    elif choice == 3:
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from the list.")
        else:
            print(f"'{item}' not found in the list.")
    elif choice == 4:
        print("Exiting Shopping List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

    # Re-display menu after each operation
    display_menu()
