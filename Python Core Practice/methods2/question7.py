""""Q7. Build an Inventory class that:
•	Tracks the total number of items across all inventories.
•	Each instance maintains its own stock dictionary ({"item": quantity}).
•	Provides a method to add or remove stock.
•	Allows updating a minimum stock threshold globally.
•	Offers a static checker to verify if a stock level is below threshold.
Demonstrate:
1.	Managing multiple inventories.
2.	Adjusting stock threshold.
3.	Using static validation inside the instance logic.
"""
class Inventory:
    di={}
    total_no_of_items=0
    min_stock=20
    def __init__(self,item,quantity):
        if Inventory.check(quantity):
            self.di[item]=quantity
            Inventory.total_no_of_items+=1
    @classmethod
    def add(cls,item,quantity):
        Inventory.di[item]=quantity
    @classmethod
    def remove(cls,item):
        Inventory.di.pop(item)
    @classmethod
    def less_the_qtr(cls,item,rv_qty):
        st=Inventory.di[item]
        fst=st-rv_qty
        Inventory.di[item]=fst
    @classmethod
    def update_min_stock(cls,new_min):
        cls.min_stock=new_min
    @staticmethod
    def check(d):
        if d in Inventory.di:
            return True
        return False
stock=Inventory("soap",60)
stock1=Inventory("Sugar",26)
stock3=Inventory("Milk-Packets",28)
print(Inventory.di)
Inventory.add("SurfExcel",52)
Inventory.remove("soap")
print(Inventory.di)
if Inventory.check("soap"):
    print("In Stock")
else:
    print("Not in Stock")
Inventory.less_the_qtr("Sugar",6) #we can remove the 'N' quantity from the stock
print(Inventory.di["Sugar"])
print(Inventory.total_no_of_items)
print(Inventory.di["Sugar"])
Inventory.increment_quant("Sugar",12)
print(Inventory.di["Sugar"])