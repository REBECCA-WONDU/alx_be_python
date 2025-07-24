# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.

    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): One of '+', '-', '*', '/'

    Returns:
    - Result of the operation or an error message (e.g. divide by zero)
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Cannot divide by zero."
        return num1 / num2
    else:
        return "Invalid operation."


# Example usage (optional, can be removed for testing purposes)
if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ").strip()

        result = perform_operation(num1, num2, operation)
        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
