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

    def test_num_digits_using_log_approach(self):
        self.assertEqual(3, ns.num_digits_using_log(125))

    def test_bitwise_decimal_to_binary(self):
        self.assertEqual(([1, 1, 1, 1, 1, 0, 1], 7), ns.bitwise_decimal_to_binary(125))

    def test_bit_counter(self):
        self.assertEqual(7, ns.bit_counter(125))

    def test_count_set_bits(self):
        self.assertEqual(6, ns.count_set_bits(125))

    def test_count_set_bits_using_bitwise_and(self):
        self.assertEqual(6, ns.count_set_bits_with_bitwise_and(125))

    def test_count_set_bits_using_bitwise_and_simple(self):
        self.assertEqual(6, ns.count_set_bits_with_bitwise_and_simple(125))

    def test_count_set_bits_using_brian_kernighan(self):
        self.assertEqual(6, ns.count_set_bits_brian_kernighan(125))


if __name__ == '__main__':
    unittest.main()
