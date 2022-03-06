"""
Problem Statement
----------------
Given an m x n board of characters and a list of strings words, return all words on the board.  Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.


Input
-----
list of words and board

Output
-------
list of words found
"""

END_SYMBOL = "*"


class PrefixTrie:

    def __init__(self):
        self.root = {}

    def insert(self, text):
        current = self.root
        for char in text:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[END_SYMBOL] = True


def build_dictionary(words):
    trie = PrefixTrie()
    for word in words:
        trie.insert(word)

    return trie.root


def find_words(board, words):
    word_dictionary = build_dictionary(words)
    row_length, col_length = len(board), len(board[0])
    is_visited = [[False for _ in range(col_length)] for _ in range(row_length)]
    found_words = set()

    def get_neighbors(r, c):
        masks = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return [(r + r_mask, c + c_mask) for r_mask, c_mask in masks if
                0 <= r + r_mask < row_length and 0 <= c + c_mask < col_length]

    def dfs(r, c, dictionary, word_so_far):
        current_board_letter = board[r][c]
        if is_visited[r][c]:
            return
        if current_board_letter not in dictionary:
            return

        word_so_far += current_board_letter
        if END_SYMBOL in dictionary[current_board_letter]:
            found_words.add(word_so_far)

        is_visited[r][c] = True
        dictionary = dictionary[current_board_letter]
        for n_r, n_c in get_neighbors(r, c):
            if not is_visited[n_r][n_c]:
                dfs(n_r, n_c, dictionary, word_so_far)

        is_visited[r][c] = False

    for row in range(row_length):
        for col in range(col_length):
            current_letter = board[row][col]
            if current_letter in word_dictionary:
                dfs(row, col, word_dictionary, "")

    return list(found_words)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
