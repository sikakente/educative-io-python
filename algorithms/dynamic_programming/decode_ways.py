"""
Problem Statement
----------------
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2" ...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the
mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.


Input
-----
encoded string

Output
-------
number of ways to decode
"""


def decode_ways(s):
    allowed_chars = set([f"{i}" for i in range(1, 27)])

    def helper(encoded_string):
        if encoded_string.startswith("0"):
            return 0
        if encoded_string == "":
            return 1

        # decode 1
        decode_1 = 0
        if len(encoded_string) >= 1:
            decoding_1_char = encoded_string[0:1]
            if decoding_1_char in allowed_chars:
                decode_1 = helper(encoded_string[1:])
        # decode 2

        decode_2 = 0
        if len(encoded_string) >= 2:
            decoding_2_char = encoded_string[0:2]
            if decoding_2_char in allowed_chars:
                decode_2 = helper(encoded_string[2:])

        return decode_2 + decode_1

    return helper(s)


def decode_ways_memoized(s):
    allowed_chars = set([f"{i}" for i in range(1, 27)])
    end = len(s)
    cache = {}

    def helper(start):
        if start in cache:
            return cache[start]
        current_string = s[start:end]
        if current_string.startswith("0"):
            return 0
        if start == end:
            return 1

        # decode 1
        decode_1 = 0
        if end - start >= 1:
            decoding_1_char = s[start:start + 1]
            if decoding_1_char in allowed_chars:
                decode_1 = helper(start + 1)
        # decode 2

        decode_2 = 0
        if end - start >= 2:
            decoding_2_char = s[start:start + 2]
            if decoding_2_char in allowed_chars:
                decode_2 = helper(start + 2)

        cache[start] = decode_2 + decode_1
        return cache[start]

    return helper(0)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
