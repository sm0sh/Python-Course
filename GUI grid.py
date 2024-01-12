import tkinter
from tkinter import*

top=Tk()
l1=Label(top,text="Name")
l1.grid(row=0,column=0)
t1=Entry(top)
t1.grid(row=0,column=1)
l2=Label(top,text="Password")
l2.grid(row=1,column=0)
t2=Entry(top)
t2.grid(row=1,column=1)
b1=Button(top,text="Submit")
b1.grid(row=3,column=0)
top.mainloop()
