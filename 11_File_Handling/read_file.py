"""
Problem: Write a program to read and display the content of a file.
Example:
    Input: filename = "sample.txt" (contains "Hello, World!")
    Output: Hello, World!

Time Complexity: O(n), where n is the size of the file
Space Complexity: O(n)
"""

filename = input("Enter file name to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
    print("File Content:")
    print(content)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")