class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def myfunc(self):
      print("Hello my name is " + self.name)
      print("and my age is 8 ")
    
p1=Person("Dholu", 8)
p2=Person("Bholu", 8)
p1.myfunc()
p2.myfunc()
