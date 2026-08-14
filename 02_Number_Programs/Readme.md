# 02_Number_Programs

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers classic number-based
problems that are frequently asked in technical interviews.

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `prime_number.py` | Checks whether a number is prime |
| 2 | `palindrome_number.py` | Checks whether a number is a palindrome |
| 3 | `armstrong_number.py` | Checks whether a number is an Armstrong number |
| 4 | `factorial.py` | Finds the factorial of a number (recursive) |
| 5 | `fibonacci.py` | Prints the Fibonacci series up to n terms |
| 6 | `perfect_number.py` | Checks whether a number is a perfect number |
| 7 | `strong_number.py` | Checks whether a number is a strong number |
| 8 | `automorphic_number.py` | Checks whether a number is an automorphic number |
| 9 | `reverse_number.py` | Reverses the digits of a number |
| 10 | `sum_of_digits.py` | Finds the sum of digits of a number |
| 11 | `count_digits.py` | Counts the number of digits in a number |

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
3. Functions are used **only where they genuinely help** — e.g.
   `factorial.py` uses a recursive function, and `strong_number.py` uses a
   small helper function to compute a digit's factorial (reused per digit).
   Simpler problems are solved directly without extra functions.

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
python prime_number.py
python palindrome_number.py
python armstrong_number.py
python factorial.py
python fibonacci.py
python perfect_number.py
python strong_number.py
python automorphic_number.py
python reverse_number.py
python sum_of_digits.py
python count_digits.py
```

## Purpose

This folder is meant purely for **interview preparation practice** — working
through classic number-theory style problems that build pattern-recognition
skills (digit extraction, divisor checks, recursion) useful for a wide range
of coding interview questions.