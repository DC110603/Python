"""7. Create a module containing two classes where one uses composition and another
uses inheritance to reuse code from a base class. Import and demonstrate the
difference between the two approaches"""
from question7.module2 import HasARelationship,CarInheritence
from question7.module1 import Engine
car1=HasARelationship()
car2=CarInheritence()
car1.start()
car1.drive()
car1.stop()
print("*************************")
car2.start()
car2.drive()
car2.stop()