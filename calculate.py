def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  # Check for division by zero
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Invalid operator"

# Main program loop
while True:
    try:
        # Get user input
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        # Calculate and display result
        result = calculator(num1, num2, operator)
        print(f"Result: {result}")

        # Ask if user wants to continue
        continue_calc = input("Do you want to perform another calculation? (yes/no): ")
        if continue_calc.lower() != 'yes':
            print("Thank you for using the calculator!")
            break

    except ValueError:
        print("Error: Please enter valid numbers")
