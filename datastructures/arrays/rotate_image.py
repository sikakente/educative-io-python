"""
Problem Statement
----------------
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.


Input
-----
a matrix to rotate

Output
-------
a rotated matrix
"""


def rotate_image(matrix):
    n = len(matrix)

    def generate_final_positions():
        positions = {}
        for row in range(n):
            for col in range(n):
                final_row = col
                final_col = ((n - 1) - row) % n
                positions[(final_row, final_col)] = matrix[row][col]

        return positions

    final_positions = generate_final_positions()

    for final_position, number in final_positions.items():
        row, col = final_position
        matrix[row][col] = number
    return matrix


def rotate_image_faster(matrix):
    """
    This is a faster approach from the discussions on leetcode:
    https://leetcode.com/problems/rotate-image/discuss/1737976/Python-or-visual-explanation-or-complexity-analysis

    It first transposes the matrix. i.e. or diagonal mirror
        ----------
        |\       |
        |  \     |
        |     \  |
        ----------
        Formula: matrix[r][c], matrix[c][r] =  matrix[c][r], matrix[r][c]
    Then Folds the transposed matrix i.e. or horizontal mirror
        ----------
        |   |    |
        |   |    |
        |   |    |
        ----------
        - matrix[r][c], matrix[r][((n-1)-c)%n)] = matrix[r][((n-1)-c)%n)], matrix[r][c]


    Parameters
    ----------
    matrix : list
        matrix representing an image
        this is an n X n matrix

    Returns
    -------
    list
        The rotated matrix

    """
    row_length, column_length = len(matrix), len(matrix[0])

    def transpose():
        for r in range(row_length):
            for c in range(column_length):
                if r > c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    def fold():
        for r in range(row_length):
            for c in range(column_length):
                center = column_length // 2
                if c < center:
                    reflected_column = ((column_length - 1) - c) % column_length
                    matrix[r][c], matrix[r][reflected_column] = matrix[r][reflected_column], matrix[r][c]

    transpose()
    fold()
    return matrix


if __name__ == '__main__':
    import doctest

    doctest.testmod()
