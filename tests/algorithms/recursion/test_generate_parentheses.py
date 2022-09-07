import unittest
import pytest
from algorithms.recursion import generate_parentheses as gc


@pytest.mark.parametrize("n,expected", [
    (3, ['((()))', '(()())', '(())()', '()(())', '()()()']),
])
def test_test_generate_parentheses(n, expected):
    assert expected == gc.generate_parentheses(n)


if __name__ == '__main__':
    unittest.main()
