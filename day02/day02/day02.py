# AOC 2015 Day 02

import pathlib
from pprint import pprint

root_path = pathlib.Path.home() / "git" / "aoc2015" / "day02"




def part1(lines):

    total_area = 0
    for line in lines:
        dimensions = line.split("x")
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])

        lw = l*w
        lh = l*h
        wh = w*h

        smallest = min(lw, lh, wh)
        area = 2*lw + 2*lh + 2*wh + smallest
        total_area += area

    return total_area

def part2(lines):
    total_length = 0

    for line in lines:
        dimensions = line.split("x")
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])

        lw = 2*l + 2*w
        lh = 2*l + 2*h
        wh = 2*w + 2*h

        smallest = min(lw, lh, wh)
        volume = w*h*l
        total_length += smallest + volume

    return total_length


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]


    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
