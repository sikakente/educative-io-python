import unittest
from datastructures.bitwise_operations import number_system as ns


class MyTestCase(unittest.TestCase):
    def test_number_system(self):
        expected = [6, 5, 2, 1]
        self.assertEqual(expected, ns.number_system(1256))


if __name__ == '__main__':
    unittest.main()
