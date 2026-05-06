from module1 import Engine
class CarInheritence(Engine):
    def drive(self):
        print("Car is Driving")


class HasARelationship(Engine):
    def __init__(self):
        self.engine=Engine()
    def drive(self):
        print("Car id Driving")
