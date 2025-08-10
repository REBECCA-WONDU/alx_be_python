def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with comprehensive error handling.
    
    Args:
        numerator: The numerator (expected to be convertible to float)
        denominator: The denominator (expected to be convertible to float)
        
    Returns:
        float: The division result if successful
        str: Error message if division fails due to:
             - Invalid numeric input (ValueError)
             - Division by zero (ZeroDivisionError)
    """
    try:
        # Convert inputs to floats (handles ValueError)
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        # Perform division (handles ZeroDivisionError)
        return num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."