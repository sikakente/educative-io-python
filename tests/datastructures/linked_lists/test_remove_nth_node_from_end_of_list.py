import unittest
import pytest
from datastructures.linked_lists import remove_nth_node_from_end_of_list as rm
from datastructures.linked_lists import utils as ls_utils


@pytest.mark.parametrize("values,n,size", [
    ([i + 1 for i in reversed(range(5))], 2, 4),
    ([1], 1, 0),
    ([2, 1], [])
])
def test_bottom_up_longest_common_subsequence(numbers, expected):
    assert expected == ts.three_sum(numbers)


if __name__ == '__main__':
    unittest.main()
