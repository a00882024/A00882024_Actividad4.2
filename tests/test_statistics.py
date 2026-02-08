"""Tests for statistics functions."""

# pylint: disable=missing-function-docstring

import unittest

from src.stats import mean, median, mode, variance, standard_deviation, count

class TestCount(unittest.TestCase):
    """Tests for the count function."""

    def test_count_multiple_values(self):
        self.assertEqual(count([1, 2, 3, 4, 5]), 5)

    def test_count_single_value(self):
        self.assertEqual(count([5]), 1)

    def test_count_empty_list(self):
        self.assertEqual(count([]), 0)


class TestMean(unittest.TestCase):
    """Tests for the mean function."""

    def test_mean_positive_numbers(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3)

    def test_mean_single_value(self):
        self.assertEqual(mean([5]), 5)

    def test_mean_negative_numbers(self):
        self.assertEqual(mean([-1, -2, -3]), -2)

    def test_mean_mixed_numbers(self):
        self.assertEqual(mean([-1, 0, 1]), 0)

    def test_mean_floats(self):
        self.assertAlmostEqual(mean([1.5, 2.5, 3.0]), 2.333333, places=5)


class TestMedian(unittest.TestCase):
    """Tests for the median function."""

    def test_median_odd_count(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)

    def test_median_even_count(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_median_single_value(self):
        self.assertEqual(median([5]), 5)

    def test_median_unsorted(self):
        self.assertEqual(median([3, 1, 2]), 2)


class TestMode(unittest.TestCase):
    """Tests for the mode function."""

    def test_mode_single_mode(self):
        self.assertEqual(mode([1, 2, 2, 3]), 2)

    def test_mode_all_same(self):
        self.assertEqual(mode([5, 5, 5]), 5)

    def test_mode_all_unique(self):
        self.assertEqual(mode([1, 2, 3]), None)


class TestVariance(unittest.TestCase):
    """Tests for the variance function."""

    def test_variance_basic(self):
        self.assertAlmostEqual(variance([1, 2, 3, 4, 5]), 2.0, places=5)

    def test_variance_same_values(self):
        self.assertEqual(variance([5, 5, 5]), 0)


class TestStandardDeviation(unittest.TestCase):
    """Tests for the standard_deviation function."""

    def test_std_basic(self):
        self.assertAlmostEqual(standard_deviation([1, 2, 3, 4, 5]), 1.41421, places=4)

    def test_std_same_values(self):
        self.assertEqual(standard_deviation([5, 5, 5]), 0)


if __name__ == '__main__':
    unittest.main()
