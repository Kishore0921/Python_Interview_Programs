"""
Problem: Write a program to reverse a string using recursion.
Example:
    Input: "hello"
    Output: "olleh"

Time Complexity: O(n)
Space Complexity: O(n), due to recursive call stack
"""


def reverse_string(text):
    if len(text) <= 1:
        return text
    return reverse_string(text[1:]) + text[0]


user_text = input("Enter a string: ")
print(f"Reversed String: {reverse_string(user_text)}")