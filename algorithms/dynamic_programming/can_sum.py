"""
Problem Statement
-----------------
Given a list of integers, and a target sum write a function to find if
the numbers in the list can sum up to the target sum.
You can assume that the list will only consist of positive integers.

 Input
 -----
 A list of positive integers
 An integer

 Output
 ------
 A boolean. True if such subsets exist and False if they do not
"""


def recursive_can_sum(numbers, target):
    """

    Parameters
    ----------
    numbers : list of integers
    target : int
        target sum

    Returns
    -------
    bool
        Boolean representing whether subsets exist which are equal to each other

    >>> recursive_can_sum([1, 2, 3, 4], 5)
    True

    """
    list_size = len(numbers)
    subsets = []

    def can_sum_helper(remaining_target, current_index):
        if remaining_target < 0:
            return False
        if remaining_target == 0:
            return True
        if current_index == list_size:
            return False
        if numbers[current_index] <= remaining_target:
            if can_sum_helper(remaining_target - numbers[current_index], current_index + 1):
                return True
        return can_sum_helper(remaining_target, current_index + 1)

    return can_sum_helper(target, 0)


def memoized_can_sum(numbers, target):
    """

    Parameters
    ----------
    numbers : list of integers
    target : int
        target sum

    Returns
    -------
    bool
        Boolean representing whether subsets exist which are equal to each other

    >>> memoized_can_sum([1, 2, 3, 4], 5)
    True

    """
    list_size = len(numbers)
    cache = {}

    def can_sum_helper(remaining_target, current_index):
        if (remaining_target, current_index) in cache:
            return cache[(remaining_target, current_index)]
        if remaining_target < 0:
            return False
        if remaining_target == 0:
            return True
        if current_index == list_size:
            return False
        if numbers[current_index] <= remaining_target:
            if can_sum_helper(remaining_target - numbers[current_index], current_index + 1):
                cache[(remaining_target, current_index)] = True
                return cache[(remaining_target, current_index)]
        cache[(remaining_target, current_index)] = can_sum_helper(remaining_target, current_index + 1)
        return cache[(remaining_target, current_index)]

    return can_sum_helper(target, 0)


def bottom_up_can_sum(numbers, target):
    """

    Parameters
    ----------
    numbers : list of integers
    target : int
        target sum

    Returns
    -------
    bool
        Boolean representing whether subsets exist which are equal to each other

    >>> bottom_up_can_sum([1, 2, 3, 4], 5)
    True

    """
    list_size = len(numbers)
    cache = [[False for _ in range(target + 1)] for _ in range(list_size + 1)]

    # initialize all values in when the target is 0 to True
    for i in range(list_size + 1):
        cache[i][0] = True

    for number_index in range(1, list_size + 1):
        current_number = numbers[number_index - 1]
        for current_target in range(1, target + 1):
            if current_number <= current_target:
                cache[number_index][current_target] = cache[number_index][current_target - current_number] or \
                                                      cache[number_index - 1][current_target]
            else:
                cache[number_index][current_target] = cache[number_index - 1][current_target]

    return cache[list_size][target]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
