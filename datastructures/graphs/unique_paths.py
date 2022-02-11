"""
Problem Statement
----------------
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take
to reach the bottom-right corner.  The test cases are generated so that the answer will be less
than or equal to 2 * 109.

Input
-----
Dimensions of the grid or graph

Output
-------
number of unique paths
"""


def unique_paths(m, n):
    cache = {}

    def helper(down, right):
        if (down, right) in cache:
            return cache[(down, right)]
        if down >= m:
            return 0
        if right >= n:
            return 0
        if down == m - 1 and right == n - 1:
            return 1

        going_down = helper(down + 1, right)
        going_right = helper(down, right + 1)

        cache[(down, right)] = going_right + going_down
        return cache[(down, right)]

    return helper(0, 0)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
