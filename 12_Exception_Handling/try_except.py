"""
Problem: Write a program demonstrating basic try-except handling for
division, catching the case where the divisor is zero.
Example:
    Input: 10, 0
    Output: Error: Division by zero is not allowed.

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