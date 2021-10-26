from src.figure import Figure
# from src.triangle import Triangle, triangle
# from src.square import Square, square
# from src.circle import Circle, circle
# from src.rectangle import Rectangle, rectangle

class Rectangle(Figure):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return (self.width + self.height) * 2

rectangle = Rectangle('rectangle', 10, 20)
print ('Площадь прямоугольника', rectangle.area)



