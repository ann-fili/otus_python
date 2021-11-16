import math
from src.figure import Figure


class Circle(Figure):

    def __init__(self, radius):
        super().__init__(name='circle')
        self.radius = radius

    @property
    def area(self):
        return round(math.pi * (self.radius ** 2))

    @property
    def perimeter(self):
        return round(2 * math.pi * self.radius)
