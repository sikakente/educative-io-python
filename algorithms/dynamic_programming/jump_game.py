"""
Problem Statement
----------------
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.  Return true if you can reach the last index, or false otherwise.


Input
-----
list of steps

Output
-------
Boolean indicating whether we can jump to the last position
"""


def jump_game(steps):
    if not steps:
        return False
    final_position = len(steps) - 1

    def helper(index):
        if index == final_position:
            return True
        max_steps_at_current_position = steps[index]
        for step in range(max_steps_at_current_position):
            next_step = step + 1
            if helper(index + next_step):
                return True

        return False

    return helper(0)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
