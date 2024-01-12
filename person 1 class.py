class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def myfunc(self):
      print("Hello my name is " + self.name + "and my age is " + self.age)
    
p1=Person("Bobby", "Thirty Six")
p1.myfunc()
