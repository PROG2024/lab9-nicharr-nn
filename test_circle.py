"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
import math


class CircleTest(unittest.TestCase):
    def test_positive_radius(self):
        """Test add_area with two circles having positive radii."""
        c1 = Circle(3)
        c2 = Circle(4)
        c3 = c1.add_area(c2)
        self.assertEqual(c3.get_radius(), 5)
        self.assertAlmostEquals(c3.get_area(), math.pi * 5 * 5)

    def test_radius_zero(self):
        """Test add_area when one of the circles has radius 0,
         the other has non-zero radius. (Result should have same radius.)"""
        c1 = Circle(0)
        c2 = Circle(5)
        c3 = c1.add_area(c2)
        self.assertEqual(c3.get_radius(), 5)
        self.assertAlmostEquals(c3.get_area(), math.pi * 5 * 5)

    def test_negative_radius(self):
        """Raises exception if the radius is negative."""
        with self.assertRaises(ValueError):
            c1 = Circle(-1)