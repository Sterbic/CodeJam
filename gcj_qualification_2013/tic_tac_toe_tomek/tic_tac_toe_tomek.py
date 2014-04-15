#!/usr/bin/env python3

"""
Google Code Jam 2013 - Qualification Round - 1. Problem
"""
__author__ = 'Luka Sterbic'

import sys


class GameResult(object):
    X_WON = "X won"
    O_WON = "O won"
    DRAW = "Draw"
    INCOMPLETE = "Game has not completed"

    class Counter(object):
        def __init__(self):
            self.x = 0
            self.o = 0
            self.t = 0

        def update(self, char):
            if char == "X":
                self.x += 1
            elif char == "O":
                self.o += 1
            elif char == "T":
                self.t += 1

    @staticmethod
    def check_result(game_state):
        game_result = GameResult.DRAW

        counters = [GameResult.Counter() for _ in range(6)]

        for row in range(4):
            line = game_state[row]

            counter = GameResult.Counter()

            for col in range(4):
                char = line[col]

                counter.update(char)
                counters[col].update(char)

                if char == ".":
                    game_result = GameResult.INCOMPLETE

                if row == col:
                    counters[4].update(char)

                if row + col == 3:
                    counters[5].update(char)

            if counter.x == 4 or (counter.x == 3 and counter.t == 1):
                return GameResult.X_WON

            if counter.o == 4 or (counter.o == 3 and counter.t == 1):
                return GameResult.O_WON

        for col in range(6):
            if counters[col].x == 4 or \
                    (counters[col].x == 3 and counters[col].t == 1):
                return GameResult.X_WON

            if counters[col].o == 4 or \
                    (counters[col].o == 3 and counters[col].t == 1):
                return GameResult.O_WON

        return game_result


def main(path):
    with open(path) as file:
        test_cases = int(file.readline())

        for test in range(1, test_cases + 1):
            game_state = [file.readline().rstrip() for _ in range(4)]
            game_result = GameResult.check_result(game_state)

            print("Case #%d: %s" % (test, game_result))
            file.readline()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 tic_tac_toe_tomek.py input_file")
        sys.exit(1)

    main(sys.argv[1])