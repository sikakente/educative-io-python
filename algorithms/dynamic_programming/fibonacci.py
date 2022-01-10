def recursive_fibonacci(n):
    """Returns the nth fibonacci number

    Time complexity: O(2^n)

    Parameters
    ----------
    n : int
        the nth fibonacci position

    Returns
    -------
    int
        the nth fibonacci number
    -------

    >>> recursive_fibonacci(0)
    0

    >>> recursive_fibonacci(1)
    1

    >>> recursive_fibonacci(3)
    2

    """
    if n < 0:
        raise ValueError("Value cannot be negative")
    if n == 1:
        return 1
    if n == 0:
        return 0
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def memoized_fibonacci(n):
    """Returns the nth fibonacci number

    Time complexity: O(n)

    Parameters
    ----------
    n : int
        the nth fibonacci position

    Returns
    -------
    int
        the nth fibonacci number
    -------

    >>> memoized_fibonacci(0)
    0

    >>> memoized_fibonacci(1)
    1

    >>> memoized_fibonacci(3)
    2

    """
    cache = {}

    def fib(m):
        if m < 0:
            raise ValueError("Value cannot be negative")
        if m in cache:
            return cache[m]
        if m == 1:
            return 1
        if m == 0:
            return 0
        cache[m] = fib(m - 1) + fib(m - 2)
        return cache[m]

    return fib(n)


def tabulated_fibonacci(n):
    """Returns the nth fibonacci number

    Time complexity: O(n)

    Parameters
    ----------
    n : int
        the nth fibonacci position

    Returns
    -------
    int
        the nth fibonacci number
    -------

    >>> tabulated_fibonacci(0)
    0

    >>> tabulated_fibonacci(1)
    1

    >>> tabulated_fibonacci(3)
    2

    """
    if n < 0:
        raise ValueError("Value cannot be negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    cache = [0 for _ in range(n + 1)]
    cache[1] = 1
    i = 2
    while i <= n:
        cache[i] = cache[i - 1] + cache[i - 2]
        i += 1

    return cache[n]


def fast_tabulated_fibonacci(n):
    """Returns the nth fibonacci number

    Time complexity: O(n)

    Parameters
    ----------
    n : int
        the nth fibonacci position

    Returns
    -------
    int
        the nth fibonacci number
    -------

    >>> fast_tabulated_fibonacci(0)
    0

    >>> fast_tabulated_fibonacci(1)
    1

    >>> fast_tabulated_fibonacci(3)
    2

    >>> fast_tabulated_fibonacci(4)
    3

    """
    if n < 0:
        raise ValueError("Value cannot be negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    i = 2
    while i <= n:
        a, b = b, a + b
        i += 1

    return b


if __name__ == '__main__':
    import doctest

    doctest.testmod()
