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
#Check if number is less than 2. If true, automatically it is not prime. Function ends and returns false.
#If it is not less than 2, function proceeds to next if
    if number < 2:
        return False
#Check if number is equal to 2. If true it is prime. Function ends and returns true. if greater than 2, function proceeds
#to the for loop
    if number == 2:
        return True
#In the for loop it starts from 2 to the number n-1. the loops repeats remainder checking by dividing number by (2,3,4...all the
# way to n-1). if there is no remainder then it is not prime and returns false. if there is a remainder it returns true
    for i in range(2, number):
        if number % i == 0:
            return False

    return True
#take input
number = int(input("Enter a number: "))
#if the function isprime is true, print "number" is a prime munber
if is_prime(number):
    print(f"{number} is a prime number.")
#if the function isprime is anything else which is false, print "number" is not a prime munber
else:
    print(f"{number} is NOT a prime number.")