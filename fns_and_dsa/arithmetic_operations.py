def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations based on the given operation.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        float or str: Result of the operation or error message for division by zero
    """
    operation = operation.lower().strip()  # Added strip() to handle any whitespace
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."