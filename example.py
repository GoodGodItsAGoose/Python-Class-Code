class DnD_Char_Maker:
    def __init__(self, name, age, gender, race):
        self.name = name
        self.age = age
        self.gender = gender
        self.race = race
    
    def who_Am_I(self):
        print("I am "+self.name+". I am a "+self.race+". I am "+str(self.age)+" years old. I am a "+self.gender)
        
charOne = DnD_Char_Maker("Grunk", 38, "Male", "Orc")

charOne.who_Am_I()