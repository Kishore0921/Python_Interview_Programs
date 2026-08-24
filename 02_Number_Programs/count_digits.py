"""
Problem: Write a program to count the number of digits in a number.
Example:
    Input: 98765
    Output: 5

Time Complexity: O(d), where d is the number of digits
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))
temp = abs(n)
count = 0

if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10

print(f"Number of Digits: {count}")