import unittest

from operations import substract, multiply, divide


class OperationsTests(unittest.TestCase):
    # 1. Test substract
    def test_substract_positive(self):
        self.assertEqual(substract(10, 7), 3)

    def test_substract_negative(self):
        self.assertEqual(substract(7, 10), -3)

    def test_substract_zero(self):
        self.assertEqual(substract(0, 0), 0)

    # 2. Test Multiply
    def test_multiply_positive_1(self):
        self.assertEqual(multiply(6, 5), 30)

    def test_multiply_positive_2(self):
        self.assertEqual(multiply(3, 7), 21)

    def test_multiply_positive_3(self):
        self.assertEqual(multiply(7, 7), 49)

    def test_multiply_negative(self):
        self.assertEqual(multiply(6, -4), -24)

    def test_multiply_zero(self):
        self.assertEqual(multiply(6, 0), 0)
        self.assertEqual(multiply(0, 6), 0)

    # 2. Test Divide
    def test_divide_zero(self):
        self.assertRaises(ValueError, divide, 0, 0)

    # 2. Test Divide
    def test_divide_greater(self):
        self.assertEqual(divide(10, 3), 3)

    # 2. Test Divide
    def test_divide_lower(self):
        self.assertEqual(divide(3, 10), 0)

if __name__ == '__main__':
    unittest.main()
