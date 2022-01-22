"""
Problem Statement
-----------------
Given a tall skyscraper and a few eggs, write a function to
figure out how many tries it would take to find which floor
of the skyscraper from which the eggs can be safely dropped
without breaking. Here are some rules;

An egg that survives a fall can be used again. A broken egg must be discarded
The effect of a fall is the same for all eggs
If an egg breaks when dropped, then, it would break if dropped from a higher floor
If an egg survives a fall, then it would survive a shorter fall

Input
-----
Two integers that represent the number of stories of the skyscraper
and number of eggs respectively

Output
------
The least number of egg-droppings to figure out the critical floor
"""


def recursive_egg_drop(eggs, floors):
    """
    Explanation
    When we drop an egg from the floor i, there can be two cases: (1) The egg breaks (2) The egg doesn’t break.

    If the egg breaks after dropping from the i(th) floor, then, we only need to check for floors lower than i
    with remaining eggs; so the problem reduces to i - 1 floors and n - 1 eggs.
    If the egg doesn’t break after dropping from the i(th)  floor, then,
    we only need to check for floors higher than i; so the problem reduces to k - i floors and n eggs.
    Since we need to minimize the number of trials in the worst case, we take the maximum of two cases.
    We consider the max of the two cases above for every floor and choose the floor that yields
    the minimum number of trials.

    Parameters
    ----------
    eggs : int
        number of eggs
    floors : int
        number of floors

    Returns
    -------
    int
        minimum number of egg droppings to figure out the critical floor

    >>> recursive_egg_drop(6, 15)
    4
    """

    # if eggs == 0 => 0
    if eggs <= 0:
        return 0

    # if floor == 1 or 0 => return floors
    if floors == 1 or floors == 0:
        return floors

    # if eggs = 1 =>  return floors
    if eggs == 1:
        return floors

    min_floors = float("inf")
    result = 0

    for floor in range(1, floors + 1):
        result = max(recursive_egg_drop(eggs - 1, floor - 1), recursive_egg_drop(eggs, floors - 1))
        if result < min_floors:
            min_floors = result

    return min_floors + 1


def memoized_egg_drop(eggs, floors):
    """
    Explanation
    When we drop an egg from the floor i, there can be two cases: (1) The egg breaks (2) The egg doesn’t break.

    If the egg breaks after dropping from the i(th) floor, then, we only need to check for floors lower than i
    with remaining eggs; so the problem reduces to i - 1 floors and n - 1 eggs.
    If the egg doesn’t break after dropping from the i(th)  floor, then,
    we only need to check for floors higher than i; so the problem reduces to k - i floors and n eggs.
    Since we need to minimize the number of trials in the worst case, we take the maximum of two cases.
    We consider the max of the two cases above for every floor and choose the floor that yields
    the minimum number of trials.

    Parameters
    ----------
    eggs : int
        number of eggs
    floors : int
        number of floors

    Returns
    -------
    int
        minimum number of egg droppings to figure out the critical floor

    >>> memoized_egg_drop(6, 15)
    4
    """
    cache = [[float("inf") for _ in range(floors + 1)] for _ in range(eggs + 1)]

    def helper(current_eggs, current_floors):

        # if eggs == 0 => 0
        if current_eggs <= 0:
            return 0

        # if floor == 1 or 0 => return floors
        if current_floors == 1 or current_floors == 0:
            return current_floors

        # if eggs = 1 =>  return floors
        if current_eggs == 1:
            return current_floors

        if cache[current_eggs][current_floors] != float("inf"):
            return cache[current_eggs][current_floors]
        result = 0

        for floor in range(1, current_floors + 1):
            result = 1 + max(recursive_egg_drop(current_eggs - 1, floor - 1),
                             recursive_egg_drop(current_eggs, floors - 1))
            if result < cache[current_eggs][current_floors]:
                cache[current_eggs][current_floors] = result

        return cache[current_eggs][current_floors]

    return helper(eggs, floors)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
