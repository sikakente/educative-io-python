"""
Problem Statement
----------------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Input
-----
string of characters

Output
-------
bool indicating whether the parentheses are valid
"""


def valid_parentheses(input_str):
    parentheses_map = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    starting_parentheses = "({["
    stack = []
    for char in input_str:
        if char in starting_parentheses:
            stack.append(char)
        else:
            if stack.pop() != parentheses_map[char]:
                return False

    return True


if __name__ == '__main__':
    import doctest

    doctest.testmod()
