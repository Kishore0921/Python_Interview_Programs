"""
Problem: Write a program to count the number of words in a string.
Example:
    Input: "Interview practice is fun"
    Output: Word Count: 4

Time Complexity: O(n)
Space Complexity: O(n)
"""

text = input("Enter a string: ")
words = text.split()
count = len(words)

print(f"Word Count: {count}")