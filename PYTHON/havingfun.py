class Variables:
    random = "what" #is a string, can't do math with numbers inside of " "
    print(random)
    print(type(random)) # type prints the type of the variable

    human = True #Boolean statement (true or false)useful for if statements
    print(human)
    print(type(human)) 

    number = 91 #is an integer, can prefix int()
    print(number)
    print(type(number))

    num = 2.0 #is a float, because it has a decimal point
    print(num)
    print(type(num))

class multipleAssignment: #multiple assignment = allows multiple variables in one line of code
    person1 = "Sandy"
    person2 = "Jacob"
    person3 = "Sam"

    person1, person2, person3 = "Sandy", "Jacob", "Sam" #multiple assignment

    print(person1)
    print(person2)
    print(person3)

    print(person1, person2, person3) #multiple assignment

    person4 = "Sam"
    person5 = "Sam"
    person3 = person4 = person5 = "Sam" #can be multiple

class Strings:
    name = "bob"
    print(len(name))                #prints the length of the variable 'name'
    print(name.find("b"))           #finds the place the letter 'b' is in
    print(name.capitalize())        #Prints the variable 'name' capitalized, only the first letter of the string
    print(name.upper())             #Prints the variable 'name' all uppercase
    print(name.lower())             #prints the variable 'name' all undercase
    print(name.isdigit())           #true or false, depending if it's a digit
    print(name.isalpha())           #checks if string is only alphabetical characters, will say false if there is a space.
    print(name.count("O"))          #counts the amount of 'O's there are in the string
    print(name.replace("o", "a"))   #replaces letters in the string
    print(name*3)                   #prints 3 times

class typeCasting: #converting one datatype of a value to another datatype of a value
    x = 1   #int
    y = 2.0 #float
    z = "3" #string
    
    print(x)
    print(y)
    print(z)
    
    str(x)      #changes to a string
    int(y)      #changes to an integer
    float(z)    #changes to a float
    
    print(str(x))   #prints as string
    print(int(y))   #prints as int
    print(float(z)) #prints as float
    
    print("Y is"+y)         #will give an error, because 'y' is an int
    print("Y is"+ str(y))   #Will not give an error, because 'y' is a str
    
    #to make change permanent
    x = str(x)
    y = int(y)
    z = float(z)
    
class Input:
    input("What is your favorite number?: ") #will allow input
    
    favnum = input("What is your favorite number?: ") #Will save the answer
    print("Your favorite number is " + favnum)
    
    name = input("What is your name?: ")
    age = int(input("How old are you?: "))
    height = float(input("How tall are you?: ")) #Allows decimals
    
    print("Your name is " + name + ".")
    print("You are " + str(age) + "years old.")
    print("You are " + str(height) + "cm tall.")
    
class mathFunctions:
    import math
    
    pi = 3.14
    x = 1
    y = 2
    z = 3
    
    print(round(pi)) #rounds to whole integer
    print(math.ceil(pi)) #rounds up
    print(math.floor(pi)) #rounds down
    print(abs(pi)) #How close the number is to 0
    print(pow(pi, 2)) #multiplies by the power of 2
    print(math.sqrt(pi)) #Prints square root of variable
    print(math.sqrt(400))
    
    print(max(x, y, z)) #finds the max number
    print(min(x, y, z)) #finds the min number
    
class stringSlicing:    #Makes a substring by extracting elements from another string
                        #uses  indexing[]  or slice(), both functions work the same
                        # [start:stop:step]
    class Indexing: #[start:stop:step]
        name = "Abs McAbserton"
        first_name = name[0:3] #first character in string is always 0, stopping index is exclusive (Wont include)
        #also can be first_name = name[:3]
        print(first_name)
        last_name = name[4:10]#prints characters from 4 to 10(the tenth being excluded)
        #also can be last_name = name[4:], will include everything to the end
        print(last_name)
        funky_name = name[0:10:2] #will print every other character from the starting character to the end character
        #also can be funky_name = name[::2], for shorthand.
        print(funky_name)
        reversed_name = name[::-1] #will count it backwards
        print(reversed_name)
    
    class Slicing: #(start,stop,step)
        websiteurl = "https://google.com" #Breaking this into "https://" and "google"
        slice = slice(8,-4)#because all website names are not the same, so you can use the "negative index", all characters have a positive and negative index, so from the ending of the website, it counts as m=-1, o=-2, c=-3, and so on.
        print(websiteurl[slice])
        
        website2 = "https://wikipedia.com"
        slice2 = slice(8, -4)
        print(website2[slice2])
              
class ifStatements : #A block of code that will only execute if its condition is true
    age = int(input("How old are you?: "))
    
    if age == 100:
        print("Wow, you are old!")
    elif age >= 18: #greater than or equal to
        print("You're an adult!")
    elif age < 0: #less than
        print("Am I talking to you from the past?")
    else: #If none of the other blocks of code are met, it will resort to this block of code.
        print("You are a child.")
        
class logisticalOperators: #(and, or, not) used to check if two or more conditional statements are true.
    temp = input("What is the temperature outside?: ")
