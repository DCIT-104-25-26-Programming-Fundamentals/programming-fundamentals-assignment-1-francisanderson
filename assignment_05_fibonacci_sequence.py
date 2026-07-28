# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def generate_fibonacci(n):
    # Create an empty list to store the Fibonacci sequence.
    sequence = []

    # The first two Fibonacci numbers are always 0 and 1.
    first = 0
    second = 1

    # Repeat the loop n times because the user requested n terms.
    for i in range(n):

        # Add the current Fibonacci number to the sequence.
        sequence.append(first)

        # Calculate the next Fibonacci number by adding the previous two numbers.
        next_number = first + second

        # Move the second number into the first position.
        first = second

        # Move the newly calculated number into the second position.
        second = next_number

    # Return the completed Fibonacci sequence.
    return sequence


def check_fibonacci(number):
    # Start generating Fibonacci numbers from the beginning.
    first = 0
    second = 1

    # Continue generating numbers until the current Fibonacci number
    # becomes greater than the number being checked.
    while first <= number:

        # If the current Fibonacci number is equal to the input number,
        # then the number belongs to the Fibonacci sequence.
        if first == number:
            return True

        # Calculate the next Fibonacci number.
        next_number = first + second

        # Move the values forward to continue the sequence.
        first = second
        second = next_number

    # If the loop finishes without finding the number,
    # then it is not a Fibonacci number.
    return False


# =========================
# MAIN PROGRAM
# =========================


# Ask the user how many Fibonacci terms they want to display.
while True:

    user_input = input("How many terms? ")

    # Try converting the input into an integer.
    # If the user enters text, ValueError will occur.
    try:
        terms = int(user_input)

    # If conversion fails, tell the user to enter a number.
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Check if the number of terms is positive.
    # A Fibonacci sequence cannot be generated with zero or negative terms.
    if terms <= 0:
        print("Error: Number of terms must be positive.")
        continue

    # Exit the loop when a valid input is received.
    break


# Call the function to generate the Fibonacci sequence.
fibonacci_sequence = generate_fibonacci(terms)

# Print the generated Fibonacci sequence.
print("Fibonacci sequence:", end=" ")

for number in fibonacci_sequence:
    print(number, end=" ")


print()


# Ask the user for a number to check.
while True:

    user_input = input("\nEnter a number to check: ")

    # Try converting the input into an integer.
    try:
        number = int(user_input)
        break

    # If conversion fails, ask the user again.
    except ValueError:
        print("Invalid input. Please enter a number.")


# Call the check_fibonacci function.
result = check_fibonacci(number)


# Display the result depending on the returned value.
if result:
    print(f"{number} is a Fibonacci number.")

else:
    print(f"{number} is NOT a Fibonacci number.")