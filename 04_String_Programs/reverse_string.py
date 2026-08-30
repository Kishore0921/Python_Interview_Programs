"""
Problem: Write a program to reverse a string.
Example:
    Input: "hello"
    Output: "olleh"

Time Complexity: O(n)
Space Complexity: O(n)
"""

text = input("Enter a string: ")
reversed_text = text[::-1]

print(f"Reversed String: {reversed_text}")