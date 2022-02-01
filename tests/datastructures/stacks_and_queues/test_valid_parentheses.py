import unittest
import pytest
from datastructures.stacks_and_queues import valid_parentheses as vp


@pytest.mark.parametrize("input_str,expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
])
def test_valid_parentheses(input_str, expected):
    assert expected == vp.valid_parentheses(input_str)


if __name__ == '__main__':
    unittest.main()
