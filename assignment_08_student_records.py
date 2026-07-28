# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_average(scores):
    # Create a variable to store the total of all scores.
    # It starts from 0 because no scores have been added yet.
    total = 0

    # Loop through every score in the list.
    # Each score is added to the total one at a time.
    for score in scores:
        total = total + score

    # Divide the total score by the number of scores entered.
    # This gives the average score.
    average = total / len(scores)

    # Return the average rounded to 2 decimal places.
    return round(average, 2)


def add_student(students):
    # Ask the user to enter the student's name.
    name = input("Student name: ")

    # Ask the user to enter the student's ID.
    # Convert it to an integer because IDs are numbers.
    student_id = int(input("Student ID: "))

    # Ask how many scores the student has.
    number_of_scores = int(input("How many scores? "))

    # Create an empty list to store the student's scores.
    scores = []

    # Loop to collect each score one by one.
    for i in range(number_of_scores):

        # Ask the user to enter a score.
        score = int(input(f"Enter score {i + 1}: "))

        # Add the score to the scores list.
        scores.append(score)

    # Create a dictionary containing the student's information.
    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    # Add the student dictionary to the main students list.
    students.append(student)

    # Confirm that the student was added successfully.
    print(f'Student "{name}" added successfully.')


def display_students(students):
    # Check if the students list is empty.
    # If there are no records, display a message and stop the function.
    if len(students) == 0:
        print("No students have been added yet.")
        return

    # Print the table heading.
    print("-" * 60)
    print("Name\t\tID\t\tScores\t\tAverage")
    print("-" * 60)

    # Loop through each student record in the list.
    for student in students:

        # Calculate the student's average score.
        average = calculate_average(student["scores"])

        # Convert the scores list into a string for display.
        scores = ", ".join(map(str, student["scores"]))

        # Display the student's information.
        print(f'{student["name"]}\t{student["id"]}\t{scores}\t{average}')

    print("-" * 60)


def find_student_average(students):
    # Ask the user for the ID of the student they want to find.
    student_id = int(input("Enter student ID: "))

    # Loop through every student record.
    for student in students:

        # Check if the current student's ID matches the entered ID.
        if student["id"] == student_id:

            # Calculate the student's average score.
            average = calculate_average(student["scores"])

            # Display the result.
            print(f'{student["name"]}\'s average score: {average}')
            return

    # If the loop finishes without finding the student,
    # the entered ID does not exist.
    print("Error: Student ID not found.")


# Create an empty list to store all student records.
students = []


# Main program loop.
# The program continues until the user chooses option 4.
while True:

    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")

    # Ask the user to select an option.
    choice = input("Enter your choice (1-4): ")

    # Check the user's menu choice.
    if choice == "1":

        # Call the function to add a student.
        add_student(students)

    elif choice == "2":

        # Call the function to display all students.
        display_students(students)

    elif choice == "3":

        # Check if there are students before searching.
        if len(students) == 0:
            print("No students have been added yet.")
        else:
            # Call the function to calculate a student's average.
            find_student_average(students)

    elif choice == "4":

        # End the program.
        print("Program ended.")
        break

    else:

        # Handle invalid menu choices.
        print("Invalid choice. Please select an option from 1 to 4.")
