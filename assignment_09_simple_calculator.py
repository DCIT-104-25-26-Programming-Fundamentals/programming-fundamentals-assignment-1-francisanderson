# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add(number1, number2):
    # Add the two numbers and return the result.
    return number1 + number2


def subtract(number1, number2):
    # Subtract the second number from the first number and return the result.
    return number1 - number2


def multiply(number1, number2):
    # Multiply the two numbers and return the result.
    return number1 * number2


def divide(number1, number2):
    # Check if the second number is zero.
    # Division by zero is not allowed, so return None.
    if number2 == 0:
        return None

    # Divide the first number by the second number.
    # Round the result to 2 decimal places before returning it.
    return round(number1 / number2, 2)


def modulus(number1, number2):
    # Check if the second number is zero.
    # Modulus by zero is not allowed.
    if number2 == 0:
        return None

    # Return the remainder after dividing the first number by the second number.
    return number1 % number2


def exponent(number1, number2):
    # Raise the first number to the power of the second number.
    return number1 ** number2


# Main program loop.
# The calculator continues running until the user selects option 7.
while True:

    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

    # Ask the user to select an operation.
    choice = input("Select an operation (1-7): ")

    # Check if the user wants to exit the calculator.
    if choice == "7":
        print("Goodbye!")
        break

    # Check if the menu choice is valid.
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice. Please select an option from 1 to 7.")
        continue


    # Ask the user to enter two numbers.
    # The input is handled inside try-except to prevent crashes
    # when the user enters text instead of numbers.
    try:
        number1 = float(input("Enter first number : "))
        number2 = float(input("Enter second number: "))

    # If the conversion to float fails, this block runs.
    # The user is informed and returned to the menu.
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue


    # Perform the selected operation.
    if choice == "1":

        result = add(number1, number2)
        print(f"Result: {number1} + {number2} = {result}")


    elif choice == "2":

        result = subtract(number1, number2)
        print(f"Result: {number1} - {number2} = {result}")


    elif choice == "3":

        result = multiply(number1, number2)
        print(f"Result: {number1} * {number2} = {result}")


    elif choice == "4":

        result = divide(number1, number2)

        # Check if the function returned None.
        # If true, the user tried dividing by zero.
        if result is None:
            print("Error: Cannot divide by zero.")

        else:
            print(f"Result: {number1} / {number2} = {result}")


    elif choice == "5":

        result = modulus(number1, number2)

        # Check if the function returned None.
        # If true, the user tried modulus with zero.
        if result is None:
            print("Error: Cannot perform modulus by zero.")

        else:
            print(f"Result: {number1} % {number2} = {result}")


    elif choice == "6":

        result = exponent(number1, number2)
        print(f"Result: {number1} ** {number2} = {result}")