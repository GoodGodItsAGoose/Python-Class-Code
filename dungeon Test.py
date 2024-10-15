import random

enemy = {
    "undead": {"health": random.randint(23,30), "damage": random.randint(2,5), "dodge chance": 13, "double hit chance": 3, "drops": random.randint(1,3), "chance drops": random.randint(1,3)},
    "bandit": {"health": random.randint(17, 25), "damage": random.randint(4,7), "dodge chance": random.randint(10,23), "double hit chance": random.randint(12,17), "drops": random.randint(2,4), "chance drops": random.randint(1,3)}, 
    "snake": {"health": random.randint(7,15), "damage": random.randint(1,3), "dodge chance": 35, "double hit chance": 18, "drops": random.randint(1,2), "chance drops": random.randint(1,2)},
    "undead guard": {"health": random.randint(27,35), "damage": random.randint(6,11), "dodge chance": 17, "double hit chance": random.randint(11,15), "drops": random.randint(4,6), "chance drops": random.randint(1,3)},
    "giant spider": {"health": random.randint(13,20), "damage": random.randint(3,6), "dodge chance": random.randint(24,34), "double hit chance": random.randint(11,18), "drops": random.randint(2,4), "chance drops": random.randint(1,3)},
    "giant armored spider": {"health": random.randint(17,26), "damage": random.randint(3,7), "dodge chance": random.randint(19,31), "double hit chance": random.randint(11,16), "drops": random.randint(2,5), "chance drops": random.randint(1,3)},
    "goblin": {"health": random.randint(13,17), "damage": random.randint(2,5), "dodge chance": random.randint(13,23), "double hit chance": random.randint(13,16), "drops": random.randint(1,3), "chance drops": random.randint(1,2)},
    "wizard": {"health": random.randint(36,44), "damage": random.randint(7,14), "dodge chance": random.randint(13,16), "double hit chance": random.randint(11,15), "drops": random.randint(5,7), "chance drops": random.randint(1,3)},
    "King's Guard": {"health": random.randint(45,53), "damage": random.randint(13,17), "dodge chance": random.randint(3,7), "double hit chance": random.randint(11,15), "drops": random.randint(7,9), "chance drops": random.randint(1,3)},
}

#player statistics
playerStats = {
    "stats": {"hp": 40, "damage": random.randint(4,6), "dodge chance": 20, "double hit chance": 16},
    "used weapon": {"hand"},
    "stored weapons":{"hand"},
    "money": {"coins": 0},
    "potions": {"damage": 1000, "dodge": 325, "health up": 44610, "restoration": 3}
}

weapons = {
    "Dagger": {"damage": 4, "speed": 7, "durablity": 7, "special": 1},
    "Iron Sword": {"damage": 6, "speed": 3, "durability": 16, "special": 3},
    "Katana": {"damage": 5, "speed": 6, "durability": 14, "special": 4},
    "Lead Pike": {"damage": 5, "speed": 3, "durability": 11, "special": 2},
    "Staff": {'damage': 3, 'speed': 6, 'durability': 9, 'special': 5},
    "Rapier": {'damage': 6, 'speed': 5, 'durability': 11, 'special': 4},
    "none": {"damage": 0, "speed": 0, "durability": 99999999999, "special": 1}
}
weaponNames = ["Dagger", "Iron Sword", "Katana", "Lead Pike", "Staff", "Rapier"]
weaponNamesLower = ["dagger", "sword", 'katana', 'pike', 'staff', 'rapier']
potionNames = ["Damage Up Potion", "Dodge Up Potion", "Health Up Potion", "Restoration Potion"]
potionCosts = [5, 4, 8, 5]
weaponCosts = [10, 25, 30, 20, 15, 35]

baddie = random.randint(1, 9)

if baddie == 1:
    baddieOne = enemy["undead"]
    baddieName = "Zombie"
elif baddie == 2:
    baddieOne = enemy["bandit"]
    baddieName = "Bandit"
elif baddie == 3:
    baddieOne = enemy["snake"]
    baddieName = "Snake"
