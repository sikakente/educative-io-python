
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


if __name__ == '__main__':
    number_system(1256)
