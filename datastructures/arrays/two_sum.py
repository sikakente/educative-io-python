"""
Problem Statement
-----------------
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input
-----
List of integers

Output
------
Indices of the two numbers that sum up to the target
"""


def two_sum(numbers, target):
    """

    Parameters
    ----------
    numbers : list
        a list of integers
    target : int
        the target sum

    Returns
    list
        a list of indices
    -------

    >>> two_sum([2,7,11,15], 9)
    [0, 1]

    """
    num_index_map = {}

    for idx, num in enumerate(numbers):
        difference = target - num
        if difference in num_index_map:
            return [num_index_map[difference], idx]
        num_index_map[num] = idx

    return []


if __name__ == '__main__':
    import doctest

    doctest.testmod()
