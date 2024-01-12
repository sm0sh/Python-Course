import tkinter
from tkinter import*

top=Tk()
l1=Label(top,text="Name")
l1.place(x=10,y=10)
t1=Entry(top)
t1.place(x=70,y=10)
l2=Label(top,text="Password")
l2.place(x=10,y=30)
t2=Entry(top)
t2.place(x=70,y=30)
l3=Label(top,text="Email")
l3.place(x=10,y=50)
t3=Entry(top)
t3.place(x=70,y=50)
top.mainloop()
