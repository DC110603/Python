""" Design a banking system with: 
• An abstract base class Account with deposit(), withdraw(), 
calculate_interest(). 
• Subclasses: SavingsAccount, CurrentAccount, FixedDepositAccount. 
• Each account must: 
o Encapsulate balance (private) 
o Provide controlled access through properties 
o Override interest calculation differently 
• Include a static method to validate amount. 
• Include a class method to update bank-wide interest policies. 
Demonstrate: 
• Polymorphic behavior by iterating through all account types 
• Preventing direct access to balance 
• Multiple interest strategies """
from abc import ABC,abstractmethod
class Account(ABC):
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def update_interest(self):
        pass
    @abstractmethod
    def calculate_interest(self):
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
    def get_balance(self,new_balance):
        self.__balance+=new_balance

class SavingsAccount(Account):
    interest=0.02
    def __init__(self, name, balance):
        super().__init__(name, balance)
    def deposit(self,amount):
        if amount>0:
            self.get_balance=amount
    def withdraw(self,amount):
        if amount<=self.get_balance:
            self.get_balance=(-amount)
        else:
            print("Insufficient Balance")
    def calculate_interest(self):
        a=self.get_balance*SavingsAccount.interest
        self.get_balance=a

    @classmethod
    def update_interest(cls, new_interest):
        cls.interest = new_interest

class CurrentAccount(Account):
    interest=0.05
    def __init__(self, name, balance):
        super().__init__(name, balance)
    def deposit(self, amount):
        self.get_balance = amount
    def withdraw(self, amount):
        if amount <= self.get_balance:
            self.get_balance = (-amount)
        else:
            print("Insufficient Balance")
    def calculate_interest(self):
        a = self.get_balance * CurrentAccount.interest
        self.get_balance = a

    @classmethod
    def update_interest(cls, new_interest):
        cls.interest = new_interest

class FixedDepositAccount(Account):
    interest=0.09
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def deposit(self,amount):
        self.get_balance=amount
    def withdraw(self,amount):
        if amount <= self.get_balance:
            self.get_balance = (-amount)
        else:
            print("Insufficient Balance")
    def calculate_interest(self):
        a = self.get_balance * FixedDepositAccount.interest
        self.get_balance = a

    @classmethod
    def update_interest(cls, new_interest):
        cls.interest = new_interest

acc1=SavingsAccount("swadeep",100000)
acc2=FixedDepositAccount("DC",1000000)
acc3=CurrentAccount("KR",500000)
l=[acc1,acc2,acc3]
for i in l:
    i.calculate_interest()
    i.deposit(300000)
    i.withdraw(10000000)
print(acc1.get_balance)
print(acc2.get_balance)
print(acc3.get_balance)
