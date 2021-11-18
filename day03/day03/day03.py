# AOC 2015 Day 3

import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2015" / "day03"




def part1(lines):

    # Setup my directions
    directions = {"^": ( 0, 1),
                  "v": ( 0,-1),
                  "<": (-1, 0),
                  ">": ( 1, 0)}

    last = (0, 0)
    presents = dict()
    presents[last] = 1
    for ch in lines[0]:
        last = (last[0] + directions[ch][0], last[1] + directions[ch][1])
        if last in presents.keys():
            presents[last] += 1
        else:
            presents[last] = 1

    return len(presents)


def part2(lines):

    # Setup my directions
    directions = {"^": ( 0, 1),
                  "v": ( 0,-1),
                  "<": (-1, 0),
                  ">": ( 1, 0)}

    robolast = (0, 0)
    reallast = (0, 0)
    presents = dict()
    presents[robolast] = 2
    robo = False
    for ch in lines[0]:
        if robo:
            robolast = (robolast[0] + directions[ch][0], robolast[1] + directions[ch][1])
            if robolast in presents.keys():
                presents[robolast] += 1
            else:
                presents[robolast] = 1
        else:
            reallast = (reallast[0] + directions[ch][0], reallast[1] + directions[ch][1])
            if reallast in presents.keys():
                presents[reallast] += 1
            else:
                presents[reallast] = 1

        robo = not robo

    return len(presents)


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]


    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
