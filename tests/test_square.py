from src.square import Square


def test_square_area():
    square = Square(18)
    assert square.area == 324

def test_square_perimeter():
    square = Square(18)
    assert square.perimeter == 100
