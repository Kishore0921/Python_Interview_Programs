"""
Problem: Write a program to merge two dictionaries. If a key exists in
both, the value from the second dictionary should be used.
Example:
    Input: {"a": 1, "b": 2}, {"b": 20, "c": 3}
    Output: {'a': 1, 'b': 20, 'c': 3}

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

dict1 = {}
n = int(input("Enter number of key-value pairs for first dictionary: "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

dict2 = {}
m = int(input("Enter number of key-value pairs for second dictionary: "))
for _ in range(m):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

merged = {**dict1, **dict2}
print(f"Merged Dictionary: {merged}")