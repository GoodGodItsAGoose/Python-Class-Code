from pathlib import Path
def uploadFile():
    file = input("Please enter the file name you've uploaded: ")
    if ".txt" in file:
        print()
    else:
        file = file+".txt"
    try: 
        open(f"texts/{file}" , 'r', encoding='UTF-8')
    except:
        UnicodeDecodeError
        print("File not found. Please try again.")
        fileReader()
    else:
        with open(f"texts/{file}" , 'r', encoding='UTF-8') as f:
            return f.read()

def exitChoice():
    choice2 = input("Would you like to leave? (Y/N): ")
    if str(choice2).lower() == "y":
        exit()
    elif str(choice2).lower() == "n":
        print()
        fileReader()
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
