"""
Problem Statement
----------------
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Input
-----
a grid

Output
-------
number of islands
"""


def num_islands(grid):
    m = len(grid)
    n = len(grid[0])

    is_visited = [[False for _ in range(n)] for _ in range(m)]

    def neighbors(row, col):
        mask = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return [(row + row_mask, col + col_mask) for row_mask, col_mask in mask if
                0 <= row + row_mask < m and 0 <= col + col_mask < n]

    def dfs(row, col):
        if not is_visited[row][col]:
            is_visited[row][col] = True

            for n_row, n_col in neighbors(row, col):
                if not is_visited[n_row][n_col] and grid[n_row][n_col] == "1":
                    dfs(n_row, n_col)

    island_count = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == "1" and not is_visited[row][col]:
                dfs(row, col)
                island_count += 1
            else:
                is_visited[row][col] = True

    return island_count


if __name__ == '__main__':
    import doctest

    doctest.testmod()
