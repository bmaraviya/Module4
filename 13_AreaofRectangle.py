""" Write a Python class named Rectangle constructed by a length and
width and a method which will compute the area of a rectangle"""

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
length = float(input("Enter the length:"))
width = float(input("Enter the width:"))

result = Rectangle(length,width)
print(f"The area of Rectangle is {result.area()}")