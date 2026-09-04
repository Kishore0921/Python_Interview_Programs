"""
Problem: Write a program to find the sum of the first n natural numbers
using recursion.
Example:
    Input: 5
    Output: 15

Time Complexity: O(n)
Space Complexity: O(n), due to recursive call stack
"""


def sum_of_n(n):
    if n == 0:
        return 0
    return n + sum_of_n(n - 1)


num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a non-negative number")
else:
    print(f"Sum: {sum_of_n(num)}")