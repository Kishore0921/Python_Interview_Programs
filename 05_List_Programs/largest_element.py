"""
Problem: Write a program to find the largest element in a list.
Example:
    Input: [3, 7, 2, 9, 4]
    Output: Largest Element: 9

Time Complexity: O(n)
Space Complexity: O(1)
"""

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(f"Largest Element: {largest}")