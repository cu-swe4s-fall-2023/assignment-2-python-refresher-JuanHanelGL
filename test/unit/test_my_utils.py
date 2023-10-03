import sys
import os
import unittest
import random



sys.path.insert(0, '../../src')

from my_utils import get_column, calculate_mean, calculate_median, calculate_std_dev

class TestMyUtils(unittest.TestCase):

    #def test_get_column(self):
    
    def test_calculate_mean(self):
        array = [random.randint(1, 100) for _ in range(100)]
        expected_mean = sum(array) / len(array)
        self.assertEqual(calculate_mean(array), expected_mean)

        with self.assertRaises(ZeroDivisionError):
            calculate_mean([])

    def test_calculate_median(self):
        array = [random.randint(1, 100) for _ in range(101)]
        sorted_array = sorted(array)
        expected_median = sorted_array[len(array) // 2]
        self.assertEqual(calculate_median(array), expected_median)

        with self.assertRaises(IndexError):
            calculate_median([])

    def test_calculate_std_dev(self):
        array = [random.randint(1, 100) for _ in range(100)]
        mean = sum(array) / len(array)
        expected_std_dev = (sum((x - mean) ** 2 for x in array) / len(array)) ** 0.5
        self.assertAlmostEqual(calculate_std_dev(array), expected_std_dev)

        with self.assertRaises(ZeroDivisionError):
            calculate_std_dev([])

if __name__ == '__main__':
    unittest.main()