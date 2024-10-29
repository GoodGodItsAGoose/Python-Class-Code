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

def fileReader():
    fileName = uploadFile()
    fileLength = len(fileName)
    print(f"Your file is {fileLength} characters long.")
        
fileReader()
