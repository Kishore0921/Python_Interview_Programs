"""
Problem: Write a program to remove duplicate elements from a list while
preserving the original order.
Example:
    Input: [1, 2, 2, 3, 4, 4, 5]
    Output: [1, 2, 3, 4, 5]

Time Complexity: O(n)
Space Complexity: O(n)
"""

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

seen = set()
result = []

for num in numbers:
    if num not in seen:
        seen.add(num)
        result.append(num)

print(f"List after removing duplicates: {result}")