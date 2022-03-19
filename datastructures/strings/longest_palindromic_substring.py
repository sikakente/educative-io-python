"""
Problem Statement
-----------------
Given a string s, return the longest palindromic substring in s.

Input
-----
A string of letters

Output
------
An string representing the longest palindromic substring
"""


def longest_palindromic_substring(input_string):
    # check even and odd palindromes
    # find max length between longer palindrome and current longest

    def palindrome_starting_from(start, end):
        while start >= 0 and end < len(input_string):
            left_char, right_char = input_string[start], input_string[end]
            if left_char != right_char:
                break
            start -= 1
            end += 1
        return start, end

    longest_palindrome = (0, 0)

    for index, char in enumerate(input_string):
        even_palindrome = palindrome_starting_from(index - 1, index)
        odd_palindrome = palindrome_starting_from(index, index)
        current_longest = max(odd_palindrome, even_palindrome, key=lambda k: k[1] - k[0])
        longest_palindrome = max(current_longest, longest_palindrome, key=lambda k: k[1] - k[0])

    left_idx, right_idx = longest_palindrome
    return input_string[left_idx + 1:right_idx]


def recursive_longest_palindromic_substring(input_string):
    all_palindromes = []

    def helper(start, end):
        if start == end:
            all_palindromes.append(input_string[start:end + 1])
            return 1
        if start > end:
            return 0

        longest = 0
        if input_string[start] == input_string[end]:
            longest_inbetween = helper(start + 1, end - 1)
            if longest_inbetween + 2 == (end - start) + 1:
                all_palindromes.append(input_string[start:end + 1])
                longest = longest_inbetween + 2
        return max(longest, helper(start + 1, end), helper(start, end - 1))

    return helper(0, len(input_string) - 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
