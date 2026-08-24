"""
Problem: Write a program to reverse the digits of a number.
Example:
    Input: 1234
    Output: 4321

Time Complexity: O(d), where d is the number of digits
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))
reversed_num = 0
temp = abs(n)

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

if n < 0:
    reversed_num = -reversed_num

print(f"Reversed Number: {reversed_num}")