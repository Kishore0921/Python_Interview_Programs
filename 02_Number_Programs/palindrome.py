"""
Problem: Write a program to check whether a number is a palindrome.
Example:
    Input: 121
    Output: Palindrome Number

Time Complexity: O(d), where d is the number of digits
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))
original = n
reversed_num = 0

while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n //= 10

if original == reversed_num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")