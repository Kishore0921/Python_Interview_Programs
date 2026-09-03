# 08_Dictionary_Programs

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers common dictionary-related
problems, including basic operations, frequency counting, sorting, and
merging.

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `dictionary_operations.py` | Demonstrates basic dictionary operations (add, update, remove, membership check) |
| 2 | `frequency_count.py` | Counts the frequency of each word in a sentence |
| 3 | `duplicate_values.py` | Finds keys that share duplicate (repeated) values |
| 4 | `dictionary_sorting.py` | Sorts a dictionary by its keys and by its values |
| 5 | `merge_dictionaries.py` | Merges two dictionaries |

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
   `duplicate_values.py` uses a `group_keys_by_value()` helper since
   grouping logic is a distinct, reusable step separate from finding the
   duplicates. Simpler problems are solved directly without extra
   functions.

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
python dictionary_operations.py
python frequency_count.py
python duplicate_values.py
python dictionary_sorting.py
python merge_dictionaries.py
```

## Purpose

This folder is meant purely for **interview preparation practice** —
dictionary questions test understanding of hashing, key-value lookups,
grouping, and sorting — all common building blocks in coding interview
problems.