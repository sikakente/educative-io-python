"""
Problem Statement
----------------
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.  Given an integer arrays nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Input
-----
a list of numbers or houses

Output
-------
maximum amount we can rob
"""


def rob(nums):
    num_size = len(nums)
    if num_size == 0:
        return 0
    if num_size <= 2:
        return max(nums)
    money_sums = [0 for _ in range(num_size)]
    money_sums[0] = nums[0]
    money_sums[1] = max(nums[0], nums[1])
    for i in range(2, num_size):
        current_money = nums[i]
        money_sums[i] = max(current_money + money_sums[i - 2], money_sums[i - 1])

    return money_sums[-1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
