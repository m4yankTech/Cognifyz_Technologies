def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print(" Welcome to the Temperature Converter! ")
    print("------------------------------------------")

    while True:
        temp = input("Enter the temperature value: ")
        try:
            temp = float(temp)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").strip().upper()

        if unit == 'C':
            converted_temp = celsius_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {converted_temp:.2f}°F")
        elif unit == 'F':
            converted_temp = fahrenheit_to_celsius(temp)
            print(f"{temp}°F is equal to {converted_temp:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            continue

        another_conversion = input("Would you like to perform another conversion? (yes/no): ").strip().lower()
        if another_conversion != 'yes':
            break
    
    print("Thank you for using the Temperature Converter! Stay cool or warm, as you like! ")

if __name__ == "__main__":
    main()