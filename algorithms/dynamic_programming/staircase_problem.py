"""
Problem Statement
-----------------
A child is running up a staircase with n steps
and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a function to count the number of possible ways
that the child can run up the stairs.

Input
-----
An integer that represents the number of stairs

Output
------
An integer that represents the number of ways
that those stairs can be climbed
"""


def recursive_staircase_problem(n):
    """

    Parameters
    ----------
    n : int
        number of steps

    Returns
    -------
    int
        number of ways a child can run a stairs

    >>> recursive_staircase_problem(4)
    7

    >>> recursive_staircase_problem(0)
    1
    """

    def staircase(m):
        if m == 0:
            return 1
        if m < 0:
            return 0
        return staircase(m - 1) + staircase(m - 2) + staircase(m - 3)

    return staircase(n)


def memoized_staircase_problem(n):
    """

    Parameters
    ----------
    n : int
        number of steps

    Returns
    -------
    int
        number of ways a child can run a stairs

    >>> memoized_staircase_problem(4)
    7

    >>> memoized_staircase_problem(0)
    1
    """
    cache = {}

    def staircase(m):
        if m in cache:
            return cache[m]
        if m == 0:
            return 1
        if m < 0:
            return 0
        cache[m] = staircase(m - 1) + staircase(m - 2) + staircase(m - 3)
        return cache[m]

    return staircase(n)


def bottom_up_staircase_problem(n):
    """

    Parameters
    ----------
    n : int
        number of steps

    Returns
    -------
    int
        number of ways a child can run a stairs

    >>> bottom_up_staircase_problem(4)
    7

    >>> bottom_up_staircase_problem(0)
    1
    """
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1

    strides = [1, 2, 3]

    i = 1

    while i <= n:
        for stride in strides:
            if stride <= i:
                cache[i] += cache[i - stride]
        i += 1

    return cache[n]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
