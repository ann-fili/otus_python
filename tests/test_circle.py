from src.circle import Circle
import pytest


def test_circle_area():
    circle = Circle(10)
    assert circle.area == 314

@pytest.mark.parametrize ('radius, expexted_area', [
    (0,  0),
    (10, 310)
])
def test_circle_area_border_case(radius, expexted_area):
    circle = Circle(radius)
    assert circle.area == expexted_area

def test_circle_perimeter():
    circle = Circle(10)
    assert circle.perimeter == 63





