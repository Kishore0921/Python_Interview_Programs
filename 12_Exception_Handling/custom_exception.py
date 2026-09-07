"""
Problem: Write a program demonstrating a custom exception class (raise
an error if a withdrawal amount exceeds the available balance).
Example:
    Input: balance = 500, withdraw_amount = 700
    Output: Error: Insufficient balance. Cannot withdraw 700 from 500.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        message = f"Insufficient balance. Cannot withdraw {amount} from {balance}."
        super().__init__(message)


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount


balance = float(input("Enter current balance: "))
amount = float(input("Enter amount to withdraw: "))

try:
    new_balance = withdraw(balance, amount)
    print(f"Withdrawal successful. New balance: {new_balance}")
except InsufficientBalanceError as e:
    print(f"Error: {e}")