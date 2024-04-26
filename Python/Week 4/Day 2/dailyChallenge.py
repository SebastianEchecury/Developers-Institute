class Circle:
    def __init__(self, radius=0, diameter=0) -> None:
        if radius != 0:
            self.__radius = radius
            self.__diameter = radius * 2
        elif diameter != 0:
            self.__diameter = diameter
            self.__radius = diameter / 2

    def __str__(self):
        return('Diameter {} - Radius {}'.format(self.__diameter, self.__radius))
    
    def __add__(self, other):
        r = self.__radius + other.__radius
        return Circle(radius=r)
    
    def __gt__(self, other):
        return self.__radius > other.__radius
    
    def __ge__(self, other):
        return self.__radius >= other.__radius
    
    def getRadius(self):
        return self.__radius

c = Circle(diameter=5)
print(str(c))

c2 = Circle(diameter=10)

c3 = c + c2
print(str(c3))

print(c3>c2)

print(c2>=c)

circles = [c3, c2, c]

for cir in circles:
    print(cir)

circles.sort()

for cir in circles:
    print(cir)

from turtle import Turtle

t = Turtle()
t.circle(c.getRadius())


