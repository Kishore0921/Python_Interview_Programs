"""
Problem: Write a program demonstrating common file operations: checking
if a file exists, writing to it, reading it back, counting its lines,
and deleting it.
Example:
    Input: filename = "sample.txt", content = "Hello\nWorld"
    Output:
        File exists: False
        File written successfully.
        File Content: Hello
                       World
        Line Count: 2
        File deleted successfully.

Time Complexity: O(n), where n is the size of the file
Space Complexity: O(n)
"""

import os


def file_exists(filename):
    return os.path.exists(filename)


def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)


def read_from_file(filename):
    with open(filename, "r") as file:
        return file.read()


def count_lines(filename):
    with open(filename, "r") as file:
        return len(file.readlines())


def delete_file(filename):
    os.remove(filename)


filename = input("Enter file name: ")
content = input("Enter content to write (use \\n for new lines): ").replace("\\n", "\n")

print(f"File exists: {file_exists(filename)}")

write_to_file(filename, content)
print("File written successfully.")

print("File Content:")
print(read_from_file(filename))

print(f"Line Count: {count_lines(filename)}")

delete_file(filename)
print("File deleted successfully.")