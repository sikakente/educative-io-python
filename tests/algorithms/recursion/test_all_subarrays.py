import unittest
import pytest
from algorithms.recursion import all_subarrays as als


@pytest.mark.parametrize("characters,expected", [
    (['A', 'B', 'C'],
     [['A'], ['A', 'B'], ['B'], ['A', 'B', 'C'], ['B', 'C'], ['C']]),
])
def test_generate_sub_arrays(characters, expected):
    assert expected == als.generate_sub_arrays(characters)


@pytest.mark.parametrize("characters,expected", [
    (['A', 'B', 'C'],
     [['A'], ['A', 'B'], ['B'], ['A', 'B', 'C'], ['B', 'C'], ['C']]),
])
def test_generate_sub_arrays_iteratively(characters, expected):
    assert expected == als.generate_sub_arrays_iteratively(characters)


if __name__ == '__main__':
    unittest.main()
