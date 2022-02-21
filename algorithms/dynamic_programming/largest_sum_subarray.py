"""
Problem Statement
----------------
Given an arrays, find the contiguous subarray with the largest sum.

Input
-----
Array of integers

Output
------
The largest subarray sum
"""


def largest_subarray_sum(numbers):
    """
    Finds the largest subarray sum from a list of integers.

    It uses Kadane's algorithm to do this.

    Same as max sum subarray

    Parameters
    ----------
    numbers : list
        a list of integers

    Returns
    -------
    int
        the largest subarray sum

    >>> largest_subarray_sum([-4, 2, -5, 1, 2, 3, 6, -5, 1])
    12
    """
    list_size = len(numbers)
    if list_size <= 0:
        return 0

    current_max = numbers[0]
    global_max = numbers[0]

    for i in range(1, list_size):
        current_num = numbers[i]
        current_max = max(current_num + current_max, current_num)
        global_max = max(global_max, current_max)

    return global_max


if __name__ == '__main__':
    import doctest

    doctest.testmod()
