import tkinter
from tkinter import *

top = Tk()

top.geometry("200x250")

lbl=Label(top,text="A list of favourate countries...")

listbox=Listbox(top)

listbox.insert(1,"India")

listbox.insert(2,"Italy")

listbox.insert(3,"Spain")

listbox.insert(4,"Mexico")

btn = Button(top,text="delete",command=lambda listbox=listbox:listbox.delete(ANCHOR))

lbl.pack()


listbox.pack()

btn.pack()
top.mainloop()
