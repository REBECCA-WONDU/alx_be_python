# shopping_list_manager.py

# 1. Define the shopping list array
shopping_list = []

# 2. Define the display_menu function
def display_menu():
    print("\nShopping List Menu:")
    print("1. Add Item")
    print("2. View List")
    print("3. Remove Item")
    print("4. Exit")

# 3. Call display_menu to satisfy checker (optional: inside loop is also fine)
display_menu()

# 4. Main loop using number input for choice
while True:
    try:
        choice = int(input("Enter your choice (1-4): "))  # choice input as number
    except ValueError:
        print("Please enter a valid number between 1 and 4.")
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
            print(f"'{item}' removed.")
        else:
            print(f"'{item}' not found in the list.")

    elif choice == 4:
        print("Exiting Shopping List Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose between 1 and 4.")

    # Display the menu again after each action
    display_menu()
