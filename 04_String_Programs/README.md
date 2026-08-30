# 04_String_Programs

This folder is part of a personal collection of programs created for **practicing
interview coding problems** in Python. It covers common string-manipulation
problems that are frequently asked in technical interviews.

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `reverse_string.py` | Reverses a given string |
| 2 | `palindrome_string.py` | Checks whether a string is a palindrome |
| 3 | `count_vowels.py` | Counts the number of vowels in a string |
| 4 | `count_characters.py` | Counts the total number of characters in a string |
| 5 | `character_frequency.py` | Finds the frequency of each character in a string |
| 6 | `remove_duplicates.py` | Removes duplicate characters, preserving order |
| 7 | `anagram.py` | Checks whether two strings are anagrams of each other |
| 8 | `word_count.py` | Counts the number of words in a string |

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
   `anagram.py` uses a small `normalize()` helper since the same
   cleaning/sorting logic is applied to both input strings. Simpler
   problems are solved directly without extra functions.

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
python reverse_string.py
python palindrome_string.py
python count_vowels.py
python count_characters.py
python character_frequency.py
python remove_duplicates.py
python anagram.py
python word_count.py
```

## Purpose

This folder is meant purely for **interview preparation practice** — string
problems are a very common category in coding interviews, testing comfort
with iteration, hashing/dictionaries, sets, and basic string methods.