"""
Problem Statement
----------------
Given two strings s and t, return true if t is an anagram of s, and false otherwise.  An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Input
-----
two strings

Output
-------
boolean indicating whether the second string is an anagram of the first string
"""
from collections import Counter


def is_anagram(s, t):
    s_freq = Counter(s)
    t_freq = Counter(t)
    s_key_set, t_key_set = set(s_freq.keys()), set(t_freq.keys())
    if len(s_key_set.difference(t_key_set)) > 0:
        return False
    for t_key in t_key_set:
        if s_freq[t_key] != t_freq[t_key]:
            return False
    return True


if __name__ == '__main__':
    import doctest

    doctest.testmod()
