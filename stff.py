from pathlib import Path
import json
path = Path('contact.json')

contactBook = []
contactList = [{
    "name": "",
    "phone number": "",
    "email": "",
    "birthday": "",
    "favorited": ""
},]
with open('contact.json', 'a'):
    #a stands for append
    print()
def addContact():
    name = input("Please enter your contact's name: ")
    number = input("Please enter your contact's phone number: ")
    email = input("Please enter your contact's email: ")
    birthday = input("Please enter your contact's birthday: ")
    
    def blankChecker(x, y):
        found = True
        while found == True:
            if x == " " or "":# loop until they are not empty
                x = input(f"Please enter a valid {y}: ")# check to see if empty
            else:
                found = False
            
    blankChecker(name, "name")
    blankChecker(number, "phone number")
    blankChecker(email, "email")
    blankChecker(birthday, "birthday")
    
def searchContact(x):
    if x == 1:
        playerInput = input("Enter the contact you are looking for: ")
        with open('contact.json', 'r') as f:
            ##Load the file
            contacts = json.load(f)
            ##Looop through the list inside the file
            for entry in contacts: #entry = key values, contacts = key list
                for person in entry:
                    ##Search to see if the username is equal to the player inputted username
                    if person.get("Username") == playerInput:
                        print()#print contact info
                    elif "exit" or "leave" in playerInput:
                        mainMenu()
                    else:
                        print("We could not find your contact. Please try again.")
                        searchContact(1)
    elif x == 2:
        playerInput = input("Enter the contact you are looking to delete: ")
        with open('contact.json', 'r') as f:
            ##Load the file
            contacts = json.load(f)
            ##Looop through the list inside the file
            for entry in contacts: #entry = key values, contacts = key list
                for person in entry:
                    ##Search to see if the username is equal to the player inputted username
                    if person.get("Username") == playerInput:
                        print(f"Would you like to delete the contact with the name {playerInput}? This action is not reversable.")
                        #delete action
                    elif "exit" or "leave" in playerInput:
                        mainMenu()
                    else:
                        print("We could not find your contact. Please try again.")
                        searchContact(2)
    elif x == 3:
        playerInput = input("Enter the contact you are looking to delete: ")
        with open('contact.json', 'r') as f:
            ##Load the file
            contacts = json.load(f)
            ##Looop through the list inside the file
            for entry in contacts: #entry = key values, contacts = key list
                for person in entry:
                    ##Search to see if the username is equal to the player inputted username
                    if person.get("Username") == playerInput:
                        y = True
                        while y == True:
                            print(f"Press 1 to edit the name of the contact named {playerInput}")
                            print(f"Press 2 to edit the phone number of the contact named {playerInput}")
                            print(f"Press 3 to edit the email of the contact named {playerInput}")
                            print(f"Press 4 to edit the birthday of the contact named {playerInput}")
                            print(f"Press 5 to save your changes to the contact named {playerInput}")
                            #modify action
                            
                    elif "exit" or "leave" in playerInput:
                        mainMenu()
                    else:
                        print("We could not find your contact. Please try again.")
                        searchContact(3)
        

def updateContact():
    print()
    
def favoriteContacts():
    print()
    #add a option to favorite contacts & a seperate list for them
    

def mainMenu():
    print("Press 1 to add contact")
    print("Press 2 to delete a contact")
    print("Press 3 to search for a contact")
    print("Press 4 to modify a contact")
    print("Press 5 to view your favorited contacts")
    print("press 6 to leave")
    option = input("")
    if option == "1":
        addContact()
    elif option == "2":
        searchContact(2)
    elif option == "3":
        searchContact(1)
    elif option == "4":
        searchContact(3)
    elif option == "5":
        favoriteContacts()
    elif option == "6":
        exit()
    else:
        print()
        

    
    