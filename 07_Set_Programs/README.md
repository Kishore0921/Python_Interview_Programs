# 07_Set_Programs

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers common set-related
problems, including basic operations and set theory operations
(union, intersection, difference).

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `set_operations.py` | Demonstrates basic set operations (add, remove, membership check, length) |
| 2 | `union.py` | Finds the union of two sets |
| 3 | `intersection.py` | Finds the intersection of two sets |
| 4 | `difference.py` | Finds the difference between two sets |
| 5 | `remove_duplicates.py` | Removes duplicate elements from a list using a set |

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
3. Functions are used **only where they genuinely help**. All problems in
   this folder are simple, direct operations built on Python's set
   operators (`|`, `&`, `-`), so none required an extra function.

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
python set_operations.py
python union.py
python intersection.py
python difference.py
python remove_duplicates.py
```

## Purpose

This folder is meant purely for **interview preparation practice** — set
questions test understanding of set theory, Python's built-in set
operators, and using sets to solve deduplication/membership problems
efficiently.