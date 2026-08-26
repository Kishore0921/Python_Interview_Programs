"""
Problem: Write a program to print an alphabet pattern (each row containing
letters from A up to the current row's letter).
Example:
    Input: 4
    Output:
        A
        A B
        A B C
        A B C D

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()


"""Consecutive alphabet pattern"""

n = int(input("Enter number of rows: "))

# Start with the ASCII value of 'A' (65)
ascii_val = 65

for i in range(1, n + 1):
    for j in range(1, i + 1):
        # Convert the ASCII number to its alphabet character
        print(chr(ascii_val), end=" ")
        ascii_val += 1  # Move to the next letter
    print()  # Move to the next line after each row
