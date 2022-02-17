"""
Problem Statement
----------------
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.  Given a string s, return true if it is a palindrome, or
false otherwise.


Input
-----
a long string

Output
-------
boolean showing whether it is a valid palindrome
"""


def valid_palindrome(s):
    chars_to_remove = "abcdefghijklmnopqrstuvwxyz0123456789"
    s = s.lower()
    characters = []
    for char in s:
        if char in chars_to_remove:
            characters.append(char)

    left, right = 0, len(characters) - 1
    while left < right:
        if characters[left] != characters[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    import doctest

    doctest.testmod()
