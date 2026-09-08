# 14_Searching

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers the two classic
searching algorithms most commonly tested in technical interviews.

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `linear_search.py` | Searches for an element by checking each item one by one |
| 2 | `binary_search.py` | Searches for an element in a sorted list by repeatedly halving the search range |

## Format

Every program follows the same structure so problems are easy to scan and
review:

1. A multi-line docstring at the top of the file containing:
   - **Problem** statement
   - **Example** (Input/Output)
   - **Time Complexity**
   - **Space Complexity**
2. The search logic implemented as a function (`linear_search()`,
   `binary_search()`), since the algorithm itself is the reusable unit
   being demonstrated — a function is genuinely needed here, unlike
   trivial one-off scripts.
3. Input/output handling written directly around the function call.

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
python linear_search.py
python binary_search.py
```

## Purpose

This folder is meant purely for **interview preparation practice** —
searching algorithms are a core interview topic, and understanding the
trade-off between linear search (works on any list, O(n)) and binary
search (requires a sorted list, but O(log n)) is fundamental before
moving on to more advanced algorithm topics.

**Note:** `binary_search.py` assumes the input list is already sorted in
ascending order, as required by the algorithm.