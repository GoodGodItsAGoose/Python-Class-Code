import random
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

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def describeCar(self):
        print(self.make + " " + self.model + " " + str(self.year))
        
class electricCar(Car):
    def __init__(self, make, model, year):
        super().__init(make, model, year)
        
my_car = electricCar('yeeter', 'of babies', 2024)
print(my_car.describeCar())


#animal, 9/30
class animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type
    
    def getAnimal(self):
        print("this is a "+self.type)
        
    def speak(self):
        print("The animal makes a sound.")
        
class Liger(animal):
    def __init__(self, name, age, type):
        super().__init__(name, age, type)
    
    def speak(self):
        print("The liger makes a sound")
        
        
class Dog(animal):
    def __init__(self, name, age, type):
        super().__init__(name, age, type)
        
    def speak(self): #overrides speak function in parent class
        print("The dog barks.")

liger1 = Liger("Jerry", 46, "Liger v2.01.3-a 1/ new mechanical projectors")
liger1.getAnimal()

dog1 = Dog("hondur", 3, "dog")
print(dog1.speak())

"""
#if ( is earlier in the line and you type another (, then add ) at the end of the line until both amounts are even?

#class that inherits another class

class RPS:
    def __init__(self, rock, paper, scissors):
        self.rock = rock
        self.paper = paper
        self.scissors = scissors
    
    def overEater(self):
        print("hello, I am overeater.")
        
        
        
    
class rock(RPS):
    def __init__(self, rock, paper, scissors):
        super().__init__(rock, paper, scissors)
    
    def roll(self):
        print("The options are "+self.rock+" "+self.paper+" "+self.scissors+".")
        print("What do you chose?")
        playerChoice = input()
        AIChoice = random.randint(1,3)
        if AIChoice == 1:
            print("I chose "+self.rock)
        elif AIChoice == 2:
            print("I chose "+self.paper)
        elif AIChoice == 3:
            print("I chose "+self.scissors)
        
class paper(RPS):
    def __init__(self, rock, paper, scissors):
        super().__init__(rock, paper, scissors)
        
    def roll(self):
        print("The options are "+self.rock+" "+self.paper+" "+self.scissors+".")
        print("What do you chose?")
        playerChoice = input()
        AIChoice = random.randint(1,3)
        if AIChoice == 1:
            print("I chose "+self.rock)
        elif AIChoice == 2:
            print("I chose "+self.paper)
        elif AIChoice == 3:
            print("I chose "+self.scissors)
        
class scissors(RPS):
    def __init__(self, rock, paper, scissors):
        super().__init__(rock, paper, scissors)
        
    def roll(self):
        print("The options are "+self.rock+" "+self.paper+" "+self.scissors+".")
        print("What do you chose?")
        playerChoice = input()
        AIChoice = random.randint(1,3)
        if AIChoice == 1:
            print("I chose "+self.rock)
        elif AIChoice == 2:
            print("I chose "+self.paper)
        elif AIChoice == 3:
            print("I chose "+self.scissors)
        
set1 = scissors("Clam", "Stingray", "Crab")
set1.roll()
