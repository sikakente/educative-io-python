"""
Problem Statement
----------------
Given an arrays of strings strs, group the anagrams together. You can return the answer in any order.  An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Input
-----
list of words

Output
-------
list of grouped anagrams
"""

from collections import defaultdict


def group_anagrams(strings):
    anagram_store = defaultdict(list)
    for string in strings:
        sorted_string = "".join(sorted(string))
        anagram_store[sorted_string].append(string)
    return [grouped_anagram for grouped_anagram in anagram_store.values()]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
