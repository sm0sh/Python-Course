class Building:
     def Name(slef):
         print("Building no 41")


class Apartment(Building):
    def Block(self):
        print("Apartment A Block")


class Floor(Apartment):
    def Room(self):
        print("6th Floor Room no 606")
        
d = Floor()
d.Name()
d.Block()
d.Room()

