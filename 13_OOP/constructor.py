"""
Topic: Constructors
This file demonstrates the different types of constructors in Python:
default constructor, parameterized constructor, and constructor with
default parameters.
"""


# ======================================================================
# 1. Default Constructor
# ======================================================================
"""
Problem: Write a program demonstrating a default constructor (a
constructor that takes no arguments other than self).
Example:
    Input: Student()
    Output: A new student record has been created.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Student:
    def __init__(self):
        print("A new student record has been created.")


student1 = Student()


# ======================================================================
# 2. Parameterized Constructor
# ======================================================================
"""
Problem: Write a program demonstrating a parameterized constructor (a
constructor that accepts arguments to initialize instance variables).
Example:
    Input: name="Alice", age=20
    Output: Student: Alice, Age: 20

Time Complexity: O(1)
Space Complexity: O(1)
"""


class StudentWithDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student2 = StudentWithDetails("Alice", 20)
print(f"Student: {student2.name}, Age: {student2.age}")


# ======================================================================
# 3. Constructor with Default Parameters
# ======================================================================
"""
Problem: Write a program demonstrating a constructor with default
parameter values, used when a value is not provided.
Example:
    Input: name="Bob" (grade not provided)
    Output: Student: Bob, Grade: A (default)

Time Complexity: O(1)
Space Complexity: O(1)
"""


class StudentWithDefaultGrade:
    def __init__(self, name, grade="A (default)"):
        self.name = name
        self.grade = grade


student3 = StudentWithDefaultGrade("Bob")
student4 = StudentWithDefaultGrade("Carol", "B")

print(f"Student: {student3.name}, Grade: {student3.grade}")
print(f"Student: {student4.name}, Grade: {student4.grade}")