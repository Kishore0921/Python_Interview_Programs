"""
Problem: Write a program to check whether a number is a perfect number.
(A number is perfect if the sum of its proper divisors equals the number
itself.)
Example:
    Input: 28
    Output: Perfect Number

Time Complexity: O(n)
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))
divisor_sum = 0

for i in range(1, n):
    if n % i == 0:
        divisor_sum += i

if divisor_sum == n and n != 0:
    print("Perfect Number")
else:
    print("Not a Perfect Number")