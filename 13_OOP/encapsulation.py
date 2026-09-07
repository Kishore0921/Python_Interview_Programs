"""
Topic: Encapsulation
This file demonstrates the different levels of member access in Python
that support encapsulation: public, protected, and private members.
"""


# ======================================================================
# 1. Public Members
# ======================================================================
"""
Problem: Write a program demonstrating public members, which are
accessible from anywhere, both inside and outside the class.
Example:
    Input: account.balance
    Output: 1000

Time Complexity: O(1)
Space Complexity: O(1)
"""


class BankAccountPublic:
    def __init__(self, balance):
        self.balance = balance  # public member


account1 = BankAccountPublic(1000)
print(f"Public balance accessed directly: {account1.balance}")


# ======================================================================
# 2. Protected Members
# ======================================================================
"""
Problem: Write a program demonstrating protected members (prefixed with
a single underscore), which are intended for use within the class and
its subclasses, though still technically accessible from outside.
Example:
    Input: account._balance
    Output: 2000 (accessible, but treated as "internal use" by
            convention)

Time Complexity: O(1)
Space Complexity: O(1)
"""


class BankAccountProtected:
    def __init__(self, balance):
        self._balance = balance  # protected member


class SavingsAccount(BankAccountProtected):
    def show_balance(self):
        print(f"Protected balance accessed in subclass: {self._balance}")


account2 = SavingsAccount(2000)
account2.show_balance()
print(f"Protected balance accessed outside (not recommended): {account2._balance}")


# ======================================================================
# 3. Private Members
# ======================================================================
"""
Problem: Write a program demonstrating private members (prefixed with a
double underscore), which are name-mangled so they cannot be accessed
directly from outside the class.
Example:
    Input: account.get_balance()
    Output: 3000

Time Complexity: O(1)
Space Complexity: O(1)
"""


class BankAccountPrivate:
    def __init__(self, balance):
        self.__balance = balance  # private member

    def get_balance(self):
        return self.__balance


account3 = BankAccountPrivate(3000)
print(f"Private balance accessed via method: {account3.get_balance()}")

try:
    print(account3.__balance)
except AttributeError as e:
    print(f"Error accessing private member directly: {e}")