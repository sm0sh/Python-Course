import tkinter
from tkinter import messagebox

from tkinter import*

top=Tk()

def msg():
    messagebox.showinfo("Alert","Button Clicked")
    
b=Button(top,text="Click me",activeforeground
    ="Blue",activebackground="Grey",
    command=msg)

b.pack()
top.mainloop()
        
