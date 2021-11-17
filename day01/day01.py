'''
Advent of Code Day 1 solution
'''

from random import randint
import pathlib
from pprint import pprint

root_path = pathlib.Path.home() / "git" / "aoc2015" / "day01"

def find_floor(directions):
    # Dictionary/Comprehension Solution
    floors = {"(": 1, ")": -1}
    return sum([floors[ch] for ch in directions])

    # Comprehension solution
    # return sum([1 for ch in directions if ch=="("]) + sum([-1 for ch in directions if ch==")"])

    # First solution
    # floor = 0
    # for ch in directions:
    #     if ch == "(":
    #         floor += 1
    #     else:
    #         floor -= 1
    # return floor


def find_basement(directions: str):

    floors = {"(": 1, ")": -1}

    # # First solution
    # floor = 0
    # char_pos = 0
    # while floor != -1:
    #     ch = directions[char_pos]

    #     # if ch == "(":
    #     #     floor += 1
    #     # else:
    #     #     floor -= 1

    #     # Dictionary solution
    #     floor += floors[ch]

    #     char_pos += 1

    # Second solution
    floor = 0
    for char_pos, ch in enumerate(directions):
        floor += floors[ch]
        if floor < 0:
            break
    return char_pos+1


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        directions = [line.strip() for line in f.readlines()]

    print(f"Part 1: Final Floor is {find_floor(directions[0])}")

    print(f"Part 2: First Move to basement is {find_basement(directions[0])}")

