# Simple Calculator in Python

# Function to perform the calculation
def calculator():
    print("Welcome to the Simple Calculator!")

    # Function to get a valid number from the user
    def get_number(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Get user input for the first number
    num1 = get_number("Enter the first number: ")

    # Get user input for the second number
    num2 = get_number("Enter the second number: ")

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
