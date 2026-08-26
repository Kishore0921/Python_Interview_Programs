"""
Problem: Write a program to print a square pattern of stars.
Example:
    Input: 4
    Output:
        * * * *
        * * * *
        * * * *
        * * * *

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()