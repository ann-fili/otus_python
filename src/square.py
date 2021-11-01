from src.figure import Figure


class Square(Figure):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.side_length = side_length

    @property
    def area(self):
        return (self.side_length * self.side_length)

    @property
    def perimeter(self):
        return (self.side_length * 4)


square = Square('square', 20)
print('Площадь квадрата', square.area)
