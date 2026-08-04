"""
Problem: Write a program to swap two numbers without using a third variable.
Example:
    Input: a = 5, b = 10
    Output: a = 10, b = 5

Time Complexity: O(1)
Space Complexity: O(1)
"""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"Before swap: a = {a}, b = {b}")

a, b = b, a
print(f"After swap: a = {a}, b = {b}")