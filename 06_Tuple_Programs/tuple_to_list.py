"""
Problem: Write a program to convert a tuple into a list.
Example:
    Input: (1, 2, 3, 4)
    Output: [1, 2, 3, 4]

Time Complexity: O(n)
Space Complexity: O(n)
"""

numbers = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
converted_list = list(numbers)

print(f"Converted List: {converted_list}")