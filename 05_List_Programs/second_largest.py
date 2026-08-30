"""
Problem: Write a program to find the second largest element in a list.
Example:
    Input: [3, 7, 2, 9, 4]
    Output: Second Largest Element: 7

Time Complexity: O(n)
Space Complexity: O(1)
"""

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = second = float("-inf")

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(f"Second Largest Element: {second}")