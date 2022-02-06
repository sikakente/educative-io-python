"""
Problem Statement
----------------
Given an m x n matrix, return all elements of the matrix in spiral order.


Input
-----
Input matrix

Output
-------
list of items in spiral order
"""


def spiral_matrix(matrix):
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    num_items = len(matrix) * len(matrix[0])
    num_items_visited = 0
    items_visited = []
    while num_items_visited < num_items:
        # go right -->
        for col in range(left, right + 1):
            items_visited.append(matrix[top][col])
            num_items_visited += 1

        # update top boundary
        top += 1

        if num_items_visited == num_items:
            break

        # go down   |
        #           V
        for row in range(top, bottom + 1):
            items_visited.append(matrix[row][right])
            num_items_visited += 1

        # update right boundary
        right -= 1

        if num_items_visited == num_items:
            break

        # go left <-
        for col in reversed(range(left, right + 1)):
            items_visited.append(matrix[bottom][col])
            num_items_visited += 1

        # update bottom boundary
        bottom -= 1

        if num_items_visited == num_items:
            break

        for row in reversed(range(top, bottom + 1)):
            items_visited.append(matrix[row][left])
            num_items_visited += 1

        # update left boundary
        left += 1

        if num_items_visited == num_items:
            break

    return items_visited


if __name__ == '__main__':
    import doctest

    doctest.testmod()
