# 13_OOP

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers core Object-Oriented
Programming (OOP) concepts — classes, constructors, inheritance,
polymorphism, encapsulation, and abstraction — which are heavily tested in
technical interviews, especially for Python-specific and design-oriented
roles.

## Contents

| # | File | Types Covered |
|---|------|----------------|
| 1 | `class_object.py` | Creating a Class, Creating an Object, Instance Variables, Instance Methods, Accessing Class Members |
| 2 | `constructor.py` | Default Constructor, Parameterized Constructor, Constructor with Default Parameters |
| 3 | `inheritance.py` | Single, Multilevel, Multiple, Hierarchical, Hybrid Inheritance |
| 4 | `polymorphism.py` | Method Overriding, Duck Typing, Operator Overloading |
| 5 | `encapsulation.py` | Public Members, Protected Members, Private Members |
| 6 | `abstraction.py` | Abstract Class, Abstract Method |

## Format

Unlike earlier folders (where each file solves one problem), every file
here covers **several related types/variations of one OOP concept**, since
that's how these topics are usually asked about and revised together.

Each file is structured as:

1. A top-of-file docstring stating the overall **Topic** and what it
   covers.
2. The file is divided into **numbered, clearly marked sections** (one per
   type), separated by comment banners, e.g.:

   ```python
   # ======================================================================
   # 1. Single Inheritance
   # ======================================================================
   ```

3. Each section has its own multi-line docstring in the same format used
   throughout this repository:

   ```python
   """
   Problem: Write a program to check whether a number is prime.
   Example:
       Input: 17
       Output: Prime Number

   Time Complexity: O(√n)
   Space Complexity: O(1)
   """
   ```

4. Classes/functions are defined directly where needed to demonstrate the
   concept — since this folder is specifically about OOP, class
   definitions are the point being practiced in every section (not
   optional, unlike plain function usage in earlier folders).

5. Later sections in a file may reuse classes defined in earlier sections
   (e.g. `inheritance.py` builds `Puppy` on top of `Dog`, which is built on
   top of `Animal`) to show how the types build on one another.

## How to Run

Each file can be run independently and will print output for every
section in order:

```bash
python class_object.py
python constructor.py
python inheritance.py
python polymorphism.py
python encapsulation.py
python abstraction.py
```

## Purpose

This folder is meant purely for **interview preparation practice** — OOP
concepts are one of the most common interview topics for Python roles,
and understanding the distinctions between each type (e.g. the different
kinds of inheritance, or public/protected/private access) is essential for
answering conceptual and design-based interview questions confidently.