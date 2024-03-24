class Circle:
     def __init__(self, radius):
         self._radius = radius
     @property
     def radius(self):
         return self._radius
     @radius.setter
     def radius(self, value):
         if not isinstance(value, int | float) or value <= 0:
             raise ValueError("Radius must be a positive number")
         self._radius = value

small = Circle(3)
print(small.radius)

small.radius = 4
print(small.radius)

small.radius = "x"

