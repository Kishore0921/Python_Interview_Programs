"""
Problem: Write a program to check whether a string is a palindrome.
Example:
    Input: "madam"
    Output: Palindrome String

Time Complexity: O(n)
Space Complexity: O(n)
"""

text = input("Enter a string: ")
cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Palindrome String")
else:
    print("Not a Palindrome String")