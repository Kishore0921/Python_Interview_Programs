"""
Problem: Write a program to perform basic operations on a tuple
(access, count, index, concatenation, slicing).
Example:
    Input: (10, 20, 30, 20, 40)
    Output:
        Length: 5
        Count of 20: 2
        Index of 30: 2
        First two elements: (10, 20)
        Concatenated: (10, 20, 30, 20, 40, 100, 200)

Time Complexity: O(n)
Space Complexity: O(n)
"""

numbers = tuple(map(int, input("Enter numbers separated by spaces: ").split()))

print(f"Tuple: {numbers}")
print(f"Length: {len(numbers)}")

value = int(input("Enter a value to count: "))
print(f"Count of {value}: {numbers.count(value)}")

search_value = int(input("Enter a value to find index of: "))
if search_value in numbers:
    print(f"Index of {search_value}: {numbers.index(search_value)}")
else:
    print(f"{search_value} not found in tuple")

print(f"First two elements: {numbers[:2]}")

extra = tuple(map(int, input("Enter numbers to concatenate: ").split()))
print(f"Concatenated: {numbers + extra}")