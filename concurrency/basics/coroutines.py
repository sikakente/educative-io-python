from functools import wraps
from collections import namedtuple


def coroutine(func):
    """
    Function decorator which primes coroutines by calling
    next(<generator_function>)

    Parameters
    ----------
    func

    Returns
    -------

    """
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


@coroutine
def averager():
    """
    Generator function which computes the running average of numbers

    Returns
    -------

    """
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


class DemoException(Exception):
    """Demo Exception"""


def demo_exc_handling():
    """
    Coroutine which handles exception
    Returns
    -------

    """
    print("-> coroutine started")
    while True:
        try:
            x = yield
        except DemoException:
            print("*** DemoException handled. Continuing...")
        else:
            print(f"-> coroutine received: {x!r}")
    raise RuntimeError("This line should never run.")


Result = namedtuple("Result", "count average")


@coroutine
def averager_with_return_value():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)


if __name__ == '__main__':
    average_gen = averager()
    print(average_gen.send(10))
    print(average_gen.send(20))
    print(average_gen.send(40))
    average_gen.close()

    print()
    print("Demo Exception")
    demo_gen = demo_exc_handling()
    next(demo_gen)
    demo_gen.send(100)
    demo_gen.throw(DemoException)

    print()
    print("Averager with return")
    averager_with_return_gen = averager_with_return_value()
    print(averager_with_return_gen.send(10))
    print(averager_with_return_gen.send(30))
    try:
        averager_with_return_gen.send(None)
    except StopIteration as exc:
        print(exc.value)

