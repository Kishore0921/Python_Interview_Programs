"""
Problem: Write a program to check whether a given year is a leap year.
Example:
    Input: 2024
    Output: Leap Year

Time Complexity: O(1)
Space Complexity: O(1)
"""

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")