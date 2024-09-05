# Starting equiptment, imput tool to use, if tool is not in registry then it takes you back to choose, need to add seperate tabs to roll all, maybe add + and - of certain classes or races
number = 0
import random
number = random.randint(1,20)

import tkinter as tk

name = "0"
TopMsg = "Character Maker!"
TopText = "Enter Name"

class charStart (object): #should just keep out of functions and classes

    def __init__ (self, master):
        Top = self.Top = tk.Toplevel(master)
        charStart.varC = tk.StringVar(Top)
        self.l= tk.Label(Top, text="Test")
        self.l.pack()
        self.e = tk.Entry(Top, textvariable=charStart.varC)
        self.e.pack()
        self.b = tk.Button(Top, text="Next", command=self.Cleanup,)
        self.b.pack()
    
    def Cleanup (self):
        self.value = self.e.get()
        charTag.charUpd()
        self.command = Race.raceFn()
        self.Top.destroy()
        
class charTag (charStart):
    cName = "N/A"
    def charUpd ():
        charTag.cName = charStart.varC.get()
        print(charTag.cName)





class Start (object):
    def __init__(self, master):
        self.master=master
        self.b = tk.Button(root, 
                    text="Get Started!", 
                    command=self.popup,)
        
        self.b.pack()

            
    def popup (self, var1, var2):
        self.w = charStart(self.master)
        self.b["state"] = "disabled" 
        self.master(self.w.Top)
        self.b["state"] = "normal"
        root.destroy()


class charInfo (object):
    def charInfo_Save (self):
        charName = charTag.cName
        charRace = "0"
        charClass = "0"
        

class defs (object):
    Info_Text = "N/A"
    def Dwarf ():
        charInfo(charRace = "Dwarf")
        defs.Info_Text = "enterinfo"
    def Elf ():
        charInfo(charRace = "Elf")
        defs.Info_Text = "enterinfo"
    def Halfling ():
        charInfo(charRace = "Halfling")
        defs.Info_Text = "enterinfo"
        print()
    def Human ():
        charInfo(charRace = "Human")
        defs.Info_Text = "enterinfo"
        print()
    def Dragonborn ():
        charInfo(charRace = "Dragonborn")
        defs.Info_Text = "enterinfo"
        print()
    def Gnome ():
        charInfo(charRace = "Gnome")
        defs.Info_Text = "enterinfo"
        print()
    def Half_Elf ():
        charInfo(charRace = "Half Elf")
        defs.Info_Text = "enterinfo"
        print()
    def Half_Orc ():
        charInfo(charRace = "Half Orc")
        defs.Info_Text = "enterinfo"
        print()
    def Tiefling ():
        charInfo(charRace = "Tiefling")
        defs.Info_Text = "enterinfo"
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

class Info(defs, object):
    def Info_Popup (self, master):
        top = self.top = tk.Toplevel(master)
        self.l = tk.Message(top, text=defs.Info_Text, width=500, pady=350)
        self.b = tk.Button(top, text="Dismiss", command=self.foo,)
        self.b.pack() 
    
    def foo(self):
        self.top.destroy()        
        
class Race (defs, object):
    def raceFn ():
        root = tk.Tk()
        root.title("Character Maker!")
        msg = tk.Message(root, text = charTag.cName, width= 350, padx=55, pady=10)
        msg.pack()
        msg = tk.Message(root, text="Choose your race!", width=150) #add def that is popups and have text change as variable changes
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
        root.bind('<double-1>', Info)

        button.pack(padx=20, pady=20)
        
    

class Class (defs, object):
    def cTab ():

        #Creating a button with specified options
        button = tk.Button(root, 
                    text="Barbarian", 
                    command=defs.Barbarian,
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

        button.pack(padx=1, pady=1)

        button = tk.Button(root, 
                    text="Bard", 
                    command=defs.Bard,
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

        button.pack(padx=1, pady=1)

        button = tk.Button(root, 
                    text="Cleric", 
                    command=defs.Cleric,
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

        button.pack(padx=1, pady=1)

        button = tk.Button(root, 
                    text="Druid", 
                    command=defs.Druid,
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

        button.pack(padx=1, pady=1)

        button = tk.Button(root, 
                    text="Fighter", 
                    command=defs.Fighter,
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
        
        button.pack(padx=1, pady=1)

        button = tk.Button(root, 
                    text="Monk", 
                    command=defs.Monk,
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

        button = tk.Button(root, 
                    text="Paladin", 
                    command=defs.Paladin,
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

        button = tk.Button(root, 
                    text="Ranger", 
                    command=defs.Ranger,
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

        button = tk.Button(root, 
                    text="Rogue", 
                    command=defs.Rogue,
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

        button = tk.Button(root, 
                    text="Sorcerer", 
                    command=defs.Sorcerer,
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

        button = tk.Button(root, 
                    text="Warlock", 
                    command=defs.Warlock,
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

        button = tk.Button(root, 
                    text="Wizard", 
                    command=defs.Wizard,
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
                
#make stat roller
#Finish race picker
#Finish 'defs' code


if __name__ == "__main__":
    root = tk.Tk()
    m = Start(root)
    root.mainloop()