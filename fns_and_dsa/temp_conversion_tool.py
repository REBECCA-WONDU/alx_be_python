# Global conversion factors - must be defined at module level
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # User interaction
    print("Temperature Conversion Tool")
    print("--------------------------")
    
    while True:
        try:
            # Get temperature input
            temp_input = input("\nEnter the temperature to convert (or 'q' to quit): ").strip()
            
            if temp_input.lower() == 'q':
                print("Goodbye!")
                break
                
            # Convert to float with proper error handling
            temperature = float(temp_input)
            
            # Get unit input with validation
            while True:
                unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
                if unit in ('C', 'F'):
                    break
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
            # Perform conversion and display result
            if unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"\n{temperature}°C is {converted_temp:.2f}°F")
            else:
                converted_temp = convert_to_celsius(temperature)
                print(f"\n{temperature}°F is {converted_temp:.2f}°C")
                
        except ValueError:
            print("Error: Invalid temperature value. Please enter a numeric value.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()