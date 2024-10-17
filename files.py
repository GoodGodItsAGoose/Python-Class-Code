from pathlib import Path
import random as r
import json

path = Path('text_files/text.txt')
"""
content = path.read_text()
print(content)
content = path.write_text("gold stick") # can you use it in a different file?(yes, b/c it will update the file permanently, removes and replaces with in ()
content = path.read_text()
print(content)

f=open('text_files/text.txt')
print(f.read())

playerBal = open('text_files/text.txt')
enemyBeat = True
if enemyBeat == True:
    newPlayerBal = playerBal + 1
    playerBal = path.write_text(str(newPlayerBal))
    
blah = open('text_files/text.txt', 'r') #lets program know that you're reading, 'w' shows you're writing

print(blah.read())


# this is the non-lib version
file1 = open('text_files/text.txt', 'a')

file1.write("hahaHA")
file1.close()
file2 = open('text_files/text.txt', 'r')
print(file2.read())

content = "blah blah blah"
content = "more blah blah blah"
content = "i wonder if my code will work"
print(content)
path.write_text(content)
content = path.read_text()
print(content)

path = Path('stuff.json')
lib = Path("stuff.json")
list = [1, 2, 6, 5]
content = json.dumps(list)# dumps takes as a string format
content = path.read_text()
numbers = json.loads(content) ##takes the read_text info and puts it on file in json?
lib.write_text(content)
print(numbers)

"""

path = Path('stuff.json')
def signUp():
    
    username = input("It appears you aren't on file. Please enter the username you would like to save: ")
    
    with open('stuff.json', 'r') as f:
        jsonData = json.load(f)
        jsonData["user"] = jsonData, username
        
    with open('stuff.json', 'w') as f:
        json.dumps(jsonData)

    print(f"We'll remember you when you come back, {username}")
    
print("Hello! If you are a returning player, please enter your username.")
playerInput = input("")

stuff = path.read_text()
if playerInput in stuff:
    print(f"Welcome back, {playerInput}")
else:
    signUp()