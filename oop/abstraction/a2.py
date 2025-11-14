# Create an abstract class PaymentMethod with an abstract method process_payment(amount). 
# Implement concrete classes CreditCard, PayPal, and BankTransfer.


from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card):
        self.card = card

    def process_payment(self, amount):
        return f"payment of {amount} is via card{self.card} "
    
class PayPal(PaymentMethod):
    def __init__(self, online_transaction):
        self.online_transaction = online_transaction

    def process_payment(self, amount):
        return f"payment of paypal is {amount} from transaction {self.online_transaction}"
    
class BankTransfer(PaymentMethod):
    def __init__(self, account_transfer):
        self.account_transfer = account_transfer

    def process_payment(self, amount):
        return f"payment of {amount} from the trasnfer {self.account_transfer}"
    

creditcard = CreditCard("dfg")
print(creditcard.process_payment(12012))
paypal = PayPal("abcvsh123")
print(paypal.process_payment(12819))