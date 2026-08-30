"""
Problem: Write a program to find the smallest element in a list.
Example:
    Input: [3, 7, 2, 9, 4]
    Output: Smallest Element: 2

Time Complexity: O(n)
Space Complexity: O(1)
"""

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print(f"Smallest Element: {smallest}")