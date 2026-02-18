# def calculate_area(length,width):
#     return length * width
# def calculate_perimeter(length,width):
#     return 2 *(length + width)

class Rectangle:
    def __int__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 *(self.length + self.width)


my_rectangle = Rectangle( length:5, width:3)


area = my_rectangle.calculate_area()
perimeter = ,my_rectangle.calculate_perimeter()

print(f"Area:  {area}")
print(f"perimeter  {perimeter}"
