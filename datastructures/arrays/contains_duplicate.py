"""
Problem Statement
----------------
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Input
-----
list of numbers

Output
-------
boolean
"""


def contains_duplicate(nums):
    dup_checker = set()
    for num in nums:
        if num in dup_checker:
            return True
        dup_checker.add(num)
    return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()
