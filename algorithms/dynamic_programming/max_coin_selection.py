"""
Problem Statement
----------------
Max coin selection


Input
-----
coins

Output
-------
int
"""


def max_coin_selection(coins):
    n = len(coins)

    def helper(start, end, player_1_coins, player_2_coins):
        if start == end:
            return coins[start]
        if start > end:
            return 0

        play_1 = coins[start] + helper(start + 1, end - 1, player_1_coins + coins[start],
                                       player_2_coins + coins[end])
        play_2 = coins[end] + helper(start + 1, end - 1, player_1_coins + coins[end],
                                     player_2_coins + coins[start])
        return max(play_1, play_2)

    max_change = helper(0, n - 1, 0, 0)
    return max_change


if __name__ == '__main__':
    import doctest

    doctest.testmod()
