#!/usr/bin/python3
"""
Temperature Conversion Tool
Converts between Celsius and Fahrenheit using global conversion factors
"""

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0
FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius
    Args:
        fahrenheit: Temperature in Fahrenheit
    Returns:
        Temperature in Celsius
    """
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit
    Args:
        celsius: Temperature in Celsius
    Returns:
        Temperature in Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def main():
    """
    Main function to handle user interaction and temperature conversion
    """
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        
        # Get unit input with validation
        while True:
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            if unit in ('C', 'F'):
                break
            print("Invalid unit. Please enter 'C' or 'F'.")
        
        # Perform conversion and display result
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
            
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()