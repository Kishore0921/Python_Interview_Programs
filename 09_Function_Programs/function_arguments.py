"""
Problem: Write a program demonstrating a function that accepts a
variable number of positional arguments (*args) and returns their sum.
Example:
    Input: 1, 2, 3, 4
    Output: Sum: 10

Time Complexity: O(n)
Space Complexity: O(1)
"""


def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = sum_all(*numbers)

print(f"Sum: {result}")