import unittest
import pytest
from datastructures.heaps.min_heap import MinHeap


@pytest.mark.parametrize("values", [
    ([8, 9, 1, 6, 4, 7, 5]),
])
def test_min_heap(values):
    min_heap = MinHeap(values)
    assert 7 == min_heap.size
    min_heap.insert(-1)
    assert -1 == min_heap.find_min()
    assert 8 == min_heap.size
    assert -1 == min_heap.extract_min()
    assert 7 == min_heap.size


if __name__ == '__main__':
    unittest.main()
