def generate_sub_arrays(array):
    """

    Parameters
    ----------
    array : list
        list of characters or number

    Returns
    -------
    list
        A list of all sub arrays

    """
    all_sub_arrays = []

    def helper(end):
        if end == len(array):
            return

        for start in range(end + 1):
            all_sub_arrays.append(array[start:end + 1])
        helper(end + 1)

    helper(0)
    return all_sub_arrays


def generate_sub_arrays_iteratively(array):
    all_sub_arrays = []

    for end in range(len(array)):
        for start in range(end + 1):
            all_sub_arrays.append(array[start:end + 1])

    return all_sub_arrays


if __name__ == '__main__':
    import doctest

    doctest.testmod()
