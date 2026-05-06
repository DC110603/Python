"""2. You are developing a payment processing module for an e-commerce website.
The system supports multiple payment methods2, and each payment method follows a
different processing flow.
Create a class named PaymentProcessor that represents the general concept of processing
a payment.
This class must:
• Define a method called process_payment(amount) which represents the act of
charging a user.
• Not assume how the payment is processed, because card payments, UPI payments,
and wallet payments all work differently.
• Contain a helper method used internally for validation, which should not be accessed
directly from outside the class.
Create specialized classes for:
• Credit card payments
• UPI payments
• Wallet payments
Each specialized class must:
• Provide its own version of process_payment().
• Reuse shared validation behavior without duplicating code.
Write client code that:
• Takes a payment object and processes payment without knowing which payment
method is being used.
Explain:
• Why keeping all payment logic in a single function leads to fragile code.
• Why allowing subclasses to redefine behavior makes the system easier to extend.
• Why internal validation methods2 should not be publicly accessible."""

from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    def process_payment(self, amount):
        if self.__validate(amount):
            self._execute_payment(amount)
    def __validate(self, amount):
        if amount <= 0:
            print("Invalid payment amount")
            return False
        return True
    @abstractmethod
    def _execute_payment(self, amount):
        pass

class CreditCardPayment(PaymentProcessor):

    def _execute_payment(self, amount):
        print(f"Processing credit card payment of {amount}")
        print("Connecting to card network...")
        print("Payment successful using Credit Card")

class UPIPayment(PaymentProcessor):

    def _execute_payment(self, amount):
        print(f"Processing UPI payment of {amount}")
        print("Verifying UPI ID...")
        print("Payment successful using UPI")

class WalletPayment(PaymentProcessor):

    def _execute_payment(self, amount):
        print(f"Processing wallet payment of {amount}")
        print("Checking wallet balance...")
        print("Payment successful using Wallet")

def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

card = CreditCardPayment()
upi = UPIPayment()
wallet = WalletPayment()

make_payment(card, 2000)
make_payment(upi, 500)
make_payment(wallet, 300)