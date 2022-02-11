"""
Problem Statement
----------------
You are climbing a staircase. It takes n steps to reach the top.  Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Input
-----
number of steps

Output
-------
number of  distinct ways to climb n stairs
"""


def num_ways_to_climb_stairs(n):
    def helper(steps):
        if steps == n:
            return 1
        if steps > n:
            return 0

        return helper(steps + 1) + helper(steps + 2)

    return helper(0)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
