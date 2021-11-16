from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__(name='rectangle')
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return (self.width + self.height) * 2
