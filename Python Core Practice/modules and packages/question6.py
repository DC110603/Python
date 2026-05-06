"""6. Create a class in a module that uses private attributes and @property /
@setter decorators. Import the class into another module and show how
encapsulation protects the data while still allowing controlled access."""
from question6.question6 import BankAccount
acc1=BankAccount("Deekshith",1000)
#acc1.getbalance=1234
print(acc1.getbalance)