import unittest
import pytest
from datastructures.strings.word_break import word_break


@pytest.mark.parametrize("word,word_dict,expected", [
    ("leetcode", ["leet", "code"], True),
    ("applepenapple", ["apple", "pen"], True),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False)
])
def test_word_break(word, word_dict, expected):
    assert expected == word_break(word, word_dict)


if __name__ == '__main__':
    unittest.main()
