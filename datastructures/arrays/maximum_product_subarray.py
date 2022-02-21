"""
Problem Statement
----------------
Given an integer arrays nums, find a contiguous non-empty subarray within the arrays that has the largest product, and return the product.  The test cases are generated so that the answer will fit in a 32-bit integer.  A subarray is a contiguous subsequence of the arrays.


Input
-----
a list of integers

Output
-------
Tha maximum product subarray
"""


def maximum_product_subarray(nums):
    # TODO: Explain this solution in detail
    nums_length = len(nums)
    if nums_length < 1:
        return 0

    curr_min = curr_max = nums[0]
    max_product = nums[0]

    # we keep track of min because if we have negative numbers in the list of nums
    # as we continue calculating the product, the product will keep flipping between a negative
    # number (if there are an odd number of negative integers) or a positive number if there are
    # an even number of negative numbers

    for i in range(1, nums_length):
        curr_num = nums[i]
        temp_max = max(curr_num, curr_min * curr_num, curr_max * curr_num)
        curr_min = min(curr_num, curr_max * curr_num, curr_min * curr_num)
        curr_max = temp_max
        max_product = max(curr_max, max_product)

    return max_product


if __name__ == '__main__':
    import doctest

    doctest.testmod()
