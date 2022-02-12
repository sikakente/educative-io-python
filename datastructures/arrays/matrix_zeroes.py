"""
Problem Statement
----------------
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.  You must do it in place.


Input
-----
m by n matrix of integers

Output
-------
matrix with zeroes set
"""


def set_matrix_zeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])

    def find_zeros():
        zeros = []
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeros.append((row, col))
        return zeros

    zero_indexes = find_zeros()

    for row, col in zero_indexes:
        # vertical  set, column stays the same
        for row_to_set in range(m):
            matrix[row_to_set][col] = 0

        # horizontal set, row stays the same
        for col_to_set in range(n):
            matrix[row][col_to_set] = 0

    return matrix


if __name__ == '__main__':
    import doctest

    doctest.testmod()
