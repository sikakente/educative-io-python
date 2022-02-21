"""
Problem Statement
----------------
You are given an arrays of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.  Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).  Return intervals after the insertion.


Input
-----
List of intervals and interval to insert

Output
-------
list of merged intervals
"""


def insert_intervals(intervals, new_interval):
    new_interval_lower_bound, new_interval_upper_bound = new_interval[0], new_interval[1]

    # put at end if the lower bound is greater than the largest number in the intervals
    if new_interval_lower_bound > intervals[-1][1]:
        return intervals + [new_interval]

    # put at beginning
    if new_interval_upper_bound < intervals[0][0]:
        return [new_interval] + intervals

    # possible merge
    merge_start_index = -1
    merge_end_index = -1

    # find index of lower bound on new interval
    for interval_index, interval in enumerate(intervals):
        interval_lower_bound, interval_upper_bound = interval[0], interval[1]
        if interval_lower_bound <= new_interval_lower_bound <= interval_upper_bound or \
                new_interval_lower_bound < interval_lower_bound:
            merge_start_index = interval_index
            merge_end_index = interval_index
            break

    # if we couldn't find an index to insert
    if merge_start_index == -1:
        intervals.append(new_interval)
        return intervals

    for interval_index in range(merge_start_index + 1, len(intervals)):
        interval_lower_bound, interval_upper_bound = intervals[interval_index][0], intervals[interval_index][1]
        if new_interval_upper_bound >= interval_lower_bound:
            merge_end_index = interval_index
        elif new_interval_upper_bound < interval_lower_bound:
            break

    merge_interval_lower_bound = min(new_interval_lower_bound, intervals[merge_start_index][0])
    merge_interval_upper_bound = max(new_interval_upper_bound, intervals[merge_end_index][1])

    intervals_before_merge = intervals[0:merge_start_index]
    intervals_after_merge = intervals[min(merge_end_index + 1, len(intervals)):len(intervals)]

    merged_intervals = []
    merged_intervals.extend(intervals_before_merge)
    merged_intervals.append([merge_interval_lower_bound, merge_interval_upper_bound])
    merged_intervals.extend(intervals_after_merge)

    return merged_intervals


if __name__ == '__main__':
    import doctest

    doctest.testmod()
