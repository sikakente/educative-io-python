import unittest
import pytest
from algorithms.sorting_and_searching import search_rotated_sorted_array as srs


@pytest.mark.parametrize("numbers,target,expected", [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 0, -1)
])
def test_test_search_rotated_sorted_array(numbers, target, expected):
    assert expected == srs.search_rotated_sorted_array(numbers, target)


@pytest.mark.parametrize("numbers,target,expected", [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 0, -1)
])
def test_test_search_rotated_sorted_array_using_pivot(numbers, target, expected):
    assert expected == srs.search_rotated_sorted_array_2(numbers, target)


if __name__ == '__main__':
    unittest.main()
