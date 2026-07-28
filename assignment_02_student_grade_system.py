# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 2
# Topic: Conditional Logic (if / elif / else) and Functions
# =============================================================================
#
# TASK: Student Grade System
#
# Write a Python program that reads a student's score and outputs the
# corresponding letter grade based on the scale below.
#
# Grading Scale:
#   Score 80 – 100  →  Grade A
#   Score 70 – 79   →  Grade B
#   Score 60 – 69   →  Grade C
#   Score 50 – 59   →  Grade D
#   Score below 50  →  Grade F
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter student score (0-100): 85
#   Grade: A
#
#   Enter student score (0-100): 73
#   Grade: B
#
#   Enter student score (0-100): 45
#   Grade: F
#
#   Enter student score (0-100): 110
#   Error: Score must be between 0 and 100.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST use functions (see scaffold below).
# - Validate that the score is within the range 0–100 inside get_grade().
#   If it is not, return None and let main() print the error message.
# - Use if / elif / else to determine the grade.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def get_grade(score):
    # Check if score is outside the valid range of 0 to 100.
    # If true, the score is invalid, so the function ends and returns None.
    if score < 0 or score > 100:
        return None

    # Check if score is 80 or above.
    # If true, the student receives Grade A.
    if score >= 80:
        return "A"

    # If the score is not 80 or above, check if it is 70 or above.
    # If true, the student receives Grade B.
    elif score >= 70:
        return "B"

    # If the score is not 70 or above, check if it is 60 or above.
    # If true, the student receives Grade C.
    elif score >= 60:
        return "C"

    # If the score is not 60 or above, check if it is 50 or above.
    # If true, the student receives Grade D.
    elif score >= 50:
        return "D"

    # If none of the previous conditions are true, the score is below 50.
    # Therefore, the student receives Grade F.
    else:
        return "F"


# The while loop allows the program to continue accepting multiple scores.
# The loop will keep running until the user chooses to exit.
while True:

    # Take student score input from the user.
    # The input is first stored as a string before converting it to an integer.
    user_input = input("Enter student score (0-100) or type q to exit: ")

    # Check if the user wants to exit the program.
    # If true, the loop stops and the program ends.
    if user_input.lower() == "q":
        break

    # Try converting the user input into an integer.
    # If the input is not a number, Python will raise a ValueError.
    try:
        score = int(user_input)

    # If the conversion fails, this block runs.
    # The program informs the user and returns to the beginning of the loop.
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Call the get_grade function and store the returned grade.
    grade = get_grade(score)

    # Check if the function returned None.
    # If true, the score was outside the valid range, so print an error message.
    if grade is None:
        print("Error: Score must be between 0 and 100.")

    # If the function returned a grade, print the student's grade.
    else:
        print(f"Grade: {grade}")