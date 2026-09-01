"""
Problem: Write a program to perform basic operations on a set
(add, remove, membership check, length).
Example:
    Input: {10, 20, 30}
    Output:
        After adding 40: {10, 20, 30, 40}
        After removing 20: {10, 30, 40}
        Is 30 present: True
        Length: 3

Time Complexity: O(1) average per operation
Space Complexity: O(n)
"""

numbers = set(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Set: {numbers}")

add_value = int(input("Enter a value to add: "))
numbers.add(add_value)
print(f"After adding {add_value}: {numbers}")

remove_value = int(input("Enter a value to remove: "))
numbers.discard(remove_value)
print(f"After removing {remove_value}: {numbers}")

check_value = int(input("Enter a value to check membership: "))
print(f"Is {check_value} present: {check_value in numbers}")

print(f"Length: {len(numbers)}")