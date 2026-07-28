# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# YOUR CODE BELOW
# =============================================================================

def read_matrix(rows, cols):
    """Read a matrix of given size from the user."""
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """Print a matrix in a neat aligned format."""
    for row in matrix:
        print("  ".join(f"{num:3}" for num in row))


def transpose_matrix(matrix):
    """Return the transpose of the given matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


def add_matrices(matrix1, matrix2):
    """Return the element-wise sum of two matrices."""
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the product of two matrices A × B."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


# =========================
# MAIN PROGRAM
# =========================

print("=== PART A: Transpose a Matrix ===")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter the matrix:")
matrix = read_matrix(rows, cols)

print("\nOriginal Matrix:")
print_matrix(matrix)

transposed = transpose_matrix(matrix)
print("\nTransposed Matrix:")
print_matrix(transposed)


print("\n=== PART B: Add Two Matrices ===")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter first matrix:")
matrix1 = read_matrix(rows, cols)

print("Enter second matrix:")
matrix2 = read_matrix(rows, cols)

print("\nMatrix 1:")
print_matrix(matrix1)
print("\nMatrix 2:")
print_matrix(matrix2)

sum_matrix = add_matrices(matrix1, matrix2)
print("\nSum of Matrices:")
print_matrix(sum_matrix)


print("\n=== PART C: Multiply Two Matrices ===")
rows_a = int(input("Enter number of rows for Matrix A: "))
cols_a = int(input("Enter number of columns for Matrix A: "))
print("Enter Matrix A:")
matrix_a = read_matrix(rows_a, cols_a)

rows_b = int(input("Enter number of rows for Matrix B: "))
cols_b = int(input("Enter number of columns for Matrix B: "))
print("Enter Matrix B:")
matrix_b = read_matrix(rows_b, cols_b)

if cols_a != rows_b:
    print("Error: Cannot multiply — columns of A must equal rows of B.")
else:
    print("\nMatrix A:")
    print_matrix(matrix_a)
    print("\nMatrix B:")
    print_matrix(matrix_b)

    product = multiply_matrices(matrix_a, matrix_b)
    print("\nProduct (A × B):")
    print_matrix(product)