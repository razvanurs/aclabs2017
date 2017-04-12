#!python3
import math
import unittest


# How to run unit tests : py -m unittest ex2.py
# import decimal (for precision)
# decimal(0.1) + decimal(0.2) = decimal(0.3)


class Shape(object):
    def __init__(self, l):
        self._l = l

    @property
    def area(self):
        raise NotImplementedError('Cannot compute area for shape')


class Circle(Shape):
    @property
    def area(self):
        return math.pi * self._l


class Square(Shape):
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    @property
    def area(self):
        return self._l * self._l


circle = Circle(10)
print(circle.area)

square = Square(10)
print(square.area)


class TestShape(unittest.TestCase):
    def test_square(self):
        self.assertEqual(Square.from_diameter(20).area, 100)

    def test_circle(self):
        self.assertEqual(Circle(1).area, math.pi)

    def test_check_failure(self):
        with self.assertRaises(NotImplementedError):
            Shape(0).area