elif baddie == 4:
    baddieOne = enemy["undead guard"]
    baddieName = "Undead Guard"
elif baddie == 5:
    baddieOne = enemy["giant spider"]
    baddieName = "Giant Spider"
elif baddie == 6:
    baddieOne = enemy["giant armored spider"]
    baddieName = "Giant Armored Spider"
elif baddie == 7:
    baddieOne = enemy["goblin"]
    baddieName = "Goblin"
elif baddie == 8:
    baddieOne = enemy["wizard"]
    baddieName = "Wizard"
elif baddie == 9:
    baddieOne = enemy["King's Guard"]
    baddieName = "King's Guard"

playerHealth = playerStats["stats"]
playerDamage = playerStats["stats"]
playerDodge = playerStats["stats"]
playerDoubleHitRate = playerStats["stats"]
playerPotions = playerStats["potions"]

yes = ["yes" or "yep" or "yup" or "okay" or "sure" or "y"]
no = ["no" , "back" , "leave" , "exit" , "n", "none"]

def dungeon():
    print("u did a dungeon")

damageBoost = 0
dodgeBoost = 0
weaponsChosen = [random.randint(1,2), random.randint(3,4), random.randint(5,6)]
potionChoice = random.randint(1,3)
def weaponChecker(x, y):
    if weaponsChosen[x] == y:
        return y - 1
    else:
        return y
        
w1 = weaponChecker(0, 1)
w2 = weaponChecker(1, 3)
w3 = weaponChecker(2, 5)
print(w3)

def buyFunc(x, price):
    print(f'You wanted to buy the {x}, correct?')
    playerChoice = input("")
    if str(yes) in playerChoice.lower():
        print(f"Alright. That'll be {price} coins.")
        print("You hand over the coins.")
        playerStats["stored weapons"] == playerStats["stored weapons"], weapons[x]
        # if playerStats["stored weapons"] and playerStats["used weapon"] == "hand":
        #   pass
        # else:
        #   print("Would you like to equip a weapon?")
    elif str(no) in playerChoice.lower():
        print("alright.")
        shop()
    else:
        print("Please re-enter choice.")
        buyFunc(x, price)
        
def shop():
    print(f"Welcome to the shop. Right now we have {weaponNames[w1]}s, {weaponNames[w2]}s, {weaponNames[w3]}s, {potionNames[potionChoice]}s and {potionNames[3]}s for sale.")
    print("Which would you like to buy?")
    playerChoice = input("")
    if str(no) in playerChoice.lower():
        print("Alright. Good day to you.")
        #go back to the main menu
    elif weaponNames[w1].lower() in playerChoice.lower():
        buyFunc(weaponNames[w1], weaponCosts[w1])
    elif weaponNames[w2].lower in playerChoice.lower():
        buyFunc(weaponNames[w2], weaponCosts[w2])
    elif weaponNames[w2].lower in playerChoice.lower():
        buyFunc(weaponNames[w3], weaponCosts[w3])
    elif potionNames[potionChoice].lower() in playerChoice.lower():
        buyFunc(potionNames[potionChoice], potionCosts[potionChoice])

        
