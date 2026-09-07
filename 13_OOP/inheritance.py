"""
Topic: Inheritance
This file demonstrates the different types of inheritance in Python:
single, multilevel, multiple, hierarchical, and hybrid inheritance.
"""


# ======================================================================
# 1. Single Inheritance
# ======================================================================
"""
Problem: Write a program demonstrating single inheritance, where one
class inherits from a single parent class.
Example:
    Input: Dog().speak()
    Output: This animal makes a sound.
            The dog barks.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Animal:
    def speak(self):
        print("This animal makes a sound.")


class Dog(Animal):
    def bark(self):
        print("The dog barks.")


dog = Dog()
dog.speak()
dog.bark()


# ======================================================================
# 2. Multilevel Inheritance
# ======================================================================
"""
Problem: Write a program demonstrating multilevel inheritance, where a
class inherits from a class that itself inherits from another class.
Example:
    Input: Puppy().speak()
    Output: This animal makes a sound.
            The dog barks.
            The puppy whines.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Puppy(Dog):
    def whine(self):
        print("The puppy whines.")


puppy = Puppy()
puppy.speak()
puppy.bark()
puppy.whine()


# ======================================================================
# 3. Multiple Inheritance
# ======================================================================
"""
Problem: Write a program demonstrating multiple inheritance, where a
class inherits from more than one parent class.
Example:
    Input: FlyingCar().drive(), FlyingCar().fly()
    Output: The car drives on the road.
            The car flies in the sky.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Car:
    def drive(self):
        print("The car drives on the road.")


class Flyable:
    def fly(self):
        print("The car flies in the sky.")


class FlyingCar(Car, Flyable):
    pass


flying_car = FlyingCar()
flying_car.drive()
flying_car.fly()


# ======================================================================
# 4. Hierarchical Inheritance
# ======================================================================
"""
Problem: Write a program demonstrating hierarchical inheritance, where
multiple classes inherit from the same parent class.
Example:
    Input: Cat().speak(), Cow().speak()
    Output: This animal makes a sound.
            This animal makes a sound.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Cat(Animal):
    def meow(self):
        print("The cat meows.")


class Cow(Animal):
    def moo(self):
        print("The cow moos.")


cat = Cat()
cow = Cow()
cat.speak()
cat.meow()
cow.speak()
cow.moo()


# ======================================================================
# 5. Hybrid Inheritance
# ======================================================================
"""
Problem: Write a program demonstrating hybrid inheritance, which
combines two or more types of inheritance (e.g. hierarchical + multiple).
Example:
    Input: WorkingStudent().study(), WorkingStudent().work()
    Output: The person studies.
            The person works.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Person:
    def introduce(self):
        print("This is a person.")


class Student(Person):
    def study(self):
        print("The person studies.")


class Worker(Person):
    def work(self):
        print("The person works.")


class WorkingStudent(Student, Worker):
    pass


working_student = WorkingStudent()
working_student.introduce()
working_student.study()
working_student.work()