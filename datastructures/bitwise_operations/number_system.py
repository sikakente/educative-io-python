
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


if __name__ == '__main__':
    number_system(1256)
