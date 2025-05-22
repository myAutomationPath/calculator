# Simple Calculator in Python

# Function to perform the calculation
def calculator():
    print("Welcome to the Simple Calculator!")

    # Get user input for the first number
    num1 = float(input("Enter the first number: "))

    # Get user input for the second number
    num2 = float(input("Enter the second number: "))

    # Get user input for the operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the operation based on user input
    if operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operation. Please enter +, -, *, or /.")

# Run the calculator function
calculator()

