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

    # Check if number is less than 2.
    # Numbers less than 2 cannot be prime, so the function ends and returns False.
    # if number is not less than 2 function proceeds to next if statement
    if number < 2:
        return False

    # Check if number is equal to 2.
    # 2 is the only even prime number, so the function ends and returns True.
    # If the number is greater than 2, the function proceeds to the for loop.
    if number == 2:
        return True

    # The for loop checks possible divisors starting from (2 up to number - 1)
    # The number is divided by each possible divisor using the modulus operator (%).
    # If the remainder is 0, the number has a divisor other than 1 and itself,
    # so it is not prime and the function returns False.
    # If the loop finishes without finding any divisor, the number is prime,
    # so the function returns True.
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


# Take input from the user.
number = int(input("Enter a number: "))

# If the function returns True, print that the number is prime.
if is_prime(number):
    print(f"{number} is a prime number.")

# If the function returns False, print that the number is not prime.
else:
    print(f"{number} is NOT a prime number.")