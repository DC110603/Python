from abc import ABC,abstractmethod
class MenuItem(ABC):
    @abstractmethod
    def get_price(self):
        pass
class Pizza(MenuItem):
    def __init__(self):
        self.quantity=10
        self.price = 299
    def change_price(self,new):
        self.price=new
    def get_price(self):
        return self.price
class Burger(MenuItem):
    def __init__(self):
        self.quantity=21
        self.price=199
    def get_price(self):
        return self.price
    def change_price(self,new):
        self.price=new
class Drink(MenuItem):
    def __init__(self):
        self.quantity=15
        self.price = 199
    def get_price(self):
        return self.price
    def change_price(self,new):
        self.price=new
class Order:
    def __init__(self):
        self.__l=[]
    def add_item(self,item):
        self.__l.append(item)
    @property
    def get_list(self):
        return self.__l
order1=Order()
order1.add_item(Pizza().quantity)
order1.add_item(Burger().quantity)
order1.add_item(Drink().quantity)
print(order1.get_list)