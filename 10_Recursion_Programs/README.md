# 10_Recursion

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers classic recursion
problems — a topic frequently tested in technical interviews to assess
understanding of base cases, recursive calls, and call-stack behavior.

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `factorial_recursion.py` | Finds the factorial of a number using recursion |
| 2 | `fibonacci_recursion.py` | Prints the Fibonacci series up to n terms using recursion |
| 3 | `sum_recursion.py` | Finds the sum of the first n natural numbers using recursion |
| 4 | `reverse_string_recursion.py` | Reverses a string using recursion |

## Format

Every program follows the same structure so problems are easy to scan and
review:

1. A multi-line docstring at the top of the file containing:
   - **Problem** statement
   - **Example** (Input/Output)
   - **Time Complexity**
   - **Space Complexity**
2. Input/output handling written directly, with the recursive function
   as the core of each file.
3. Since this folder is specifically about **recursion**, every file
   includes a recursive function by definition — that is the concept
   being practiced, unlike other folders where functions are added only
   if the problem logic needs them.

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
python factorial_recursion.py
python fibonacci_recursion.py
python sum_recursion.py
python reverse_string_recursion.py
```

## Purpose

This folder is meant purely for **interview preparation practice** —
recursion is a foundational concept tested heavily in interviews, and
mastering base cases, recursive breakdown of a problem, and reasoning
about time/space complexity (especially call-stack space) is essential
before moving on to more advanced recursive topics like backtracking,
divide-and-conquer, and dynamic programming.

**Note:** `fibonacci_recursion.py` uses plain (non-memoized) recursion,
which is intentionally inefficient (O(2^n)) to illustrate the naive
recursive approach — a common interview follow-up is to discuss
optimizing it with memoization or an iterative approach.