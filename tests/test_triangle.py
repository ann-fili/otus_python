from src.triangle import Triangle


def test_triangle_area():
    triangle = Triangle(13, 14, 15)
    assert triangle.area == 84


def test_triangle_perimeter():
    triangle = Triangle(13, 14, 15)
    assert triangle.perimeter == 100
