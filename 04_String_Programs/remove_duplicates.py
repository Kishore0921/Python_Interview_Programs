"""
Problem: Write a program to remove duplicate characters from a string
while preserving the original order.
Example:
    Input: "programming"
    Output: "progamin"

Time Complexity: O(n)
Space Complexity: O(n)
"""

text = input("Enter a string: ")
seen = set()
result = []

for ch in text:
    if ch not in seen:
        seen.add(ch)
        result.append(ch)

print(f"String after removing duplicates: {''.join(result)}")