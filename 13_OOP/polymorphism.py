"""
Topic: Polymorphism
This file demonstrates the different forms of polymorphism in Python:
method overriding, duck typing, and operator overloading.
"""


# ======================================================================
# 1. Method Overriding
# ======================================================================
"""
Problem: Write a program demonstrating method overriding, where a child
class provides its own implementation of a method already defined in
its parent class.
Example:
    Input: Dog().speak(), Cat().speak()
    Output: The dog barks.
            The cat meows.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Animal:
    def speak(self):
        print("This animal makes a sound.")


class Dog(Animal):
    def speak(self):
        print("The dog barks.")


class Cat(Animal):
    def speak(self):
        print("The cat meows.")


for creature in (Dog(), Cat()):
    creature.speak()


# ======================================================================
# 2. Duck Typing
# ======================================================================
"""
Problem: Write a program demonstrating duck typing, where an object's
suitability is determined by the presence of methods/attributes rather
than its actual type ("if it walks like a duck and quacks like a duck").
Example:
    Input: make_it_speak(Duck()), make_it_speak(Robot())
    Output: Quack!
            Beep, I am speaking.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Duck:
    def speak(self):
        print("Quack!")


class Robot:
    def speak(self):
        print("Beep, I am speaking.")


def make_it_speak(entity):
    entity.speak()


make_it_speak(Duck())
make_it_speak(Robot())


# ======================================================================
# 3. Operator Overloading
# ======================================================================
"""
Problem: Write a program demonstrating operator overloading, where a
built-in operator (like +) is given custom behavior for a user-defined
class.
Example:
    Input: Point(1, 2) + Point(3, 4)
    Output: Point(4, 6)

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2

print(p3)