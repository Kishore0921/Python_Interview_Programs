"""
Problem: Write a program demonstrating handling of multiple exception
types for the same block of code (invalid input and division by zero).
Example:
    Input: "abc", 5
    Output: Error: Invalid input, please enter numeric values.

Time Complexity: O(1)
Space Complexity: O(1)
"""

try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input, please enter numeric values.")
except Exception as e:
    print(f"Unexpected error: {e}")