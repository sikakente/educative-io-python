import unittest
import pytest
from datastructures.tries.suffix_trie import SuffixTrie


def test_suffix_trie():
    trie = SuffixTrie("wealth")
    assert trie.contains("wealth")
    assert not trie.contains("poverty")


if __name__ == '__main__':
    unittest.main()
