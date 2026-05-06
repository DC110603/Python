
class A:
    def __init__(self, name, roll_no):
        self.__name=name
        self.__roll_no=roll_no

    @property
    def name(self):
        return self.__name
    @name.setter
    def name (self,new_name):
        passw = int(input())
        if passw == 1234:
            self.__name = new_name
    @property
    def roll_number(self):
        return self.__roll_no
    @roll_number.setter
    def roll_number(self,new_roll):
        passw = int(input())
        if passw == 1234:
            self.__roll_no=new_roll


s1=A("swadeep",69)
s1.name = "swadeepa"
print(s1.name)