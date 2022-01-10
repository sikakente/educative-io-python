import unittest
from algorithms.dynamic_programming import fibonacci as fib


class FibonacciTest(unittest.TestCase):
    def test_recursive_fibonacci(self):
        self.assertEqual(0, fib.recursive_fibonacci(0))
        self.assertEqual(1, fib.recursive_fibonacci(1))
        self.assertEqual(1, fib.recursive_fibonacci(2))
        self.assertEqual(3, fib.recursive_fibonacci(4))
        with self.assertRaises(ValueError):
            fib.recursive_fibonacci(-1)

    def test_memoized_fibonacci(self):
        self.assertEqual(0, fib.memoized_fibonacci(0))
        self.assertEqual(1, fib.memoized_fibonacci(1))
        self.assertEqual(1, fib.memoized_fibonacci(2))
        self.assertEqual(3, fib.memoized_fibonacci(4))
        with self.assertRaises(ValueError):
            fib.memoized_fibonacci(-1)

    def test_tabulated_fibonacci(self):
        self.assertEqual(0, fib.tabulated_fibonacci(0))
        self.assertEqual(1, fib.tabulated_fibonacci(1))
        self.assertEqual(1, fib.tabulated_fibonacci(2))
        self.assertEqual(3, fib.tabulated_fibonacci(4))
        with self.assertRaises(ValueError):
            fib.tabulated_fibonacci(-1)

    def test_fast_tabulated_fibonacci(self):
        self.assertEqual(0, fib.fast_tabulated_fibonacci(0))
        self.assertEqual(1, fib.fast_tabulated_fibonacci(1))
        self.assertEqual(1, fib.fast_tabulated_fibonacci(2))
        self.assertEqual(3, fib.fast_tabulated_fibonacci(4))
        with self.assertRaises(ValueError):
            fib.tabulated_fibonacci(-1)


if __name__ == '__main__':
    unittest.main()
