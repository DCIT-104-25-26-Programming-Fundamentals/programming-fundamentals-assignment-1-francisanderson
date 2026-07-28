def display_matrix(matrix):
    # Loop through each row in the matrix.
    # Each row is printed as a separate line to create a grid format.
    for row in matrix:

        # Loop through each value in the row.
        # The values are separated by spaces for neat display.
        for value in row:
            print(value, end=" ")

        # Move to the next line after printing one complete row.
        print()


def transpose_matrix(matrix):
    # Create an empty list to store the transposed matrix.
    transpose = []

    # The number of columns in the original matrix becomes
    # the number of rows in the transposed matrix.
    for column in range(len(matrix[0])):

        # Create an empty row for the new matrix.
        new_row = []

        # The number of rows in the original matrix becomes
        # the number of values in each new row.
        for row in range(len(matrix)):

            # Add the value from the current row and column position.
            new_row.append(matrix[row][column])

        # Add the completed row to the transposed matrix.
        transpose.append(new_row)

    # Return the new transposed matrix.
    return transpose


def add_matrices(matrix_a, matrix_b):
    # Create an empty list to store the result matrix.
    result = []

    # Loop through each row of the matrices.
    for i in range(len(matrix_a)):

        # Create an empty row for the result.
        row = []

        # Loop through each column of the matrices.
        for j in range(len(matrix_a[0])):

            # Add the values at the same position in both matrices.
            row.append(matrix_a[i][j] + matrix_b[i][j])

        # Add the completed row to the result matrix.
        result.append(row)

    # Return the added matrix.
    return result


def multiply_matrices(matrix_a, matrix_b):
    # Create an empty list to store the multiplication result.
    result = []

    # The number of rows in matrix A determines the rows of the result.
    for i in range(len(matrix_a)):

        # Create an empty row for the result.
        row = []

        # The number of columns in matrix B determines the columns of the result.
        for j in range(len(matrix_b[0])):

            # Store the sum of multiplied values for the current position.
            total = 0

            # Multiply each value in the row of A with the matching value
            # in the column of B, then add the results.
            for k in range(len(matrix_b)):

                total = total + (matrix_a[i][k] * matrix_b[k][j])

            # Add the calculated value to the current row.
            row.append(total)

        # Add the completed row to the result matrix.
        result.append(row)

    # Return the multiplied matrix.
    return result


def read_matrix(rows, columns):
    # Create an empty list to store the matrix.
    matrix = []

    # Loop through each row that the user needs to enter.
    for i in range(rows):

        # Keep asking until the user enters a valid row.
        while True:
            values = input(f"Enter row {i + 1}: ").split()

            # Check if the number of values entered matches the columns.
            if len(values) == columns:
                break

            # If the number of values is incorrect, ask again.
            print(f"Please enter exactly {columns} values.")

        # Convert all values in the row from strings to integers.
        row = []

        for value in values:
            row.append(int(value))

        # Add the completed row to the matrix.
        matrix.append(row)

    # Return the completed matrix.
    return matrix


# =========================
# MAIN PROGRAM
# =========================

# Read the size of the first matrix.
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

# Read matrix A from the user.
print("Enter Matrix A:")
matrix_a = read_matrix(rows, columns)

# Display original matrix.
print("\nOriginal Matrix:")
display_matrix(matrix_a)

# PART A: Transpose matrix A.
print("\nTransposed Matrix:")
transposed = transpose_matrix(matrix_a)
display_matrix(transposed)


# PART B: Matrix Addition.
print("\nEnter Matrix B for Addition:")
matrix_b = read_matrix(rows, columns)

print("\nMatrix Addition Result:")
addition_result = add_matrices(matrix_a, matrix_b)
display_matrix(addition_result)


# PART C: Matrix Multiplication.
print("\nMatrix Multiplication")
print("Matrix multiplication requires Matrix A columns = Matrix B rows.")

while True:

    # Ask for the size of matrix B for multiplication.
    rows_b = int(input("Enter number of rows for Matrix B: "))
    columns_b = int(input("Enter number of columns for Matrix B: "))

    # Check if multiplication is possible.
    if rows_b == columns:
        break

    print("Invalid size. Matrix B rows must equal Matrix A columns.")

print("Enter Matrix B for Multiplication:")
matrix_b_multiply = read_matrix(rows_b, columns_b)

print("\nMatrix Multiplication Result:")
multiplication_result = multiply_matrices(matrix_a, matrix_b_multiply)
display_matrix(multiplication_result)