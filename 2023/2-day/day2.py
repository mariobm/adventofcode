#!/usr/bin/env python3

# advent of code 2023 2. day solution
# https://adventofcode.com/2023/day/2
# Usage: python input1.txt

import sys

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    print("Part 1: {}".format(part1(lines))) # 54081
    print("Part 2: {}".format(part2(lines))) # 54649

def part1(lines):
    rules = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    possible_game_ids = []
    for game_id, line in enumerate(lines):
        subsets = line.split(":")[1]
        hasBrokenRule = False
        for colours in subsets.split(";"):
            current_colour_sum = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }

            for colour in colours.split(","):
                number, colour = colour.split()
                current_colour_sum[colour] += int(number)

                hasBrokenRule = current_colour_sum[colour] > rules[colour]
                if hasBrokenRule:
                    break
            if hasBrokenRule:
                break
        if not hasBrokenRule:
            possible_game_ids.append(game_id+1)
    return sum(possible_game_ids)

def part2(lines):
    power_sum = []
    for line in lines:
        subsets = line.split(":")[1]
        max_colours = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for colours in subsets.split(";"):
            for colour in colours.split(","):
                number, colour = colour.split()
                max_colours[colour] = max(max_colours[colour], int(number))

        power_sum.append(max_colours["red"] * max_colours["green"] * max_colours["blue"])
    return sum(power_sum)

if __name__ == '__main__':
    main()
