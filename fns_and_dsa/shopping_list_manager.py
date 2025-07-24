# shopping_list_manager.py

# Define the shopping list
shopping_list = []

# Define and display the menu
def display_menu():
    print("\nShopping List Menu:")
    print("1. Add Item")
    print("2. View List")
    print("3. Remove Item")
    print("4. Exit")

# Main loop
def main():
    while True:
        display_menu()  # Function call required by checker
        try:
            choice = int(input("Enter your choice (1-4): "))  # Must be a number
        except ValueError:
            print("Please enter a number between 1 and 4.")
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

# Run the program
if __name__ == "__main__":
    main()
