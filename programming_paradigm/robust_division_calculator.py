def safe_divide(numerator, denominator):
    """
    Performs division with robust error handling.
    Returns specific string outputs exactly as required by the task.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."