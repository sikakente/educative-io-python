"""
Problem Statement
-----------------
Find the maximum sum of a subsequence made up of nonadjacent elements in an arrays.

Input
-----
A list of integers

Output
------
The max sum of non-adjacent numbers in the given list

"""


def max_sum_subsequence(numbers):
    """

    Parameters
    ----------
    numbers : list
        A list of integers

    Returns
    -------
    int
        The maximum sum of non adjacent numbers in the list

    >>> max_sum_subsequence([1, 6, 10, 14, -5, -1, 2, -1, 3])
    25
    """
    # base case
    list_size = len(numbers)
    if list_size <= 0:
        return 0
    if list_size == 1:
        return numbers[0]
    if list_size == 2:
        return max(numbers)

    max_sums = [num for num in numbers]

    for i in range(2, list_size):
        max_sums[i] = max(max_sums[i] + max_sums[i - 2], max_sums[i - 1], max_sums[i - 2])

    return max_sums[-1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
