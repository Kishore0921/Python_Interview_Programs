"""
Problem: Write a program to find the largest of three numbers.
Example:
    Input: 10, 25, 15
    Output: Largest Number: 25

Time Complexity: O(1)
Space Complexity: O(1)
"""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

print(f"Largest Number: {largest}")