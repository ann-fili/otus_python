import math
from src.figure import Figure


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
print('Площадь круга', circle.area)
