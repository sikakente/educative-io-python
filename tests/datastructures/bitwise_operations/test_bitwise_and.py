import unittest
from datastructures.bitwise_operations import bitwise_and as bsa


class BitwiseAndTest(unittest.TestCase):
    def test_count_set_bits(self):
        self.assertEqual(6, bsa.count_set_bits(125))

    def test_count_set_bits_using_bitwise_and(self):
        self.assertEqual(6, bsa.count_set_bits_with_bitwise_and(125))

    def test_count_set_bits_using_bitwise_and_simple(self):
        self.assertEqual(6, bsa.count_set_bits_with_bitwise_and_simple(125))

    def test_count_set_bits_using_brian_kernighan(self):
        self.assertEqual(6, bsa.count_set_bits_brian_kernighan(125))

    def test_count_set_bits_using_lookup_table(self):
        self.assertEqual(6, bsa.count_set_bits_using_lookup_table(125))

    def test_number_of_set_bit_counts_in_range(self):
        self.assertEqual([0, 1, 1, 2, 1, 2, 2], bsa.number_of_set_bit_counts_in_range(6))


if __name__ == '__main__':
    unittest.main()
