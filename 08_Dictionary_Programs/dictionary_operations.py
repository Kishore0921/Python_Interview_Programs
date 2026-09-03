"""
Problem: Write a program to perform basic operations on a dictionary
(add, update, remove, access, membership check).
Example:
    Input: {"a": 1, "b": 2}
    Output:
        After adding c:3: {'a': 1, 'b': 2, 'c': 3}
        After updating a:10: {'a': 10, 'b': 2, 'c': 3}
        After removing b: {'a': 10, 'c': 3}
        Is 'c' present: True

Time Complexity: O(1) average per operation
Space Complexity: O(n)
"""

data = {}
n = int(input("Enter number of key-value pairs: "))

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

print(f"Dictionary: {data}")

add_key = input("Enter a new key to add: ")
add_value = input("Enter its value: ")
data[add_key] = add_value
print(f"After adding {add_key}:{add_value} -> {data}")

update_key = input("Enter a key to update: ")
update_value = input("Enter new value: ")
if update_key in data:
    data[update_key] = update_value
print(f"After updating {update_key}:{update_value} -> {data}")

remove_key = input("Enter a key to remove: ")
data.pop(remove_key, None)
print(f"After removing {remove_key} -> {data}")

check_key = input("Enter a key to check membership: ")
print(f"Is '{check_key}' present: {check_key in data}")