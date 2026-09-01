"""
Problem: Write a program to convert a list into a tuple.
Example:
    Input: [1, 2, 3, 4]
    Output: (1, 2, 3, 4)

Time Complexity: O(n)
Space Complexity: O(n)
"""

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
converted_tuple = tuple(numbers)

print(f"Converted Tuple: {converted_tuple}")