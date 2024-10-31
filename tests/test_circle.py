import unittest
import math
from circle import area, perimeter

class TestCircleArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(area(5), 25 * math.pi)
        self.assertAlmostEqual(area(10), 100 * math.pi)
        self.assertAlmostEqual(area(0.2), 0.04 * math.pi)


    def test_zero_values(self):
        self.assertAlmostEqual(area(0), 0)
#
class TestCirclePerimeter(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(perimeter(5), 10 * math.pi)
        self.assertAlmostEqual(perimeter(0.2), 0.4 * math.pi)
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test_zero_values(self):
        self.assertAlmostEqual(perimeter(0), 0)


if __name__ == '__main__':
    unittest.main()