import unittest
from square import area, perimeter

class TestSquareArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(area(5), 25)
        self.assertAlmostEqual(area(0.2), 0.04)
        self.assertAlmostEqual(area(100), 10000)


    def test_zero_values(self):
        self.assertAlmostEqual(area(0), 0)

class TestSquarePerimeter(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(perimeter(5), 20)
        self.assertAlmostEqual(perimeter(0.2), 0.8)
        self.assertAlmostEqual(perimeter(13), 52)

    def test_zero_values(self):
        self.assertAlmostEqual(perimeter(0), 0)


if __name__ == '__main__':
    unittest.main()