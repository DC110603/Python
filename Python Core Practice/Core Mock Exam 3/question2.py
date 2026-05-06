from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    def __init__(self,user,balance):
        self.user=user
        self.__balance=balance
    @abstractmethod
    def pay(self):
        pass
    def validate(amount):
        if amount>0:
            return True
        return False
    @property
    def get_balance(self):
        return self.__balance

    def __add__(self, other):
        return self.pay(), other.pay()

class CardPayment(PaymentMethod):
    def __init__(self, user, balance):
        super().__init__(user, balance)

    def pay(self):
        if PaymentMethod.validate(self.get_balance):
            return f"Payment Done Using '{self.user}' Card"
        else:
            return f"Incorrect Amount"


class WalletPayment(PaymentMethod):
    def __init__(self, user, balance):
        super().__init__(user, balance)

    def pay(self):
        if PaymentMethod.validate(self.get_balance):
            return f"Payment Done Using '{self.user}' Wallet"
        else:
            return f"Incorrect Amount"
class UPIPayment(PaymentMethod):
    def __init__(self, user, balance):
        super().__init__(user, balance)

    def pay(self):
        if PaymentMethod.validate(self.get_balance):
            return f"Payment Done Using '{self.user}' UPI id"
        else:
            return "Incorrect Amount"

user1=CardPayment("DC",3000)
user2=WalletPayment("Amy",5500)
user3=UPIPayment("Joe",2300)
l=[user1,user2,user3]
for i in l:
    print(i.pay())
print(user1+user2)
