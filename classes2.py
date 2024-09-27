"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sayName(self):
        print(self.name + " is now sitting.")
        print(self.age)
        
dog1 = Dog("james", 7)
dog2 = Dog("Parker", 146)
print(dog1.sayName())
print(dog2.sayName())
"""

class car:
    def __init__(self, name, make, model, year):
        self.name = name
        self.make = make
        self.model = model
        self.year = year
        
    def sayStuff(self):
        print(self.name)
        print(self.make)
        print(self.model)
        print(str(self.year))
        
car1 = car("honda civic", "yapping", "loud noise verison", 2023)
print(car1.sayStuff())