"""
Problem Statement
-----------------
Given a string s, find the length of the longest
substring without repeating characters.

Input
-----
String that may or may not contain repeating character

Output
-----
Length of the longest substring without repeating characters
"""


def longest_substring_without_repeating_characters(input_str):
    # keep track of the longest
    longest_substring = ""
    # keep track of the current substring
    current_substring = ""
    # keep track of index of last characters
    character_index_map = {}
    # for each character
    for index, char in enumerate(input_str):
        if char in current_substring:
            start, end = character_index_map[char] + 1, index + 1
            current_substring = current_substring[start:end]
        else:
            current_substring = f"{current_substring}{char}"
        character_index_map[char] = index
        longest_substring = max(longest_substring, current_substring, key=len)

    return len(longest_substring)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
