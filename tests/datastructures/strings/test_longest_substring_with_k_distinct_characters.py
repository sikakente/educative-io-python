import unittest
import pytest
from datastructures.strings.longest_substring_with_k_distinct_characters import \
    longest_substring_with_k_distinct_characters, longest_substring_with_k_distinct_characters_2


@pytest.mark.parametrize("input_str,k,expected", [
    # ("abcbdbdbbdcdabd", 2, "bdbdbbd"),
    # ("abcbdbdbbdcdabd", 3, "bcbdbdbbdcd"),
    # ("abcbdbdbbdcdabd", 5, "abcbdbdbbdcdabd")
])
def test_longest_substring_with_k_distinct_characters(input_str, k, expected):
    assert expected == longest_substring_with_k_distinct_characters(input_str, k)


@pytest.mark.parametrize("input_str,k,expected", [
    ("abcbdbdbbdcdabd", 2, "bdbdbbd"),
    ("abcbdbdbbdcdabd", 3, "bcbdbdbbdcd"),
    ("abcbdbdbbdcdabd", 5, "abcbdbdbbdcdabd")
])
def test_longest_substring_with_k_distinct_characters_2(input_str, k, expected):
    assert expected == longest_substring_with_k_distinct_characters_2(input_str, k)


if __name__ == '__main__':
    unittest.main()
