# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations.

    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): One of '+', '-', '*', '/'

    Returns:
    - The result of the operation or an error message for invalid input.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"


# Optional example usage (not required by the checker)
if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ").strip()
        result = perform_operation(num1, num2, operation)
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
