"""
Problem Statement
-----------------
Find the number of ways a player can score 'n' runs.

Imagine a game where a player can score 1, 2 or 4 runs. Given a score, n,
find the total number of ways to score n runs.

For example, to score 5 runs, a player can score in 10 ways

Input
-----
Number of runs

Outputs
-------
number of ways to score runs
"""


def recursive_game_scoring(n):
    """

    Parameters
    ----------
    n : int
        The number of runs in a game

    Returns
    -------
    int
        The number of ways to score n runs

    >>> recursive_game_scoring(5)
    10

    """
    scores = [1, 2, 4]
    all_runs = []

    def helper(runs_left, current_runs):
        if runs_left < 0:
            return 0
        if runs_left == 0:
            all_runs.append(current_runs[:])
            return 1
        ways = 0
        for score in scores:
            if score <= runs_left:
                current_runs.append(score)
                ways += helper(runs_left - score, current_runs)
                current_runs.pop()
        return ways

    return helper(n, [])


def memoized_game_scoring(n):
    """

    Parameters
    ----------
    n : int
        The number of runs in a game

    Returns
    -------
    int
        The number of ways to score n runs

    >>> memoized_game_scoring(5)
    10

    """
    scores = [1, 2, 4]
    all_runs = []
    cache = {}

    def helper(runs_left, current_runs):
        if runs_left in cache:
            return cache[runs_left]
        if runs_left < 0:
            return 0
        if runs_left == 0:
            all_runs.append(current_runs[:])
            return 1
        ways = 0
        for score in scores:
            if score <= runs_left:
                current_runs.append(score)
                ways += helper(runs_left - score, current_runs)
                current_runs.pop()
        cache[runs_left] = ways
        return cache[runs_left]

    return helper(n, [])


def bottom_up_game_scoring(n):
    """

    Parameters
    ----------
    n : int
        The number of runs in a game

    Returns
    -------
    int
        The number of ways to score n runs

    >>> bottom_up_game_scoring(5)
    10

    """
    scores = [1, 2, 4]
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1

    for run in range(1, n + 1):
        for score_idx in range(1, len(scores) + 1):
            current_score = scores[score_idx - 1]
            if current_score <= run:
                ways[run] += ways[run - current_score]

    return ways[n]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
