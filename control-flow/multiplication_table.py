# multiplication_table.py
# Generate and print the multiplication table for a given number

try:
    number = int(input("Enter a number to see its multiplication table: "))

    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

except ValueError:
    print("Invalid input. Please enter an integer.")
