""""Q2. Design a class Product that:
•	Maintains a base tax rate applicable to all products.
•	Each product has a name and base price.
•	Has a method to compute final price including tax.
•	Can change tax rate for all products using one method.
•	Includes a function to check whether a given price is valid or not (non-negative and realistic).
Demonstrate:
1.	Creating multiple products.
2.	Changing the tax rate.
3.	Showing updated prices and validity checks.
"""
class Product:
    base_tax_rate=12
    def __init__(self,name,base_price):
        if Product.check_validity(base_price):
            self.name=name
            self.base_price=base_price
    def final_price(self):
        tax=self.base_price/Product.base_tax_rate
        return self.base_price+tax
    @classmethod
    def change_tax_rate(cls,new_rate):
        cls.base_tax_rate=new_rate
    @staticmethod
    def check_validity(price):
        if price <= 0:
            return False
        return True

pd1=Product("Laptop",72000)
pd2=Product("I-Phone",92000)
pd3=Product("Shampoo",0) #It Doesn't Create any Object Because the Price is Negative
print(pd1.final_price()) #Prints the Final Price
print(pd2.final_price())#Prints the Final Price
#print(pd3.final_price()) #It will Give an Error Because the Object is not created
Product.change_tax_rate(8) #Changing the Base Tax Rate
print(Product.base_tax_rate) #Prints the Changed base tax rate