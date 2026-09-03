"""
Problem: Write a program demonstrating a function with default argument
values (a function that calculates the price after a discount, with a
default discount rate).
Example:
    Input: price = 100 (discount not provided)
    Output: Price after discount: 90.0

Time Complexity: O(1)
Space Complexity: O(1)
"""


def apply_discount(price, discount=10):
    return price - (price * discount / 100)


price = float(input("Enter price: "))
discount_input = input("Enter discount percent (leave blank for default 10%): ")

if discount_input.strip() == "":
    final_price = apply_discount(price)
else:
    final_price = apply_discount(price, float(discount_input))

print(f"Price after discount: {final_price}")