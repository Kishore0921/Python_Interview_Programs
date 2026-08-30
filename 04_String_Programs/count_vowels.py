"""
Problem: Write a program to count the number of vowels in a string.
Example:
    Input: "Hello World"
    Output: Vowel Count: 3

Time Complexity: O(n)
Space Complexity: O(1)
"""

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print(f"Vowel Count: {count}")