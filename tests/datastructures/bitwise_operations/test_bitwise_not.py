import unittest
from datastructures.bitwise_operations import bitwise_not as bnot


class BinaryNotTest(unittest.TestCase):
    def test_switch_number_sign(self):
        self.assertEqual(-10, bnot.switch_number_sign(10))
        self.assertEqual(10, bnot.switch_number_sign(-10))


if __name__ == '__main__':
    unittest.main()
