#!/usr/bin/env python3
# advent of code 2022 2. day solution

import sys
import re

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        lines = [re.split('\s+', line.strip()) for line in lines]
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))

def part1(lines):
    values = {
        'X': {
            'A': 3,
            'B': 0,
            'C': 6,
        },
        'Y': {
            'A': 6,
            'B': 3,
            'C': 0,
        },
        'Z': {
            'A': 0,
            'B': 6,
            'C': 3,
        },
    }

    return sum([values[me][elf] + (ord(me) - 87) for elf, me in lines])

def part2(lines):
    values = {
        'X': {
            'A': 3,
            'B': 1,
            'C': 2,
        },
        'Y': {
            'A': 4,
            'B': 5,
            'C': 6,
        },
        'Z': {
            'A': 8,
            'B': 9,
            'C': 7,
        },
    }
    return sum([values[me][elf] for elf, me in lines])

if __name__ == '__main__':
    # testni primer
    main()
    print(sum(1+(o-65-(89-y))%3+3*(y-88)for(o,y)in map(lambda x:map(ord,x.split()),open(sys.argv[1]).readlines())))
    # 14264, 
    # 12382