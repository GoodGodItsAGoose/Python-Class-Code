import random
import time
class bank:
    def __init__(self, accBalance, accID, accHolderName):
        self.accBalance = accBalance
        self.accID = accID
        self.accHolderName = accHolderName
    
    def info(self):
        infoCheck = True
        while infoCheck == True:
            print("Press 1 to check your balance. Press 2 to check your account ID, and press 3 to create a new account.")
            infoChoice = input()
            if int(infoChoice) == 1:
                print("You have "+str(self.accBalance)+" dollars.")
                infoCheck = False
            elif int(infoChoice) == 2:
                print("Your account ID is: "+str(self.accID))
                infoCheck = False
            elif int(infoChoice) == 3:
                newAccount()
            else:
                print("Please re-enter choice.")
                infoCheck = True
            
        
    def withdraw(self):
        time.sleep(1)
        print("How much would you like to withdraw?")
        withdrawAmount = input()
        if int(withdrawAmount) > self.accBalance:
            time.sleep(1)
            print("You cannot withdraw that amount. You have "+str(self.accBalance)+" dollars.")
        else:
            newAccBalance = self.accBalance - int(withdrawAmount)
            self.accBalance = newAccBalance
            print("You've withdrawn "+str(withdrawAmount)+" dollars from your bank account. Now you have "+str(self.accBalance)+" dollars.")
            return self.accBalance
    
    def deposit(self):
        time.sleep(1)
        print("How much would you like to withdraw?")
        depositAmount = input()
        newAccBalance = int(depositAmount) + self.accBalance
        self.accBalance = newAccBalance
        print("You've deposited "+str(depositAmount)+" dollars. Now you have "+str(self.accBalance)+" dollars.")
        return self.accBalance
            

class savingsAccount(bank):
    def __init__(self, accBalance, accID, accHolderName):
        super().__init__(accBalance, accID, accHolderName)
    #add deets later, gives interest (more than checkings)
        
    def openAccount(self):
        print("Hello! Please enter your account name.")
        accountName = str(input("Enter new account holder name: "))
        accID = random.randint(100000, 999999999)
        
    def openExistingAccount(self):
        self.accHolderName
    
    def interest(self):
        newAccBalance = self.accBalance + (self.accBalance * 0.02)
        self.accBalance = newAccBalance
        
    def startUpSavings(self):
        try:
            self.accBalance
        except NameError:
            self.accBalance = 0
        else:
            self.accBalance = self.accBalance
        time.sleep(1)
        print("Hello! You've set up a Savings Account. Currently you have "+str(self.accBalance)+". Your account ID is "+str(self.accID)+".")
        accCheckIn() # could have it return this (up) and print it?

class checkingsAccount(bank):
    def __init__(self, accBalance, accID, accHolderName):
        super().__init__(accBalance, accID, accHolderName)
    #add deets later, where most of the money will be
    
    def startUpCheckings(self):
        try:
            self.accBalance
        except NameError:
            self.accBalance = 0
        else:
            self.accBalance = self.accBalance
        time.sleep(1)
        print("Hello! You've set up a Checkings account. Currently you have "+str(self.accBalance)+". Your account ID is "+str(self.accID)+".")
        accCheckIn()


class transaction(bank):
    #generates random transaction ID
    print()

def newAccount():
    print("Please enter your new account name.")
    name = input("")

    while accountDone == False:
        time.sleep(1)
        print("Thank you! Please enter 1 for a Savings Account, and 2 for a Checking Account.")
        time.sleep(1)
        print("The difference is that Checking accounts are better for regular transactions, but gain less or even no interest.")
        time.sleep(1)
        print("Savings accounts are used better for saving money and typically earn more interest.")
        accountType = input()
        if int(accountType) == 1:
            accountDone = True
            savingsAccount.startUpSavings(self=account1) #wont work, ask why
            account2 = savingsAccount(0, random.randint(1000000000, 999999999999), name)
        elif int(accountType) == 2:
            accountDone = True
            checkingsAccount.startUpCheckings(self=account1)
            account2 = checkingsAccount(0, random.randint(1000000000, 999999999999), name)
        else:
            print("Please re-enter choice.")
            accountDone = False
    

print("Hello! Welcome to the bank. Please enter your name.")
name = input("")
accountDone = False
while accountDone == False:
    time.sleep(1)
    print("Thank you! Please enter 1 for a Savings Account, and 2 for a Checking Account.")
    time.sleep(1)
    print("The difference is that Checking accounts are better for regular transactions, but gain less or even no interest.")
    time.sleep(1)
    print("Savings accounts are used better for saving money and typically earn more interest.")
    accountType = input()
    if int(accountType) == 1:
        accountDone = True
        savingsAccount.startUpSavings(self=account1) #wont work, ask why
        account1 = savingsAccount(0, random.randint(1000000000, 999999999999), name)
    elif int(accountType) == 2:
        accountDone = True
        checkingsAccount.startUpCheckings(self=account1)
        account1 = checkingsAccount(0, random.randint(1000000000, 999999999999), name)
    else:
        print("Please re-enter choice.")
        accountDone = False

print("Hello. Which")

def accCheckIn():
    checkInDone = False
    while checkInDone == False:
        print("If you would like to deposit cash, press 1. If you would like to withdraw cash, press 2. If you would like to check your infomration, press 3.")
        accChoice = input()
        if int(accChoice) == 1:
            bank.deposit(self=account1)
        elif int(accChoice) == 2:
            bank.withdraw(self=account1)
        elif int(accChoice) == 3:
            bank.info()
        else:
            print("Please re-enter choice.")
            checkInDone = False     
