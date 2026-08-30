"""
Problem: Write a program to find the frequency of each character in a
string.
Example:
    Input: "hello"
    Output:
        h: 1
        e: 1
        l: 2
        o: 1

Time Complexity: O(n)
Space Complexity: O(k), where k is the number of unique characters
"""

text = input("Enter a string: ")
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch, count in frequency.items():
    print(f"{ch}: {count}")