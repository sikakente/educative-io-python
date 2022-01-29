import unittest
import pytest
from algorithms.recursion import letter_combinations as lc


@pytest.mark.parametrize("characters,expected", [
    (['A', 'B', 'C'],
     [['A', 'B', 'C'], ['A', 'C', 'B'],
      ['B', 'A', 'C'], ['B', 'C', 'A'],
      ['C', 'B', 'A'], ['C', 'A', 'B']]),
])
def test_letter_combinations(characters, expected):
    assert expected == lc.letter_combinations(characters)


if __name__ == '__main__':
    unittest.main()
