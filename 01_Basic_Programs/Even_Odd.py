"""
Problem: Write a program to check whether a number is even or odd.
Example:
    Input: 7
    Output: Odd Number

Time Complexity: O(1)
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")