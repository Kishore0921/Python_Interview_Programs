"""
Problem: Write a program to reverse a list.
Example:
    Input: [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]

Time Complexity: O(n)
Space Complexity: O(n)
"""

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
reversed_list = numbers[::-1]

print(f"Reversed List: {reversed_list}")