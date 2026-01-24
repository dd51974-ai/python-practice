import sys


def luhn_check(number):
    if number.isdigit():
        last_digit = int(str(number[-1]))
        reverse_sequence = list(int(d) for d in str(int(number[-2::-1])))