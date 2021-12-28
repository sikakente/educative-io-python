
def number_system(number, base=10):
    numbers = []
    while number:
        remainder, quotient = number % base, number // base
        numbers.append(remainder)
        number = quotient

    return numbers


if __name__ == '__main__':
    number_system(1256)
