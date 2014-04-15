#!/usr/bin/env python3

"""
Google Code Jam 2013 - Qualification Round - 2. Problem
"""
__author__ = 'Luka Sterbic'

import sys


class Lawn(object):
    def __init__(self, height, width, pattern):
        self.height = height
        self.width = width
        self.pattern = pattern

    def is_obtainable(self):
        for i in range(self.height):
            for j in range(self.width):
                larger_in_col = False

                for k in range(self.height):
                    if self.pattern[k][j] > self.pattern[i][j]:
                        larger_in_col = True
                        break

                if not larger_in_col:
                    continue

                for k in range(self.width):
                    if self.pattern[i][k] > self.pattern[i][j]:
                        return False

        return True


def main(path):
    with open(path) as file:
        test_cases = int(file.readline())

        for test in range(1, test_cases + 1):
            height, width = file.readline().split()

            height = int(height)
            width = int(width)
            grass = []

            for row in range(height):
                grass.append([int(x) for x in file.readline().split()])

            lawn = Lawn(height, width, grass)
            result = "YES" if lawn.is_obtainable() else "NO"

            print("Case #%d: %s" % (test, result))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 lawnmower.py input_file")
        sys.exit(1)

    main(sys.argv[1])