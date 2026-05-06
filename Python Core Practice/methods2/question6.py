""""Q6. Design a class Vehicle that:
•	Keeps a record of service charge rate common to all vehicles.
•	Each vehicle has a model, kilometers_run, and service history.
•	Has a function to calculate service charge based on km and rate.
•	Provides a method to update the service rate for all vehicles.
•	Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
Demonstrate:
1.	Creating vehicles with different km and models.
2.	Updating the service rate.
3.	Showing charges and eligibility checks.
"""
class Vehicle:
    service_charge_rate=2
    def __init__(self,model,kilometers_run,service_history,age_of_vehicle):
        if Vehicle.check_eligibility(age_of_vehicle):
            self.model=model
            self.kilometers_run=kilometers_run
            self.service_history=service_history
    def service(self):
        self.service_history+=1
    def service_charge(self):
        return self.kilometers_run*Vehicle.service_charge_rate
    @classmethod
    def update_service_rate(cls,new_rate):
        cls.service_charge_rate=new_rate
    @staticmethod
    def check_eligibility(age):
        if age<=15:
            return True
        return False
car1=Vehicle("XUV300",68000,3,4)
car2=Vehicle("Fortuner",140000,9,12)
print(car1.service_charge())
print(car2.service_charge())
Vehicle.update_service_rate(4)
print(car1.service_charge())
print(car2.service_charge())
car3=Vehicle("Alto",300000,16,16) #Object will not create because the age is greater than 15 years



