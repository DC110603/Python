""""Q8. Create a HotelRoom class that:
•	Keeps a base price per night (shared).
•	Each room has room_number, nights_booked, and guest_name.
•	Has a method to calculate total bill.
•	Allows updating the base price across all rooms.
•	Provides a static utility to check if a number of nights is valid (e.g., positive integer only).
Demonstrate:
1.	Creating rooms and bookings.
2.	Changing base price.
3.	Checking bill updates and validation.
"""
class HotelRoom:
    per_night=1899
    tax_rate=8
    def __init__(self,room_number,nights_booked,guest_name):
        if HotelRoom.valid(nights_booked):
            self.room_number=room_number
            self.nights_booked=nights_booked
            self.guest_name=guest_name
    def total_bill(self):
        fp=self.nights_booked*HotelRoom.per_night #calculates the base rate for stay for 'n' nights
        fp1=fp/HotelRoom.tax_rate #claculates tax
        return fp+fp1 #returns the base price + tax
    @classmethod
    def update_base_rate(cls,new_rate):
        cls.per_night=new_rate
    @staticmethod
    def valid(no_of_nights):
        return no_of_nights>0 #only allows positive values while creating a object
guest1=HotelRoom(801,3,"Swadeep")
guest2=HotelRoom(802,4,"Deekshith")
guest3=HotelRoom(803,2,"Sai krishna")
print("Bill:",guest1.total_bill())
print("Bill:",guest2.total_bill())
print("Bill:",guest3.total_bill())
HotelRoom.update_base_rate(2099)
print("Base price per night:",HotelRoom.per_night)
print("Bill after updating the base rate:",guest1.total_bill())
print("Bill after updating the base rate:",guest2.total_bill())
print("Bill after updating the base rate:",guest3.total_bill())
