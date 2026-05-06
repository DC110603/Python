"""6. Create a class in a module that uses private attributes and @property /
@setter decorators. Import the class into another module and show how
encapsulation protects the data while still allowing controlled access."""

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    @property
    def getbalance(self):
        return self.__balance
    @getbalance.setter
    def getbalance(self,password):
        if password==1234:
            e=int(input("Enter New Balance: "))
            self.__balance=e
        else:
            print("enter correct password")
    def __str__(self):
        return f"Name: {self.name}"