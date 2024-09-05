
myname = input("Please type your name:")
print(f"\nHello, {myname}!")

myquestion =int(input("Please enter the first number of your equation:"))
print(type(myquestion))

mysymbol = input("Please enter your math symbol:")
print(type(mysymbol))

myquestion2 =int(input("Please enter the second number of your equation:"))
print(type(myquestion2))

addition = {myquestion};{mysymbol};{myquestion2}
print(addition)

if mysymbol == "+":
    print(myquestion + myquestion2)
elif mysymbol == "-":
    print(myquestion - myquestion2)
elif mysymbol == "x" or mysymbol == "*" or mysymbol == "X":
    print(myquestion * myquestion2)
elif mysymbol == "/":
    print(myquestion / myquestion2)
else: 
    print("Follow directions, please. You're not in kindergarten anymore.")
