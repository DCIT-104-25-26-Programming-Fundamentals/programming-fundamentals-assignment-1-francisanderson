# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    # Create a variable to store the total sum.
    # It starts from 0 because no numbers have been added yet.
    total = 0

    # Loop through every number in the list.
    # Each number is added to the total one at a time.
    for number in numbers:
        total = total + number

    # Return the final calculated sum.
    return total


def calculate_average(numbers):
    # Call the calculate_sum function to get the total of all numbers.
    total = calculate_sum(numbers)

    # Divide the total by the number of items in the list.
    # len(numbers) gives the number of values stored in the list.
    average = total / len(numbers)

    # Return the calculated average.
    return average


def calculate_maximum(numbers):
    # Assume the first number in the list is the largest initially.
    # The program will compare it with the remaining numbers.
    maximum = numbers[0]

    # Loop through each number in the list.
    for number in numbers:

        # Check if the current number is greater than the current maximum.
        # If true, update maximum with the new larger number.
        if number > maximum:
            maximum = number

    # Return the largest number found.
    return maximum


def calculate_minimum(numbers):
    # Assume the first number in the list is the smallest initially.
    # The program will compare it with the remaining numbers.
    minimum = numbers[0]

    # Loop through each number in the list.
    for number in numbers:

        # Check if the current number is smaller than the current minimum.
        # If true, update minimum with the new smaller number.
        if number < minimum:
            minimum = number

    # Return the smallest number found.
    return minimum


# Ask the user how many numbers they want to enter.
user_input = input("How many numbers? ")

# Try converting the input into an integer.
# If the user enters text instead of a number, ValueError will occur.
try:
    n = int(user_input)

# If conversion fails, inform the user that the input is invalid.
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

# Check if the number of values is positive.
# If n is 0 or negative, the program stops because a list cannot be created.
if n <= 0:
    print("Error: Number of values must be positive.")
    exit()


# Create an empty list to store the numbers entered by the user.
numbers = []

# Loop n times to collect all numbers from the user.
for i in range(n):

    # Keep asking until the user enters a valid number.
    while True:
        user_input = input(f"Enter number {i + 1}: ")

        # Try converting the input into a number.
        try:
            number = float(user_input)
            break

        # If the user enters text, display an error and ask again.
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Add the valid number to the list.
    numbers.append(number)


# Calculate all required statistics by calling their functions.
total = calculate_sum(numbers)
average = calculate_average(numbers)
maximum = calculate_maximum(numbers)
minimum = calculate_minimum(numbers)


# Display the results.
print("\nResults:")
print(f"Sum:     {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
