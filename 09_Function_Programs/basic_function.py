"""
Problem: Write a program demonstrating a basic function definition and
call (a function that greets a user by name).
Example:
    Input: "Alice"
    Output: Hello, Alice!

Time Complexity: O(1)
Space Complexity: O(1)
"""


def greet(name):
    print(f"Hello, {name}!")


user_name = input("Enter your name: ")
greet(user_name)