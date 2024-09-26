class DnD_Char_Maker:
    def __init__(
        self, name, age, gender, race, eyeColor, skinColor, hairColor, hairStyle, height, noseShape, lipShape,
        bodyType, favHobbies, favColor, favAesthetic
        ):
        self.name = name
        self.age = age
        self.gender = gender
        self.race = race
        self.eyeColor = eyeColor
        self.skinColor = skinColor
        self.hairColor = hairColor
        self.hairStyle = hairStyle
        self.height = height
        self.noseShape = noseShape
        self.lipShape = lipShape
        self.bodyType = bodyType
        
        
    
    def who_Am_I(self):
        print("I am "+self.name+". I am a "+self.race+". I am "+str(self.age)+" years old. I am a "+self.gender)
        

print("Please enter your character name.")
charName = input("")
print("Please enter your character's age.")
charAge = input("")
print("Please enter your character's gender.")
charGender = input("")
print("Please enter your character's race.")
charRace = input("")
print("Please enter your character's eye color.")
charEyeColor = input("")
print("Please enter your character's skin color.")
charSkinColor = input("")
print("Please enter your character's hair color.")
charHairColor = input("")
print("Please enter your character's hair style.")
charHairStyle = input("")
print("Please enter your character's height.")
charHeight = input("")
print("Please enter your character's nose shape.")
charNoseShape = input("")
print("Please enter your character's lip shape.")
charLipShape = input("")
print("Please enter your character's body type.")
charBodyType = input("")

charOne = DnD_Char_Maker(
    charName, charAge, charGender, charRace, charEyeColor, charSkinColor, charHairColor, charHairStyle,
    charHeight, charNoseShape, charLipShape, charBodyType
)
charOne.who_Am_I()
