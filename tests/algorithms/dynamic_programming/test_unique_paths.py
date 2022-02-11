import unittest
import pytest
from algorithms.dynamic_programming import unique_paths as up


@pytest.mark.parametrize("m, n,expected", [
    (3, 7, 28),
])
def test_unique_paths(m, n, expected):
    assert expected == up.unique_paths(m, n)


if __name__ == '__main__':
    unittest.main()
