import math
from src.figure import Figure


class Triangle(Figure):
    def __init__(self, l1, l2, l3):
        super().__init__(name='triangle')
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.s = (self.l1 + self.l2 + self.l3) / 2

    @property
    def perimeter(self):
        return self.l1 + self.l2 + self.l3

    @property
    def area(self):
        res = (self.s - self.l1) * (self.s - self.l2) * (self.s - self.l3)
        return math.sqrt(res * self.s)
