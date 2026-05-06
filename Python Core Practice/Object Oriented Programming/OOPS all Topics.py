from abc import ABC, abstractmethod
class Account(ABC):
    def _init_(self, name, balance):
        self.name = name
        self.__balance = balance
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
    @abstractmethod
    def calculate_interest(self):
        pass
    @classmethod
    @abstractmethod
    def change_interest(cls,interest):
        pass
    @staticmethod
    def validate_balance(balance):
        if balance < 0:
            return False
        return True
    def set_balance(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
    def _str_(self):
        return f'{self.name} balance: {self.__balance}'
    def _repr_(self):
        return f'{self.name} balance: {self.__balance}'
class SavingsAccount(Account):
    interest=0.1
    def _init_(self, name, balance):
        super()._init_(name,balance)
    @classmethod
    def change_interest(cls,interest):
        cls.interest=interest
    def deposit(self, amount):
        self.set_balance(amount)
    def withdraw(self, amount):
        if Account.validate_balance(self.get_balance()):
            if self.get_balance()>amount:
                self.set_balance(-amount)
    def calculate_interest(self):
        a=self.get_balance()*self.interest+1000000
        self.set_balance(a)

class CurrentAccount(Account):
    interest=0.05
    def _init_(self, name, balance):
        super()._init_(name,balance)

    def deposit(self, amount):
        self.set_balance(amount)

    def withdraw(self, amount):
        if Account.validate_balance(self.get_balance()):
            if self.get_balance() > amount:
                self.set_balance(-amount)

    def calculate_interest(self):
        a = self.get_balance() * self.interest
        self.set_balance(a)

    @classmethod
    def change_interest(cls, interest):
        cls.interest = interest
class FixedDepositeAccount(Account):


    interest=0.12
    def _init_(self, name, balance):
        super()._init_(name,balance)

    @classmethod
    def change_interest(cls, interest):
        cls.interest = interest

    def deposit(self, amount):
        self.set_balance(amount)

    def withdraw(self, amount):
        if Account.validate_balance(self.get_balance()):
            if self.get_balance() > amount:
                self.set_balance(-amount)

    def calculate_interest(self):
        a = self.get_balance() * self.interest
        self.set_balance(a)

acc1=SavingsAccount("Tauseef", 1000000)
acc2=CurrentAccount("Yashwanth", 100000000)
l=[acc1,acc2]
print(l)
for i in l:
    i.deposit(100000000)
    i.withdraw(1000000)
    i.calculate_interest()
    print(i.get_balance())
print(l)