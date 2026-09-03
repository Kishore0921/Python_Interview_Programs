"""
Problem: Write a program demonstrating lambda functions (an anonymous
function that squares a number, and using a lambda with map() to square
a list of numbers).
Example:
    Input: [1, 2, 3, 4]
    Output: [1, 4, 9, 16]

Time Complexity: O(n)
Space Complexity: O(n)
"""

square = lambda x: x * x

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
squared_numbers = list(map(lambda x: x * x, numbers))

print(f"Square of first number: {square(numbers[0])}")
print(f"Squared List: {squared_numbers}")