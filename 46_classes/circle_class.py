import math
class Circle:
     def __init__(self, radius):
         self.radius = radius
     def area(self):
         return math.pi * pow(self.radius, 2)

small = Circle(3)
print(small.radius)

small.area()

large = Circle(42)
print(large.radius)

large.area()

large.radius = 85
print(large.area())

