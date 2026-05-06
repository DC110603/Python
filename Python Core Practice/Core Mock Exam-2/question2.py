class Wifi:
    def __init__(self,name,passw):
        self.wifi_name=name
        self.__passw=passw
    @property
    def get_passw(self):
        return self.__passw
    @get_passw.setter
    def get_passw(self,new_pass):
        if new_pass>0:
            self.__passw=new_pass
    def __str__(self):
        return f"wifi name is {self.wifi_name}"
    def __repr__(self):
        return f"wifi name is {self.wifi_name}"



class Building:
    building_name="My-Homes"
    def __init__(self,rooms,floors,lift):
        self.rooms=rooms
        self.floors=floors
        self.lift=lift
    def __str__(self):
        return f"Building_Name is {self.building_name}, Total rooms are {self.rooms}, Total floors are {self.floors}, Lift Access {"Available" if self.lift== True else "Not-Available"}"
    def __repr__(self):
        return f"{self.building_name},{self.floors}, {self.rooms}, {"Available" if self.lift== True else "Not-Available"}"

class Hostel(Building,Wifi):
    def __init__(self, rooms, floors, lift):
        super().__init__(rooms, floors, lift)
        self.rooms = rooms
        self.floors = floors
        self.lift = lift

    def __add__(self, other):
        return self.rooms + other.rooms


obj=Wifi("Airtel-Fiber",969696)
hstl1=Hostel(30,4,True)
hstl2=Hostel(10,1,False)
print(hstl1)
print(hstl2)
print(hstl1 + hstl2)
obj.get_passw = 1234
print(obj.get_passw)

