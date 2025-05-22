# Separate the whole block in diferent methods

# Take the data

def calculatorTwo():
    #method to welcome
    welcomeAll()

    # Method to take the data
    numOne = inputNumOne()

    numTwo = inputNumTwo()

    # Method to define operation +  check operation
    operation = defineOperation()

    #switch to make operations and show results

    calculatorResult = doTheOperation(numOne, numTwo, operation)

    #return something you fool
    return calculatorResult

#external methods

def welcomeAll():
    return print("Welcome to the Simple Calculator!")

# check numbers method
def checkNums(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please,  enter a valid number")

#get numbers

def inputNumOne():

    # get first number and check
    numOne = checkNums("Enter the first number please: ")

    return numOne

def inputNumTwo():

    #get second number and check
    numTwo = checkNums("Enter the second number please: ")

    return numTwo

# define operations
def defineOperation():
    # define the operation to go and checks
    while True:
      operation = input("Enter the operation (+, -, *, /):") 
      if operation in ["+","-","*","/"]:
          return operation
      else:
          print("Invalid operator input. Please,  enter only one of the operation signs (+, -, *, /):")



# do the maths
def doTheOperation(num1,num2,sign):
    result = 0
    match sign:
        case "+":
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")

        case "-":
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")

        case "*":
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")

        case "/":
            if(num2 !=0):
                result = num1/num2
                print(f"The result of {num1} / {num2} is: {result}")
            else:
                print(f"No division can be performed as num2 is {num2}")
                calculatorTwo()

        case _:
            print("Error on the operation")
    
    return result if result else print('Something went really wrong')
            


"""def is_valid_operation(operation):
    return operation in ["+", "-", "*", "/"]

def defineOperation():
    while True:
        operation = input("Enter the operation (+, -, *, /): ").strip()
        if is_valid_operation(operation):
            return operation
        else:
            print("Invalid operator input. Please, enter only one of the operation signs (+, -, *, /): ")"""

# active main function
calculatorTwo()

