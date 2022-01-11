def recursive_knapsack(profits, profits_length, weights, capacity):
    """

    Parameters
    ----------
    profits : list
        integer list containing profits
    profits_length : int
        number of profits in profit list
    weights : list
        integer list of weights
    capacity : int
        capacity of the bag

    Returns
    -------
    int
        maximum profit

    >>> profits = [60, 100, 120]
    >>> profits_length = 3
    >>> weights = [10, 20, 30]
    >>> capacity = 50
    >>> recursive_knapsack(profits, profits_length, weights, capacity)
    220

    """

    def ks(remaining_capacity, profits_so_far, current_item):
        if remaining_capacity == 0:  # the bag is full
            return profits_so_far
        if remaining_capacity < 0:  # the bag is over full
            return float("-inf")
        if current_item >= profits_length:
            return profits_so_far

        including = ks(remaining_capacity - weights[current_item], profits_so_far + profits[current_item],
                       current_item + 1)
        excluding = ks(remaining_capacity, profits_so_far, current_item + 1)

        return max(including, excluding)

    return ks(capacity, 0, 0)


def memoized_knapsack(profits, profits_length, weights, capacity):
    """

    Parameters
    ----------
    profits : list
        integer list containing profits
    profits_length : int
        number of profits in profit list
    weights : list
        integer list of weights
    capacity : int
        capacity of the bag

    Returns
    -------
    int
        maximum profit

    >>> profits = [60, 100, 120]
    >>> profits_length = 3
    >>> weights = [10, 20, 30]
    >>> capacity = 50
    >>> memoized_knapsack(profits, profits_length, weights, capacity)
    220

    """
    cache = {}

    def ks(remaining_capacity, profits_so_far, current_item):
        if (remaining_capacity, current_item) in cache:
            return cache[(remaining_capacity, current_item)]
        if remaining_capacity == 0:  # the bag is full
            return profits_so_far
        if remaining_capacity < 0:  # the bag is over full
            return float("-inf")
        if current_item >= profits_length:
            return profits_so_far

        including = ks(remaining_capacity - weights[current_item], profits_so_far + profits[current_item],
                       current_item + 1)
        excluding = ks(remaining_capacity, profits_so_far, current_item + 1)

        cache[(remaining_capacity, current_item)] = max(including, excluding)
        return cache[(remaining_capacity, current_item)]

    return ks(capacity, 0, 0)


def bottom_up_knapsack(profits, profits_length, weights, capacity):
    """

    Parameters
    ----------
    profits : list
        integer list containing profits
    profits_length : int
        number of profits in profit list
    weights : list
        integer list of weights
    capacity : int
        capacity of the bag

    Returns
    -------
    int
        maximum profit

    >>> profits = [60, 100, 120]
    >>> profits_length = 3
    >>> weights = [10, 20, 30]
    >>> capacity = 50
    >>> bottom_up_knapsack(profits, profits_length, weights, capacity)
    220

    """

    cache = [[0 for _ in range(capacity + 1)] for _ in range(profits_length + 1)]

    for p in range(1, profits_length + 1):
        for c in range(1, capacity + 1):
            if weights[p - 1] <= c:
                cache[p][c] = max(profits[p - 1] + cache[p - 1][c - weights[p - 1]], cache[p - 1][c])
            else:
                cache[p][c] = cache[p - 1][c]

    return cache[profits_length][capacity]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
