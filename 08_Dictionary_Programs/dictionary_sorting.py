"""
Problem: Write a program to sort a dictionary by its keys and by its
values.
Example:
    Input: {"banana": 3, "apple": 5, "cherry": 1}
    Output:
        Sorted by key: {'apple': 5, 'banana': 3, 'cherry': 1}
        Sorted by value: {'cherry': 1, 'banana': 3, 'apple': 5}

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

data = {}
n = int(input("Enter number of key-value pairs: "))

for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

print(f"Dictionary: {data}")

sorted_by_key = dict(sorted(data.items(), key=lambda item: item[0]))
sorted_by_value = dict(sorted(data.items(), key=lambda item: item[1]))

print(f"Sorted by key: {sorted_by_key}")
print(f"Sorted by value: {sorted_by_value}")