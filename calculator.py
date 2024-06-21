def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error! Division by zero."

def main():
    print("Welcome to the Basic Calculator!")
    print("---------------------------------")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        operator = input("Enter an operator (+, -, *, /, %): ").strip()

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        elif operator == '%':
            result = modulo(num1, num2)
        else:
            print("Invalid operator. Please enter one of +, -, *, /, %.")
            continue

        print(f"The result of {num1} {operator} {num2} is: {result}")
        
        another_calculation = input("Would you like to perform another calculation? (yes/no): ").strip().lower()
        if another_calculation != 'yes':
            break
    
    print("Thank you for using the Basic Calculator! Have a great day!")

if __name__ == "__main__":
    main()
