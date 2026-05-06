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
from abc import ABC,abstractmethod
class PaymentProcessor(ABC):
    pass
class Credit_card_payments(PaymentProcessor):
    pass
class UPI_payments(PaymentProcessor):
    pass
class Wallet_payments(PaymentProcessor):
    pass
