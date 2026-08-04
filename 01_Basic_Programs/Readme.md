# 01_Basic_Programs

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers fundamental programming
concepts that are commonly asked in technical interviews and are a good
starting point before moving on to more advanced topics like data structures
and algorithms.

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `Hello_World.py` | Prints "Hello, World!" to the console |
| 2 | `Add_Two_Numbers.py` | Adds two numbers entered by the user |
| 3 | `Even_Odd.py` | Checks whether a number is even or odd |
| 4 | `Leap_Year.py` | Checks whether a given year is a leap year |
| 5 | `Swap_Two_Numbers.py` | Swaps two numbers without using a third variable |
| 6 | `Largest_Of_Three.py` | Finds the largest among three numbers |
| 7 | `Calculator.py` | A simple calculator (+, -, *, /) |

## Format

Every program follows the same structure so problems are easy to scan and
review:

1. A multi-line docstring at the top of the file containing:
   - **Problem** statement
   - **Example** (Input/Output)
   - **Time Complexity**
   - **Space Complexity**
2. Direct, straight-line code (input → logic → output) with no unnecessary
   wrapping in `main()` or helper functions.
3. Functions are used **only where they genuinely help** (e.g. reusable
   logic, recursion, clarity for a non-trivial algorithm) — not added to
   every file just for structure.

Example docstring format used throughout:

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

## How to Run

Each file can be run independently:

```bash
python Hello_World.py
python Add_Two_Numbers.py
python Even_Odd.py
python Leap_Year.py
python Swap_Two_Numbers.py
python Largest_Of_Three.py
python Calculator.py
```

## Purpose

This folder is meant purely for **interview preparation practice** — building
a strong foundation with basic programs before progressing to more complex
topics (arrays, strings, recursion, data structures, algorithms, etc.) in
later folders.