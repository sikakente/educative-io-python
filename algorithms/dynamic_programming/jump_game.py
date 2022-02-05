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


def jump_game_faster(steps):
    num_steps = len(steps)
    steps_left = steps[0]

    for i in range(1, num_steps):
        # as we take each step we need to reduce the steps we have left
        steps_left -= 1
        # if we have negative steps left it means we can make any more steps from this position
        if steps_left < 0:
            return False
        # if we reach a position where we can make more steps that the steps we have left
        # it means we can reach further so we can update the steps we have left with the steps
        # at this position
        if steps[i] > steps_left:
            steps_left = steps[i]

    return True


if __name__ == '__main__':
    import doctest

    doctest.testmod()
