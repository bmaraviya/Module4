"""Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle"""
pie = 3.14
class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return pie*radius*radius
    
    def perimeter(self):
        return 2*pie*radius


radius = float(input("Enter Radius:"))
result = Circle.area(radius)
rs = Circle.perimeter(radius)
print(f"The area of circle is {result}")
print(f"The perimeter of circle is {rs}")