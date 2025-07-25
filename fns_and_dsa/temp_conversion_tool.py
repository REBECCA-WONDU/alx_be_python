# Global conversion factors
FAHRENHEIT_TO_CELSIUS_OFFSET = 32
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius"""
    return (fahrenheit - FAHRENHEIT_TO_CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit"""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_TO_CELSIUS_OFFSET

def get_temperature_input():
    """Get and validate temperature input from user"""
    while True:
        try:
            temp_input = input("Enter the temperature to convert: ")
            return float(temp_input)
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def get_unit_input():
    """Get and validate unit input from user"""
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ('C', 'F'):
            return unit
        print("Invalid unit. Please enter 'C' or 'F'.")

def display_conversion(temperature, unit):
    """Perform conversion and display result"""
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp:.2f}°F")
    else:
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp:.2f}°C")

def main():
    """Main function to run the temperature conversion program"""
    temperature = get_temperature_input()
    unit = get_unit_input()
    display_conversion(temperature, unit)

if __name__ == "__main__":
    main()