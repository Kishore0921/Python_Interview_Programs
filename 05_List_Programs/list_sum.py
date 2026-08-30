"""
Problem: Write a program to find the sum of all elements in a list.
Example:
    Input: [1, 2, 3, 4, 5]
    Output: Sum: 15

Time Complexity: O(n)
Space Complexity: O(1)
"""

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

total = 0
for num in numbers:
    total += num

print(f"Sum: {total}")