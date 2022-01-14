"""
Problem Statement
-----------------
Given a list of integers, write a function to find if any two
subsets of the input list exist—such that the sum of both subsets
 is equal. You can assume that the list will only consist of
 positive integers.

 Input
 -----
 A list of positive integers

 Output
 ------
 A boolean. True if such subsets exist and False if they do not
"""


def recursive_partition_problem(numbers):
    """

    Parameters
    ----------
    numbers : list of integers

    Returns
    -------
    (bool, list)
        Boolean representing whether subsets exist which are equal to each other

    >>> recursive_partition_problem([1, 2, 3, 4])
    (True, [[1, 4], [2, 3]])

    """
    sum_of_numbers = sum(numbers)
    half_sum_of_numbers = sum_of_numbers / 2
    is_even = sum_of_numbers % 2 == 0
    if not is_even:
        return False
    list_size = len(numbers)
    subsets = []

    def pp(remaining_target, current_index, current_subset):
        if remaining_target < 0:
            return False
        if remaining_target == 0:
            subsets.append(current_subset[:])
            return True
        if current_index == list_size:
            return False
        current_subset.append(numbers[current_index])
        including = pp(remaining_target - numbers[current_index], current_index + 1, current_subset)
        current_subset.pop()
        excluding = pp(remaining_target, current_index + 1, current_subset)
        return including or excluding

    return pp(half_sum_of_numbers, 0, []), subsets


def memoized_partition_problem(numbers):
    """

    Parameters
    ----------
    numbers : list of integers

    Returns
    -------
    (bool, list)
        Boolean representing whether subsets exist which are equal to each other

    >>> memoized_partition_problem([1, 2, 3, 4])
    (True, [[1, 4], [2, 3]])

    """
    sum_of_numbers = sum(numbers)
    half_sum_of_numbers = sum_of_numbers / 2
    is_even = sum_of_numbers % 2 == 0
    if not is_even:
        return False
    list_size = len(numbers)
    subsets = []
    cache = {}

    def pp(remaining_target, current_index, current_subset):
        if (remaining_target, current_index) in cache:
            return cache[(remaining_target, current_index)]
        if remaining_target < 0:
            return False
        if remaining_target == 0:
            subsets.append(current_subset[:])
            return True
        if current_index == list_size:
            return False
        current_subset.append(numbers[current_index])
        including = pp(remaining_target - numbers[current_index], current_index + 1, current_subset)
        current_subset.pop()
        excluding = pp(remaining_target, current_index + 1, current_subset)
        cache[(remaining_target, current_index)] = including or excluding
        return cache[(remaining_target, current_index)]

    return pp(half_sum_of_numbers, 0, []), subsets


def bottom_up_partition_problem(numbers):
    """

    Parameters
    ----------
    numbers : list of integers

    Returns
    -------
    bool
        Boolean representing whether subsets exist which are equal to each other

    >>> bottom_up_partition_problem([1, 2, 3, 4])
    True

    """
    sum_of_numbers = sum(numbers)
    target_sum = sum_of_numbers // 2
    is_even = sum_of_numbers % 2 == 0
    if not is_even:
        return False
    list_size = len(numbers)
    cache = [[False for _ in range(target_sum + 1)] for _ in range(list_size + 1)]

    # initialize all values in when the target is 0 to True
    for i in range(list_size + 1):
        cache[i][0] = True

    for number_index in range(1, list_size + 1):
        current_number = numbers[number_index - 1]
        for current_target in range(1, target_sum + 1):
            if current_number <= current_target:
                cache[number_index][current_target] = cache[number_index - 1][current_target - current_number] or \
                                                      cache[number_index - 1][current_target]
            else:
                cache[number_index][current_target] = cache[number_index - 1][current_target]

    return cache[list_size][target_sum]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
