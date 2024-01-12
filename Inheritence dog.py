class Animal:
     def speak(self):
         print("Animal Speaking")


class Dog(Animal):
    def bark(self):
        print("dog barking")


class DogChild(Dog):
    def eat(self):
        print("Eating bread...chomp...chomp...")
        
d = DogChild()
d.bark()
d.speak()
d.eat()

