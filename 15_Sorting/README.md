# 15_Sorting

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers classic sorting
algorithms that are among the most frequently asked topics in technical
interviews.

## Contents

| # | File | Description | Time Complexity |
|---|------|-------------|------------------|
| 1 | `bubble_sort.py` | Repeatedly swaps adjacent out-of-order elements | O(n²) |
| 2 | `selection_sort.py` | Repeatedly selects the minimum and places it in position | O(n²) |
| 3 | `insertion_sort.py` | Builds the sorted list one element at a time by insertion | O(n²) |
| 4 | `merge_sort.py` | Divides the list, sorts each half, and merges them | O(n log n) |

## Format

Every program follows the same structure so problems are easy to scan and
review:

1. A multi-line docstring at the top of the file containing:
   - **Problem** statement
   - **Example** (Input/Output)
   - **Time Complexity**
   - **Space Complexity**
2. The sorting logic implemented as a function (e.g. `bubble_sort()`,
   `merge_sort()`), since the algorithm itself is the reusable unit being
   demonstrated — a function is genuinely needed here, unlike trivial
   one-off scripts.
3. `merge_sort.py` additionally uses a small `merge()` helper function,
   since combining two sorted halves is a distinct, reusable step within
   the recursive algorithm.
4. Input/output handling written directly around the function call.

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
python bubble_sort.py
python selection_sort.py
python insertion_sort.py
python merge_sort.py
```

## Purpose

This folder is meant purely for **interview preparation practice** —
sorting algorithms are a cornerstone of coding interviews, testing
understanding of nested loops, in-place swapping, recursion, and
divide-and-conquer, as well as reasoning about time/space trade-offs
between simpler O(n²) algorithms and more efficient O(n log n)
approaches.