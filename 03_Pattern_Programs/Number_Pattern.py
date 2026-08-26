"""
Problem: Write a program to print a number pattern (each row containing
numbers from 1 up to the row number).
Example:
    Input: 4
    Output:
        1
        1 2
        1 2 3
        1 2 3 4

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


""" Consecutive number pattern"""

n = int(input("Enter number of rows: "))

# Initialize a counter to track the continuous numbers
current_number = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(current_number, end=" ")
        current_number += 1  # Increment the counter after printing
    print()  # Move to the next line after each row
