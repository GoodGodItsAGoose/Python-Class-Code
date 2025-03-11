import random
import info as i

# change damage amount to vary

def dungeonRun():
    enemy = {
        "undead": {"health": random.randint(23,30), "damage": random.randint(2,5), "dodge chance": 13, "double hit chance": 3, "chance drops": random.randint(1,3), "chance": 16},
        "bandit": {"health": random.randint(17, 25), "damage": random.randint(4,7), "dodge chance": random.randint(10,23), "double hit chance": random.randint(12,17), "chance drops": random.randint(1,3), "chance": 30}, 
        "snake": {"health": random.randint(7,15), "damage": random.randint(1,3), "dodge chance": 35, "double hit chance": 18, "chance drops": random.randint(1,2), "chance": 45},
        "undead guard": {"health": random.randint(27,35), "damage": random.randint(6,11), "dodge chance": 17, "double hit chance": random.randint(11,15), "chance drops": random.randint(1,3), "chance": 57},
        "giant spider": {"health": random.randint(13,20), "damage": random.randint(3,6), "dodge chance": random.randint(24,34), "double hit chance": random.randint(11,18), "chance drops": random.randint(1,3), "chance": 68},
        "giant armored spider": {"health": random.randint(17,26), "damage": random.randint(3,7), "dodge chance": random.randint(19,31), "double hit chance": random.randint(11,16), "chance drops": random.randint(1,3), "chance": 77},
        "goblin": {"health": random.randint(13,17), "damage": random.randint(2,5), "dodge chance": random.randint(13,23), "double hit chance": random.randint(13,16), "chance drops": random.randint(1,2), "chance": 90},
        "wizard": {"health": random.randint(36,44), "damage": random.randint(7,14), "dodge chance": random.randint(13,16), "double hit chance": random.randint(11,15), "chance drops": random.randint(1,3), "chance": 97},
        "King's Guard": {"health": random.randint(45,53), "damage": random.randint(13,17), "dodge chance": random.randint(3,7), "double hit chance": random.randint(11,15), "chance drops": random.randint(1,3), "chance": 100},
    }
    baddie = random.randint(1, 100)



    if i.between(baddie, 1, enemy["undead"]["chance"]) ==  True:
        baddieOne = enemy["undead"]
        baddieName = "Zombie"
        drops = 1
    elif i.between(baddie, enemy["undead"]["chance"]+1, enemy["bandit"]['chance']) == True:
        baddieOne = enemy["bandit"]
        baddieName = "Bandit"
        drops =  2
    elif i.between(baddie, enemy["bandit"]["chance"]+1, enemy["snake"]['chance']) == True:
        baddieOne = enemy["snake"]
        baddieName = "Snake"
        drops = 1
    elif i.between(baddie, enemy["snake"]["chance"]+1, enemy["undead guard"]['chance']) == True:
        baddieOne = enemy["undead guard"]
        baddieName = "Undead Guard"
        drops = 3
    elif i.between(baddie, enemy["undead guard"]["chance"]+1, enemy["giant spider"]['chance']) == True:
        baddieOne = enemy["giant spider"]
        baddieName = "Giant Spider"
        drops = 2
    elif i.between(baddie, enemy["giant spider"]["chance"]+1, enemy["giant armored spider"]['chance']) == True:
        baddieOne = enemy["giant armored spider"]
        baddieName = "Giant Armored Spider"
        drops = 3
    elif i.between(baddie, enemy["giant armored spider"]["chance"]+1, enemy["goblin"]['chance']) == True:
        baddieOne = enemy["goblin"]
        baddieName = "Goblin"
        drops = 2
    elif i.between(baddie, enemy["goblin"]["chance"]+1, enemy["wizard"]['chance']) == True:
        baddieOne = enemy["wizard"]
        baddieName = "Wizard"
        drops = 3
    elif i.between(baddie, enemy["wizard"]["chance"]+1, enemy["King's Guard"]['chance']) == True:
        baddieOne = enemy["King's Guard"]
        baddieName = "King's Guard"
        drops = 4

    print(f"You came across a {baddieName}!")

    dungeonGoing = True
    while dungeonGoing == True:
        def potionChecker(ones, twos):
            if twos > 0:
                twos -=  1
                print(f"You drank 1 {ones}! You have {twos} {ones}s left!")
                return twos
            else: 
                print(f"You're out of {ones}s!")
        
        def potionOut(potionName):
            if i.playerPotions[potionName] == 0:
                return False
            return True
        
        def enemyAttack(b):
            dodgeChance = random.randint(1,100)
            if dodgeChance <= 31 + b:
                print(f"The {baddieName} swung at you, but you dodged!")
            else:
                if i.playerHealth['hp'] > 0 and baddieOne['health'] > 0:
                    i.playerHealth["hp"] -= baddieOne["damage"]
                    if i.playerHealth['hp'] <= 0:
                        i.playerHealth['hp'] = 0
                        print(f"The {baddieName} hit you for {baddieOne['damage']} hp! You died!")
                        i.playerHealth['hp'] = 40
                        exit()
                    else:
                        print(f"The {baddieName} hit you for {baddieOne['damage']} hp! You have {i.playerHealth['hp']} hp left!")
        
        def playerAttack(a):
            dodgeChance = random.randint(1,100)
            if dodgeChance <= baddieOne['dodge chance']:
                print(f'You swung at the {baddieName}, but it dodged! It has {baddieOne['health']} hp left!')
            else:
                if i.playerHealth['hp'] > 0 and baddieOne['health'] > 0:
                    baddieOne['health'] -= i.playerDamage['damage'] + a
                    if baddieOne['health'] <= 0:
                        baddieOne['health'] = 0
                        drop = i.findAPotion(drops)
                        print(f'You killed the {baddieName}! You got {drop}!')
                        i.playerHealth['hp'] = 40
                        dungeonRun()
                    else:
                        print(f"You hit the {baddieName} for {i.playerDamage['damage']} hp! It now has {baddieOne['health']} hp left!")

        def restoreHealth():
            if i.playerHealth['hp'] <= 15:
                print("Would you like to drink a health potion?")
                playerChoice = input("")
                if "yes" or "y" in playerChoice.lower():
                    restor = random.randint(5,15)
                    if restor >= 13:
                        restor += random.randint(0,5)
                    i.playerHealth['hp'] += restor
                    print(f"You restored {restor} hp! You now have {i.playerHealth['hp']} hp!")
                    i.playerPotions['restoration'] = potionChecker("Restoration Potion", i.playerPotions['restoration'])

        def dungeonCheckIn():
            print("What would you like to do? You can drink a potion or attack.")
            playerChoice = input("")
            i.playerBoosts["damage up"] = 0
            i.playerBoosts["dodge up"] = 0
            if "drink" in str(playerChoice).lower(): #wont allow u to attack
                print(f"You have {i.playerPotions["damage"]} Damage Up potions, {i.playerPotions["dodge"]} Dodge Chance Up potions, and {i.playerPotions["restoration"]} Restoration potions.")   
                print("Which potion would you like to drink? Note that boosting potions last for 1 attack.")
                playerChoice = input("")
                
                if "damage" in playerChoice.lower():
                    if potionOut(i.potionNamesReal[0]) == True:
                        i.playerBoosts["damage up"] = random.randint(3,6)
                        print("You boosted your damage by "+str(i.playerBoosts["damage up"])+" points!")
                    i.playerPotions['damage'] = potionChecker("Damage Potion", i.playerPotions['damage'])
                    
                elif "dodge" in playerChoice.lower():
                    if potionOut(i.potionNamesReal[1]) == True:
                        i.playerBoosts["dodge up"] = random.randint(5,9)
                        print("You boosted your dodge stat by "+str(i.playerBoosts["dodge up"])+" points!")
                    i.playerPotions['dodge'] = potionChecker("Dodge Up Potion", i.playerPotions['dodge'])
                    
                elif "restor" in playerChoice.lower(): 
                    if potionOut(i.potionNamesReal[2]) == True:
                        restor = random.randint(5,15)
                        if restor >= 13:
                            restor += random.randint(0,5)
                        i.playerHealth['hp'] += restor
                        print(f"You restored {restor} hp! You now have {i.playerHealth['hp']} hp!")
                    i.playerPotions['restoration'] = potionChecker("Restoration Potion", i.playerPotions['restoration'])
                    
                elif "no" or "n" in playerChoice.lower() or i.playerPotions['damage'] == 0 and i.playerPotions['dodge'] == 0 and i.playerPotions['health up'] and i.playerPotions['restoration'] == 0:
                    print()
                    
            elif "attack" in playerChoice.lower():
                def attackStuff (x, y):
                    print()
                    for _ in range(x):
                        playerAttack(i.playerBoosts["damage up"])
                    for _ in range(y):
                        enemyAttack(i.playerBoosts["dodge up"])
                    print()
                    dungeonCheckIn()
                    
                doubleHit = random.randint(1,100)
                
                restoreHealth()
                
                if i.playerDoubleHitRate["double hit chance"] <= doubleHit and baddieOne["double hit chance"] > doubleHit:
                    attackStuff(2, 1)
                elif baddieOne["double hit chance"] <= doubleHit and i.playerDoubleHitRate["double hit chance"] > doubleHit:
                    attackStuff(1, 2)
                elif baddieOne["double hit chance"] >= doubleHit and i.playerDoubleHitRate["double hit chance"] >= doubleHit:
                    attackStuff(2, 2)
                else:
                    attackStuff(1, 1)
                    
        
        dungeonCheckIn()

                    
dungeonRun()
