def chance(percentage):
    chanceNum = r.randint(1,100)
    if chanceNum < percentage:
        return False
    return True

def between(total, min, max):
    if total <= max and total >= min:
        return True
    return False
