"""
Problem: Write a program to print a pyramid pattern of stars.
Example:
    Input: 4
    Output:
           *
          * *
         * * *
        * * * *

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def print_row(spaces, stars):
    print(" " * spaces, end="")
    for _ in range(stars):
        print("*", end=" ")
    print()


n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print_row(n - i, i)