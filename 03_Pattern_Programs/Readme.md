# 03_Pattern_Programs

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers classic pattern-printing
problems (stars, numbers, alphabets) that are commonly asked to test
understanding of nested loops.

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `square_pattern.py` | Prints a square pattern of stars |
| 2 | `triangle_pattern.py` | Prints a right-angled triangle pattern of stars |
| 3 | `inverted_triangle.py` | Prints an inverted right-angled triangle pattern of stars |
| 4 | `pyramid_pattern.py` | Prints a centered pyramid pattern of stars |
| 5 | `number_pattern.py` | Prints a number pattern (1, 1 2, 1 2 3, ...) |
| 6 | `alphabet_pattern.py` | Prints an alphabet pattern (A, A B, A B C, ...) |

## Format

Every program follows the same structure so problems are easy to scan and
review:

1. A multi-line docstring at the top of the file containing:
   - **Problem** statement
   - **Example** (Input/Output)
   - **Time Complexity**
   - **Space Complexity**
2. Direct, straight-line code (nested loops) with no unnecessary wrapping
   in `main()` or helper functions.
3. Functions are used **only where they genuinely help** — e.g.
   `pyramid_pattern.py` uses a small `print_row()` helper since the
   spacing + star logic is repeated for every row. Simpler patterns are
   printed directly without extra functions.

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
python square_pattern.py
python triangle_pattern.py
python inverted_triangle.py
python pyramid_pattern.py
python number_pattern.py
python alphabet_pattern.py
```

## Purpose

This folder is meant purely for **interview preparation practice** — pattern
problems are a common way interviewers test comfort with nested loops,
row/column indexing, and basic control flow before moving on to more
complex algorithmic questions.