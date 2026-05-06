""""Q9. Create a class BankAccount with:
•	class variable bank_name
•	instance variables holder and balance
•	instance method deposit(amount)
•	class method change_bank_name(cls, new_name)
•	static method validate_amount(amount) → returns True if amount > 0
Show transactions and how static + class methods work together.
"""
class BankAccount:
    bank_name="State Bank of India"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def validate_amount(amount):
        if amount>0:
            return True
        return False

t1=BankAccount("swadeep",326)
t2=BankAccount("Deekshith",419)
print(t1.balance) #balance before deposit
print(t2.balance) ##balance before deposit
t1.deposit(200)
t2.deposit(300)
print(t1.balance) #balance after deposit
print(t2.balance) #balance after deposit
BankAccount.validate_amount(t1.balance)
BankAccount.validate_amount(t2.balance)
print(BankAccount.bank_name) #bank name before changing
BankAccount.change_bank_name("Kotak Mahindra Bank")
print(BankAccount.bank_name) #bank name after changing