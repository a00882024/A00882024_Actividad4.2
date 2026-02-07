"""Tests for number conversion functions."""

# pylint: disable=missing-function-docstring

import unittest

from src.converters import decimal_to_binary, decimal_to_hexadecimal


class TestDecimalToBinary(unittest.TestCase):
    """Tests for the decimal_to_binary function."""

    def test_zero(self):
        self.assertEqual(decimal_to_binary(0), '0')

    def test_one(self):
        self.assertEqual(decimal_to_binary(1), '1')

    def test_small_number(self):
        self.assertEqual(decimal_to_binary(5), '101')

    def test_power_of_two(self):
        self.assertEqual(decimal_to_binary(8), '1000')

    def test_larger_number(self):
        self.assertEqual(decimal_to_binary(255), '11111111')

    def test_negative_number(self):
        self.assertEqual(decimal_to_binary(-5), '-101')


class TestDecimalToHexadecimal(unittest.TestCase):
    """Tests for the decimal_to_hexadecimal function."""

    def test_zero(self):
        self.assertEqual(decimal_to_hexadecimal(0), '0')

    def test_single_digit(self):
        self.assertEqual(decimal_to_hexadecimal(9), '9')

    def test_letter_digit(self):
        self.assertEqual(decimal_to_hexadecimal(10), 'A')

    def test_small_number(self):
        self.assertEqual(decimal_to_hexadecimal(15), 'F')

    def test_two_digits(self):
        self.assertEqual(decimal_to_hexadecimal(255), 'FF')

    def test_larger_number(self):
        self.assertEqual(decimal_to_hexadecimal(4096), '1000')

    def test_mixed_digits(self):
        self.assertEqual(decimal_to_hexadecimal(171), 'AB')

    def test_negative_number(self):
        self.assertEqual(decimal_to_hexadecimal(-255), '-FF')


if __name__ == '__main__':
    unittest.main()
