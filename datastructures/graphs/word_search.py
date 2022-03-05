"""
Problem Statement
----------------
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.


Input
-----
board and word

Output
-------
true or false
"""


def exist(board, word):
    word_length = len(word)
    row_length, col_length = len(board), len(board[0])
    is_visited = [[False for _ in range(col_length)] for _ in range(row_length)]

    def get_neighbors(r, c):
        masks = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return [(r + r_mask, c + c_mask) for r_mask, c_mask in masks if
                0 <= r + r_mask < row_length and 0 <= c + c_mask < col_length]

    def dfs(r, c, word_index, current_word):
        if word_index == word_length:
            return True
        current_board_letter = board[r][c]
        current_word_letter = word[word_index]
        if current_board_letter != current_word_letter:
            return False
        if word_index == word_length - 1 and current_word_letter == current_board_letter:
            return True

        is_visited[r][c] = True
        current_word += current_word_letter

        for n_r, n_c in get_neighbors(r, c):
            if not is_visited[n_r][n_c] and dfs(n_r, n_c, word_index + 1, current_word):
                return True

        is_visited[r][c] = False
        return False

    for row in range(row_length):
        for col in range(col_length):
            current_letter = board[row][col]
            if current_letter == word[0]:
                if dfs(row, col, 0, ""):
                    return True

    return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()
