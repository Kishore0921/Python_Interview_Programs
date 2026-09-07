# 12_Exception_Handling

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers exception handling
concepts — try/except, multiple exception types, finally blocks, and
custom exceptions — which are commonly probed in technical interviews to
assess robust, defensive coding practices.

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `try_except.py` | Demonstrates basic try-except handling (division by zero) |
| 2 | `multiple_exceptions.py` | Demonstrates handling multiple exception types in one block |
| 3 | `finally.py` | Demonstrates a finally block that always runs |
| 4 | `custom_exception.py` | Demonstrates defining and raising a custom exception class |

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
   `custom_exception.py` defines a custom exception class and a small
   `withdraw()` function, since raising a custom exception naturally
   requires an operation to raise it from. The simpler try/except demos
   are written directly without extra functions.

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
python try_except.py
python multiple_exceptions.py
python finally.py
python custom_exception.py
```

## Purpose

This folder is meant purely for **interview preparation practice** —
exception handling questions test understanding of `try`/`except`/`finally`
control flow, catching specific vs. generic exceptions, and designing
custom exception classes for domain-specific error handling.