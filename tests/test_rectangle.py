import unittest
from rectangle import area, perimeter

class TestRectangleArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(area(5, 10), 50)
        self.assertAlmostEqual(area(0.1, 0.2), 0.02)
        self.assertAlmostEqual(area(32123, 477237), 15330284151)

    def test_zero_values(self):
        self.assertAlmostEqual(area(0, 10), 0)
        self.assertAlmostEqual(area(5, 0), 0)
        self.assertAlmostEqual(area(0, 0), 0)

class TestRectanglePerimeter(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(perimeter(5, 10), 30)
        self.assertAlmostEqual(perimeter(0.2, 0.3), 1)
        self.assertAlmostEqual(perimeter(0.2, 0.03), 0.46)
        self.assertAlmostEqual(perimeter(1001, 500), 3002)

    def test_zero_values(self):
        self.assertAlmostEqual(perimeter(0, 0), 0)


if __name__ == '__main__':
    unittest.main()