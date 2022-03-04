"""
Problem Statement
----------------
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Input
-----
a list of numbers and k

Output
-------
a list of k frequent elements
"""
import heapq
from collections import Counter


def top_k_frequent(nums, k):
    num_freq = Counter(nums)
    frequency_heap = [(-freq, num) for num, freq in num_freq.items()]
    heapq.heapify(frequency_heap)
    top_k = []
    for _ in range(k):
        _, num = heapq.heappop(frequency_heap)
        top_k.append(num)

    return top_k


if __name__ == '__main__':
    import doctest

    doctest.testmod()
