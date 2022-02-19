import unittest
import pytest
from datastructures.linked_lists.utils import build_list
from datastructures.linked_lists.reverse_linked_list import reverse_list


@pytest.mark.parametrize("values,expected", [
    ([1, 2, 3, 4, 5], 5),
    ([1, 2], 2),
    ([], None)
])
def test_reverse_list(values, expected):
    linked_list = build_list(values, reverse=True)
    reversed_list = reverse_list(linked_list.head)
    if reversed_list:
        assert expected == reversed_list.value
    else:
        assert expected == reversed_list


if __name__ == '__main__':
    unittest.main()
