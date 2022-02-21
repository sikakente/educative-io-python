"""
Problem Statement
----------------
There is an integer arrays nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an
unknown pivot index k (1 <= k < nums.length) such that the resulting arrays is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the arrays nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Input
-----
Partially sorted arrays

Output
-------
Index of number being search for
"""


def search_rotated_sorted_array(numbers, target):
    hi = len(numbers) - 1
    lo = 0

    while lo <= hi:
        mid = (hi + lo) // 2
        if numbers[mid] == target:
            return mid
        if numbers[lo] <= numbers[mid]:
            if numbers[lo] <= target <= numbers[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if numbers[mid] <= target <= numbers[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    return -1


def search_rotated_sorted_array_2(numbers, target):
    list_size = len(numbers)

    def get_pivot(lo, hi):
        while lo < hi:
            mid = (lo + hi) // 2
            if numbers[mid] >= numbers[0]:
                lo = mid + 1
            else:
                hi = mid

        return lo

    def binary_search(lo, hi):
        while lo <= hi:
            mid = (lo + hi) // 2
            if numbers[mid] == target:
                return mid
            if target < numbers[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1

    high, low = list_size - 1, 0
    pivot = get_pivot(low, high)
    return binary_search(pivot, list_size - 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
