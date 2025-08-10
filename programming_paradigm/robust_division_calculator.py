def safe_divide(numerator, denominator):
    """
    Perform division with robust error handling.
    
    Args:
        numerator: The numerator as a string (to be converted to float)
        denominator: The denominator as a string (to be converted to float)
        
    Returns:
        float: The result of division if successful
        str: Error message if division fails
    """
    try:
        # Try to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        result = num / den
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."