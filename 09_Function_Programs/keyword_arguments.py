"""
Problem: Write a program demonstrating a function called using keyword
arguments (a function that builds and prints a simple user profile).
Example:
    Input: name="Alice", age=25, city="London"
    Output: Alice is 25 years old and lives in London.

Time Complexity: O(1)
Space Complexity: O(1)
"""


def build_profile(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")


user_name = input("Enter name: ")
user_age = int(input("Enter age: "))
user_city = input("Enter city: ")

build_profile(name=user_name, age=user_age, city=user_city)