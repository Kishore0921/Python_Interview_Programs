"""
Topic: Abstraction
This file demonstrates abstraction in Python using the abc module:
abstract classes and abstract methods.
"""

from abc import ABC, abstractmethod


# ======================================================================
# 1. Abstract Class
# ======================================================================
"""
Problem: Write a program demonstrating an abstract class, which cannot
be instantiated directly and is meant to be subclassed.
Example:
    Input: Shape()
    Output: Error: Can't instantiate abstract class Shape with abstract
            method area

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


try:
    shape = Shape()
except TypeError as e:
    print(f"Error: {e}")


# ======================================================================
# 2. Abstract Method
# ======================================================================
"""
Problem: Write a program demonstrating abstract methods, which must be
implemented by any concrete subclass of an abstract class.
Example:
    Input: Circle(5).area(), Rectangle(4, 6).area()
    Output: Circle Area: 78.5
            Rectangle Area: 24

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle Area: {circle.area()}")
print(f"Rectangle Area: {rectangle.area()}")