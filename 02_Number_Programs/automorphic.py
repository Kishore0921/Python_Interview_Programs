"""
Problem: Write a program to check whether a number is an automorphic number.
(A number is automorphic if its square ends in the same digits as the
number itself.)
Example:
    Input: 25
    Output: Automorphic Number
    (25^2 = 625, which ends with 25)

Time Complexity: O(d), where d is the number of digits
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))
square = n * n

if str(square).endswith(str(n)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")