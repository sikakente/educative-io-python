import unittest
import pytest
from datastructures.linked_lists import utils as ls_utils


@pytest.mark.parametrize("values,size,first_item", [
    ([i + 1 for i in reversed(range(5))], 5, 1),
    ([0], 1, 0)
])
def test_linked_list_utils(values, size, first_item):
    linked_list = ls_utils.build_list(values)
    assert size == linked_list.size
    assert first_item == linked_list.head.value
    assert values == linked_list.to_array()


if __name__ == '__main__':
    unittest.main()
