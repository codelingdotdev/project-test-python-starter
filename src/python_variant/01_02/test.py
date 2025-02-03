import unittest
from src.main import sum

class TestSumFunction(unittest.TestCase):
    def test_sum_positive_numbers(self):
        self.assertEqual(sum(1, 2), 4)
        self.assertEqual(sum(10, 5), 16)

    def test_sum_negative_numbers(self):
        self.assertEqual(sum(-1, -2), -2)
        self.assertEqual(sum(-10, -5), -14)

    def test_sum_mixed_numbers(self):
        self.assertEqual(sum(-1, 2), 2)
        self.assertEqual(sum(10, -5), 6)

if __name__ == '__main__':
    unittest.main()