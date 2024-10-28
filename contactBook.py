import json
import ast
contactList = []

#adds a contact with name, phone number, email, and birthday information with a blank checker.
# def addContact(x):
#     name = input("Please enter your contact's name: ")
#     number = input("Please enter your contact's phone number: ")
#     email = input("Please enter your contact's email: ")
#     birthday = input("Please enter your contact's birthday: ")
    
#     def blankChecker(x, y, z):
#         found = True
#         while found == True:
#             if x == " " or "":# loop until they are not empty
#                 x = input(f"Please enter a valid {y}: ")# check to see if empty
#                 return x
#             elif z == 1:
#                 try:#will it work with () and - in it?
#                     int(x)
#                 except TypeError:
#                     x = input(f"Please enter a valid Phone Number: ")
#                     blankChecker(x,y)
#                 return x
#             else:
#                 found = False
    
#     name = blankChecker(name, "name", 0)
#     number = blankChecker(number, "phone number", 1)
#     email = blankChecker(email, "email", 0)
#     birthday = blankChecker(birthday, "birthday", 0)
    
#     contactList = {
#         "name": name,
#         "number": number,
#         "email": email,
#         "birthday": birthday
#         }
#     if x == 1:
#         #adds contact to the txt file
#         with open('contacts.txt', 'a') as f:
#             f.write(str(contactList))
#             f.close()
#     elif x == 2:
#         print() #updates

# #function for finding a certain contact
# def contactRunThru(userInput, x):
#     with open('contacts.txt', 'r') as f:
#         for line in f:
#             f.read()
#             if {"name": userInput} or {"number": userInput} in f:
#                 n = contactList
#                 #pull the {blah blah} from txt file
#                 info = [n, True]
#     f =  open('contacts.txt', 'r')
#     f = f.read().split()
#     if userInput in f:
#         info = [f, True]
#         return info
#     elif "back" in userInput:
#         mainMenu()
#     else:
#         print("We could not find your contact. Please try again. Type 'back' to go back to the main menu.")
#         searchContact(x)

def addContact(x):
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
    
    #template for writing into the file
    contactList = {
        "name": name,
        "number": number,
        "email": email,
        "birthday": birthday
        }
    if x == 1:
        #adds contact to the txt file
        with open('contacts.txt', 'a') as f:
            ##Convert it to json and dump it inside the text file
            json.dump(contactList, f) #json's version of writing into file
            ##Adds it to the next line
            f.write("\n")
            #saves the file
            f.close()
            print(f"Saved contact name as {name}.")
            mainMenu()
    elif x == 2:
        with open('contacts.txt', 'a') as f:
            ##Convert it to json and dump it inside the text file
            for _ in f:
                json.dump(contactList, f) #json's version of writing into file
                ##Adds it to the next line
                f.write("\n")
                print(f"Updated contact {name}.")
                mainMenu()
    


def contactRunThru(userInput, x):
    ##Reads the text file
    contact2 = {}
    with open("contacts.txt", "r") as f:
        for line in f: #in goes to __iter__, why?
            f2 = f.read()
            contact = f2
            contact2 = {f2}
            print(contact2)
            print(contact)
            print("/")
            print("Continuing further")
            ##Removes spaces at the beginning and end of the string
            ##Checks to see if the values inside are equal to the user input
            if "back" in userInput:
                mainMenu()
            elif contact["name"] in userInput or contact["number"] == userInput:
                #1 is for printing contact info, 2 is for deleting contact info, 3 is for ___
                if x == 1:
                    print(f"Contact name: {contact['name']}")
                    print(f"Contact phone number: {contact['number']}")
                    print(f"Contact email: {contact['email']}")
                    print(f"Contact birthday: {contact['birthday']}")
                    print()
                    mainMenu()
                elif x == 2:
                    
                    #finding and deleting a contact
                    for contact in contact2:
                        if contact['name'].lower() != userInput.lower():
                            #adding the contact to the contact2 list for future use
                            contact2 = contact
                            updatedContacts = []
                        if len(updatedContacts) < len(contact2): #what does this do, exactly?
                            print("rewriting contact info")
                            with open('contacts.txt', 'w') as f:
                                json.dump(contact, f)   #dumps takes string format, dump for storing in file, (second argument being file)
                                print('\n')
                    print()
                    mainMenu()
                elif x == 3:
                    return True
            else:   
                print("We could not find your contact. Please try again. Type 'back' to go back to the main menu.")
                searchContact(x)
        print(";")


#searching for contacts
def searchContact(x):
    #general searching
    if x == 1:
        playerInput = input("Enter the name or phone number of the contact you are looking for: ")
        contactRunThru(playerInput, 1)
    #searching for a contact to delete        
    elif x == 2:
        playerInput = input("Enter the name or phone number of the contact you are looking to delete: ")
        if playerInput == "back":
            mainMenu()
        print(f"Would you like to delete the contact with the name {playerInput}? This action is not reversable.")
        print("Type 'y' for yes or 'n' for no.")
        playerInput2 = input("")
        if 'y' in playerInput2:
            contactRunThru(playerInput, 2)
        elif 'n' in playerInput2:
            mainMenu()
    #searching for a contact to edit it
    elif x == 3:
        playerInput = input("Enter the name or phone number of the contact you are looking to edit: ")
        if contactRunThru(playerInput, 3) == True:
            #edits and replaces contact info by overriding the existing contact info
            addContact(2)
            
    

    
#main menu function
def mainMenu():
    print("Press 1 to add contact")
    print("Press 2 to search for a contact")
    print("Press 3 to delete a contact")
    print("Press 4 to modify a contact")
    print("press 5 to leave")
    option = input("")
    print()
    if option == "1":
        addContact(1)
    elif option == "2":
        searchContact(1)
    elif option == "3":
        searchContact(2)
    elif option == "4":
        searchContact(3)
    elif option == "5":
        exit()
    else:
        print("Please enter a valid choice.")
        print()
        mainMenu()
        

    
mainMenu()