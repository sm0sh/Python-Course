class Car:
    
    def __init__(self,name,price,color):
        self.price = price
        self.color = color
        self.name = name


car1 = Car("Pugo","10 Lakhs", "red")
car2 = Car("Mavo","6 Lakhs", "blue")

print('car1 details:')
print('Price is  ', car1.price)
print('Color: ', car1.color)
print('Name: ', car1.name)


print('car2 details:')
print('Price is ', car2.price)
print('Color: ', car2.color)
print('Name: ', car2.name)
             
