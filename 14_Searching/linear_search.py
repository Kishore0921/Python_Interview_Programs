"""
Problem: Write a program to search for an element in a list using
linear search.
Example:
    Input: [4, 2, 7, 1, 9], target = 7
    Output: Element found at index 2

Time Complexity: O(n)
Space Complexity: O(1)
"""


def linear_search(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return -1


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the number to search for: "))

result = linear_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")