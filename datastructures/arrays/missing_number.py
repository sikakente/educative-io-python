"""
Problem Statement
----------------
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


Input
-----
list of numbers

Output
-------
the missing number
"""


def missing_number(nums):
    if 0 not in nums:
        return 0
    n = len(nums)
    actual = sum(nums)
    expected_sum = (n * (n + 1)) // 2

    if expected_sum != actual:
        return int(expected_sum - actual)
    return -1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
