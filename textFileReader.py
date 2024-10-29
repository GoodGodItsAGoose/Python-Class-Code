def uploadFile():
    file = input("Please enter the file name you've uploaded: ")
    if ".txt" in file:
        print()
    else:
        file = file+".txt"
    #checks to see if file name will work
    try: 
        open(f"texts/{file}" , 'r', encoding='UTF-8')
    except:
        UnicodeDecodeError
        print("File not found. Please try again.")
        fileReader()
    else:
        #opens the file and returns the text
        with open(f"texts/{file}" , 'r', encoding='UTF-8') as f:
            return f.read()

#choice to exit(what the name says it does)
def exitChoice():
    choice2 = input("Would you like to leave? (Y/N): ")
    if str(choice2).lower() == "y":
        exit()
    elif str(choice2).lower() == "n":
        print()
        fileReader()

# main function, able to read or upload a new file.
def fileReader():
    fileName = uploadFile()
    fileLength = len(fileName)
    print(f"Your file is {fileLength} characters long.")
    print()
    choice = input("Would you like to read it? (Y/N): ")
    if choice.lower() == "y":
        print(fileName)
        print()
        exitChoice()
    else:
        exitChoice()
        
        
fileReader()
