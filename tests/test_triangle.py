import unittest
from triangle import area, perimeter

class TestTriangleArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(area(5, 2), 5)
        self.assertAlmostEqual(area(100, 10), 500)
        self.assertAlmostEqual(area(0.2, 0.1), 0.01)


    def test_zero_values(self):
        self.assertAlmostEqual(area(0, 5), 0)
        self.assertAlmostEqual(area(10, 0), 0)
        self.assertAlmostEqual(area(0, 0), 0)

class TestTrianglePerimeter(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(perimeter(5, 2, 3), 10)
        self.assertAlmostEqual(perimeter(0.2, 0.1, 0.1), 0.4)
        self.assertAlmostEqual(perimeter(100, 240, 90), 430)

    def test_zero_values(self):
        self.assertAlmostEqual(perimeter(0, 0, 0), 0)


if __name__ == '__main__':
    unittest.main()