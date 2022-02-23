"""
Problem Statement
----------------
Given an integer array nums, return the length of the longest strictly increasing subsequence.  A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].


Input
-----
list of numbers

Output
-------
length of the longest increasing subsequence
"""


def longest_increasing_subsequence(nums):
    n = len(nums)

    def helper(idx, previous_num):
        if idx == n:
            return 0
        current_num = nums[idx]
        including = 0
        if previous_num < current_num:
            including = 1 + helper(idx + 1, current_num)

        return max(including, helper(idx + 1, previous_num))

    return helper(0, float("-inf"))


def longest_increasing_subsequence_bottom_up(nums):
    n = len(nums)
    cache = [1 for _ in range(n + 1)]
    cache[0] = 0

    for i in range(1, n + 1):
        current_num = nums[i - 1]
        for j in range(i):
            if nums[j - 1] < current_num:
                cache[i] = max(1 + cache[j], cache[i])

    return max(cache)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
