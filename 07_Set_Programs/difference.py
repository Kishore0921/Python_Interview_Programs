"""
Problem: Write a program to find the difference between two sets.
Example:
    Input: {1, 2, 3}, {2, 3, 4}
    Output: {1}

Time Complexity: O(len(set1))
Space Complexity: O(n)
"""

set1 = set(map(int, input("Enter first set of numbers: ").split()))
set2 = set(map(int, input("Enter second set of numbers: ").split()))

result = set1 - set2
print(f"Difference (set1 - set2): {result}")