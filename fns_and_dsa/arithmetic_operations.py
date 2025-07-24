def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2
        case _:
            return "Invalid operation"

# Example usage
if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
        result = perform_operation(num1, num2, operation)
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
