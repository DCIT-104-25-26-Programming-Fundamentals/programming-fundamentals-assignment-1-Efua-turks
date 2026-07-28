# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================


def print_single_table(num):
    """Prints the multiplication table for a given number from 1 to 12."""
    print(f"Multiplication Table for {num}:")
    for i in range(1, 13):
        # f-string formatting ensures neat alignment
        print(f"{num:2d}  x  {i:2d}  =  {num * i:3d}")


def print_all_tables(n):
    """Prints multiplication tables for numbers from 1 to N."""
    for i in range(1, n + 1):
        print_single_table(i)
        if i < n:  # Add separator line between tables, except after the last one
            print("-" * 27)


# =============================================================================
# MAIN PROGRAM
# =============================================================================
if __name__ == "__main__":
    # --- PART A ---
    try:
        user_num = int(input("Enter a number for Part A: "))
        if user_num <= 0:
            print("Error: Please enter a positive integer greater than 0.")
        else:
            print_single_table(user_num)
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")

    print("\n" + "=" * 40 + "\n")  # Visual gap between Part A and Part B

    # --- PART B ---
    try:
        max_num = int(input("Enter N for Part B (Tables 1 to N): "))
        if max_num <= 0:
            print("Error: Please enter a positive integer greater than 0.")
        else:
            print_all_tables(max_num)
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")