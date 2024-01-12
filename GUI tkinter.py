import tkinter
from tkinter import*

top = Tk()
b1=Button(top,text="Red",fg="Red",bg="white")

b1.pack(side=TOP)

b2=Button(top,text="Blue",fg="blue",bg="white")

b2.pack(side=LEFT)

b3=Button(top,text="Green",fg="green",bg="white")

b3.pack(side=RIGHT)

b4=Button(top,text="Yellow",fg="yellow",bg="white")

b4.pack(side=BOTTOM)
