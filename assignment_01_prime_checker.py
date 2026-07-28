# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================
#
# TASK: Prime Number Checker
#
# Write a Python program that checks whether a given number is prime.
#
# A prime number is a whole number greater than 1 that has no divisors
# other than 1 and itself (e.g., 2, 3, 5, 7, 11, 13 ...).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter a number: 7
#   7 is a prime number.
#
#   Enter a number: 10
#   10 is NOT a prime number.
#
#   Enter a number: 1
#   1 is NOT a prime number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement the logic inside a function (see scaffold below).
# - Numbers less than 2 are NOT prime — handle this inside the function.
# - The main block must call the function and print the result.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def is_prime(number):

    # Check if the number is less than 2.
    # Numbers less than 2 cannot be prime, so return False.
    # If the number is 2 or greater, continue to the next condition.
    if number < 2:
        return False

    # Check if the number is equal to 2.
    # 2 is the only even prime number, so return True.
    # If the number is greater than 2, continue to the loop.
    if number == 2:
        return True

    # Check every number from 2 up to (number - 1).
    # If any number divides evenly into the given number,
    # then the number is not prime and return False.
    # If no divisor is found after the loop finishes,
    # the number is prime and return True.
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def main():

    # Keep the program running until the user chooses to quit.
    while True:

        # Try to convert the user's input into an integer.
        # If the user enters a string or any non-integer value,
        # int() raises a ValueError.
        # The except block catches the error so the program
        # does not crash and instead prints a friendly message.
        try:
            number = int(input("Enter a number: "))

            # Call the function and display whether the number is prime.
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is NOT a prime number.")

        # This block runs only if the user entered an invalid value,
        # such as letters, symbols, or a decimal number.
        except ValueError:
            print("Error: Please enter a valid integer.")

        # Ask the user whether they want to continue.
        # Convert the input to uppercase so both
        # uppercase and lowercase letters are accepted.
        choice = input("\nDo you want to check another number? (Y/N): ").upper()

        # If the user enters anything other than Y,
        # end the program with a goodbye message.
        if choice != "Y":
            print("Thank you for using the Prime Number Checker. Goodbye!")
            break


# Start the program by calling the main function.
main()