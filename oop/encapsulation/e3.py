# Real-World Example: Complete Encapsulation

class BankAccount:  # Fixed class name
    bank_name = 'my bank'

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner                      # public
        self._account_number = account_number   # protected
        self.__balance = balance                # private
        self.__transaction_history = []         # private - fixed attribute name

    @property
    def balance(self):
        return self.__balance
    
    @property
    def account_number(self):
        return f"****{self._account_number[-4:]}"  # Fixed: use _account_number
    
    @property
    def transactions(self):
        return self.__transaction_history.copy()  # Fixed attribute name
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__add_transaction(f"Deposited ${amount}")  # Fixed method name and string
            return f"Deposited ${amount}. Balance: ${self.__balance}"
        else:
            return 'Invalid deposit amount'
        
    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        elif amount > self.__balance:
            return "Insufficient balance"
        else:
            self.__balance -= amount
            self.__add_transaction(f"Withdrew ${amount}")  # Fixed method name
            return f"Withdrew ${amount}. Balance: ${self.__balance}"
        
    def transfer(self, other_account, amount):
        if amount > self.__balance:
            return "Insufficient balance"
        
        self.__balance -= amount
        other_account.__balance += amount
        self.__add_transaction(f"Transferred ${amount} to {other_account.owner}")
        other_account.__add_transaction(f"Received ${amount} from {self.owner}")
        return f"Transferred ${amount} to {other_account.owner}"
    
    def __add_transaction(self, transaction):  # Fixed method name consistency
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__transaction_history.append(f"{timestamp} - {transaction}")

    def display_statement(self):
        print(f"\n{'='*50}")
        print(f"Account Statement - {self.bank_name}")
        print(f"{'='*50}")
        print(f"Owner: {self.owner}")
        print(f"Account: {self.account_number}")
        print(f"Current Balance: ${self.__balance}")
        print(f"\nTransaction History:")
        for transaction in self.__transaction_history:
            print(f"  {transaction}")
        print(f"{'='*50}\n")

# Test the corrected code
acc1 = BankAccount("Alice", "1234567890", 1000)
acc2 = BankAccount("Bob", "0987654321", 500)

print("\n=== Accessing Data (Encapsulated) ===")
print(f"Alice's balance: ${acc1.balance}")
print(f"Alice's account: {acc1.account_number}")

print("\n=== Operations with Validation ===")
print(acc1.deposit(500))
print(acc1.withdraw(200))
print(acc1.withdraw(5000))  # Insufficient funds
print(acc1.deposit(-100))   # Invalid amount

print("\n=== Transfer Between Accounts ===")
print(acc1.transfer(acc2, 300))

print("\n=== Account Statements ===")
acc1.display_statement()
acc2.display_statement()

print("\n=== Transaction History (Read-only) ===")
history = acc1.transactions
print(f"Alice has {len(history)} transactions")
for transaction in history:
    print(f"  {transaction}")