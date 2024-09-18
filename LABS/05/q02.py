from abc import ABC, abstractmethod
class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def area(self):
        print("Area of Triangle : ",self.width*self.height)


class Square(Shape):
    def __init__(self, side):
        self.side = side


    def area(self):
        print("Area of Square : ", self.side * self.side)


class Rectangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        print("Area of Rectangle : ", self.base * self.height)

s = Square(2)
s.area()

r = Rectangle(3,2)
r.area()

t = Triangle(4,2)
t.area()
