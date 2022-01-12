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


if __name__ == '__main__':
    import doctest

    doctest.testmod()
