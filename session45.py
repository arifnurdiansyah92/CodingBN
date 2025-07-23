# The parent class with ENCAPSULATED data (__balance)
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance # Private attribute

    def get_balance(self):
        return self.__balance

    def show_type(self):
        print("This is a generic bank account.")

# 1. INHERITANCE: SavingsAccount inherits from Account
class SavingsAccount(Account):
    # 2. POLYMORPHISM: It has its own version of show_type()
    def show_type(self):
        print(f"This is a Savings Account for {self.owner}.")

# Another child class
class CheckingAccount(Account):
    def show_type(self):
        print(f"This is a Checking Account for {self.owner}.")

# Create a list of different account objects
my_accounts = [SavingsAccount("Arif", 10000), CheckingAccount("Bob"), Account("Charlie")]

# The same method call, account.show_type(), does different things!
for account in my_accounts:
    account.show_type()
    print(f"Balance: {account.get_balance()}\n")