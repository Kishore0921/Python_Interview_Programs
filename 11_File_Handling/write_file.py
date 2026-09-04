"""
Problem: Write a program to write content to a file. If the file
already exists, its content should be overwritten.
Example:
    Input: filename = "sample.txt", content = "Hello, World!"
    Output: File 'sample.txt' written successfully.

Time Complexity: O(n), where n is the length of the content
Space Complexity: O(1)
"""

filename = input("Enter file name to write to: ")
content = input("Enter content to write: ")

with open(filename, "w") as file:
    file.write(content)

print(f"File '{filename}' written successfully.")