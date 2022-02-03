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


if __name__ == '__main__':
    import doctest

    doctest.testmod()
