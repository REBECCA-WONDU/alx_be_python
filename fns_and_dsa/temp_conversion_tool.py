#!/usr/bin/python3
"""
Temperature Conversion Tool
Converts between Celsius and Fahrenheit using global conversion factors
"""

# Global conversion factors - must be exactly as specified
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius
    Args:
        fahrenheit: temperature in Fahrenheit
    Returns:
        temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit
    Args:
        celsius: temperature in Celsius
    Returns:
        temperature in Fahrenheit
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    """
    Handles user interaction and temperature conversion
    """
    # Get temperature input
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    # Get unit input
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        if unit in ('C', 'F'):
            break
        print("Invalid unit. Please enter 'C' or 'F'.")

    # Perform conversion
    if unit == 'C':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    else:
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")

if __name__ == "__main__":
    main()