import unittest
import pytest
from algorithms.dynamic_programming.decode_ways import decode_ways, decode_ways_memoized


# @pytest.mark.parametrize("s,expected", [
#     ("12", 2),
#     ("226", 3),
#     ("06", 0)
# ])
# def test_decode_ways(s, expected):
#     assert expected == decode_ways(s)


@pytest.mark.parametrize("s,expected", [
    ("12", 2),
    ("226", 3),
    ("06", 0)
])
def test_decode_ways(s, expected):
    assert expected == decode_ways_memoized(s)


if __name__ == '__main__':
    unittest.main()
