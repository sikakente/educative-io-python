"""
Problem Statement
----------------
You are given an integer arrays height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Input
-----
List of heights

Output
------
Max area
"""


def container_with_most_water(heights):
    """

    Parameters
    ----------
    heights : list
        A list of integers representing heights of containers

    Returns
    -------
    int
        area of container with most water

    >>> container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7])
    49

    >>> container_with_most_water([1, 1])
    1
    """

    max_area = 0
    left_idx, right_idx = 0, len(heights) - 1

    while left_idx < right_idx:
        left_height, right_height = heights[left_idx], heights[right_idx]
        min_height = min(left_height, right_height)
        width = right_idx - left_idx
        current_area = min_height * width
        if left_height < right_height:
            left_idx += 1
        elif right_height < left_height:
            right_idx -= 1
        else:
            left_idx += 1
            right_idx -= 1
        max_area = max(current_area, max_area)

    return max_area


if __name__ == '__main__':
    import doctest

    doctest.testmod()
