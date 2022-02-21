"""
Problem Statement
----------------
Given an integer arrays nums, return an arrays answer such that answer[i] is equal to the product of all the elements of nums except nums[i].  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.  You must write an algorithm that runs in O(n) time and without using the division operation.


Input
-----
number of integers

Output
-------
list of products
"""


def product_except_self(nums):
    num_size = len(nums)
    left_to_right_products, right_to_left_products = [1 for _ in nums], [1 for _ in nums]

    for i in range(1, num_size):
        left_to_right_products[i] = nums[i - 1] * left_to_right_products[i - 1]

    for i in reversed(range(0, num_size - 1)):
        right_to_left_products[i] = nums[i + 1] * right_to_left_products[i + 1]

    return [left_to_right_products[i] * right_to_left_products[i] for i in range(num_size)]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
