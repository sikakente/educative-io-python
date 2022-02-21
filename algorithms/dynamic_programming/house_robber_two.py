"""
Problem Statement
----------------
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.  Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Input
-----
list of numbers

Output
-------
maximum money we can rob (int)
"""


def rob(nums):
    num_size = len(nums)
    if num_size == 0:
        return 0
    if num_size <= 2:
        return max(nums)

    return max(rob_helper(0, num_size - 1, nums), rob_helper(1, num_size, nums))


def rob_helper(start, end, nums):
    # uses house robber problem
    num_size = len(nums)
    if end - start == 1:
        return nums[start]
    if end - start == 2:
        return max(nums[start], nums[start + 1])
    money_sums = [0 for _ in range(num_size)]
    money_sums[start] = nums[start]
    money_sums[start + 1] = max(nums[start], nums[start + 1])
    for i in range(start, end):
        current_money = nums[i]
        money_sums[i] = max(current_money + money_sums[i - 2], money_sums[i - 1])

    return money_sums[end - 1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
