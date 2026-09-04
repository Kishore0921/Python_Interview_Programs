"""
Problem: Write a program to print the Fibonacci series up to n terms
using recursion.
Example:
    Input: 7
    Output: 0 1 1 2 3 5 8

Time Complexity: O(2^n), due to repeated recursive calls
Space Complexity: O(n), due to recursive call stack
"""


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("Enter number of terms: "))
series = [fibonacci(i) for i in range(terms)]

print("Fibonacci Series:", *series)