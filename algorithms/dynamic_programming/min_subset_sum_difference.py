"""
Problem Statement
-----------------
Given a set of positive numbers, partition the set into two
subsets with minimum difference between their subset sums.

Input
-----
List of positive numbers

Output
------
An integer representing the smallest difference between subset in a list
"""


def min_subset_sum_difference(numbers):
    """

    Parameters
    ----------
    numbers : list
        A list of positve numbers

    Returns
    -------
    int
        the minimum difference between subsets of the list

    >>> min_subset_sum_difference([1, 2, 3, 9])
    3
    """

    def helper(idx, sum_1, sum_2):
        if idx == len(numbers):
            return abs(sum_1 - sum_2)

        current_num = numbers[idx]
        difference_1 = helper(idx + 1, sum_1 + current_num, sum_2)
        difference_2 = helper(idx + 1, sum_1, sum_2 + current_num)

        return min(difference_1, difference_2)

    return helper(0, 0, 0)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
