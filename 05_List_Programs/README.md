# 05_List_Programs

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers common list-manipulation
problems that are frequently asked in technical interviews.

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `largest_element.py` | Finds the largest element in a list |
| 2 | `smallest_element.py` | Finds the smallest element in a list |
| 3 | `second_largest.py` | Finds the second largest element in a list |
| 4 | `reverse_list.py` | Reverses a list |
| 5 | `remove_duplicates.py` | Removes duplicate elements, preserving order |
| 6 | `list_sum.py` | Finds the sum of all elements in a list |
| 7 | `list_frequency.py` | Finds the frequency of each element in a list |

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
   this folder are simple single-pass operations, so none required an
   extra function — logic is written directly for clarity.

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
python largest_element.py
python smallest_element.py
python second_largest.py
python reverse_list.py
python remove_duplicates.py
python list_sum.py
python list_frequency.py
```

## Purpose

This folder is meant purely for **interview preparation practice** — list
problems are one of the most common categories in coding interviews,
testing comfort with iteration, tracking running values (min/max), sets,
and dictionaries.