def dungeonRun():
    dungeonGoing = True
    while dungeonGoing == True:
        def potionChecker(ones, twos):
            if twos > 0:
                twos -=  1
                print(f"You drank 1 {ones}! You have {twos} {ones}s left!")
                return twos
            else: print(f"You're out of {ones}s!")
        
        def enemyAttack(b):
            dodgeChance = random.randint(1,100)
            if dodgeChance <= 31 + b:
                print(f"The {baddieName} swung at you, but you dodged!")
            else:
                if playerHealth['hp'] > 0 and baddieOne['health'] > 0:
                    playerHealth["hp"] -= baddieOne["damage"]
                    if playerHealth['hp'] <= 0:
                        playerHealth['hp'] = 0
                        print(f"The {baddieName} hit you for {baddieOne['damage']} hp! You died!")
                        playerHealth['hp'] = 40
                        dungeonGoing = False
                        exit()
                    else:
                        print(f"The {baddieName} hit you for {baddieOne['damage']} hp! You have {playerHealth['hp']} hp left!")
        
        def playerAttack(a):
            dodgeChance = random.randint(1,100)
            if dodgeChance <= baddieOne['dodge chance']:
                print(f'You swung at the {baddieName}, but it dodged! It has {baddieOne['health']} hp left!')
            else:
                if playerHealth['hp'] > 0 and baddieOne['health'] > 0:
                    baddieOne['health'] -= playerDamage['damage'] + a
                    if baddieOne['health'] <= 0:
                        baddieOne['health'] = 0
                        print(f'You killed the {baddieName}! You got {baddieOne['drops']} gold coins!')
                        playerHealth['hp'] = 40
                        dungeonGoing = False
                        exit()
                    else:
                        print(f"You hit the {baddieName} for {playerDamage['damage']} hp! It now has {baddieOne['health']} hp left!")

        def restoreHealth():
            if playerHealth['hp'] <= 15:
                print("Would you like to drink a health potion?")
                playerChoice = input("")
                if str(yes) in playerChoice.lower():
                    restor = random.randint(5,15)
                    playerHealth['hp'] += restor
                    print(f"You restored {restor} hp! You now have {playerHealth['hp']} hp!")

        def dungeonCheckIn():
            print("What would you like to do?")
            playerChoice = input("")
            if ("health" or "drink") or (("potion" or "hp") or ("dodge" or "restor")) in str(playerChoice).lower(): #wont allow u to attack
                print(f"You have {playerPotions["damage"]} Damage Up potions, {playerPotions["dodge"]} Dodge Chance Up potions, {playerPotions["health up"]} Health Up potions, and {playerPotions["restoration"]} Restoration potions.")   
                print("Which potion would you like to drink?")
                playerChoice = input("")
                if "damage" in playerChoice.lower():
                    damageBoost = random.randint(3,6)
                    print("You boosted your damage by "+str(damageBoost)+" points!")
                    playerPotions['damage'] = potionChecker("Damage Potion", playerPotions['damage'])
                elif "dodge" in playerChoice.lower():
                    dodgeBoost = random.randint(5,9)
                    print("You boosted your dodge stat by "+str(dodgeBoost)+" points!")
                    playerPotions['dodge'] = potionChecker("Dodge Up Potion", playerPotions['dodge'])
                elif "health" in playerChoice.lower() and "restore" not in playerChoice.lower():
                    healthBoost = random.randint(5, 15)
                    if healthBoost >= 13:
                        healthBoost += random.randint(0,10)
                    print("You boosted your health by "+str(healthBoost)+" points!")
                    playerHealth['hp'] += healthBoost
                    playerPotions['health up'] = potionChecker("Health Up Potion", playerPotions['health up'])
                elif "restoration" in playerChoice.lower(): 
                    playerPotions['restoration'] = potionChecker("Restoration Potion", playerPotions['restoration'])
                elif str(no) in playerChoice.lower() or playerPotions['damage'] == 0 and playerPotions['dodge'] == 0 and playerPotions['health up'] and playerPotions['restoration'] == 0:
                    print()
            elif "attack" in playerChoice.lower():
                def attackStuff (x, y):
                    print()
                    for _ in range(x):
                        playerAttack(damageBoost)
                    for _ in 1:
                        enemyAttack(dodgeBoost)
                    print()
                    dungeonCheckIn()
                doubleHit = random.randint(1,100)
                print(doubleHit)
                print(playerDoubleHitRate["double hit chance"])
                print(baddieOne['double hit chance'])
                restoreHealth()
                if playerDoubleHitRate["double hit chance"] <= doubleHit and baddieOne["double hit chance"] > doubleHit:
                    attackStuff(2, 1)
                elif baddieOne["double hit chance"] <= doubleHit and playerDoubleHitRate["double hit chance"] > doubleHit:
                    attackStuff(1, 2)
                elif baddieOne["double hit chance"] >= doubleHit and playerDoubleHitRate["double hit chance"] >= doubleHit:
                    attackStuff(2, 2)
                else:
                    attackStuff(1, 1)
                    
        
        dungeonCheckIn()
                
dungeonRun()