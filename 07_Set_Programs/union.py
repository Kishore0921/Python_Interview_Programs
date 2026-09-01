"""
Problem: Write a program to find the union of two sets.
Example:
    Input: {1, 2, 3}, {3, 4, 5}
    Output: {1, 2, 3, 4, 5}

Time Complexity: O(len(set1) + len(set2))
Space Complexity: O(n)
"""

set1 = set(map(int, input("Enter first set of numbers: ").split()))
set2 = set(map(int, input("Enter second set of numbers: ").split()))

result = set1 | set2
print(f"Union: {result}")