"""
Problem Statement
----------------
Find the longest substring of a string containing `k` distinct characters
Given a string and a positive number k,
find the longest substring of the string containing k distinct characters.
If k is more than the total number of distinct characters in the string, return the whole string.


Input
-----
string of characters

Output
-------
The longest substring containing distinct character
"""
from collections import Counter, defaultdict


def longest_substring_with_k_distinct_characters(input_str, k):
    char_count = Counter(input_str)
    distinct_char_count = len(char_count.keys())
    if k > len(char_count.keys()):
        return input_str

    right = left = 0
    char_checker = defaultdict(int)
    longest_substring_indexes = [0, 0]

    distinct_count = 0

    while right < len(input_str):
        current_char = input_str[right]
        if char_checker[current_char] > 0 and distinct_count == k:
            char_checker[current_char] = char_checker[current_char] + 1
            longest_substring_indexes = max(longest_substring_indexes, [left, right], key=lambda x: x[1] - x[0])
        elif distinct_count == k and char_checker[current_char] == 0:
            # move left
            first_char_to_remove_char = input_str[left]
            char_checker[current_char] = char_checker[current_char] + 1
            distinct_count += 1
            while char_checker[first_char_to_remove_char] > 0 and (right + 1) - left > k:
                char_to_remove_char = input_str[left]
                left += 1
                char_checker[char_to_remove_char] = char_checker[char_to_remove_char] - 1
                longest_substring_indexes = max(longest_substring_indexes, [left, right], key=lambda x: x[1] - x[0])
                if char_to_remove_char != first_char_to_remove_char and char_checker[char_to_remove_char] == 0:
                    distinct_count -= 1
            if input_str[left] != first_char_to_remove_char:
                distinct_count -= 1
        elif distinct_count < k:
            char_checker[current_char] = char_checker[current_char] + 1
            distinct_count += 1
            if distinct_count == k:
                longest_substring_indexes = max(longest_substring_indexes, [left, right], key=lambda x: x[1] - x[0])
        right += 1

    longest_left_idx, longest_right_idx = longest_substring_indexes[0], min(longest_substring_indexes[1] + 1,
                                                                            len(input_str))
    return input_str if longest_right_idx - longest_left_idx == 0 else input_str[longest_left_idx:longest_right_idx]


NUM_CHARS = 128


def longest_substring_with_k_distinct_characters_2(input_str, k):
    char_frequency = [0 for _ in range(NUM_CHARS)]
    left = right = 0
    begin = end = 0
    window = set()
    input_size = len(input_str)

    while right < input_size:
        current_char = input_str[right]
        char_frequency[ord(current_char)] = char_frequency[ord(current_char)] + 1
        window.add(current_char)
        # move left if there are more than k distinct chars in current window
        while len(window) > k:
            left_char = input_str[left]
            char_frequency[ord(left_char)] = char_frequency[ord(left_char)] - 1
            if char_frequency[ord(left_char)] == 0:
                window.remove(left_char)
            left += 1

        # update window size
        if right - left > end - begin:
            begin, end = left, right

        right += 1

    return input_str[begin:end + 1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
