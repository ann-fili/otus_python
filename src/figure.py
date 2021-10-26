
class Figure:
    def __init__(self, name, *args):
        self.name = name

    @property
    def area(self):
        raise NotImplementedError

    @property
    def perimeter(self):
        raise NotImplementedError

    def add_area(self, *others):
        for other in others:
            return self.area + other.area + other.area
        if not isinstance(others, Figure):
            raise ValueError (f'{type(others)} is not Figure')

    def __repr__(self):
        return self.name
