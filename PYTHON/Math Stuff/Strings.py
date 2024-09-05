import tkinter as tk
import sys


class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.l=tk.Label(master,text="Enter Equation")
        self.l.pack()
        self.e=tk.Entry(master)# put in numbers twice might not work, att'get' not in obj 'int'
        self.e.pack()
        self.b=tk.Button(master,text="Mafs",command=self.solve)
        self.b.pack()
        self.b2=tk.Button(master,text="Print!",command=lambda: sys.stdout.write(self.entryValue()+'\n'))#ans needs to be defined in this def, need to define in solve too
        self.b2.pack() #need to change this to spit out answer get to print, entryvalue needs to be output
        self.value=self.e.get() #trying to get self.e to go to answer, so it prints the answer.
    def popup(self):
        self=mainWindow(self.master)
        self.b["state"] = "disabled" 
        self.master(self.master)
        self.b["state"] = "normal"
#trying to get command to print answer, need answer to be gotten and changed to a variable, then print that variable, but the print(variable) needs to be before mainWindow
    def solve(self):
        string_two = self.value #is breaking .rfind() Fix: Was ()
        print(string_two)

        honk = string_two#need to fix so it replaces spaces
        plus = "+"
        times = "x" or "X" or "*"
        minus = "-"
        divide = " / "
        if "+" in string_two:
            variablete = string_two.rfind("+")
            print(variablete)
        elif "-" in string_two:
            variablete = string_two.rfind("-")
            print(variablete)
        elif "/" in string_two:
            variablete = string_two.rfind("/")
            print(variablete)
        elif "x" or "X" or "*" in string_two:
            if "x" in string_two:
                variablete = string_two.rfind("x")
                print(variablete)
            elif "X" in string_two:
                variablete = string_two.rfind("X")
                print(variablete)
            elif "*" in string_two:
                variablete = string_two.rfind("*")
                print(variablete)
            else:
                print(variablete, string_two, honk)
                Top = tk.Toplevel()
                Top.title("Mafs")
                Top.geometry('150x75')
                msg = tk.Message(Top, text="Error")
                msg.pack(padx=20, pady=20)
                button = tk.Button(Top, text="Dismiss", command=Top.destroy)
                button.pack()

        variable = int(honk[0:variablete])

        variablethree = honk[variablete:variablete + 1]

        variabletwo = int(honk[1 + variablete :1000])

        if "+" in honk:
            ans=int(variable + variabletwo)
            Top = tk.Toplevel()
            Top.title("Mafs")
            Top.geometry('150x90')
            msg = tk.Message(Top, text=variable + variabletwo)
            msg.pack(padx=20, pady=20)
            button = tk.Button(Top, text="Dismiss", command=Top.destroy)
            button.pack()
            self.e=ans
        elif "-" in honk:
            ans=int(variable - variabletwo)
            Top = tk.Toplevel()
            Top.title("Mafs")
            Top.geometry('150x90')
            msg = tk.Message(Top, text=(variable - variabletwo))
            msg.pack(padx=20, pady=20)
            button = tk.Button(Top, text="Dismiss", command=Top.destroy)
            button.pack()
            self.e=ans
        elif "/" in honk:
            ans=int(variable / variabletwo)
            Top = tk.Toplevel()
            Top.title("Mafs")
            Top.geometry('150x90')
            msg = tk.Message(Top, text=(variable / variabletwo))
            msg.pack(padx=20, pady=20)
            button = tk.Button(Top, text="Dismiss", command=Top.destroy)
            button.pack()
            self.e=ans
        elif "x" or "X" or "*" in honk:
            ans=int(variable * variabletwo)
            Top = tk.Toplevel()
            Top.title("Mafs")
            Top.geometry('150x90')
            msg = tk.Message(Top, text=(variable * variabletwo))
            msg.pack(padx=20, pady=20)
            button = tk.Button(Top, text="Dismiss", command=Top.destroy)
            button.pack()
            self.e=ans
        else: 
            Top = tk.Toplevel()
            Top.title("Mafs")
            Top.geometry('150x75')
            msg = tk.Message(Top, text="Error")
            msg.pack(padx=20, pady=20)
            button = tk.Button(Top, text="Dismiss", command=Top.destroy)
            button.pack()

    def entryValue(self):
        return self.new_method()

    def new_method(self):
        return self.value # should go to answer of solve and __init__, why __init__? just go to solve and get answer of solve, then print answer of solve.


if __name__ == "__main__":
    root=tk.Tk()
    m=mainWindow(root)
    root.mainloop()