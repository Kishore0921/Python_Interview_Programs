"""
Problem: Write a program demonstrating the use of a finally block, which
runs whether or not an exception occurs (simulated file handling).
Example:
    Input: 10, 0
    Output:
        Error: Division by zero is not allowed.
        Execution completed (finally block ran).

Time Complexity: O(1)
Space Complexity: O(1)
"""

a = float(input("Enter numerator: "))
b = float(input("Enter denominator: "))

try:
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed (finally block ran).")