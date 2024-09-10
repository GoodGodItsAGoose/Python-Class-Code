import random

#major work in progress, will be stitching together and adding more.
#This is a text-based adventure game

#weapon stats is a work in progress, future use will be for inventory management and fighting baddies
def weaponStats ():
    print('WIP')
    #weapons
    list = ["Sword", "Spear", "Bow", "Dagger", "Rusty Dagger", "Lost Soul's Dagger", "Gnarled Stick", "Long Pole", "Scabanna", "Serrated Knife", "Katana", "Morning Star", "Pike", "Walking Stick"] #explain scabanna
    print(f'{list[0]}')
    print(f'{list[1]}')
    print(f'{list[2]}')
    print(f'{list[3]}')
    print(f'{list[4]}')
    print(f'{list[5]}')
    print(f'{list[6]}')
    print(f'{list[7]}')
    print(f'{list[8]}')
    print(f'{list[9]}')
    print(f'{list[10]}')
    print()
    
    #inventory
    list = ["Aged Note", "Bundle of Rope", "Rations", "Mysterious Crystal", "Stinky Cheese", "Old Vic's Boot", "Stick", "Ranger's Cloak", "Noble's Cloak", "Jester's Hat", "Heart of Darkness", "Soul Lantern", "Raincoat", "Lantern", "Torch", "Hook", "Roll of String", "Tattered Fabric", "Silk", "Leather Flask" "Golden Earl FlowerStone", "King's Gambit", "Score of Keyline Arrows", "Score of Flint Arrows", "Score of Pristine Steel Arrows", "Keystone", "Olive Branch", "Weathered Mossy Rock", "Pebble", "The Usurped King's Tale", "Quill and Ink", "Nightshade Berries", "Kinslit Berries", "Plant Book", "Map", "From the Emerald Crown: Tales of the Unknown", "Keeper's Glory: Folklore Tales from a Time Long Past", "Wooden Boat Model", "Well Key", "Chest Key", "Gate Key", "Stoneridge Tavern Key"]
    print(f'{list[0]}')
    print(f'{list[1]}')
    print(f'{list[2]}')
    print(f'{list[3]}')
    print(f'{list[4]}')
    print(f'{list[5]}')
    print(f'{list[6]}')
    print(f'{list[7]}')
    print(f'{list[8]}')
    print(f'{list[9]}')
    print(f'{list[10]}')
    print(f'{list[11]}')
    print(f'{list[12]}')
    print(f'{list[13]}')
    print(f'{list[14]}')
    print(f'{list[15]}')
    print(f'{list[16]}')
    print(f'{list[17]}')
    print(f'{list[18]}')
    print(f'{list[19]}')
    print(f'{list[20]}')
    print(f'{list[21]}')
    print(f'{list[22]}')
    print(f'{list[23]}')
    print(f'{list[24]}')
    print(f'{list[25]}')
    print(f'{list[26]}')
    print(f'{list[27]}')
    print(f'{list[28]}')
    print(f'{list[29]}')
    print(f'{list[30]}')
    print(f'{list[31]}')
    print(f'{list[32]}')
    print(f'{list[33]}')
    print(f'{list[34]}')
    print(f'{list[35]}')
    print(f'{list[36]}')
    print(f'{list[37]}')
    print(f'{list[38]}')
    print(f'{list[39]}')
    print(f'{list[40]}')
    
#example of what to do with multiple choices

