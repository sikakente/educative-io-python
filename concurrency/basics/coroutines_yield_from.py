
def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i


def gen_with_yield_from():
    yield from 'AB'
    yield from range(1, 3)


def chain(*iterables):
    """
    Yield from multiple iterables
    Parameters
    ----------
    iterables

    Returns
    -------

    """
    for it in iterables:
        yield from it


if __name__ == '__main__':
    print(list(gen()))
    print(list(gen_with_yield_from()))

    print(list(chain('ABC', tuple(range(10)))))
