
number = 0
import random
number = random.randint(1,20)
import tkinter as tk
def Label ():
    number = "hi"
    
def D20 ():
    number = "D20 Roll:", random.randint(1,20)
    Top = tk.Toplevel()
    Top.title("Roll Outcome:")
    Top.geometry('150x75')
    msg = tk.Message(Top, text=number)
    msg.pack(padx=20, pady=20)
    button = tk.Button(Top, text="Dismiss", command=Top.destroy)
    button.pack()
def D10 ():
    number = "D10 Roll:", random.randint(1,10)
    Top = tk.Toplevel()
    Top.title("Roll Outcome:")
    Top.geometry('150x75')
    msg = tk.Message(Top, text=number)
    msg.pack(padx=20, pady=20)
    button = tk.Button(Top, text="Dismiss", command=Top.destroy)
    button.pack()
def D12 ():
    number = "D12 Roll:", random.randint(1,12)
    Top = tk.Toplevel()
    Top.title("Roll Outcome:")
    Top.geometry('150x75')
    msg = tk.Message(Top, text=number)
    msg.pack(padx=20, pady=20)
    button = tk.Button(Top, text="Dismiss", command=Top.destroy)
    button.pack()
def D8 ():
    number = "D8 Roll:", random.randint(1,8)
    Top = tk.Toplevel()
    Top.title("Roll Outcome:")
    Top.geometry('150x75')
    msg = tk.Message(Top, text=number)
    msg.pack(padx=20, pady=20)
    button = tk.Button(Top, text="Dismiss", command=Top.destroy)
    button.pack()
def D6 ():
    number = "D6 Roll:", random.randint(1,6)
    Top = tk.Toplevel()
    Top.title("Roll Outcome:")
    Top.geometry('150x75')
    msg = tk.Message(Top, text=number)
    msg.pack(padx=20, pady=20)
    button = tk.Button(Top, text="Dismiss", command=Top.destroy)
    button.pack()
def D4 ():
    number = "D4 Roll:", random.randint(1,4)
    Top = tk.Toplevel()
    Top.title("Roll Outcome")
    Top.geometry('150x75')
    msg = tk.Message(Top, text=number)
    msg.pack(padx=20, pady=20)
    button = tk.Button(Top, text="Dismiss", command=Top.destroy)
    button.pack()


root = tk.Tk()
root.title("Rolls!")

# Creating a button with specified options
button = tk.Button(root, 
                   text="D20", 
                   command=D20,
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
                   text="D10", 
                   command=D10,
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
                   text="D12", 
                   command=D12,
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
                   text="D8", 
                   command=D8,
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
                   text="D6", 
                   command=D6,
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
                   text="D4", 
                   command=D4,
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