"""
Problem Statement
----------------
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that
every character in t (including duplicates) is included in the window. If there is no such substring,
return the empty string "".  The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.


Input
-----
two strings

Output
-------
length of the minimum substring matching containing all
"""
from collections import Counter


def minimum_window_substring(s, t):
    s_len = len(s)
    t_len = len(t)

    if t_len > s_len:
        return ""

    t_counter = Counter(t)

    left = 0
    right = 0

    min_substring = f"{s}_NULL"
    min_substring_length = s_len + 5

    count = sum(t_counter.values())

    while right < s_len:
        right_char = s[right]
        current_substring = s[left:right + 1]

        # moving right
        if right_char in t_counter:
            t_counter[right_char] = t_counter[right_char] - 1
            if t_counter[right_char] >= 0:
                count -= 1
                if count == 0:  # match
                    # move left
                    min_substring = min(min_substring, s[left:right + 1], key=len)
                    min_substring_length = min(min_substring_length, (right + 1) - left)
                    while left <= right:
                        left_char = s[left]
                        if left_char in t_counter and count > 0:
                            break
                        left += 1
                        current_substring = s[left:right + 1]
                        if left_char in t_counter:
                            t_counter[left_char] += 1
                        if t_counter[left_char] > 0:
                            count += 1
                        if count == 0:  # possible match
                            min_substring = min(min_substring, s[left:right + 1], key=len)
                            min_substring_length = min(min_substring_length, (right + 1) - left)

        right += 1

    return "" if min_substring == f"{s}_NULL" else min_substring


if __name__ == '__main__':
    import doctest

    doctest.testmod()
