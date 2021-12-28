import math


def number_system(number, base=10):
    numbers = []
    while number:
        remainder, quotient = number % base, number // base
        numbers.append(remainder)
        number = quotient

    return numbers


def decimal_number_system(number):
    return number_system(number, base=10)


def binary_number_system(number):
    return number_system(number, base=2)


def binary_to_decimal(number):
    base = 2
    power = 0
    decimal_number = 0
    while number:
        remainder, quotient = number % base, number // 10
        decimal_number += remainder * 2 ** power
        number = quotient
        power += 1
    return decimal_number


def num_digits(number):
    base = 10
    count = 0
    while number:
        number = number // base
        count += 1
    return count


def num_digits_using_log(number):
    if number != 0:
        return math.floor(math.log10(number) + 1)
    return -1


def bitwise_decimal_to_binary(number):
    bit_count = 0
    decimal_number = []
    while number:
        number, remainder = number >> 1, number % 2
        bit_count += 1
        decimal_number.append(remainder)

    return list(reversed(decimal_number)), bit_count


def bit_counter(number):
    bit_count = 0
    while 1 << bit_count <= number:
        bit_count += 1
    return bit_count


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
