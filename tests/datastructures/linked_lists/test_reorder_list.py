import unittest
import pytest
from datastructures.linked_lists.utils import build_list, to_array
from datastructures.linked_lists.reorder_list import reorder_list


@pytest.mark.parametrize("values,expected", [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3])
])
def test_reorder_list(values, expected):
    linked_list = build_list(values, reverse=True)
    reorder_list(linked_list.head)
    assert expected == to_array(linked_list.head, reverse=True)


if __name__ == '__main__':
    unittest.main()
