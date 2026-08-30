"""
Problem: Write a program to count the total number of characters in a
string (including spaces).
Example:
    Input: "Hello World"
    Output: Character Count: 11

Time Complexity: O(n)
Space Complexity: O(1)
"""

text = input("Enter a string: ")
count = len(text)

print(f"Character Count: {count}")