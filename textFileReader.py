from pathlib import Path
import json
def uploadFile():
    file = input("Please enter the file name you've uploaded, or type 'history' to see previous entries: ")
    with open("fileNames.txt", "r") as f:
        if "history" in file.lower():
            clear = input("Would you like to clear your history? THIS ACTION CAN NOT BE UNDONE (Y/N): ")
            if "y" in clear.lower():
                #sets the fileNames.txt to a blank
                p = ""
                path = Path("fileNames.txt")
                #overrides text writen to clear the history
                path.write_text(p)
                print("Cleared History.")
                #reruns to the beginning of the menu function
                fileReader()
            elif "n" in clear.lower():
                with open("fileNames.txt", 'r') as f:
                    if f == "":
                        print("No history found.")
                    else:
                        print(f.read())
                    
                    fileReader()
        elif file not in f:
            #adds .txt to the end if .txt was missing so the opening of the file works
            if ".txt" in file.lower():
                # placeHolderString just so the if statment is valid
                placeHolderString = None
            else:
                file = file+".txt"
            with open("fileNames.txt", "a") as f:
                json.dump(file, f)
                f.write("\n")
                f.close()
    # checks to see if file name will work
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
