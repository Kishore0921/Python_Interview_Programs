"""
Problem: Write a program to check whether a number is an Armstrong number.
(A number is an Armstrong number if the sum of its own digits, each raised
to the power of the number of digits, equals the number itself.)
Example:
    Input: 153
    Output: Armstrong Number

Time Complexity: O(d), where d is the number of digits
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))
original = n
num_digits = len(str(n))
total = 0

temp = n
while temp > 0:
    digit = temp % 10
    total += digit ** num_digits
    temp //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")