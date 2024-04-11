_PI = 3.14

class Circle:
    def __init__(self, radius):
        self.radius = _validate(radius)

    def calculate_area(self):
        return round(_PI * self.radius**2, 2)

class Square:
    def __init__(self, side):
        self.side = _validate(side)

    def calculate_area(self):
        return round(self.side**2, 2)

def _validate(value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        return value

Circle(-1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = _validate(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = _validate(value)

def _validate(value):
    if not isinstance(value, int | float):
        raise ValueError("number expected")
    return value