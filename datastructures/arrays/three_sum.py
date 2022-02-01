"""
Problem Statement
----------------
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
"""


def three_sum(numbers):
    """

    Parameters
    ----------
    numbers : list
        A list of integers

    Returns
    -------
    list
        containing triplets

    """

    list_size = len(numbers)
    if list_size < 3:
        return []

    triplets = set()

    # sort list
    # for each item to n - 2
    numbers = list(sorted(numbers))

    for i in range(list_size - 3):
        current_num = numbers[i]
        left, right = i + 1, list_size - 1
        while left < right:
            left_num, right_num = numbers[left], numbers[right]
            current_sum = current_num + left_num + right_num
            if current_sum == 0:
                triplets.add((current_num, left_num, right_num))
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return [list(triplet) for triplet in triplets] if triplets else []


if __name__ == '__main__':
    import doctest

    doctest.testmod()
