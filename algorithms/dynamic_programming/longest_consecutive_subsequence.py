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


if __name__ == '__main__':
    import doctest

    doctest.testmod()
