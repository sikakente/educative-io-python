"""
Problem Statement
----------------
Find all substrings of a string that are a permutation of another string Find all substrings of a string that contains all characters of another string. In other words, find all substrings of the first string that are anagrams of the second string.


Input
-----
two strings

Output
-------
all permutations of another string
"""
from collections import Counter


def all_permutation_substring(s, t):
    t_char_frequency = Counter(t)
    count = len(t_char_frequency.keys())
    left = right = 0
    s_size = len(s)
    permutations = []

    while right < s_size:
        current_char = s[right]
        t_char_frequency[current_char] = t_char_frequency[current_char] - 1

        if t_char_frequency[current_char] == 0:
            count -= 1

        while t_char_frequency[current_char] < 0:
            char_to_remove = s[left]
            t_char_frequency[char_to_remove] = t_char_frequency[char_to_remove] + 1
            left += 1
            if t_char_frequency[char_to_remove] == 1:
                count += 1

        if count == 0:
            permutations.append(s[left:right + 1])

        right += 1

    return permutations


if __name__ == '__main__':
    import doctest

    doctest.testmod()
