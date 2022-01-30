"""

"""


def recursive_longest_common_subsequence(text_1, text_2):
    """

    Parameters
    ----------
    text_1 : str
        first string
    text_2 : str
        second string

    Returns
    -------
    int
        length of the longest common subsequence

    >>> recursive_longest_common_subsequence("abcde", "ace")
    3
    """

    def helper(idx_1, idx_2):
        if idx_1 == len(text_1):
            return 0
        if idx_2 == len(text_2):
            return 0

        match = 0
        if text_1[idx_1] == text_2[idx_2]:
            return 1 + helper(idx_1 + 1, idx_2 + 1)

        return max(helper(idx_1 + 1, idx_2), helper(idx_1, idx_2 + 1))

    return helper(0, 0)


def bottom_up_longest_common_subsequence(text_1, text_2):
    """

    Parameters
    ----------
    text_1 : str
        first string
    text_2 : str
        second string

    Returns
    -------
    int
        length of the longest common subsequence

    >>> bottom_up_longest_common_subsequence("abcde", "ace")
    3
    """
    cache = [[0 for _ in range(len(text_2) + 1)] for _ in range(len(text_1) + 1)]

    for idx_1 in range(1, len(text_1) + 1):
        for idx_2 in range(1, len(text_2) + 1):
            char_1, char_2 = text_1[idx_1 - 1], text_2[idx_2 - 1]
            if char_1 == char_2:
                cache[idx_1][idx_2] = cache[idx_1 - 1][idx_2 - 1] + 1
            else:
                cache[idx_1][idx_2] = max(cache[idx_1 - 1][idx_2], cache[idx_1][idx_2 - 1])

    return cache[len(text_1)][len(text_2)]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
