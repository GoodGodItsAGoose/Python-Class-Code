import random
thisVariable = 1
class charInfo (object):
    def charInfo_Save (self):
        charName = "n/a"
        charRace = "0"
        charClass = "0"

class defs (object):
    Info_Text = "N/A"
    def Dwarf ():
        charInfo(charRace = "Dwarf")
        defs.Info_Text = "enterinfo"
    def Elf ():
        charInfo(charRace = "Elf")
        defs.Info_Text = "enterinfo"
    def Halfling ():
        charInfo(charRace = "Halfling")
        defs.Info_Text = "enterinfo"
        print()
    def Human ():
        charInfo(charRace = "Human")
        defs.Info_Text = "enterinfo"
        print()
    def Dragonborn ():
        charInfo(charRace = "Dragonborn")
        defs.Info_Text = "enterinfo"
        print()
    def Gnome ():
        charInfo(charRace = "Gnome")
        defs.Info_Text = "enterinfo"
        print()
    def Half_Elf ():
        charInfo(charRace = "Half Elf")
        defs.Info_Text = "enterinfo"
        print()
    def Half_Orc ():
        charInfo(charRace = "Half Orc")
        defs.Info_Text = "enterinfo"
        print()
    def Tiefling ():
        charInfo(charRace = "Tiefling")
        defs.Info_Text = "enterinfo"
        print()
        
    def Barbarian ():
        charInfo(charClass = "Barbarian")
    def Bard ():
        charInfo(charClass = "Bard")
    def Cleric ():
        print()
    def Druid ():
        print()
    def Fighter ():
        print()
    def Monk ():
        print()
    def Paladin ():
        print()
    def Ranger ():
        print()
    def Rogue ():
        print()
    def Sorcerer ():
        print()
    def Warlock ():
        print()
    def Wizard ():
        print()
        
class charStart (object):
    def charBeginning ():
        charInfo(charName = input("What would you like to name your character?: "))
    def charClassSelect ():
        
        print (random.randint(1, 16))
        list = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
        charClassChoice = random.randint(1, 16)
        for charClassChoice in list:
            if charClassChoice == 1:
                print(f'{list[0]}')
            elif charClassChoice == 2:
                print(f'{list[1]}')
            elif charClassChoice == 3:
                print(f'{list[2]}')
            elif charClassChoice == 4:
                print(f'{list[3]}')
            elif charClassChoice == 5:
                print(f'{list[4]}')
            elif charClassChoice == 6:
                print(f'{list[5]}')
            elif charClassChoice == 7:
                print(f'{list[6]}')
            elif charClassChoice == 8:
                print(f'{list[7]}')
            elif charClassChoice == 9:
                print(f'{list[8]}')
            elif charClassChoice == 10:
                print(f'{list[9]}')
            elif charClassChoice == 11:
                print(f'{list[10]}')
            elif charClassChoice == 12:
                print(f'{list[11]}')
            elif charClassChoice == 13:
                print(f'{list[12]}')
            elif charClassChoice == 14:
                print(f'{list[13]}')
                
                