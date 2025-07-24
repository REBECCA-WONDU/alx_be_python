shopping_list = []

def display_menu():
    print("\nShopping List Menu:")
    print("1. Add Item")
    print("2. View List")
    print("3. Remove Item")
    print("4. Exit")

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"'{item}' added to the shopping list.")
    elif choice == 2:
        print("\nYour Shopping List:")
        for idx, item in enumerate(shopping_list, 1):
            print(f"{idx}. {item}")
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
