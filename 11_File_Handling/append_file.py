"""
Problem: Write a program to append content to the end of an existing
file (or create it if it does not exist).
Example:
    Input: filename = "sample.txt", content = "This is a new line."
    Output: Content appended to 'sample.txt' successfully.

Time Complexity: O(n), where n is the length of the content
Space Complexity: O(1)
"""

filename = input("Enter file name to append to: ")
content = input("Enter content to append: ")

with open(filename, "a") as file:
    file.write(content + "\n")

print(f"Content appended to '{filename}' successfully.")