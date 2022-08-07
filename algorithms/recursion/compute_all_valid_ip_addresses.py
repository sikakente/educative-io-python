"""
Problem Statement
----------------
Compute all valid ip addresses from a string of number


Input
-----
str

Output
-------
list
"""


def compute_all_valid_ip_addresses(input_str):
    n = len(input_str)
    result = []
    current_pair = []

    def compute_ip_helper(start, remaining_dot, current_string):
        if current_string and int(current_string) > 256:
            return
        if current_string.startswith("00"):
            return
        if current_string and 1 <= int(current_string) < 256 and current_string.startswith('0'):
            return
        if len(current_pair) == 4 and start < n:
            return

        if len(current_pair) == 4 and start == n:
            result.append('.'.join(current_pair))
            return

        for i in range(start, min(start + 3, n)):
            current_substring = input_str[start:i + 1]
            current_pair.append(current_substring)
            compute_ip_helper(i + 1, remaining_dot - 1, current_substring)
            current_pair.pop()

    compute_ip_helper(0, 3, "")
    print(result)

    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
