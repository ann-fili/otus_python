import math
from src.figure import Figure
# from src.triangle import Triangle, triangle
# from src.square import Square, square
# from src.circle import Circle, circle
# from src.rectangle import Rectangle, rectangle

class Circle(Figure):

    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    @property
    def area(self):
        return round(math.pi * (self.radius ** 2))
    @property
    def perimeter(self):
        return round(2 * math.pi * self.radius)

circle = Circle('circle', 10)
print ('Площадь круга', circle.area)



