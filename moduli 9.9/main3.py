import math


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __int__(self , radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __int__(self , width , height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __int__(self , base , height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
rectangle = Rectangle( 4 , 8)
triangle = Triangle( 3 , 8)


print("Area of the Circle is " , circle.area())
print("Area of the Rectangle " , rectangle.area())
print("Area of the Triangle " , triangle.area())