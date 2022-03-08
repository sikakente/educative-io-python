import unittest
import pytest
from datastructures.tries.prefix_trie import PrefixTrie


def test_prefix_trie():
    trie = PrefixTrie("wealth")
    assert trie.contains("wealth")
    assert not trie.contains("poverty")


if __name__ == '__main__':
    unittest.main()
