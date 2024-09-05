import tkinter as tk
string_two = "stuff"
honk = string_two
if "+" in string_two:
    variablete = honk.rfind("+")
elif "-" in string_two:
    variablete = honk.rfind("-")
elif "/" in string_two:
    variablete = honk.rfind("/")
elif "x" or "X" or "*" in string_two:
    if "x" in string_two:
        variablete = honk.rfind("x")
    elif "X" in string_two:
        variablete = honk.rfind("X")
    elif "*" in string_two:
        variablete = honk.rfind("*") 
    else:
        Top = tk.Toplevel()
        Top.title("Mafs")
        Top.geometry('150x75')
        msg = tk.Message(Top, text="Error")
        msg.pack(padx=20, pady=20)
        button = tk.Button(Top, text="Dismiss", command=Top.destroy)
        button.pack()

exit()
import tkinter as tk

# function to run on pressing
# 'ENTER' key from keyboard.
def key_handler_function(event):
    print("You clicked ENTER key in your keyboard")

# main application window
root = tk.Tk()
root.title("GeeksForGeeks")
root.geometry("300x200")


# Binding ENTER key to function
root.bind("<Return>", key_handler_function)

# run the application
root.mainloop()
exit()
root =tk.Tk()
mystring =tk.StringVar(root)
def getvalue():
    print(mystring.get())
e1 = tk.Entry(root,textvariable = mystring,width=100,fg="blue",bd=3,selectbackground='violet').pack()
button1 = tk.Button(root, 
                text='Submit', 
                fg='White', 
                bg= 'dark green',height = 1, width = 10,command=getvalue).pack()

root.mainloop()
exit()
import tkinter as tk


class charName (object): #should just keep out of functions and classes
    def __init__ (self, master):
        Top = self.Top = tk.Toplevel(master)
        self.l= tk.Label(Top, text="Test")
        self.l.pack()
        self.e = tk.Entry(Top)
        self.e.pack()
        self.b = tk.Button(Top, text="Next", command=self.Cleanup,)
        self.b.pack()
    
    def Cleanup (self):
        self.value = self.e.get()
        self.command = Race.rTab()
        self.Top.destroy()




class Start (object):
    def __init__(self, master):
        self.master=master
        self.b = tk.Button(root, 
                    text="Get Started!", 
                    command=self.popup,)
        
        self.b.pack()
        
            
    def popup (self):
        self.w = charName(self.master)
        self.b["state"] = "disabled" 
        self.master(self.w.Top)
        self.b["state"] = "normal"
        self.master.destroy()

class charInfo (object):
    def charInfo_Save (self):
        charName = self.entryValue
        charRace = "0"
        charClass = "0"
        

class defs (object):
    def Dwarf ():
        charInfo(charRace = "Dwarf")
        root.destroy()
    def Elf ():
        charInfo(charRace = "Elf")
    def Halfling ():
        print()
    def Human ():
        print()
    def Dragonborn ():
        print()
    def Gnome ():
        print()
    def Half_Elf ():
        print()
    def Half_Orc ():
        print()
    def Tiefling ():
        print()
        
    def Barbarian ():
        print()
    def Bard ():
        print()
    def Cleric ():
        print()
    def Druid ():
        print()
    def Fighter ():
        print()
    def Monk ():
        print()
    def Paladin ():
        print()
    def Ranger ():
        print()
    def Rogue ():
        print()
    def Sorcerer ():
        print()
    def Warlock ():
        print()
    def Wizard ():
        print()


class Race (defs, object):
    def rTab ():
        root = tk.Tk()
        root.title("Character Maker!")
        msg = tk.Message(root, text="Choose your race!") #add def that is popups and have text change as variable changes
        msg.pack(padx=20, pady=20)                      #as the code is ran though? pops up with the name and dismiss button

        button = tk.Button(root, 
                    text="Dwarf", 
                    command=defs.Dwarf,
                    activebackground="blue", 
                    activeforeground="white",
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",
                    padx=10,
                    pady=5,
                    width=15,
                    wraplength=100)

        button.pack(padx=20, pady=20)
        
        
    
    
if __name__ == "__main__":
    root=tk.Tk()
    m=Start(root)
    root.mainloop()
exit()
class ClassA(object):
    var1 = 0
    var2 = 0


    def __init__(self):
        ClassA.var1 = 1
        ClassA.var2 = 2

    def methodA(self):
        ClassA.var1 = ClassA.var1 + ClassA.var2
        return ClassA.var1



class ClassB(ClassA):
    def __init__(self):
        print (ClassA.var1)
        print (ClassA.var2)