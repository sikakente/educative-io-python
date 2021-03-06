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

    Time Complexity: O(1)
    Space Complexity: O(1)

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


def count_set_bits_using_lookup_table(number):
    """Count bit set using lookup table

    This approach requires an O(1) time solution to count the set bits.
    However, this requires some preprocessing.
    So, we divide our 32-bit input into 8-bit chunks, so there are four chunks.
    We have 8 bits in each chunk, then the range is from 0 - 255 (0 to 2^7-1).
    So, we may need to count set bits from o to 255 in individual chunks

    Algorithm:
    1. Initialize table[0] with 0
    2. Loop through, in the range from 1 to 256
        for i = 1 to 255
            - table[1] = (1 & 1) + table[1 / 2] => table[1] = 1 + table[0] => table[1] = 1
            - table[2] = (2 & 1) + table[2 / 2] => table[2] = 0 + table[1] => table[2] = 1
            - table[3] = (3 & 1) + table[3 / 2] => table[3] = 1 + table[1] => table[1] = 2
            ...
    3. Initialize result = 0
    4. Loop through, in the range from 0 to 3
        - To check on each of the 4 8-bit chunkc using result += table[n & 0xff]
        - Shift n by 8 bits (n >>= 8), we do this to get the second last 8 bits
    5. return result

    Time Complexity: O(1)
    Space Complexity: O(256) ~= O(1)

    Parameters
    ----------
    number : int
        a decimal number e.g 125

    Returns
    -------
    int
        an integer representing the count of set bits in a binary number

    >>> count_set_bits_using_lookup_table(125)
    6

    >>> count_set_bits_using_lookup_table(1000007878)
    17

    >>> count_set_bits_using_lookup_table(1)
    1

    >>> count_set_bits_using_lookup_table(0)
    0
    """
    table = [0 for _ in range(256)]
    i = 1
    while i < 256:
        table[i] = (i & 1) + table[i >> 1]
        i += 1

    res = 0
    i = 0
    while i < 4:
        res += table[number & 0xff]
        number >>= 8
        i += 1

    return res


def number_of_set_bit_counts_in_range(number):
    """Gets a list containing the number of set bits for each number in a range

    Parameters
    ----------
    number : int
        the highest number in the range for which to count the set bits

    Returns
    -------
    list
        a list containing the number of set bits in a range

    >>> number_of_set_bit_counts_in_range(6)
    [0, 1, 1, 2, 1, 2, 2]
    """
    return [count_set_bits_using_lookup_table(n) for n in range(number+1)]


def even_or_odd(numbers):
    """Iterates through a list of integers and returns a list indicating
    which numbers are odd or even

    Parameters
    ----------
    numbers: list
        integer list e.g. [1, 2, 3, 4]

    Returns
    -------
    list
        a string list containing the words "Odd" or "Even" corresponding to
        whether the number at the index in the supplied integer list is even or odd

    >>> even_or_odd([1, 2, 3, 4])
    ['Odd', 'Even', 'Odd', 'Even']
    """
    even_or_odd_list = [None for i in range(len(numbers))]
    for idx, num in enumerate(numbers):
        even_or_odd_list[idx] = 'Even' if num & 1 == 0 else 'Odd'

    return even_or_odd_list


def is_power_of_two(number):
    if number < 1:
        return False
    if number == 1:
        return True
    while number > 2:
        number = number >> 1
        if number & 1 == 1:
            return False
    return True


def is_power_of_two_brian_kernighan(number):
    """Checks whether a given integer is a power of 2

    It uses the Brian Kernighan algorithm used to count the set bits.
    We know that powers of 2 only have 1 set bit.
    e.g 2^0 = 1, 2^1= 10, 2^2= 100 ...

    By applying a bitwise & to the given integer and the next smallest integer
    if the the result is 0, then we know it is a power of 2. Otherwise it is not
    e.g Given 4:
    n = 4       => 100
    n -1 = 3    =>  11
    ---------------------
    &           => 0 True
    ---------------------

    n = 5       => 101
    n -1 = 3    => 100
    ---------------------
    &           => 001 False
    ---------------------

    Parameters
    ----------
    number : int
        positive integer

    Returns
    -------
    bool
        indicates whether the given number is a power of 2. e.g. True or False

    """
    if number == 0:
        return False
    return (number & (number - 1)) == 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
