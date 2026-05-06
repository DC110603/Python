"""3. Create:
• Abstract class PaymentMethod with pay(), validate()
• Subclasses: CardPayment, WalletPayment, UPIPayment
• Encapsulate user balance
• Use @property to control reading available funds
• Overload + operator to combine two payment methods2 into “split payment”
• Demonstrate polymorphism through a checkout loop. """
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    @abstractmethod
    def pay(self):
        pass
    @staticmethod
    def validate(amount):
        if amount>0:
            return True
        return False
    @property
    def get_balance(self):
        return self.__balance
    @get_balance.setter
    def get_balance(self,add_balance):
        self.__balance+=add_balance


class CardPayment(PaymentMethod):
    tax=0.03

    def pay(self, amount):
        if super().validate(amount):
            if amount <= self.get_balance:
                a = self.get_balance * self.tax
                self.get_balance = (-amount + a)
            else:
                return f"Insufficient Balance"
        else:
            return f"Enter correct Amount"
class WalletPayment(PaymentMethod):
    tax=0.02

    def pay(self, amount):
        if super().validate(amount):
            if amount <= self.get_balance:
                a = self.get_balance * self.tax
                self.get_balance = (-amount + a)
            else:
                return f"Insufficient Balance"
        else:
            return f"Enter correct Amount"
class UpiPayment(PaymentMethod):
    tax=0.01

    def pay(self, amount):
        if super().validate(amount):
            if amount <= self.get_balance:
                a = self.get_balance * self.tax
                self.get_balance = (-amount + a)
            else:
                return f"Insufficient Balance"
        else:
            return f"Enter correct Amount"
class SplitPayment(PaymentMethod):
    tax=0.02
    def pay(self, amount,acc2):
        if super().validate(amount):
            if amount <= self.get_balance:
                half=amount/2
                a = self.get_balance * self.tax
                self.get_balance = (-half + a)
                acc2.get_balance = (-half + a)
                return None
            else:
                return f"Insufficient Balance"
        else:
            return f"Enter correct Amount"


