import tkinter as tk
import sys

class popupWindow(object):
    def __init__(self,master):
        top=self.top=tk.Toplevel(master)
        self.l=tk.Label(top,text="Hello World")
        self.l.pack()
        self.e=tk.Entry(top)
        self.e.pack()
        self.b=tk.Button(top,text='Ok',command=self.cleanup) #closes window
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.b=tk.Button(master,text="Get Started!",command=self.popup)
        self.b.pack()
        self.b2=tk.Button(master,text="Print!",command=lambda: sys.stdout.write(self.entryValue()+'\n'))
        self.b2.pack() #prints, unless no entry. If no entry then breaks.

    def popup(self):
        self.w=popupWindow(self.master)
        self.b["state"] = "disabled" 
        self.master(self.w.top)
        self.b["state"] = "normal"

    def entryValue(self):
        return self.new_method()

    def new_method(self):
        return self.w.value # goes to print


if __name__ == "__main__":
    root=tk.Tk()
    m=mainWindow(root)
    root.mainloop()
    
#Source: https://stackoverflow.com/questions/10020885/creating-a-popup-message-box-with-an-entry-field