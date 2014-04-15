#!/usr/bin/env python3

"""
Google Code Jam 2014 - Qualification Round - 2. Problem
"""
__author__ = 'Luka Sterbic'

import sys


phi = (5 ** 0.5 - 1) / 2


def calc_time_fixed_factories(n, c, f, x):
    rate = 2.0
    time = 0.0
    bought = 0

    while bought < n:
        time += c / rate
        rate += f
        bought += 1

    return time + x / rate


def calc_best_time(c, f, x):
    time = calc_time_fixed_factories(0, c, f, x)
    factories = 1

    while True:
        new_time = calc_time_fixed_factories(factories, c, f, x)

        if new_time > time:
            break

        time = new_time
        factories *= 2

    min_factories = factories // 4
    max_factories = factories
    span = max_factories - min_factories + 1

    first = round(max_factories - span * phi)
    second = round(min_factories + span * phi)

    first = (first, calc_time_fixed_factories(first, c, f, x))
    second = (second, calc_time_fixed_factories(second, c, f, x))

    while max_factories - min_factories > 3 and first != second:
        if first[1] >= second[1]:
            min_factories = first[0]
            first = second

            span = max_factories - min_factories + 1

            second = round(min_factories + span * phi)
            second = (second, calc_time_fixed_factories(second, c, f, x))
        else:
            max_factories = second[0]
            second = first

            span = max_factories - min_factories + 1

            first = round(max_factories - span * phi)
            first = (first, calc_time_fixed_factories(first, c, f, x))

    test_values = range(min_factories, max_factories + 1)
    results = [calc_time_fixed_factories(n, c, f, x)
               for n in test_values if n >= 0]

    return min(results)


def main(path):
    with open(path) as file:
        test_cases = int(file.readline())

        for test in range(1, test_cases + 1):
            c, f, x = [float(num) for num in file.readline().split()]
            print("Case #%d: %0.7f" % (test, calc_best_time(c, f, x)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 cookie_clicker_alpha.py input_file")
        sys.exit(1)

    main(sys.argv[1])