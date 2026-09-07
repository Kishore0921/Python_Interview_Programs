"""
Topic: Classes and Objects
This file demonstrates the fundamentals of classes and objects in Python:
creating a class, creating an object, instance variables, instance
methods, and accessing class members.
"""


# ======================================================================
# 1. Creating a Class
# ======================================================================
"""
Problem: Write a program to define a simple class representing a Car.
Example:
    Input: (class definition only, no output)
    Output: Class 'Car' is defined.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Car:
    pass


print("Class 'Car' is defined.")


# ======================================================================
# 2. Creating an Object
# ======================================================================
"""
Problem: Write a program to create an object (instance) of a class.
Example:
    Input: Car()
    Output: <class '__main__.Car'> object created.

Time Complexity: O(1)
Space Complexity: O(1)
"""

my_car = Car()
print(f"{type(my_car)} object created.")


# ======================================================================
# 3. Instance Variables
# ======================================================================
"""
Problem: Write a program to define instance variables that are unique
to each object of a class.
Example:
    Input: brand="Toyota", model="Corolla"
    Output: Toyota Corolla

Time Complexity: O(1)
Space Complexity: O(1)
"""


class CarWithAttributes:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = CarWithAttributes("Toyota", "Corolla")
car2 = CarWithAttributes("Honda", "Civic")

print(f"{car1.brand} {car1.model}")
print(f"{car2.brand} {car2.model}")


# ======================================================================
# 4. Instance Methods
# ======================================================================
"""
Problem: Write a program to define instance methods that operate on an
object's instance variables.
Example:
    Input: brand="Toyota", model="Corolla"
    Output: This car is a Toyota Corolla.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class CarWithMethods:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        print(f"This car is a {self.brand} {self.model}.")


car3 = CarWithMethods("Ford", "Mustang")
car3.describe()


# ======================================================================
# 5. Accessing Class Members
# ======================================================================
"""
Problem: Write a program to access and modify an object's attributes
and call its methods using dot notation.
Example:
    Input: car.brand = "Tesla"
    Output: Updated brand: Tesla

Time Complexity: O(1)
Space Complexity: O(1)
"""

car4 = CarWithMethods("Tesla", "Model 3")
print(f"Before update: {car4.brand}")

car4.brand = "Tesla"
print(f"Updated brand: {car4.brand}")
car4.describe()