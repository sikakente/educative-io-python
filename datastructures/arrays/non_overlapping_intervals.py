"""
Problem Statement
----------------
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


Input
-----
a list of intervals

Output
-------
minimum number of intervals to erase
"""


def erase_overlapping_intervals(intervals):
    intervals.sort()
    n = len(intervals)
    previous_interval_end = float("-inf")
    num_erased = 0
    for interval in intervals:
        # no overlap
        if interval[0] >= previous_interval_end:
            previous_interval_end = interval[1]
        else:
            num_erased += 1
            previous_interval_end = min(previous_interval_end, interval[1])

    return num_erased


if __name__ == '__main__':
    import doctest

    doctest.testmod()
