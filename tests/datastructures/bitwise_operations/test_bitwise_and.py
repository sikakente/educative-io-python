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

    def test_even_or_odd(self):
        numbers = [i for i in range(1, 5)]
        self.assertEqual(['Odd', 'Even', 'Odd', 'Even'], bsa.even_or_odd(numbers))

    def test_is_power_of_two(self):
        self.assertTrue(bsa.is_power_of_two(4))
        self.assertFalse(bsa.is_power_of_two(12))
        self.assertFalse(bsa.is_power_of_two(0))
        self.assertTrue(bsa.is_power_of_two(1))

    def test_is_power_of_two_kernighan(self):
        self.assertTrue(bsa.is_power_of_two_brian_kernighan(4))
        self.assertFalse(bsa.is_power_of_two_brian_kernighan(12))
        self.assertFalse(bsa.is_power_of_two_brian_kernighan(0))
        self.assertTrue(bsa.is_power_of_two_brian_kernighan(1))


if __name__ == '__main__':
    unittest.main()
