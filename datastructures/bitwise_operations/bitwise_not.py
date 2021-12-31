def switch_number_sign(number):
    """Negates a number using bitwise operation

    Parameters
    ----------
    number : int
        integer to negate e.g. 2

    Returns
    -------
    int
        negated integer value of number provided

    >>> switch_number_sign(10)
    -10

    >>> switch_number_sign(-10)
    10
    """
    return ~number + 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
