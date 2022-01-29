"""
Problem Statement
-----------------
Given a list of characters, generate all possible combinations of the character

Input
-----
List of characters e.g. [A, B, C, D]

Output
-----
A list of all possible combinations
"""


def letter_combinations(characters):
    """

    Parameters
    ----------
    characters : list
        A list of characters e.g. [A, B, C]

    Returns
    -------
    list
        A list of all combinations

    >>> letter_combinations(['A', 'B', 'C'])
    [['A', 'B', 'C'], ['A', 'C', 'B'], ['B', 'A', 'C'], ['B', 'C', 'A'], ['C', 'B', 'A'], ['C', 'A', 'B']]
    """
    all_combinations = []

    def helper(current_idx):
        if current_idx == len(characters):
            all_combinations.append(characters[:])
            return

        for i in range(current_idx, len(characters)):
            characters[current_idx], characters[i] = characters[i], characters[current_idx]
            helper(current_idx + 1)
            characters[current_idx], characters[i] = characters[i], characters[current_idx]

    helper(0)
    return all_combinations


if __name__ == '__main__':
    import doctest

    doctest.testmod()
