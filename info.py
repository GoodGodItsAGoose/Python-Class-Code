import random

"""
OPTIMIZE THE HELL UP

issues:
- fails to start 2/3 times

to add:
- make fighting more immersive
    - Maybe add weapon / other attack messages
- balance enemies and drop rates
"""

#player statistics
playerStats = {
    "stats": {"hp": 40, "damage": random.randint(4,8), "dodge chance": 20, "double hit chance": 16},
    "used weapon": {"hand"},
    "stored weapons":{"hand"},
    "money": {"coins": 0},
    "potions": {"damage": 0, "dodge": 0, "restoration": 5},
    "ups": {"damage up": 0, "dodge up": 0}
}

playerHealth = playerStats["stats"]
playerDamage = playerStats["stats"]
playerDodge = playerStats["stats"]
playerDoubleHitRate = playerStats["stats"]
playerPotions = playerStats["potions"]
playerBoosts = playerStats["ups"]

potionNames = ["Damage Up Potion", "Dodge Up Potion", "Restoration Potion"]
potionNamesReal = ["damage", "dodge", "restoration"]
potionChances = [35, 65, 90, 10]

def chance(percentage):
    chanceNum = random.randint(1,100)
    if chanceNum < percentage:
        return False
    return True

def between(total, min, max):
    if total <= max and total >= min:
        return True
    return False

# out of num of options, each have different percentages of probability of occurring

def findAPotion(chance=1):
    amount = random.randint(1,chance)
    potion_type = random.randint(0,2)
    num = 0
    for _ in range(4):
        if potion_type == num:
            playerPotions[potionNamesReal[potion_type]] += amount
            if amount == 1:
                return f"{amount} {potionNames[potion_type]}"
            elif amount != 1:
                return f"{amount} {potionNames[potion_type]}s"
        num += 1

playerBoosts["damage up"] = 0
playerBoosts["dodge up"] = 0
