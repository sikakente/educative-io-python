"""
Problem Statement
----------------
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.


Input
-----
list of intervals

Output
-------
List of merged intervals
"""
from collections import namedtuple

Interval = namedtuple("Interval", "lower_bound, upper_bound")


def merge_intervals(intervals):
    num_intervals = len(intervals)
    intervals = list(sorted(intervals))
    first_interval_lower_bound, first_interval_upper_bound = intervals[0][0], intervals[0][1]
    merged_intervals = [Interval(upper_bound=first_interval_upper_bound, lower_bound=first_interval_lower_bound)]
    for i in range(1, num_intervals):
        current_lower_bound, current_upper_bound = intervals[i][0], intervals[i][1]
        merged_intervals_size = len(merged_intervals)
        merged = False
        for bound_index in range(merged_intervals_size):
            bound = merged_intervals[bound_index]
            if bound.lower_bound <= current_lower_bound <= bound.upper_bound or \
                    bound.lower_bound <= current_upper_bound <= bound.upper_bound:
                new_lower_bound = min(current_lower_bound, bound.lower_bound)
                new_upper_bound = max(current_upper_bound, bound.upper_bound)
                merged_intervals[bound_index] = Interval(lower_bound=new_lower_bound, upper_bound=new_upper_bound)
                merged = True
        if not merged:
            merged_intervals.append(Interval(upper_bound=current_upper_bound, lower_bound=current_lower_bound))

    return [[interval.lower_bound, interval.upper_bound] for interval in merged_intervals]


def merge_intervals_faster(intervals):
    num_intervals = len(intervals)
    intervals = list(sorted(intervals))
    first_interval_lower_bound, first_interval_upper_bound = intervals[0][0], intervals[0][1]
    merged_intervals = [Interval(upper_bound=first_interval_upper_bound, lower_bound=first_interval_lower_bound)]
    for i in range(1, num_intervals):
        current_lower_bound, current_upper_bound = intervals[i][0], intervals[i][1]
        bound = merged_intervals[-1]
        if bound.lower_bound <= current_lower_bound <= bound.upper_bound or \
                bound.lower_bound <= current_upper_bound <= bound.upper_bound:
            new_lower_bound = min(current_lower_bound, bound.lower_bound)
            new_upper_bound = max(current_upper_bound, bound.upper_bound)
            merged_intervals[-1] = Interval(lower_bound=new_lower_bound, upper_bound=new_upper_bound)
        else:
            merged_intervals.append(Interval(upper_bound=current_upper_bound, lower_bound=current_lower_bound))

    return [[interval.lower_bound, interval.upper_bound] for interval in merged_intervals]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
