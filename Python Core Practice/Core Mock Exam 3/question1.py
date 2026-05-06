class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.__price=price
        self.quantity=quantity

class Warehouse:
    total_warehouses=0
    def __init__(self):
        self.list=set()
        Warehouse.total_warehouses+=1
    def add_prod(self,other):
        self.list.add(other.name)
    def __len__(self):
        return len(self.list)
    def __contains__(self, item):
        return item in self.list
    def __add__(self, other):
        for i in other.list:
            self.list.add(i)
        return self.list




prod1=Product("Icecream",30,122)
prod2=Product("Cool Drinks",20,132)
prod3=Product("Chocolates",35,321)
prod4=Product("Milkshakes",40,32)
warehouse1=Warehouse()
warehouse1.add_prod(prod1)
warehouse1.add_prod(prod2)
warehouse1.add_prod(prod3)
warehouse2=Warehouse()
warehouse2.add_prod(prod4)
print(warehouse1+warehouse2)

