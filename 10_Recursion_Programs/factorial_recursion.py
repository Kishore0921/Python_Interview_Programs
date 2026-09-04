"""
Problem: Write a program to find the factorial of a number using
recursion.
Example:
    Input: 5
    Output: 120

Time Complexity: O(n)
Space Complexity: O(n), due to recursive call stack
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"Factorial: {factorial(num)}")