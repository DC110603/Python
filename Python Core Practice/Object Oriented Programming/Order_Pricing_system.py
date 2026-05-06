"""You are designing an order pricing system.
An order’s final price depends on:
• Base price
• Discounts
• Taxes
Design separate classes that:
• Each handle exactly one responsibility.
• Can be combined  to compute the final price.
Create a final order class that:
• Inherits behavior from multiple pricing-related classes.
• Clearly demonstrates how Python decides which method to execute when multiple
classes define the same method.
Explain:
• How Python determines execution order.
• Why careless multiple inheritance can introduce bugs.
• Why this pattern should be used sparingly. """

class B_price:
    def __init__(self,b_price):
        self.b_price=b_price

class Discount:
    def __init__(self, perc):
        self.perc=perc

class Taxes:
    def __init__(self, rate):
        self.rate=rate

class Order(B_price,Discount,Taxes):
    def __init__(self, b_price, perc, rate):
        B_price.__init__(self,b_price)
        Discount.__init__(self,perc)
        Taxes.__init__(self,rate)

    def calculate_final_price(self):
        total_price_after_tax=self.b_price+(self.b_price*self.rate)
        return total_price_after_tax-(total_price_after_tax*self.perc)

order1=Order(899,0.08,0.12)
print(order1.calculate_final_price())
