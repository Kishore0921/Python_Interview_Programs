# 09_Function_Programs

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers core function concepts —
definitions, arguments, return values, defaults, keyword arguments, and
lambdas — which are frequently probed in technical interviews.

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `basic_function.py` | Demonstrates a basic function definition and call |
| 2 | `function_arguments.py` | Demonstrates variable-length positional arguments (`*args`) |
| 3 | `return_values.py` | Demonstrates a function returning multiple values |
| 4 | `default_arguments.py` | Demonstrates a function with a default argument value |
| 5 | `keyword_arguments.py` | Demonstrates calling a function with keyword arguments |
| 6 | `lambda_functions.py` | Demonstrates anonymous (lambda) functions |

## Format

Every program follows the same structure so problems are easy to scan and
review:

1. A multi-line docstring at the top of the file containing:
   - **Problem** statement
   - **Example** (Input/Output)
   - **Time Complexity**
   - **Space Complexity**
2. Input/output handling written directly, with the concept being
   demonstrated (the function) as the core of each file.
3. Since this folder specifically covers **function concepts**, every
   file includes a function (or lambda) — that is the point being
   practiced, unlike other folders where functions are added only if
   the problem logic needs them.

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
python basic_function.py
python function_arguments.py
python return_values.py
python default_arguments.py
python keyword_arguments.py
python lambda_functions.py
```

## Purpose

This folder is meant purely for **interview preparation practice** —
understanding functions deeply (arguments, defaults, return values,
keyword calls, and lambdas) is foundational for writing clean, reusable
code and is commonly probed in interviews, especially for Python-specific
roles.