# Separate the whole block in diferent methods

# Take the data

def calculatorTwo():
    #method to welcome
    welcomeAll()

    # Want to perform an operation?
    choiceOfOperation()

    # Method to take the data
    numOne = inputNumOne()

    numTwo = inputNumTwo()

    # Method to define operation +  check operation
    operation = defineOperation()

    #switch to make operations and show results

    calculatorResult = doTheOperation(numOne, numTwo, operation)

    # runaway for goats

    seeYouSoon()

    #return something you fool
    return calculatorResult

#external methods

def welcomeAll():
    return print("Welcome to the Simple Calculator!")

# give people the choice
def choiceOfOperation():
    myChoice = input("Would you like to use the calculator?\n If 'YES' press 1, if 'NO' press 2: ")

    return inputNumOne() if myChoice == 1 else seeYouSoon()

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

# escape
def seeYouSoon():
    print("Thanks a million and see you soon")
    exit()

# active main function
calculatorTwo()

