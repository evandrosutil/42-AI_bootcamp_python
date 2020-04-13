#!/usr/bin/env python3

import sys


def operations(num1, num2):
    """
    This function performs 5 mathematical operations between two given
    numbers and prints its results.
    """
    result = dict()
    result['sum'] = num1 + num2
    result['difference'] = num1 - num2
    result['product'] = num1 * num2
    try:
        result['quotient'] = num1 / num2
        result['remainder'] = num1 % num2
    except ZeroDivisionError:
        result['quotient'] = 'ERROR (div by zero)'
        result['remainder'] = 'ERROR (modulo by zero)'

    for key, value in result.items():
        print(f'{key.capitalize():10}: {value}')


if __name__ == "__main__":
    usage_msg = (
        "Usage: python operations.py <number1> <number2>\n"
        "Example:\n\tpython operations.py 10 3")
    if len(sys.argv) != 3:
        if len(sys.argv) > 3:
            print('InputError: two many arguments\n')
        print(usage_msg)
        exit()
    try:
        num1, num2 = int(sys.argv[1]), int(sys.argv[2])
    except ValueError:
        print('InputError: only numbers\n')
        print(usage_msg)
        exit()
    operations(num1, num2)
