"""
Problem Statement
-----------------
Given a string, find the length of its longest palindromic subsequence.
In a palindromic subsequence, elements read the same, backward and forward.

A subsequence is a sequence that can be derived from another sequence
by deleting some or no elements without changing the order of the remaining elements.

Input
-----
A string

Output
------
The length of the longest palindromic subsequence
"""


def recursive_longest_palindromic_subsequence(input_string):
    """

    Parameters
    ----------
    input_string : str
        String with palindromic subsequence

    Returns
    -------
    int
        length of the longest palindromic subsequence

    >>> recursive_longest_palindromic_subsequence("abdbca")
    5

    >>> recursive_longest_palindromic_subsequence("cddpd")
    3

    >>> recursive_longest_palindromic_subsequence("pqr")
    1

    """

    def helper(start, end):
        #
        if start == end:
            return 1
        if start > end:
            return 0

        if input_string[start] == input_string[end]:
            return 2 + helper(start + 1, end - 1)

        return max(helper(start + 1, end), helper(start, end - 1))

    return helper(0, len(input_string) - 1)


def memoized_longest_palindromic_subsequence(input_string):
    """

    Parameters
    ----------
    input_string : str
        String with palindromic subsequence

    Returns
    -------
    int
        length of the longest palindromic subsequence

    >>> memoized_longest_palindromic_subsequence("abdbca")
    5

    >>> memoized_longest_palindromic_subsequence("cddpd")
    3

    >>> memoized_longest_palindromic_subsequence("pqr")
    1

    """
    cache = {}

    def helper(start, end):
        if (start, end) in cache:
            return cache[(start, end)]
        if start == end:
            return 1
        if start > end:
            return 0

        if input_string[start] == input_string[end]:
            cache[(start, end)] = 2 + helper(start + 1, end - 1)
            return cache[(start, end)]

        cache[(start, end)] = max(helper(start + 1, end), helper(start, end - 1))
        return cache[(start, end)]

    return helper(0, len(input_string) - 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
