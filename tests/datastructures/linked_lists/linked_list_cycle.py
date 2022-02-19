import unittest
import pytest
from datastructures.linked_lists.utils import build_list_with_cycle
from datastructures.linked_lists.linked_list_cycle import has_cycle


@pytest.mark.parametrize("values, pos, expected", [
    ([3, 2, 0, -4], 1, True),
    ([1, 2], 0, True),
    ([1], -1, False)
])
def test_has_cycle(values, pos, expected):
    linked_list = build_list_with_cycle(values, pos, reverse=True)
    assert expected == has_cycle(linked_list.head)


if __name__ == '__main__':
    unittest.main()
