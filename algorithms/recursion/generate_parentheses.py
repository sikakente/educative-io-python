"""
Problem Statement
----------------
Generate all valid parentheses


Input
-----
number of parenthesis

Output
-------
list of parentheses
"""


def generate_parentheses(n):
    if n == 0:
        return []
    if n == 1:
        return ["()"]
    result = []

    CLOSE, OPEN = ")", "("

    def helper(opened=0, closed=0, current=[]):
        if opened == n and closed == n:
            result.append("".join(current[:]))
            return

        if closed > opened:
            return
        
        if opened == n and closed < n:
            current.append(CLOSE)
            helper(opened, closed + 1, current)
            current.pop()
            return

        if opened == closed:
            current.append(OPEN)
            helper(opened + 1, closed, current)
            current.pop()
            return

        current.append(OPEN)
        helper(opened + 1, closed, current)
        current.pop()

        current.append(CLOSE)
        helper(opened, closed + 1, current)
        current.pop()

        return

    helper(0, 0)
    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
