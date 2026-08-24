"""
Problem: Write a program to check whether a number is a strong number.
(A number is strong if the sum of the factorials of its digits equals
the number itself.)
Example:
    Input: 145
    Output: Strong Number
    (1! + 4! + 5! = 1 + 24 + 120 = 145)

Time Complexity: O(d), where d is the number of digits
Space Complexity: O(1)
"""


def digit_factorial(digit):
    result = 1
    for i in range(1, digit + 1):
        result *= i
    return result


n = int(input("Enter a number: "))
original = n
total = 0

while n > 0:
    digit = n % 10
    total += digit_factorial(digit)
    n //= 10

if total == original:
    print("Strong Number")
else:
    print("Not a Strong Number")