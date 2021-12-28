import unittest
from datastructures.bitwise_operations import number_system as ns


class MyTestCase(unittest.TestCase):
    def test_number_system(self):
        expected = [6, 5, 2, 1]
        self.assertEqual(expected, ns.number_system(1256))

    def test_decimal_number_system(self):
        expected = [6, 5, 2, 1]
        self.assertEqual(expected, ns.decimal_number_system(1256))

    def test_binary_number_system(self):
        expected = [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1]
        self.assertEqual(expected, ns.binary_number_system(1256))

    def test_binary_to_decimal(self):
        self.assertEqual(37, ns.binary_to_decimal(100101))

    def test_num_digits(self):
        self.assertEqual(3, ns.num_digits(125))


if __name__ == '__main__':
    unittest.main()
