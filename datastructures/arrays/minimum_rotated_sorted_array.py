"""
Problem Statement
----------------
Suppose an arrays of length n sorted in ascending order is rotated between 1 and n times.
For example, the arrays nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an arrays [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the arrays [a[n-1],
a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated arrays nums of unique elements, return the minimum element of this arrays.
You must write an algorithm that runs in O(log n) time.


Input
-----
list of integers

Output
-------
minimum in rotated sorted arrays
"""


def min_in_rotated_sorted_array(nums):
    low, high = 0, len(nums) - 1

    if nums[low] <= nums[high]:
        return nums[low]

    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[0]:
            high = mid
        else:
            low = mid + 1

    min_num = nums[high]
    return min(nums[0], min_num)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
