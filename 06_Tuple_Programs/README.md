# 06_Tuple_Programs

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers common tuple-related
problems, including basic operations and conversions between tuples and
lists.

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `tuple_operations.py` | Demonstrates basic tuple operations (access, count, index, concatenation, slicing) |
| 2 | `tuple_to_list.py` | Converts a tuple into a list |
| 3 | `list_to_tuple.py` | Converts a list into a tuple |
| 4 | `tuple_frequency.py` | Finds the frequency of each element in a tuple |

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
   this folder are simple, direct operations, so none required an extra
   function — logic is written directly for clarity.

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
python tuple_operations.py
python tuple_to_list.py
python list_to_tuple.py
python tuple_frequency.py
```

## Purpose

This folder is meant purely for **interview preparation practice** — tuple
questions test understanding of immutability, built-in tuple methods
(`count`, `index`), and conversions between Python's core sequence types.