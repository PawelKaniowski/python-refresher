import math


def circle_area(radius):
    return math.pi * pow(radius, 2)


print(circle_area(3))

circle = {
    "radius": 3,
    "color": "blue"
}
print(circle_area(circle["radius"]))
