import random
from pathlib import Path
from collections import defaultdict
path = Path('text_files/passwordText.txt')
password = path.read_text()
#maybe input numbers for encoding of unlock number? then they put the number in and if it is the correct number, it;ll give out the right numbers,
#but if not then the numbers given wont work?
passwordGenerator = random.randint(100000, 999999) #number generator
#number list for use of running through all 0-9 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#Placeholder
passwordNumbers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
#splits the password number key
num = [int(n) for n in str(passwordGenerator)] #<--- THIS IS THE PASSWORD PICKED APART (picks the password into seperate numbers)
#saves the index of each number in a list
passwordNumbers = [ 
    {i for i, x in enumerate(num) if x == 1},
    {i for i, x in enumerate(num) if x == 2},
    {i for i, x in enumerate(num) if x == 3},
    {i for i, x in enumerate(num) if x == 4},
    {i for i, x in enumerate(num) if x == 5},
    {i for i, x in enumerate(num) if x == 6},
    {i for i, x in enumerate(num) if x == 7},
    {i for i, x in enumerate(num) if x == 8},
    {i for i, x in enumerate(num) if x == 9},
    {i for i, x in enumerate(num) if x == 0},
]#why not like lists? only dicts?


passwordNumbers = list(passwordNumbers)

print(passwordNumbers)
print(passwordGenerator)
print(num)
print(type(num[1]))
#switches list to int
for i in range(0, len(num)):
    num[i] = int(num[i])

#function to add password layers to the thing being encrypted, WIP
def random(n):
    if 1 in n:
        print()
    elif 2 in n:
        print()
    elif 3 in n:
        print()
    elif 4 in n:
        print()
    elif 5 in n:
        print()
    elif 6 in n:
        print()
    elif 7 in n:
        print()
    elif 8 in n:
        print()
    elif 9 in n:
        print()
    elif 0 in n:
        print()
        
#previous test
"""
myList = []
def test(ones, twos, threes):
    for one in ones:
        if one in twos:
            myList.append(one)
            print(one) #if myList[1] == 1 but simpler, trying to get it so if the first number = 1(etc etc) then it does something
            if myList[0] == threes:
                for one in ones:
                    if one == ones:
                        return True
                    elif one != ones:
                        return False
                print()
            elif myList[1] == threes:
                print()
            elif myList[2] == threes:
                print()
            elif myList[3] == threes:
                print()
            elif myList[4] == threes:
                print()
            elif myList[5] == threes:
                print()

test(numbers, num, numbers)
print(myList)
"""
