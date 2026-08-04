"""
Problem: Write a program to build a simple calculator that performs
addition, subtraction, multiplication, and division on two numbers.
Example:
    Input: a = 10, b = 5, operation = '+'
    Output: Result: 15

Time Complexity: O(1)
Space Complexity: O(1)
"""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print(f"Result: {a + b}")
elif operation == '-':
    print(f"Result: {a - b}")
elif operation == '*':
    print(f"Result: {a * b}")
elif operation == '/':
    if b == 0:
        print("Error: Division by zero is not allowed")
    else:
        print(f"Result: {a / b}")
else:
    print("Error: Invalid operation. Use +, -, *, or /")