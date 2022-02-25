import unittest
import pytest
from datastructures.linked_lists.utils import build_list, to_array
from datastructures.heaps.merge_k_sorted_lists import merge_k_lists


@pytest.mark.parametrize("list_values,expected", [
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([], []),
    ([[]], [])
])
def test_merge_k_lists(list_values, expected):
    lists = [build_list(values, reverse=True) for values in list_values]
    lists = [linked_list.head for linked_list in lists]
    merged_list = merge_k_lists(lists)
    assert expected == to_array(merged_list, reverse=True)


if __name__ == '__main__':
    unittest.main()
