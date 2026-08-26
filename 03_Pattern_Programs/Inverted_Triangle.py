"""
Problem: Write a program to print an inverted right-angled triangle pattern
of stars.
Example:
    Input: 4
    Output:
        * * * *
        * * *
        * *
        *

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()