class shape:
    data1 = "abc"

    def no_of_sides(self):
        print("My sides need to be defined, I am from shape class,")


    def twoD(self):
        print('I am a 2D object')

class square(shape):
    data2="XYZ"

    def no_of_sides(self):
        print("I have 4 sides. I am from square class")


    def color(self):
        print("I have teal color. I am from square class.")
        
sq=square()
(sq.no_of_sides())
(sq.color())
(sq.twoD())
