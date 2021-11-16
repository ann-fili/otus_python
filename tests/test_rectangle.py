from src.rectangle import Rectangle


def test_rectangle_area():
    rectangle = Rectangle(10, 20)
    assert rectangle.area == 200


def test_rectangle_perimeter():
    rectangle = Rectangle(4, 5)
    assert rectangle.perimeter == 100
