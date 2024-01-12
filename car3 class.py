class Car:
    
    def _intit_(self,name,colour,price):
        self.name = name
        self.price = price
        self.colour = colour

car1=Car("Innova","Black","22 lakhs")
car2=Car("Fortuner","White","46 lakhs")
car3=Car("Polo","Red","9 lakhs")

print("car1 details")
print("Car colour is:",car1.colour)
print("Car price is:",car1.price)
print("Car name is:",car1.name)

print("car2 details")
print("Car colour is:",car2.colour)
print("Car price is:",car2.price)
print("Car name is:",car2.name)

print("car3 details")
print("Car colour is:",car3.colour)
print("Car price is:",car3.price)
print("Car name is:",car3.name)
