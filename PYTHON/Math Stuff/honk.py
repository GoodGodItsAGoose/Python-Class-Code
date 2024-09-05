name = input("Enter Character Name: ")
import tkinter as tk

def GetStarted ():
    Top = tk.Toplevel()
    Top.title("Character Maker!")
    Top.geometry('200x75')
    msg = tk.Message(Top, text=name)
    msg.pack(padx=20, pady=20)
    button = tk.Button(Top, text="Next!", command=Top.destroy)
    button.pack()
    Top.mainloop

root = tk.Tk()
root.title("Character Maker")

root.withdraw()
# the input dialog
USER_INP = tk.askstring(title="Test",
                                  prompt="What's your Name?:")

# check it out
print("Hello", USER_INP)

button = tk.Button(root, 
                   text="Get Started!", 
                   command=GetStarted,
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

root.mainloop()