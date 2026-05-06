"""create a base class named 'Modes' that contains an instance variable 'modes' (number of speed modes
create two subclasses  'fan' and 'ac'. each subclasss must define its own init method that :
accepts brand and modes as parameters
performance validation on the modes value before assigning it to the instance variable
"""

class Modes:
    def __init__(self,mode):
        self.mode=mode


class Fan(Modes):
    def __init__(self, brand, mode):
        if mode>=3 and mode <=5:
            self.brand=brand
            super().__init__(mode)
    def __str__(self):
        return f"The brand is {self.brand} and mode is {self.mode}." # It Returns in the form of a String
    def __repr__(self):
        return f"{self.brand},{self.mode}"# it Returns in the form of Tuple


class Ac(Modes):
    def __init__(self, brand, mode):
        if mode==3 or mode==4:
            super().__init__(mode)
            self.brand=brand
    def __str__(self):
        return f"The brand is {self.brand} and the mode is {self.mode}"
    def __repr__(self):
        return f"{self.brand},{self.mode}" # it Returns in the form of Tuple

obj=Fan("Havells",3)
obj1=Ac("Voltas",4)
#obj3=Fan("mnnmn",1)
print([obj])
print(obj1)
#print(obj3)