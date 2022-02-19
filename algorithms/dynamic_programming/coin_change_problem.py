"""
Problem Statement
----------------
Given an infinite number of quarters (25 cents), dimes (10 cents),
 nickels (5 cents), and pennies (1 cent), write some code to calculate
 the number of ways to represent n cents.

Input
-----
The values of the coins available to represent the
cents with (the denominations), the number of denominations,
and the number of cents

Output
------
The number of ways that the given number of cents can be represented

"""


def recursive_coin_change(amount, denoms, denoms_length):
    """

    Parameters
    ----------
    amount : int
        Target amount
    denoms : list<int>
        denominations
    denoms_length : int
        number of unique denominations

    Returns
    -------
    int
        count of ways

    >>> recursive_coin_change(10, [25, 10, 5, 1], 4)
    4
    """

    def helper(current_amount, current_index):
        if current_amount == 0:
            return 1
        if current_index == denoms_length:
            return 0

        current_denom = denoms[current_index]
        including = 0
        if current_denom <= current_amount:
            including = helper(current_amount - current_denom, current_index)

        excluding = helper(current_amount, current_index + 1)
        return including + excluding

    return helper(amount, 0)


def memoized_coin_change(amount, denoms, denoms_length):
    """
    Memoized version

    Parameters
    ----------
    amount : int
        Target amount
    denoms : list<int>
        denominations
    denoms_length : int
        number of unique denominations

    Returns
    -------
    int
        count of ways

    >>> memoized_coin_change(10, [25, 10, 5, 1], 4)
    4
    """

    cache = {}

    def helper(current_amount, current_index):
        if (current_amount, current_index) in cache:
            return cache[(current_amount, current_index)]
        if current_amount == 0:
            return 1
        if current_index == denoms_length:
            return 0

        current_denom = denoms[current_index]
        including = 0
        if current_denom <= current_amount:
            including = helper(current_amount - current_denom, current_index)

        excluding = helper(current_amount, current_index + 1)
        cache[(current_amount, current_index)] = including + excluding
        return cache[(current_amount, current_index)]

    return helper(amount, 0)


def bottom_up_coin_change(amount, denoms, denoms_length):
    """

    Parameters
    ----------
    amount : int
        Target amount
    denoms : list<int>
        denominations
    denoms_length : int
        number of unique denominations

    Returns
    -------
    int
        count of ways

    >>> bottom_up_coin_change(10, [25, 10, 5, 1], 4)
    4
    """

    cache = [[0 for _ in range(amount + 1)] for _ in range(denoms_length + 1)]

    for i in range(denoms_length + 1):
        cache[i][0] = 1

    for denom_index in range(1, denoms_length + 1):
        denom = denoms[denom_index - 1]
        for amount in range(1, amount + 1):
            if denom <= amount:
                cache[denom_index][amount] = cache[denom_index][amount - denom] + cache[denom_index - 1][amount]

    return cache[denoms_length][amount]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
