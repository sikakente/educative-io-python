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