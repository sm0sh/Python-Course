import tkinter
from tkinter import *

top = Tk()

top.geometry("200x200")

c = Canvas(top,bg = "black",height = "200",width = 200)

arc = c.create_arc((5,10,150,200),start = 0,extent = 150,fill = "purple")

c.pack()

top.mainloop()
