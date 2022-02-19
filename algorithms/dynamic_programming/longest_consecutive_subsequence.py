"""
Problem Statement
----------------
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.


Input
-----
a list of integers

Output
-------
The size of the longest consecutive subsequence
"""
from collections import defaultdict


def longest_consecutive_subsequence(nums):
    nums_size = len(nums)
    if nums_size == 0:
        return 0
    if nums_size == 1:
        return 1

    nums.sort()
    cache = {}

    def helper(idx, previous_num):
        if idx in cache:
            return cache[idx]
        if idx == nums_size:
            return 0

        current_num = nums[idx]
        including = 0
        if current_num - previous_num == 1:
            including = 1 + helper(idx + 1, current_num)

        excluding = helper(idx + 1, previous_num)
        cache[idx] = max(including, excluding)
        return cache[idx]

    res = helper(0, nums[0] - 1)
    return res


def longest_consecutive_subsequence_using_sliding_window(nums):
    nums_size = len(nums)
    if nums_size == 0:
        return 0
    if nums_size == 1:
        return 1

    nums.sort()

    right = left = 0
    lcs_window_left, lcs_window_right = 0, 0
    previous_num = nums[0] - 1
    while right < nums_size:
        current_num = nums[right]
        if current_num - previous_num != 1:
            left = right
        else:
            if lcs_window_right - lcs_window_left < right - left:
                lcs_window_left, lcs_window_right = left, right

        right += 1
        previous_num = current_num

    return lcs_window_right + 1 - lcs_window_left


def lcs_linear_run_time(nums):
    nums_size = len(nums)
    if nums_size == 0:
        return 0
    if nums_size == 1:
        return 1

    num_checker = {num: False for num in nums}
    max_window_size = 0

    nums_to_visit = len(num_checker.keys())
    nums_seen = 0

    for num, used in num_checker.items():
        if used:
            continue
        current_window_size = 1
        num_checker[num] = True
        nums_seen += 1
        # check numbers above
        next_num = num + 1
        while next_num in num_checker:
            num_checker[next_num] = True
            next_num += 1
            current_window_size += 1
            nums_seen += 1

        # check numbers below
        next_num = num - 1
        while next_num in num_checker:
            num_checker[next_num] = True
            next_num -= 1
            current_window_size += 1
            nums_seen += 1

        max_window_size = max(current_window_size, max_window_size)
        if nums_seen == nums_to_visit:
            break

    return max_window_size


if __name__ == '__main__':
    import doctest

    doctest.testmod()
