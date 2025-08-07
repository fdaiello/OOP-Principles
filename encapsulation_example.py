# Encapsulation Example
# Bundling data and methods that operate on the data within a single unit (class)
# and restricting direct access to some of an object's components.

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Public attribute
        self.__balance = initial_balance      # Private attribute (by convention)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        # Public method to access the private balance
        return self.__balance

# Usage
my_account = BankAccount("Alice Smith", 1000)

print(f"Account holder: {my_account.account_holder}")
print(f"Initial balance: {my_account.get_balance()}")

my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(1500) # This will fail due to insufficient funds

# Attempting to access private attribute directly (not recommended)
# print(my_account.__balance) # This would raise an AttributeError

# Python's name mangling makes it accessible, but still discouraged
print(f"Balance via name mangling (discouraged): {my_account._BankAccount__balance}")


