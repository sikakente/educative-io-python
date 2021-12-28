def count_set_bits(number):
    set_bits_count = 0
    while number:
        if number % 2 == 1:
            set_bits_count += 1
        number = number >> 1
    return set_bits_count


def count_set_bits_with_bitwise_and(number):
    set_bits_count = 0
    while number:
        if number & 1 == 1:
            set_bits_count += 1
        number = number >> 1
    return set_bits_count


def count_set_bits_with_bitwise_and_simple(number):
    """Counts set bits in a decimal number

    Parameters
    ----------
    number : int
        decimal number e.g

    Returns
    -------
    int
        a count of set bits in a number

    >>> count_set_bits_with_bitwise_and_simple(125)
    6
    """
    set_bits_count = 0
    while number:
        set_bits_count += number & 1
        number = number >> 1
    return set_bits_count


def count_set_bits_brian_kernighan(number):
    """Counts the set bits in binary number given a decimal number

    This uses Brian Kernighan's algorithm to count the set bits in a
    number.
    A set bit is equal to 1
    An unset bit is equal to 0

    The Brian Kernighan approach only counts set bits using this formula
    n = n & (n-1)
    count ++
    while n > 0

    n  = 40    => 00000000 00000000 00000000 00101000
    n - 1 = 39    => 00000000 00000000 00000000 00100111
    -----------------------------------------------------------
    (n & (n - 1)) = 32  => 00000000 00000000 00000000 00100000
    -----------------------------------------------------------

    Parameters
    ----------
    number : int
        a decimal number e.g 125

    Returns
    -------
    int
        an integer representing the count of set bits in a binary number

    >>> count_set_bits_brian_kernighan(125)
    6
    """
    set_bits_count = 0
    while number:
        number &= number - 1
        set_bits_count += 1
    return set_bits_count


if __name__ == '__main__':
    import doctest
    doctest.testmod()