#running the main game
def main ():
    locations = {
        "Will's Glade": {'name': "Will's Glade", 'South': 'Quillin Forest', 'North': 'Quillin Forest', 'East': 'Fortune Path', 'West': 'Quillin Forest', 'item': "Mysterious Crystal" "Aged Note" "Bundle of Rope" "Rusty Dagger", "Rations": '1' "Ration" "Ration" "Ration" },
        'Town Square': {'name': 'Halsford Town Square', 'South': 'Fortune Path', 'North': 'Ivory Forest Trail', 'East': 'Quillin Forest', 'West': 'Hickory Road'}
    }
    
    #The location of the player
    currentLoc = locations["Will's Glade"]
    
    #Commands available to the player, will add more
    commands = [['South', 'North', 'East', 'West'], ['item']]
    
    #The player's inventory
    inventory = []
    
    #continues running on a seperate loop from the main gameplay, to prevent future issues with not running.
    Run = True
    while Run == True:
        introChoice = "Stuff" #1 variable for all entires, goes through here then runs n makes sure they dont request one of the below?
        #Options for opening inventory, showing location, showing items in the location, and showing your rations.
        if introChoice.lower() in "inventory":
            print('Inventory: {}.'.format(inventory, )) #prints the player's inventory
        elif introChoice.lower() in "location":
            print('Location: {}.'.format(currentLoc['name'], )) #prints the name of the location the player is in
        elif introChoice.lower() in "items" or "item":
            print('Items: {}.'.format(currentLoc['item'], )) #lists item in the location
        elif introChoice.lower() in "ration" or "rations":
            #Ration counter
            if currentLoc['Rations'].count('Ration'):
                rationCount = [currentLoc['Rations'].count('Ration')]
            print("Rations {}.".format(rationCount, ))
        elif introChoice.lower() in "option" or "options":
            print("The commands you can enter: /n Location /n Inventory /n Items /n Rations")
            #add player stats, weapons, n other

    def introScene ():
        #player has made a choice?
        isChoice = True
        
        #intro is finished? (might use later)
        introDone = False
        
        #Player entry
        introChoice = ""
        print("You wake up in a glade surrounded by trees, with no landmarks to tell you where you are. You find a bundle near you. ")
        while isChoice == True:
            print("What would you like to do?")
            choice = input("")
            
            #runs through the starting choices for the start of the game
            if choice.lower() in "bundle": #Player chooses to open bundle
                print()
                print("You chose to inspect the bundle.") 
                isChoice = False
                introDone = True #maybe use later?
                introChoice = "bundle"
            elif choice.lower() in 'explore' or 'left' or 'right' or 'foreward' or 'forward' or 'walk': #Player chooses to explore the area
                print()
                print("You choose to explore the glade.")
                print()
                isChoice = False
                introDone = True
                introChoice = "explore"
            elif choice.lower() in 'quit': #player is a poopy and leaves
                print()
                print("End")
                exit()
            else: #if entry is unrecognized
                print()
                print("Please re-enter your choice.")
                isChoice = True
                introDone = False
            
            #if the player chooses to explore, the player can have more acceptable entries (Work in progress)
            if introChoice == "explore":
                print(" In front of you extends further into the glade. Behind you is a dense line of trees. To the left, a berry bush, and to the right, a trail leading into the woods.")
                print("What would you like to do?")
                choice = input()
                tree = False
                berries = False
                trail = False
                moreGlade = False
                # walk off, options are:
                    #go down path
                        #loop back, eyes drawn to bundle
                    #look around at shrubbery (find berries, need a cloth to collect)
                    #collect bundle
                
                #accepted entries for extended exploration
                if trail == False and berries == False and trail == False and moreGlade == False:
                    print()#how go back to previous options? diff function?
                elif choice.lower() in "berries" or "bush" or "left" and berries == False:
                    print()
                elif choice.lower() in "tree" or "behind" or "backward" and tree == False:
                    print()
                elif choice.lower() in "forward" or "foreward" or "continue" and moreGlade == False:
                    print()
                elif choice.lower() in "trail" or "right" and trail == False:
                    print()
                else:
                    print("please re-enter where you would like to go.")
            elif introChoice == "bundle":
                print("You find {}.".format(currentLoc['Item'], ) )
                #options are:
                    #explore, find path you can go down
                    #look at shrubbery (can grab berries)
            else: #goes back through and restarts at the beginning of the journey
                isChoice = True
                
    def chestTest ():
        isChoice = False
        inspect = False # for checking if the player has inspected the lock
        investigate = False #For checking if the player has investigated the board on the barrel
        #add variable for when player has collected key, beforehand, in loop
        
        while isChoice == False:
            print("The porch stairs have fallen through, so you climb up the side. The door is strewn across the deck, almost as if something had ripped it from the hinges and tossed onto the porch. Inside the house, you see a bedframe and a small storage chest that has a lock on it to the left and a makeshift table made of a board set upon a barrel in front of you.")
            print("What do you want to do?")
            choice = input("")
            
            chestKey = False
            
            inventory.index("Chest Key") #make it so when get key then chestKey = True
            #checks if key is in inventory
            for item in inventory:
                if item[inventory]:
                    chestKey = True
                    print('thos works')
            
            #runs through options for going through one of the houses
            if inspect == True and investigate == True: #player is forced back to the path if the player has explored both options.
                    print("You go back to the path.")
                    isChoice = True
            else:
                if choice.lower() in 'lock' or 'chest' or 'left' or 'storage' and inspect == False or chestKey == True: #player investigates lock
                    print("You walk to the chest and look at the lock. It’s covered with rust, so you try rattling it a few times. It doesn’t give. There must be a key in one of these houses that you could use to unlock the chest.")
                    isChoice = False
                    inspect = True
                elif choice.lower() in 'lock' or 'chest' or 'left' or 'storage' and inspect == True and chestKey == False:
                    print("You remember that the lock is rusty but still stable, and that there should be a key inside of one of the other houses.")
                    isChoice = False
                    inspect = True
                elif choice.lower() in 'table' or 'barrel' or 'forward' or 'foreward' and investigate == False: #player investigates table
                    print("You walk to the makeshift table. There is a piece of cloth laid across the middle, with an overturned plate and moldy food on one side.")
                    isChoice = False
                    investigate = True
                elif choice.lower in 'table' or 'barrel' or 'forward' or 'foreward' and investigate == True:
                    print("You've already investigated the table.")
                    isChoice = False
                    investigate = True
                elif choice.lower() in "right": #adding freedom to choose where to go
                    print("You walk to the right, and conk your head straight into the wall.")
                    isChoice = False
                elif choice.lower() in 'back' or 'leave':
                    print("You went back to the path.")
                    isChoice = True
                else:
                    print("Please choose an option")
                    isChoice = False


            """
            HW: Clean up code, make it more readable w/ comments
            
            loop = comment
            
            comments tell you exactly what it is doing
            
            can do 1 comment for a function
            
            make list of optional movements, use said list instead of doing '___ in "yada yada" '
            """
    

if __name__ == "__main__":
    isName = True
    print("Welcome!")
    
    while isName == True:
        
        print("Please enter your name.")
        
        name = input("")
        if name == "":
            isName = True
        elif name == "no" or name == "No" or name == "NO":
            isName = True
        else: 
            print("Good luck out there, " +name+ ".")
            isName = False
            print("Please type 'Options' for a list of options you can choose from.")
            main()
            
        
        
    