#!/usr/bin/env python
# -*- coding: utf-8 -*-

PASSWORDS = []
PART2 = []


def split_int(number):
    return list(map(int, list(str(number))))


def check_passwords(first, last):
    for password in range(first, last):
        digits = split_int(password)
        if digits != sorted(digits):
            continue
        if any(digits.count(x) > 1 for x in digits):
            PASSWORDS.append(digits)
        if any(digits.count(x) == 2 for x in digits):
            PART2.append(digits)


check_passwords(125730, 579381)
print(len(PASSWORDS))
print(len(PART2))
