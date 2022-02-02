import unittest
import pytest
from datastructures.linked_lists import utils as ls_utils
from datastructures.linked_lists import merge_two_sorted_lists as merge


@pytest.mark.parametrize("list_1,list_2,expected", [
    ([4, 2, 1], [4, 3, 1], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
    ([], [0], [0])
])
def test_merge_two_sorted_list(list_1, list_2, expected):
    list_1 = ls_utils.build_list(list_1)
    list_2 = ls_utils.build_list(list_2)
    merged = merge.merge_two_sorted_lists(list_1.head, list_2.head)
    list_3 = ls_utils.LinkedList()
    list_3.head = merged

    assert len(expected) == ls_utils.list_size(merged)
    assert expected == list_3.to_array(reverse=True)


if __name__ == '__main__':
    unittest.main()
