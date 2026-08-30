"""
Problem: Write a program to check whether two strings are anagrams of
each other.
Example:
    Input: "listen", "silent"
    Output: Anagram Strings

Time Complexity: O(n log n), due to sorting
Space Complexity: O(n)
"""


def normalize(text):
    return sorted(text.replace(" ", "").lower())


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if normalize(str1) == normalize(str2):
    print("Anagram Strings")
else:
    print("Not Anagram Strings")