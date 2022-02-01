import unittest
import pytest
from datastructures.linked_lists import remove_nth_node_from_end_of_list as rm
from datastructures.linked_lists import utils as ls_utils


@pytest.mark.parametrize("values,n,size,items", [
    ([i + 1 for i in reversed(range(5))], 2, 4, [5, 3, 2, 1]),
    ([1], 1, 0, []),
    ([2, 1], 1, 1, [1])
])
def test_remove_nth_node(values, n, size, items):
    linked_list = ls_utils.build_list(values)
    list_after_removing_nth_node = rm.remove_nth_node(linked_list.head, n)
    linked_list.head = list_after_removing_nth_node
    items_after_removal = linked_list.to_array()
    assert items == items_after_removal
    assert size == len(items_after_removal)


if __name__ == '__main__':
    unittest.main()
