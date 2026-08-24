"""
Problem: Write a program to print the Fibonacci series up to n terms.
Example:
    Input: 7
    Output: 0 1 1 2 3 5 8

Time Complexity: O(n)
Space Complexity: O(1)
"""

n = int(input("Enter number of terms: "))

a, b = 0, 1
series = []

for _ in range(n):
    series.append(a)
    a, b = b, a + b

print("Fibonacci Series:", *series)