# 11_File_Handling

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers common file-handling
operations — reading, writing, appending, and managing files — which are
often tested to check comfort with I/O and the `with` context manager.

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `read_file.py` | Reads and displays the content of a file |
| 2 | `write_file.py` | Writes content to a file (overwrites if it exists) |
| 3 | `append_file.py` | Appends content to the end of a file |
| 4 | `file_operations.py` | Demonstrates multiple file operations together (exists check, write, read, line count, delete) |

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
   `file_operations.py` breaks each operation (`file_exists`,
   `write_to_file`, `read_from_file`, `count_lines`, `delete_file`) into
   its own small function since several distinct operations are
   demonstrated together in one script. The single-purpose scripts
   (`read_file.py`, `write_file.py`, `append_file.py`) are written
   directly without extra functions.

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
python read_file.py
python write_file.py
python append_file.py
python file_operations.py
```

## Purpose

This folder is meant purely for **interview preparation practice** — file
handling questions test comfort with Python's `open()`, the `with`
statement for safe resource handling, exception handling for missing
files, and the `os` module for file-system operations.

**Note:** All scripts use relative file paths, so they will read/write
files in the directory from which the script is run.