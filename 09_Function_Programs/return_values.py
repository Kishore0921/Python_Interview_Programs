"""
Problem: Write a program demonstrating a function that returns multiple
values (minimum and maximum of a list) using a single return statement.
Example:
    Input: [4, 2, 9, 1, 7]
    Output: Min: 1, Max: 9

Time Complexity: O(n)
Space Complexity: O(1)
"""


def min_and_max(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest


values = list(map(int, input("Enter numbers separated by spaces: ").split()))
low, high = min_and_max(values)

print(f"Min: {low}, Max: {high}")