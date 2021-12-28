import unittest
from datastructures.bitwise_operations import bitwise_or as bso


class BitwiseOrTest(unittest.TestCase):
    def test_min_flips(self):
        self.assertEqual(3, bso.min_flips(2, 6, 5))


if __name__ == '__main__':
    unittest.main()
