import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# tests/test_math_utils.py
import unittest
from math_utils import add, divide, fib

class TestMathUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Runs once for the test class (e.g., open shared resources)
        cls.shared_samples = [(2, 3, 5), (-1, 1, 0), (0, 0, 0)]

    def setUp(self):
        # Runs before each test — good for fresh state
        self.a, self.b, self.expected = 2, 3, 5

    def tearDown(self):
        # Runs after each test — good for cleanup
        pass

    def test_add_table_driven(self):
        for a, b, expected in self.shared_samples:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(add(a, b), expected)

    def test_divide_normal_and_edge_cases(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_fib_small_values(self):
        # Demonstrates multiple asserts + subTest
        cases = [(0, 0), (1, 1), (2, 1), (3, 2), (7, 13)]
        for n, expected in cases:
            with self.subTest(n=n):
                self.assertEqual(fib(n), expected)

    def test_fib_raises_on_negative(self):
        with self.assertRaises(ValueError):
            fib(-1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
