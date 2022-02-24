import unittest
import pytest
from datastructures.heaps.max_heap import MaxHeap


@pytest.mark.parametrize("values", [
    ([8, 9, 1, 6, 4, 7, 5]),
])
def test_max_heap(values):
    max_heap = MaxHeap(values)
    assert 7 == max_heap.size
    max_heap.insert(1000)
    assert 1000 == max_heap.find_max()
    assert 8 == max_heap.size
    assert 1000 == max_heap.extract_min()
    assert 7 == max_heap.size


if __name__ == '__main__':
    unittest.main()
