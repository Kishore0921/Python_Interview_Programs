"""
Problem: Write a program to remove duplicate elements from a list using
a set.
Example:
    Input: [1, 2, 2, 3, 4, 4, 5]
    Output: [1, 2, 3, 4, 5]

Time Complexity: O(n)
Space Complexity: O(n)
"""

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = list(set(numbers))
unique_numbers.sort()

print(f"List after removing duplicates: {unique_numbers}")