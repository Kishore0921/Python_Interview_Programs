"""
Problem: Write a program to find keys in a dictionary that have
duplicate (repeated) values.
Example:
    Input: {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
    Output: Keys with duplicate values: ['a', 'c'], ['b', 'e']

Time Complexity: O(n)
Space Complexity: O(n)
"""


def group_keys_by_value(data):
    value_to_keys = {}
    for key, value in data.items():
        value_to_keys.setdefault(value, []).append(key)
    return value_to_keys


data = {}
n = int(input("Enter number of key-value pairs: "))

for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

print(f"Dictionary: {data}")

grouped = group_keys_by_value(data)
duplicates = [keys for keys in grouped.values() if len(keys) > 1]

print(f"Keys with duplicate values: {duplicates}")