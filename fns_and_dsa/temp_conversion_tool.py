# Global conversion factors - must be defined at the top level
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    # User interaction
    temp_input = input("Enter the temperature to convert: ")
    
    try:
        temperature = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    
    if unit == 'C':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    elif unit == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()