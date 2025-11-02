# Create a BankAccount class with:

# Attributes: account_holder, balance (start with 0)
# Methods:

# deposit(amount) - adds money to balance
# withdraw(amount) - removes money (check if sufficient balance)
# check_balance() - prints current balance

class Bankaccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"deposited{amount} new balance {self.balance}")
        else:
            print("amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"withdrawn{amount} new balance {self.balance}")
            else:
                print(f"Insufficient balance {self.balance}")
        else:
            print("amount must be positive")

    def check_balance(self):
        print(f"Account holder name is {self.account_holder}")
        print(f"current balance is {self.balance}")

account1 = Bankaccount("Alice")
account1.check_balance()

account1.deposit(900)
account1.withdraw(200)
account1.check_balance()