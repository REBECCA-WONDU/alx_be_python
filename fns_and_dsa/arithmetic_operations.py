# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on an operation symbol.

    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): One of '+', '-', '*', '/'

    Returns:
    - Result of the operation or an error message
    """
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
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
        operation = input("Enter operation (+, -, *, /): ").strip()
        result = perform_operation(num1, num2, operation)
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
