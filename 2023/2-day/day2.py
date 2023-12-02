#!/usr/bin/env python3

# advent of code 2023 2. day solution
# https://adventofcode.com/2023/day/2
# Usage: python input1.txt

import sys, re

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    print("Part 1: {}".format(part1(lines))) # 2505
    print("Part 2: {}".format(part2(lines))) # 70265

def part1(lines):
    rules = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    possible_game_ids = []
    for game_id, line in enumerate(lines):
        hasBrokenRule = False
        for num, col in re.findall(r'(\d+) (\w+)', line):
            hasBrokenRule = int(num) > rules[col]
            if hasBrokenRule:
                break
        if not hasBrokenRule:
            possible_game_ids.append(game_id+1)
    return sum(possible_game_ids)

def part2(lines):
    power_sum = []
    for line in lines:
        max_colours = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for num, col in re.findall(r'(\d+) (\w+)', line):
            max_colours[col] = max(max_colours[col], int(num))

        power_sum.append(max_colours["red"] * max_colours["green"] * max_colours["blue"])
    return sum(power_sum)

if __name__ == '__main__':
    main()
