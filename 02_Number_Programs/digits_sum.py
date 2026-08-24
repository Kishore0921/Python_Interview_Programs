"""
Problem: Write a program to find the sum of digits of a number.
Example:
    Input: 12345
    Output: 15

Time Complexity: O(d), where d is the number of digits
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))
temp = abs(n)
digit_sum = 0

while temp > 0:
    digit_sum += temp % 10
    temp //= 10

print(f"Sum of Digits: {digit_sum}")